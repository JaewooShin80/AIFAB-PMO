# AIFAB 웹 IDE 개발환경 Terraform 세팅 가이드 (v1-0)

| 구분 | 내용 |
|:---|:---|
| 버전 | v1-0 (2026-07-13) |
| 대상 | AI 인프라팀 (구축), AI Board (승인·운영) |
| 관련 문서 | AWS 기반 탑다운 AIFAB 과제 운영환경 구축운영 기획안 v1-0, 바텀업 샌드박스 기획안 v1-0 |

---

## 1. 개요

### 1.1 목적

시티즌 개발자가 **브라우저에서 SSO 로그인만 하면, Claude 하네스(AIFAB 하네스)가 적용된 VS Code 유사 웹 IDE로 즉시 진입**하는 개발환경을 Terraform으로 표준화한다. 승인 워크플로(그림 1) → Terraform 자원 자동 생성 흐름에 워크스페이스 프로비저닝을 편입하는 것이 목표다.

### 1.2 요구사항

| # | 요구사항 | 내용 |
|:---|:---|:---|
| R1 | 즉시 진입 | 웹 접속 → 계정 인증(SSO) → IDE 실행까지 사용자 조작 최소화. EC2 콘솔·SSH 접근 배제 |
| R2 | VS Code 유사 환경 | 브라우저 기반 VS Code(Code-OSS/code-server) — 별도 클라이언트 설치 불요 |
| R3 | 하네스 선적용 | Claude Code CLI + AIFAB 하네스(전역 CLAUDE.md·commands·plugins)가 첫 진입 시 이미 설치된 상태 |
| R4 | 키리스 LLM 연동 | Amazon Bedrock 경유(`CLAUDE_CODE_USE_BEDROCK=1`), IAM 롤 기반 — API 키 배포·관리 금지 |
| R5 | 사내망 한정 | 인터넷 인바운드 차단, VPC 내부 통신(기획안 4장 네트워크 원칙 준수) |
| R6 | IaC 자동화 | 과제 승인 시 Terraform으로 팀 워크스페이스 자동 생성·회수 |
| R7 | 가동 정책 연동 | 유휴 자동 종료(시간제 가동 정책, 기획안 3.6) |

### 1.3 후보 검토 결과

| 후보 | 판정 | 사유 |
|:---|:---|:---|
| **SageMaker Studio Code Editor** | **채택 후보 (1안)** | 완전 관리형 웹 VS Code, IAM Identity Center SSO 직결, EC2 비노출 |
| **Coder (OSS)** | **채택 후보 (2안)** | 워크스페이스 정의가 Terraform 네이티브, code-server 웹 IDE, 통제력 최대 |
| CodeCatalyst Dev Environments | 불가 | 2025-11-07부로 신규 고객 수용 중단 |
| Cloud9 | 불가 | 단종 (신규 사용 불가) |
| App Studio | 부적합 | 로우코드 빌더 — Claude Code 하네스 탑재 불가 |

---

## 2. 1안 — SageMaker Studio Code Editor (완전 관리형)

### 2.1 아키텍처·접속 흐름

```
사용자 브라우저
  → IAM Identity Center SSO 로그인 (Entra ID 연동, 기획안 3.3)
  → SageMaker Studio URL → Code Editor Space 기동 (관리형 ml.* 인스턴스)
  → Lifecycle Config/커스텀 이미지로 하네스 적용 완료 상태에서 IDE 시작
```

- 사용자는 EC2·인스턴스를 보지 않는다. AWS가 기반 인스턴스 패치·업그레이드 수행
- Space 단위 격리: **팀당 공유 Space 1개**(협업) 또는 인당 개인 Space — 파일럿은 팀당 1개 기준
- `VpcOnly` 모드로 사내망 요건(R5) 충족 — Studio 트래픽이 과제 VPC 내부로만 흐름

### 2.2 Terraform 구성 골격

**1회 구축분 (도메인·공통):**

```hcl
resource "aws_sagemaker_domain" "aifab" {
  domain_name             = "aifab-dev"
  auth_mode               = "SSO"                  # IAM Identity Center
  vpc_id                  = var.vpc_id
  subnet_ids              = var.private_subnet_ids
  app_network_access_type = "VpcOnly"              # 사내망 한정

  default_user_settings {
    execution_role = aws_iam_role.workspace.arn    # Bedrock 권한 포함 (4장)
    code_editor_app_settings {
      default_resource_spec {
        instance_type       = "ml.t3.xlarge"       # 4 vCPU / 16 GB
        sagemaker_image_arn = aws_sagemaker_image.aifab_harness.arn  # 커스텀 이미지(권장)
      }
      lifecycle_config_arns = [aws_sagemaker_studio_lifecycle_config.harness.arn]
      app_lifecycle_management {
        idle_settings {                            # R7: 유휴 자동 종료
          lifecycle_management  = "ENABLED"
          idle_timeout_in_minutes = 60
        }
      }
    }
  }
}

resource "aws_sagemaker_studio_lifecycle_config" "harness" {
  studio_lifecycle_config_name     = "aifab-harness-bootstrap"
  studio_lifecycle_config_app_type = "CodeEditor"
  studio_lifecycle_config_content  = base64encode(file("${path.module}/scripts/bootstrap.sh"))
}
```

**과제 승인 시 반복 생성분 (골든 패스 모듈 `webide-workspace`):**

```hcl
resource "aws_sagemaker_user_profile" "member" {
  for_each          = toset(var.team_members)      # SCIM 동기화된 SSO 사용자
  domain_id         = var.domain_id
  user_profile_name = each.value
}

resource "aws_sagemaker_space" "team" {
  domain_id  = var.domain_id
  space_name = "team-${var.project_code}"
  ownership_settings { owner_user_profile_name = var.team_lead }
  space_sharing_settings { sharing_type = "Shared" }
  space_settings {
    app_type = "CodeEditor"
    space_storage_settings {
      ebs_storage_settings { ebs_volume_size_in_gb = 100 }
    }
  }
}
```

### 2.3 하네스 적용 방식

| 방식 | 내용 | 권장 |
|:---|:---|:---|
| **커스텀 이미지** | Docker 이미지에 Node.js·Claude Code CLI·AIFAB 하네스·git·AWS CLI 선탑재 → ECR 등록 → `sagemaker_image_arn` 지정 | **기본** — 기동 시간 최단, 버전 고정 |
| Lifecycle Config | Space 기동 시 `bootstrap.sh` 실행 (하네스 최신화·사용자별 초기화) | 보조 — 이미지와 병행 |

`scripts/bootstrap.sh` 핵심:

```bash
#!/bin/bash
# 하네스 최신화 (이미지에 선탑재된 버전을 사내 GitLab 기준으로 갱신)
git -C /opt/aifab-harness pull || git clone https://gitlab.internal/aifab/harness /opt/aifab-harness
mkdir -p ~/.claude && cp -r /opt/aifab-harness/.claude/* ~/.claude/

# Bedrock 연동 (키리스 — 실행 롤 자격증명 자동 사용)
cat >> ~/.bashrc <<'EOF'
export CLAUDE_CODE_USE_BEDROCK=1
export AWS_REGION=ap-northeast-2
EOF
```

### 2.4 운영 포인트

- **회수**: 과제 종료 시 `terraform destroy`(모듈 단위)로 Space·프로파일 삭제, EBS 데이터 파기 확인을 종료 체크리스트에 연동
- **제약**: IDE 커스터마이징은 커스텀 이미지 범위로 한정. Code-OSS 기반이라 MS 마켓플레이스 일부 확장 미지원(Open VSX 사용)
- **VPC 엔드포인트**: `sagemaker.api`·`sagemaker.runtime`·`studio` 등 인터페이스 엔드포인트 필요 (Landing Zone 공용 구성 재사용 검토)

---

## 3. 2안 — Coder (자체 운영 플랫폼)

### 3.1 아키텍처·접속 흐름

```
사용자 브라우저
  → 내부 ALB (사설 인증서) → Coder 서버 → OIDC 로그인 (Entra ID 직결)
  → 워크스페이스 기동 버튼 → Terraform 템플릿 실행 → EC2 워크스페이스 생성
  → code-server(웹 VS Code) 자동 오픈 — 골든 AMI에 하네스 선탑재
```

- Coder의 워크스페이스 템플릿 = Terraform 코드. 그림 1의 "Terraform 자원 자동 생성"과 동일 체계로 통합
- 사용자는 EC2를 직접 다루지 않으나, **플랫폼(서버·DB)은 AI 인프라팀이 운영**

### 3.2 Terraform 구성 골격

**플랫폼 (1회 구축, Shared Services Account):**

```hcl
resource "aws_instance" "coder_server" {        # 또는 ECS Fargate
  ami           = data.aws_ami.al2023.id
  instance_type = "t3.large"
  subnet_id     = var.private_subnet_id
  user_data     = file("${path.module}/scripts/install-coder.sh")
}

resource "aws_db_instance" "coder" {
  engine         = "postgres"
  instance_class = "db.t3.small"
  allocated_storage = 20
}

resource "aws_lb" "coder" {                     # 내부 ALB + 사설 ACM 인증서
  internal           = true
  load_balancer_type = "application"
  subnets            = var.private_subnet_ids
}
# Coder 서버 설정: OIDC(Entra ID) 로그인, 워크스페이스 autostop 기본값
```

**워크스페이스 템플릿 (Coder 템플릿 — 과제 승인 시 팀별 인스턴스화):**

```hcl
data "coder_workspace" "me" {}

resource "coder_agent" "dev" {
  os   = "linux"
  arch = "amd64"
  startup_script = <<-EOT
    git -C /opt/aifab-harness pull
    cp -r /opt/aifab-harness/.claude/* ~/.claude/
  EOT
  env = {
    CLAUDE_CODE_USE_BEDROCK = "1"
    AWS_REGION              = "ap-northeast-2"
  }
}

module "code_server" {                          # 웹 VS Code 자동 기동
  source   = "registry.coder.com/modules/code-server/coder"
  agent_id = coder_agent.dev.id
}

resource "aws_instance" "workspace" {
  ami                  = data.aws_ami.aifab_golden.id   # Packer 골든 AMI
  instance_type        = "t3.xlarge"
  subnet_id            = var.team_subnet_id
  iam_instance_profile = var.bedrock_profile            # 4장 IAM 롤
  user_data            = coder_agent.dev.init_script    # 부팅 시 Coder 에이전트 접속
}
```

### 3.3 하네스 적용 방식

- **Packer 골든 AMI**: Node.js·Claude Code CLI·AIFAB 하네스·code-server 의존성·git·AWS CLI 베이크. 하네스 버전업 시 AMI 재빌드 → 템플릿 버전 갱신 → 기존 워크스페이스는 재기동 시 반영
- startup_script는 하네스 최신화·사용자 초기화만 수행 (기동 시간 최소화)

### 3.4 운영 포인트

- **autostop/autostart 내장**: 시간제 가동(셧다운/웨이크업) 정책과 그대로 대응 — 별도 EventBridge 개발 불요
- **운영 부담**: Coder 서버 버전업·백업·모니터링, 골든 AMI 유지보수를 AI 인프라팀이 상시 수행 (월 0.5인 내외 공수 가정)
- **통제력**: 워크스페이스 스펙·이미지·정책을 Terraform으로 전면 통제, EC2 요금만 지불 (관리형 마크업 없음)

---

## 4. 공통 — Bedrock 키리스 연동 (양안 동일)

```hcl
resource "aws_iam_role_policy" "bedrock_invoke" {
  role = aws_iam_role.workspace.id               # 1안: 실행 롤 / 2안: 인스턴스 프로파일
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = ["bedrock:InvokeModel", "bedrock:InvokeModelWithResponseStream",
                  "bedrock:GetInferenceProfile", "bedrock:ListInferenceProfiles"]
      Resource = var.approved_model_arns          # 승인 Claude 모델·추론 프로파일 ARN 한정
    }]
  })
}
```

- API 키를 만들지도, 배포하지도 않는다 — 자격증명은 롤에서 자동 해결
- 모델 ARN 화이트리스트로 승인 외 모델 호출 차단 (SCP 가드레일과 이중화)
- 토큰 사용량은 CloudWatch 지표·비용 태그로 과제별 계측

---

## 5. 비용 비교 — 상시 5~10팀 접속 기준

### 5.1 산정 전제

- 서울 리전, 2026년 상반기 요금 수준의 **개략 추정치** (버지니아 단가 × 서울 계수 약 1.2 적용, 확정 시 재산정)
- 팀당 워크스페이스 1개, 4 vCPU/16GB급(t3.xlarge / ml.t3.xlarge), 스토리지 100GB/팀
- **Bedrock 토큰 비용은 양안 공통·사용량 기반이므로 5.2~5.3에서 제외** (5.5에서 별도 추정)
- 시나리오 A: 상시 가동(월 730h) / 시나리오 B: 업무시간 가동 + 유휴 자동 종료(월 200h)

**적용 단가(추정, USD/시간):**

| 인스턴스 (4 vCPU/16GB) | 1안 SageMaker | 2안 EC2 |
|:---|:---|:---|
| t3.xlarge급 | ml.t3.xlarge 약 0.25 | t3.xlarge 약 0.21 |
| (상향 옵션) m5.xlarge급 | ml.m5.xlarge 약 0.29 | m5.xlarge 약 0.24 |

### 5.2 시나리오 A — 상시 가동 (월 730h, USD/월)

| 항목 | 1안 5팀 | 1안 10팀 | 2안 5팀 | 2안 10팀 |
|:---|---:|---:|---:|---:|
| 워크스페이스 컴퓨트 | 약 910 | 약 1,830 | 약 760 | 약 1,520 |
| 스토리지 (100GB/팀) | 약 50 | 약 100 | 약 45 | 약 90 |
| 플랫폼 고정비 | — | — | 약 150 | 약 150 |
| VPC 엔드포인트 등 | 약 50 | 약 50 | (고정비 포함) | (고정비 포함) |
| **합계** | **약 1,010** | **약 1,980** | **약 955** | **약 1,760** |

*2안 플랫폼 고정비: Coder 서버 t3.large(약 76) + RDS db.t3.small(약 50) + 내부 ALB(약 25)*

### 5.3 시나리오 B — 업무시간 + 유휴 자동 종료 (월 200h, USD/월)

| 항목 | 1안 5팀 | 1안 10팀 | 2안 5팀 | 2안 10팀 |
|:---|---:|---:|---:|---:|
| 워크스페이스 컴퓨트 | 약 250 | 약 500 | 약 210 | 약 420 |
| 스토리지 (100GB/팀) | 약 50 | 약 100 | 약 45 | 약 90 |
| 플랫폼 고정비 | — | — | 약 150 | 약 150 |
| VPC 엔드포인트 등 | 약 50 | 약 50 | (고정비 포함) | (고정비 포함) |
| **합계** | **약 350** | **약 650** | **약 405** | **약 660** |

### 5.4 해석

- **유휴 종료 적용 시(시나리오 B) 총액은 사실상 동급** — 5팀 규모에서는 고정비가 없는 1안이 오히려 소폭 저렴
- **상시 가동(시나리오 A)에서는 2안이 약 5~10% 저렴**하나, 그 차액(월 50~220 USD)은 Coder 플랫폼 운영 공수(월 0.5인 내외)로 상쇄되고 남음
- 팀 수가 20팀 이상으로 확대되고 상시 가동 비중이 높아지면 관리형 마크업 누적으로 2안의 비용 우위가 뚜렷해짐

### 5.5 Bedrock 토큰 비용 (Claude Code 사용량 — 양안 공통)

**토큰 단가 (USD / 100만 토큰, 2026 상반기 수준 추정):**

| 모델 | 입력 | 출력 | 캐시 읽기 | 용도 |
|:---|---:|---:|---:|:---|
| **Sonnet (기본 권장)** | 3.00 | 15.00 | 0.30 | 코드 작업 표준 |
| Haiku | 1.00 | 5.00 | 0.10 | 단순 작업·보일러플레이트 |
| Opus | 15.00 | 75.00 | 1.50 | 복잡한 설계 (Sonnet의 5배) |

- Claude Code는 프롬프트 캐싱을 자동 활용 — 긴 세션에서도 입력 대부분이 캐시 읽기(90% 할인)로 처리되어 실효 비용은 명목 단가보다 크게 낮음
- 업계 앵커: Claude Code 개발자 평균 약 $6/일, 상위 90%도 $12/일 이내 (Anthropic 공개 통계)

**대표 작업(대시보드 작성) 시나리오별 추정 (Sonnet 기준):**

| 시나리오 | 작업 규모 | 실작업 시간 | 예상 비용 |
|:---|:---|:---|---:|
| 간단 — Streamlit/Dash, 차트 3~5개, 데이터 1소스 | 반나절~1일 | 3~5h | $5~15 |
| 중간 — React 대시보드, API 연동, 필터·드릴다운 | 2~3일 | 12~18h | $25~70 |
| 복합 — 다중 데이터소스, 인증, 배포 파이프라인 포함 | 1주+ | 30h+ | $60~150 |

**파일럿 규모 환산 (3주 스프린트 1회, USD):**

| 규모 | 산식 | 스프린트당 예상 |
|:---|:---|---:|
| 5팀 × 2인 | 10인 × 15영업일 × $6 | 약 900 |
| 10팀 × 2인 | 20인 × 15영업일 × $6 | 약 1,800 |
| 헤비 유저 가정(2배) | — | 1,800~3,600 |

- 인프라 비용(5.3 유휴종료 기준 월 350~660)과 합산 시 **파일럿 월 총액 약 1,300~2,500 USD 수준**
- 종량제 특성상 미사용 시 $0 — 사용 강도가 검증되지 않은 파일럿 단계에 저위험. 팀플랜 프리미엄 시트(인당 월정액) 전환은 사용량 실측 후 재검토
- 통제 수단: 과제별 비용 태그 + CloudWatch 토큰 지표 + AWS Budgets 과제당 상한 알람 (기획안 9장 비용 체계에 편입)

---

## 6. 종합 비교·권고

| 기준 | 1안 SageMaker Code Editor | 2안 Coder |
|:---|:---|:---|
| 진입 경험 (R1·R2) | SSO → 브라우저 IDE 즉시 (최단) | SSO → 워크스페이스 기동 버튼 → IDE |
| 하네스 적용 (R3) | 커스텀 이미지 + Lifecycle Config | Packer 골든 AMI + startup_script |
| 플랫폼 운영 부담 | **없음 (AWS 관리형)** | 서버·DB·AMI 유지보수 상시 발생 |
| 커스터마이징 자유도 | 이미지 범위로 제한 | **전면 통제 (Terraform 네이티브)** |
| 시간제 가동 (R7) | 유휴 자동 종료 내장 | autostop/autostart 내장 |
| 비용 (5~10팀·유휴종료) | 동급 (5팀에선 소폭 우위) | 동급 |
| 비용 (확대·상시화 시) | 마크업 누적 | **우위** |
| 승인 워크플로 통합 (R6) | TF 모듈 호출 (user_profile·space) | TF 모듈 호출 + Coder 템플릿 체계 일원화 |

**권고**: 파일럿(5~10팀)은 **1안 SageMaker Code Editor**로 시작한다. 플랫폼 운영 공수가 없어 AI 인프라팀 리소스를 골든 패스·하네스 품질에 집중할 수 있고, 유휴 종료 기준 비용도 동급 이하다. 파일럿 종료 시점에 ① 팀 수 확대 계획 ② 상시 가동 비중 ③ IDE 커스터마이징 요구를 재평가해 2안 전환 여부를 판단한다 (양안 모두 하네스는 이미지/AMI로 이식 가능해 전환 비용 제한적).

---

## 7. 참고 자료

- Code Editor in Amazon SageMaker Studio — https://docs.aws.amazon.com/sagemaker/latest/dg/code-editor.html
- Claude Code on Amazon Bedrock — https://code.claude.com/docs/en/amazon-bedrock
- Guidance for Claude Code with Amazon Bedrock (AWS 솔루션) — https://docs.aws.amazon.com/solutions/claude-code-with-amazon-bedrock/
- Coder Docs: Templates — https://coder.com/docs/about/contributing/templates
- Coder GitHub — https://github.com/coder/coder
- Amazon CodeCatalyst FAQ (신규 고객 중단 고지) — https://codecatalyst.aws/explore/faq
- Amazon SageMaker AI Pricing — https://aws.amazon.com/sagemaker/ai/pricing/
- Amazon EC2 On-Demand Pricing — https://aws.amazon.com/ec2/pricing/on-demand/
