# AIFAB 웹 IDE 개발환경 구축 방향 (최종)

| 구분 | 내용 |
|:---|:---|
| 버전 | 최종 v1-0 (2026-07-14) |
| 결정 | **EC2 + Coder(자체 운영 플랫폼) 채택** — SageMaker Code Editor 안은 미채택 |
| 대상 | AI 인프라팀 (구축·운영), AI Board (승인) |
| 근거 문서 | `../fab/26.07.13_AIFAB_웹IDE_개발환경_Terraform_세팅가이드_v1-0.md` (2안 비교 검토 원본) |

---

## 1. 결정 요약

시티즌 개발자용 웹 IDE 개발환경은 **Coder(OSS) 플랫폼 + EC2 워크스페이스** 구성으로 확정한다. 개발부터 배포까지의 전체 흐름은 다음과 같다.

```
사용자 (사내망)
  → SSO 로그인 (Coder OIDC ← Entra ID)
  → Coder 웹 IDE (EC2 워크스페이스 · 골든 AMI: code-server + Claude Code + AIFAB 하네스)
  → 코드 push → GitLab (사내 형상관리)
  → CodePipeline / CodeBuild (빌드 · Semgrep SAST · gitleaks 시크릿 검출)
  → ECR (이미지 저장 · Tag 불변) → Inspector 스캔 (Critical/High 0건)
  → Fargate dev/스테이징 배포
  → 승인 게이트 (AI Board·정보보호팀) → 운영 배포 (Blue/Green, 탑다운)
```

## 2. 결정 배경·사유

| # | 사유 | 내용 |
|:--|:---|:---|
| 1 | **GitLab 중심 형상관리와의 자연스러운 연계** | 개발 흐름의 중심을 사내 GitLab에 두는 구조 — Coder는 워크스페이스만 제공하고 형상·리뷰·파이프라인 트리거는 GitLab이 관장. 관리형 서비스 특유의 자체 저장소·규격에 종속되지 않음 |
| 2 | **Terraform 네이티브 통합** | Coder 워크스페이스 정의 자체가 Terraform 템플릿 — 승인 워크플로 → Terraform 자원 자동 생성 체계(그림 1)와 단일 체계로 일원화 |
| 3 | **하네스 전면 통제** | 골든 AMI(Packer)에 Claude Code·AIFAB 하네스·개발 도구를 자유롭게 베이크 — IDE 확장·런타임·버전을 조직이 완전 통제 |
| 4 | **확대 시 비용 우위** | EC2 정가만 지불(관리형 마크업 없음) — 파일럿 이후 팀 확대·상시 가동 비중 증가 시 비용 격차 확대 |
| 5 | **시간제 가동 정책 내장** | Coder autostop/autostart가 셧다운/웨이크업 정책(기획안 3.6)에 그대로 대응 — 별도 스케줄러 개발 불요 |

**SageMaker Code Editor 미채택 사유**: ① IDE 커스터마이징이 커스텀 이미지 규격 범위로 제한 ② ml.* 인스턴스 마크업(동급 EC2 대비 약 20%) ③ Code Editor는 개인 Space 전용(공유 Space 미지원)으로 팀 협업 구조 제약 ④ SageMaker 도메인·Space 개념 종속. (검토 상세는 세팅 가이드 6장)

## 3. 아키텍처 구성

### 3.1 플랫폼 (1회 구축 — Shared Services Account)

| 구성 요소 | 스펙 (기본안) | 비고 |
|:---|:---|:---|
| Coder 서버 | EC2 t3.large (또는 ECS Fargate) | 워크스페이스 오케스트레이션 |
| DB | RDS PostgreSQL db.t3.small | Coder 메타데이터 |
| 접속 | 내부 ALB(internal) + 사설 인증서 | 사내망 CIDR 한정 SG, 인터넷 인바운드 차단 |
| 인증 | Coder OIDC ← Entra ID | 기획안 3.3 SAML·SCIM 체계와 일원화 |

### 3.2 워크스페이스 (과제 승인 시 자동 생성 — 팀별)

| 구성 요소 | 내용 |
|:---|:---|
| 컴퓨트 | EC2 t3.xlarge (4 vCPU/16GB) 기본 — Coder 템플릿에서 팀별 조정 가능 |
| 이미지 | **골든 AMI (Packer 베이크)**: code-server(웹 VS Code) + Node.js + Claude Code CLI + AIFAB 하네스(전역 CLAUDE.md·commands·plugins) + git + AWS CLI |
| 하네스 최신화 | 워크스페이스 startup_script가 사내 GitLab의 하네스 레포를 pull하여 `~/.claude/` 갱신 |
| LLM 연동 | **Bedrock 키리스**: 인스턴스 IAM 롤에 `bedrock:InvokeModel*`(승인 모델·APAC 추론 프로파일 ARN 한정) + `CLAUDE_CODE_USE_BEDROCK=1` — API 키 배포·관리 없음 |
| 가동 정책 | autostop(유휴 자동 종료) + autostart — 시간제 가동. 업무시간 외 자동 셧다운 |
| 스토리지 | EBS 100GB/팀 (gp3) |

### 3.3 개발·배포 흐름 (골든 패스 연계)

1. **환경 확보**: 과제 승인 → Terraform이 Coder 워크스페이스 + GitLab 레포(골든 패스 스켈레톤) + CI/CD 파이프라인 자동 생성
2. **개발**: 브라우저 SSO 로그인 → 웹 VS Code 진입 → 터미널에서 `claude` 즉시 사용 (하네스 적용 상태)
3. **형상**: GitLab push / MR(머지 리퀘스트) — 리뷰는 3-lane 위험 분류 체계 적용
4. **파이프라인**: 머지 → CodePipeline → CodeBuild(빌드·테스트·Semgrep·gitleaks) → ECR push(Tag 불변) → Inspector 스캔 → 통과 시 Fargate dev/스테이징 자동 배포
5. **운영 반영(탑다운)**: 스테이징 검증 → AI Board·정보보호팀 승인 게이트 → Blue/Green 운영 배포(이상 징후 시 자동 롤백)

## 4. 구축 계획 (8월 골든 패스 기간 내 — Track A 편입)

| 주차 | 작업 | 완료 기준 |
|:---|:---|:---|
| 7월 5주~8월 1주 | Coder 플랫폼 구축 (서버·RDS·ALB·OIDC 연동) | Entra ID SSO 로그인 성공 |
| 8월 1~2주 | 골든 AMI 개발 (Packer — code-server·Claude Code·하네스 베이크), 워크스페이스 Terraform 템플릿 작성 | 워크스페이스 기동 → `claude` 실행 → Bedrock 응답 확인 |
| 8월 2~3주 | GitLab·CodePipeline 연계 E2E 검증, autostop 정책·Budgets 알람 적용 | 폼 입력 → 워크스페이스+레포+파이프라인 자동 생성 → 스테이징 배포 1시간 이내 |
| 8월 4주 | 통합 드라이런 (비개발자 대상) — **8/28 Readiness Review 항목 포함** | 드라이런 통과, 완비 선언 |

## 5. 비용 (서울 리전, USD/월, 개략 추정)

| 구분 | 파일럿 2~3팀 | 5팀 | 10팀 |
|:---|---:|---:|---:|
| 인프라 — 업무시간+유휴종료 | **약 250~300** | 약 405 | 약 660 |
| 인프라 — 상시 가동 시 | 약 500~600 | 약 955 | 약 1,760 |
| Claude Code 토큰 (Bedrock 종량제) | 스프린트당 약 400~900 | 약 900 | 약 1,800 |

- 플랫폼 고정비(서버+DB+ALB 약 150/월) 포함. Bedrock 토큰은 개발자 평균 $6/일 기준, 미사용 시 0
- 통제: 과제별 비용 태그 + AWS Budgets 80%/100% 알람 + 유휴 자동 종료

## 6. 운영·리스크

| 항목 | 내용 |
|:---|:---|
| 운영 공수 | 플랫폼(서버·DB·AMI) 유지보수 — AI 인프라팀 **월 0.5인 내외** 상정 |
| 버전 관리 | Coder 서버 분기별 버전업, 골든 AMI는 하네스 변경 시 재빌드 → 템플릿 버전 갱신 (기존 워크스페이스는 재기동 시 반영) |
| 백업 | RDS 자동 백업 7일, 워크스페이스는 코드가 GitLab에 있으므로 재생성 가능(펫이 아닌 캐틀 원칙) |
| 리스크 1 — 플랫폼 단일 장애점 | Coder 서버 장애 시 신규 워크스페이스 기동 불가(기동 중인 것은 유지) → 온콜 P1 대응(초동 30분), 서버 재구성 Runbook 준비 |
| 리스크 2 — 운영 공수 증가 | 확대 시 공수 재평가 — 20팀+ 규모에서 전담 0.5→1인 검토 |
| 정보보호팀 협의 연계 | 아웃바운드 화이트리스트(E-1)·웹 IDE 데이터 경로(E-2)는 협의사항 문서 기준으로 8월 중 확정 |

## 7. 참고 문서

- 비교 검토 원본(1안/2안·Terraform 골격·VPC Endpoint 목록): `../fab/26.07.13_AIFAB_웹IDE_개발환경_Terraform_세팅가이드_v1-0.md`
- 협의 사항: `AIFAB_AI인프라팀_정보보호팀_협의사항_최종_v1-0.md`
- 종합 계획(PMO 제출용): `AIFAB_기획_상세준비_운영계획_PMO제출_v1-0.md`
