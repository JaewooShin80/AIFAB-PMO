# AWS 기반 바텀업 샌드박스 구축·운영 기획안

팹 운영 현장 주도(Bottom-up) 과제 지원 플랫폼

- 문서 구분 : 운영 기획(안)
- 버전 : v2.0 (재작성본, 기존 보완본 통합)
- 작성일 : 2026. 07. 10.

---

## 1. 추진 배경 및 목적

### 1.1 추진 배경

- AIFAB 프로그램을 통해 사내 시티즌 개발자를 육성하였고, Capa Belt 과정에서 Claude Code 교육을 이수한 현장 개발 인력이 확보됨
- AIFAB 프로그램은 T2Y 달성을 목표로 하는 탑다운 AI 과제 수행을 위해 기획되었으나, 탑다운 과제 범위에 해당하지 않는 현장의 개선 아이디어를 수행할 방법론이 부재함
- 이에 AIFAB을 위해 마련한 샌드박스를 일부 확대하여, 일반 시티즌 개발자가 자율(바텀업) 과제를 수행할 수 있는 환경을 제공하고자 함
- 다만 통제 없는 자율 개발을 허용할 경우 보안·데이터·자원 관리 리스크가 발생하므로, 정책이 플랫폼 차원에서 강제되는 샌드박스 운영이 필요
- 과제 심사·모니터링·보고를 수작업으로 수행하면 운영 보드의 부담이 과다해지므로 AI 기반 자동화가 전제 조건
- 신속한 자원 생성·회수, 계정 단위의 격리, 관리형 AI 서비스(Amazon Bedrock) 활용을 위해 AWS 클라우드 기반으로 구축

### 1.2 목적

- AWS Organization으로 탑다운/바텀업 환경을 계정 수준에서 분리·격리하고, 바텀업 과제의 신청부터 배포·선셋까지 전 생애주기를 플랫폼으로 지원
- Amazon Bedrock(Claude) 기반 AI Agent로 과제 적합성 심사[^1]와 주간 리포트[^2]를 자동화하여 최소 인력으로 지속 운영 가능한 체계 확보
- Security by Design: 실데이터 사용 금지, 사내망 한정 접근, 트래픽 통제 등 보안 정책을 아키텍처에 내재화
- 우수과제의 탑다운 격상(마이그레이션) 파이프라인과 저활용 과제의 자동 선셋 체계 확보

### 1.3 적용 범위

과제 신청 → AI 사전심사 → 보드 승인 → 자원 프로비저닝 → 개발 → 배포 → 운영 모니터링 → 격상 또는 선셋에 이르는 바텀업 과제 전 생애주기와, 이를 지원하는 AWS 인프라·보안·자동화 체계 전반을 대상으로 한다.

## 2. 운영 정책 및 거버넌스

### 2.1 역할 분담(R&R)

| **주체** | **담당 범위** |
|:---|:---|
| 인프라(전산) | 샌드박스 사용자 확인·신청 프로세스, 전산자원 신청 프로세스 시스템 구현 및 AWS 플랫폼(Landing Zone) 운영 |
| 운영 보드 | 샌드박스 정책 수립, 하네스(공통 개발·실행 환경과 가드레일) 구성, 과제 적합성 심사·승인, 격상·선셋 최종 판단 |
| AI Agent (Bedrock) | 과제 적합성 사전 심사, 사용량 모니터링, 주간 리포트 자동 생성 등 보드 판단 업무 보조 |
| 정보보호팀 | 배포 구간 보안 요건 협의·승인, 정기 보안 점검, 보안 사고 대응 공조 |
| 과제 수행자(현업) | 과제 신청·개발·운영 오너십, 담당자 변경 시 이관 책임 |

### 2.2 운영 원칙 (Human-in-the-loop)

AI Agent는 판단을 보조하고 최종 승인 권한은 운영 보드가 보유한다. 에이전트의 판단 정확도가 검증되면 저위험 건부터 자동 처리 범위를 단계적으로 확대한다.

### 2.3 핵심 운영 정책

| **구분** | **정책** |
|:---|:---|
| 데이터 | 실데이터(운영 데이터) 사용 금지. 마스킹·비식별·합성 데이터 또는 승인된 샘플 데이터만 허용하며, 반입 시 등급 분류와 승인 절차 적용 |
| 접근 통제 | 사내망 한정 접근(인터넷 인바운드 차단), IAM Identity Center 기반 SSO와 최소권한 원칙 ([부록 A](#부록-a-접근-통제-정책-상세-해설) 참고) |
| 자원·트래픽 | 과제별 쿼터(컴퓨팅·스토리지·API 호출량)와 Rate Limit 적용, 임계치 초과 시 자동 알람·차단 |
| 산출물 통제 | 산출물·문서가 사외에서 열리지 않도록 기술적 강제(외부 공유 차단, 아웃바운드 화이트리스트, 문서 DRM·워터마크) |
| 감사 | 전 계정 CloudTrail 기록, 접근·배포·데이터 사용 이력 전수 보존, 정보보호팀 정기 점검 ([부록 B](#부록-b-cloudtrail-상세-해설) 참고) |

### 2.4 격상·선셋 기준

- 격상: 활성 사용자 수, 사용 빈도, 업무 효과(절감 공수), 안정성(오류율) 기준을 충족한 과제를 분기 단위로 보드가 심의하여 탑다운 공식 과제로 전환. 격상 시 코드 리뷰·문서화·실데이터 연동 재설계(보안 재심사)·정식 운영 조직 지정을 체크리스트로 관리
- 선셋(예시 기준, 보드 확정): 최근 4주 접속 0건 또는 주간 활성 사용자 기준 미달이 4주 지속되면 1차 알람 → 2주 유예 → 접속 차단 → 4주 보관 후 자원 회수·데이터 파기. 오너가 소명하면 보드 판단으로 연장 가능
- 담당자 퇴직·부서이동으로 오너가 없는(Orphan) 과제는 즉시 선셋 후보로 분류하여 이관 또는 종료 처리

## 3. AWS 전체 아키텍처

AWS Organization으로 Shared Services(공통), Top-down(공식 과제), Bottom-up Sandbox(자율 과제) 계정을 분리한다. Shared Services 계정에는 신청 포털과 승인 자동화(API Gateway, Lambda, Step Functions), Bedrock AI Agent, Terraform을 배치하고, 승인이 완료되면 Terraform이 Sandbox 계정에 표준 스택(ECS/Fargate, EC2, S3, RDS)을 자동 생성한다. CloudTrail, GuardDuty, Security Hub, CloudWatch는 전 계정 공통의 보안·관측 계층으로 운영한다.

![그림 1. AWS 전체 아키텍처 (계정 분리 및 신청·프로비저닝 흐름)](media/fig1-aws-architecture.png)

*그림 1. AWS 전체 아키텍처 (계정 분리 및 신청·프로비저닝 흐름)*

### 3.1 레이어별 서비스 구성

| **영역** | **AWS 서비스** | **역할** |
|:---|:---|:---|
| 계정 거버넌스 | AWS Organizations (SCP) | 탑다운/바텀업 계정 분리, 금지 행위의 조직 차원 차단 |
| 인증·권한 | IAM Identity Center | 사내 SSO 연동, 권한세트 기반 최소권한 부여 |
| 신청·승인 자동화 | API Gateway, Lambda, Step Functions | 신청 접수, 심사 워크플로, 승인·프로비저닝 오케스트레이션 |
| AI 심사·리포트 | Amazon Bedrock(Claude), Knowledge Bases | 적합성 사전 심사, 주간 리포트 자동 생성(RAG 기반) |
| IaC | Terraform (CloudFormation 병용 가능) | 과제별 표준 스택 자동 생성·회수 |
| 실행 환경 | ECS/Fargate, EC2, Lambda | 과제 앱 실행, 개발 서버, 경량 처리 ([부록 C](#부록-c-과제-앱ecsfargate-상세-해설) 참고) |
| 저장소 | S3, RDS, DynamoDB | 데이터·산출물 저장, 과제 DB, 심사 결과 저장 |
| 보안·관측 | CloudTrail, GuardDuty, Security Hub, CloudWatch, Config, Inspector, Macie | 감사 기록, 위협 탐지, 통합 대시보드, 로그·지표 |
| 분석·리포트 연계 | Athena + Databricks/Snowflake | 사용량 집계·분석, 리포트 데이터 공급 |

## 4. 네트워크(VPC/Subnet) 구성도

Bottom-up Sandbox 계정에 전용 VPC(예: 10.20.0.0/16)를 2개 가용영역으로 구성한다. 인바운드는 Direct Connect/VPN과 Transit Gateway를 경유한 사내망 트래픽만 허용하고 인터넷 인바운드는 차단한다. Public Subnet에는 내부 ALB와 NAT Gateway(허용 목록 기반 아웃바운드 전용)만 두고, 애플리케이션과 데이터는 Private Subnet에 분리 배치한다. S3·ECR·Bedrock·Logs 등 AWS 서비스 통신은 VPC Endpoint를 사용해 인터넷을 경유하지 않는다.

![그림 2. 네트워크(VPC/Subnet) 구성도](media/fig2-network-vpc.png)

*그림 2. 네트워크(VPC/Subnet) 구성도*

### 4.1 서브넷 설계(예시)

| **서브넷** | **CIDR(예시)** | **배치 자원** | **통신 정책** |
|:---|:---|:---|:---|
| Public (AZ-a/c) | 10.20.0.0/24, 10.20.1.0/24 | 내부 ALB, NAT GW | 사내망 인바운드만 허용, 아웃바운드는 도메인 화이트리스트 |
| Private App (AZ-a/c) | 10.20.10.0/24, 10.20.11.0/24 | ECS/Fargate, Lambda, 개발 EC2 | ALB 경유 수신, VPC Endpoint로 AWS 서비스 통신 |
| Private Data (AZ-a/c) | 10.20.20.0/24, 10.20.21.0/24 | RDS(KMS 암호화) | App 서브넷에서만 접근 허용(보안그룹 제한) |

## 5. 보안 아키텍처

보안은 계정·접근 통제, 네트워크 보안, 데이터 보호, 위협 탐지·감사의 4개 계층으로 설계하고 모든 탐지 결과를 Security Hub로 통합하여 보드와 정보보호팀에 알림(SNS)한다. 특히 Macie로 샌드박스 내 실데이터·개인정보 유입을 상시 탐지하여 "실데이터 사용 금지" 정책의 실효성을 기술적으로 담보한다.

![그림 3. 보안 아키텍처 (4계층 + 통합 탐지)](media/fig3-security-architecture.png)

*그림 3. 보안 아키텍처 (4계층 + 통합 탐지)*

### 5.1 계층별 통제 항목

| **계층** | **주요 통제** |
|:---|:---|
| 계정·접근 | Organizations SCP로 금지 행위 차단(리전 제한, 퍼블릭 리소스 생성 금지 등), Identity Center SSO·권한세트, IAM 최소권한 |
| 네트워크 | 인터넷 인바운드 차단, 내부 ALB + WAF, 보안그룹/NACL, PrivateLink(VPC Endpoint)로 인터넷 미경유 통신 |
| 데이터 | KMS 전 구간 암호화, S3 Block Public Access, 버킷 정책으로 계정 외 접근 차단, Macie 실데이터·PII 탐지 |
| 탐지·감사 | GuardDuty 위협 탐지, Inspector 이미지 취약점 점검, CloudTrail 조직 전체 기록, Config Rules 정책 준수 상시 점검 |

### 5.2 정보보호팀 협의 항목

- 배포 승인 게이트 기준(스테이징→운영 2단계)과 배포 전 자동 보안 점검 항목의 확정
- 아웃바운드 허용 도메인(화이트리스트) 목록과 예외 승인 절차
- 로그 보존 기간, 정기 취약점 점검 주기, 감사 리포트 공유 방식
- 보안 사고 발생 시 대응 절차(격리·차단 권한)와 책임 주체

## 6. AI Agent 아키텍처 (Amazon Bedrock 기반)

보드가 수행하던 반복 판단 업무를 두 개의 에이전트로 자동화한다. 심사 에이전트는 신청 접수 시 Step Functions 워크플로에서 Bedrock(Claude)을 호출해 과제를 사전 심사하고, 리포트 에이전트는 EventBridge 주간 스케줄로 사용량을 집계·요약해 배포한다.

![그림 4. AI Agent 아키텍처 (심사 에이전트 + 주간 리포트 에이전트)](media/fig4-ai-agent.png)

*그림 4. AI Agent 아키텍처 (심사 에이전트 + 주간 리포트 에이전트)*

### 6.1 심사 에이전트

- 판단 항목: ① 적합성(정책·보안 기준 부합) ② 중복성(기존 과제 카탈로그 대비) ③ 데이터 리스크(실데이터 요구·유출 위험) ④ 자원 적정성(요청 규모의 과다 여부)
- Knowledge Bases(RAG): 운영 정책 문서와 과제 카탈로그를 S3에 적재하고 OpenSearch 벡터 검색으로 근거를 조회하여 판단 정확도 확보
- 출력: 승인 권고 / 조건부 승인 / 보드 검토 필요의 3단계 분류와 판단 근거 리포트. 결과는 DynamoDB에 저장하고 SNS로 보드에 통지
- Bedrock Guardrails로 출력 범위를 통제하고, 보드의 최종 판정과 에이전트 권고의 불일치 사례를 축적해 심사 기준을 지속 보정(피드백 루프)

### 6.2 주간 리포트 에이전트

- EventBridge 주간 스케줄 → 사용량 집계(CloudWatch·Athena, Databricks/Snowflake 연계) → Bedrock 요약 생성 → SES 메일 발송 및 사내 위키(Confluence) 게시
- 리포트 구성: 신규 신청·승인 현황, 과제별 사용량·자원 사용률, 우수과제 후보, 선셋 후보, 배포 이력, 보안 이벤트

### 6.3 에이전트 거버넌스

- 최종 승인 권한은 보드 보유(HITL), 판단 로그·프롬프트·정책 버전을 모두 보존하여 감사 가능성 확보
- 정확도 검증 후 저위험 건 자동 승인, 선셋 알람·집행 자동화로 단계적 확대

## 7. CI/CD 및 배포 구조

바텀업 서버(샌드박스 계정)는 개발부터 사내 서비스 배포까지 지원한다. 과제별 Git 리포지토리에서 시작해 CodePipeline이 빌드·보안 스캔·스테이징 배포를 자동 수행하고, 운영 배포는 보드·정보보호팀의 승인 게이트를 통과해야 한다. 스캔 실패 시 파이프라인이 자동 차단된다. 인프라 변경은 Terraform 코드 리뷰(PR) 기반으로만 반영한다.

![그림 5. CI/CD 및 배포 구조](media/fig5-cicd.png)

*그림 5. CI/CD 및 배포 구조*

### 7.1 단계별 게이트

| **단계** | **자동/수동** | **통과 기준** |
|:---|:---|:---|
| 빌드·테스트 (CodeBuild) | 자동 | 단위 테스트 통과, 하드코딩 시크릿 미검출 |
| 이미지 스캔 (ECR·Inspector) | 자동 | Critical/High 취약점 0건 (기준은 정보보호팀 협의로 확정) |
| Staging 검증 | 자동 + 오너 | 기능 검증 완료, 정책 준수 체크 통과 |
| 운영 배포 승인 | 수동 | 보드·정보보호팀 승인 게이트 통과 |
| 배포 후 모니터링 | 자동 | 오류율·사용량 임계치 관리, 이상 시 알람 |

## 8. 데이터 흐름도

원본 운영 데이터는 샌드박스로 반출하지 않는다. 승인 절차를 거친 마스킹·비식별 처리본만 KMS로 암호화된 Landing 버킷에 반입하며, Macie가 실데이터·개인정보의 유입을 상시 탐지한다. 과제 사용 로그와 텔레메트리는 CloudWatch를 거쳐 로그 버킷에 적재되고, Databricks/Snowflake에서 집계된 뒤 Bedrock이 주간 리포트로 요약하여 보드·경영진에 전달된다. 사외 접근·반출 경로는 정책과 기술 통제로 차단한다.

![그림 6. 데이터 흐름도 (반입 → 사용 → 텔레메트리 → 리포트)](media/fig6-data-flow.png)

*그림 6. 데이터 흐름도 (반입 → 사용 → 텔레메트리 → 리포트)*

### 8.1 구간별 데이터 통제

| **구간** | **통제 방안** |
|:---|:---|
| 반입 | 마스킹·비식별 처리와 반입 승인 절차, Macie 자동 탐지로 이중 확인 |
| 저장 | KMS 암호화, S3 Block Public Access, 버킷 정책으로 계정 외 접근 차단 |
| 사용 | 과제별 IAM 격리, 자원·API 쿼터, 접근 이력 전수 기록(CloudTrail) |
| 반출 | 아웃바운드 화이트리스트, 외부 공유 차단, 산출물 사외 열람 방지(DRM·워터마크), DLP 연계 검토 |

## 9. 운영 프로세스 (BPMN)

신청부터 격상·선셋까지의 운영 프로세스를 BPMN 표기로 정의한다. 색상은 담당 주체(신청자·AI 에이전트·운영 보드·자동화)를 나타내며, 게이트웨이(마름모)에서 승인 여부와 사용량 판정에 따라 경로가 분기한다.

![그림 7. 운영 프로세스 (BPMN 표기 기반)](media/fig7-bpmn-process.png)

*그림 7. 운영 프로세스 (BPMN 표기 기반)*

### 9.1 단계별 정의

| **단계** | **수행 주체** | **내용** | **목표 소요** |
|:---|:---|:---|:---|
| 신청 접수 | 과제 신청자 | 포털에서 목적·기대효과·필요 데이터·필요 자원 입력 | 즉시 |
| AI 사전심사 | AI 에이전트 | 적합성·중복성·데이터 리스크·자원 적정성 판단, 근거 리포트 생성 | 10분 이내 |
| 보드 승인 | 운영 보드 | 에이전트 근거 확인 후 승인·조건부 승인·반려 결정 | 3영업일 이내 |
| 자원 프로비저닝 | 자동화 | Terraform으로 과제별 표준 스택 자동 생성 | 30분 이내 |
| 개발·배포 | 신청자/자동화 | CI/CD 파이프라인, 보안 스캔과 승인 게이트 통과 후 운영 배포 | 과제별 상이 |
| 운영 모니터링 | 자동화 | 사용량 텔레메트리 수집, 주간 리포트 자동 생성 | 주 1회 |
| 격상 / 선셋 | 보드/자동화 | 우수과제 분기 심의·탑다운 이관 / 저활용 과제 알람·유예·자원 회수 | 분기 / 상시 |

## 10. 단계별 구축 로드맵

| **단계** | **기간(예시)** | **주요 작업** | **산출물** |
|:---|:---|:---|:---|
| 1단계: Landing Zone | M1 ~ M2 | Organizations 계정 분리(SCP), Identity Center SSO, VPC·사내망 연동, 기본 보안(CloudTrail·GuardDuty·Security Hub) | 격리된 샌드박스 기반 환경 |
| 2단계: 신청 자동화 | M2 ~ M3 | 신청 포털, API Gateway·Lambda·Step Functions 워크플로, Terraform 표준 모듈, 쿼터·태깅 표준 | 신청부터 자원 생성까지 자동화 |
| 3단계: AI Agent·CI/CD | M3 ~ M5 | Bedrock 심사 에이전트와 Knowledge Base, 주간 리포트 에이전트, CodePipeline 표준 파이프라인·승인 게이트 | 자동 사전심사·리포트, 배포 체계 |
| 4단계: 정착·고도화 | M5 ~ M6 | 격상·선셋 자동화, 저위험 건 자동 승인 확대, 비용 최적화(Spot·수명주기) | 전 생애주기 운영 정착 |

기간은 예시이며, 정보보호팀 협의 일정과 사내망 연동(Direct Connect/VPN) 리드타임에 따라 조정한다.

## 11. 예상 비용 및 AWS 서비스 구성

### 11.1 산정 전제

- 서울 리전(ap-northeast-2), 과제 10~15개 상시 운영 규모 가정
- 2026년 상반기 요금 수준 기준의 개략 추정치이며, 확정 시 AWS Pricing Calculator로 재산정 필요
- Direct Connect 회선료, Databricks/Snowflake 라이선스, 인건비는 제외

### 11.2 월 예상 비용(추정)

| **항목** | **구성 가정** | **월 예상(USD)** |
|:---|:---|:---|
| ECS/Fargate | 상시 태스크 10개(0.5 vCPU / 1GB) + 스테이징 여유분 | 약 250 |
| EC2 개발 서버 | m5.large 2대 (야간 자동 중지 적용 전 기준) | 약 170 |
| RDS | db.t3.medium 2대(과제 공용) + 스토리지 | 약 180 |
| 네트워킹 | 내부 ALB, NAT Gateway, VPC Endpoint 5종 | 약 150 |
| S3·로그 | 데이터 2TB + CloudWatch Logs | 약 80 |
| Bedrock (Claude) | 심사·리포트 월 2,000건, 평균 입력 10K/출력 2K 토큰 | 약 100 ~ 200 |
| 보안 서비스 | GuardDuty, Security Hub, Config, Inspector, Macie | 약 120 |
| CI/CD·기타 | CodeBuild, ECR, DynamoDB, Step Functions, SNS/SES | 약 50 |

**합계: 월 약 1,100 ~ 1,200 USD (환율 1,400원/USD 기준 약 150 ~ 170만 원) 수준으로 추정된다. Bedrock은 사용량 과금이므로 과제 수와 호출량 증가에 비례한다.**

### 11.3 비용 최적화 방안

- 저활용 과제의 자동 선셋으로 유휴 자원 즉시 회수 (본 기획의 핵심 비용 통제 장치)
- 비운영 워크로드에 Fargate Spot 적용, 개발 서버 야간·주말 자동 중지
- S3 수명주기 정책(로그 장기 보관은 Glacier 계열 전환), 운영 정착 후 Savings Plans 검토

## 12. 기대 효과

### 12.1 정량 효과

- 심사 리드타임 단축: 수작업 심사 수 일 → AI 사전심사 10분 + 보드 확인으로 1일 이내 목표
- 환경 준비 시간 단축: 과제별 개발환경 수작업 구성 수 주 → Terraform 자동 프로비저닝 30분 이내
- 보드 운영 공수 절감: 심사·모니터링·주간 보고 자동화로 반복 업무 최소화
- 유휴 자원 자동 회수(선셋)로 클라우드 비용 상시 통제

### 12.2 정성 효과

- 보안 정책(실데이터 금지·사내망 한정·트래픽 통제)이 플랫폼에 내재화되어, 리스크 통제 하에 현장 주도 혁신 확산
- 우수과제의 탑다운 격상 파이프라인 확보로 바텀업 성과의 전사 확산
- 계정 수준 격리로 바텀업 과제의 장애·부하가 공식(탑다운) 환경에 영향을 주지 않음
- 주간 리포트 기반의 데이터 중심 의사결정과 감사 대응력 확보

### 12.3 운영 KPI

신청 건수, 승인율, 활성 과제 수, 격상 건수, 절감 공수, 평균 심사 소요시간, 선셋 회수 자원(비용)을 분기 단위로 측정하여 플랫폼 효과를 정량 관리한다.

## 부록 A. 접근 통제 정책 상세 해설

2.3 핵심 운영 정책의 "접근 통제" 항목은 **네트워크 → 인증 → 인가**로 이어지는 3중 방어 체계를 한 줄로 요약한 것이다. 각 계층이 독립적으로 작동하여, 어느 한 층이 무력화되어도 나머지 계층이 피해 확산을 차단하는 심층 방어(Defense in Depth) 구조를 이룬다.

### A.1 사내망 한정 접근 (인터넷 인바운드 차단)

"어디서 접근할 수 있는가"를 통제하는 네트워크 경계 정책이다.

- **인바운드(Inbound)** 는 외부에서 샌드박스로 들어오는 트래픽을 의미하며, 이를 인터넷 기준으로 전면 차단한다. 즉, 공인 IP를 통해 샌드박스의 어떤 자원에도 접속할 수 없다.
- 접속 가능한 유일한 경로는 사내망이다. 4장 네트워크 구성 기준으로 사내 PC → Direct Connect(전용회선)/VPN → Transit Gateway → 샌드박스 VPC의 내부 ALB 경로만 허용되며, 이 경로를 경유하지 않으면 네트워크 수준에서 도달 자체가 불가능하다.
- 반대 방향인 **아웃바운드**(샌드박스 → 외부)는 전면 차단이 아니라, NAT Gateway를 통해 허용 목록(화이트리스트)에 등록된 도메인만 통과하도록 제한한다(예: 패키지 저장소).
- **목적**: 인터넷에 노출된 서버는 상시 자동화 공격의 대상이 된다. 인바운드를 차단하면 외부 공격 표면(attack surface)이 제거되고, 개발자가 취약한 앱을 배포하더라도 사외 접근이 불가능하므로 피해가 사내로 한정된다.

### A.2 IAM Identity Center 기반 SSO

"누구인가"를 확인하는 인증 정책이다. IAM Identity Center는 AWS의 통합 로그인 서비스(구 명칭 AWS SSO)이다.

- **SSO(Single Sign-On)**: 사내 계정(사내 IdP 연동) 하나로 로그인하면 AWS 계정마다 별도 ID/비밀번호를 생성하지 않고 허용된 모든 AWS 계정에 접근한다.
- **계정별 IAM User를 생성하지 않는 것이 핵심**이다. IAM User는 장기 비밀번호·액세스 키를 보유하게 되어 유출 사고의 주요 원인이 되지만, Identity Center는 로그인 시마다 수 시간 단위의 **임시 자격 증명**을 발급하므로 유출되어도 곧 만료된다.
- **퇴직·부서이동 시** 사내 인사 시스템/IdP에서 계정을 비활성화하면 AWS 접근도 자동으로 차단된다. 이는 2.4의 "Orphan 과제 즉시 선셋" 정책이 실제 작동할 수 있는 기술적 기반이다.
- 접근 권한은 **Permission Set**(권한 묶음) 단위로 "사용자 → 계정 → 역할"을 매핑한다. 예: 과제 수행자 A → Sandbox 계정의 `SandboxDeveloper` 권한세트.

### A.3 최소권한 원칙 (Principle of Least Privilege)

"무엇을 할 수 있는가"를 통제하는 인가 정책이다.

- 업무 수행에 필요한 최소한의 권한만 부여하고 그 외는 전부 거부한다.
- 예시: 과제 A 수행자는 자기 과제에 태깅된 ECS 서비스·S3 버킷·RDS만 접근할 수 있고, 다른 과제의 리소스는 조회조차 불가하며, IAM 정책 수정·VPC 변경 같은 인프라 권한은 부여되지 않는다(인프라 변경은 7장의 Terraform PR로만 수행).
- 5.1의 **Organizations SCP**와 계층 구조를 이룬다. SCP는 조직 차원에서 "누구도 절대 할 수 없는 행위"(퍼블릭 리소스 생성, 리전 이탈 등)를 정의하는 상한선이고, 최소권한 원칙은 그 아래에서 개인별로 "할 수 있는 행위"를 좁히는 개념이다.
- **목적**: 계정 탈취나 실수가 발생해도 피해 범위(blast radius)가 해당 사용자가 보유한 최소 권한 이내로 한정된다.

### A.4 3중 방어 체계 종합

| 계층 | 통제 질문 | 수단 | 해당 계층이 뚫린 경우 |
|:---|:---|:---|:---|
| 네트워크 | 어디서 오는가 | 사내망 한정, 인터넷 인바운드 차단 | 사내망에 있어도 로그인(인증) 필요 |
| 인증 | 누구인가 | Identity Center SSO, 임시 자격 증명 | 로그인해도 권한(인가) 없으면 무력 |
| 인가 | 무엇을 할 수 있는가 | 최소권한, Permission Set, SCP | 피해가 개인 권한 범위로 한정 |

## 부록 B. CloudTrail 상세 해설

2.3 핵심 운영 정책의 "감사" 항목과 5.1 "탐지·감사" 계층의 근간이 되는 서비스로, AWS 계정 안에서 일어난 **모든 API 호출을 기록하는 감사(Audit) 서비스**이다. AWS에서는 콘솔 조작, CLI 명령, SDK 호출, 서비스 간 자동 호출이 전부 API 호출로 처리되므로, CloudTrail을 활성화하면 "계정 안에서 누가 무엇을 했는지"의 전수 기록이 남는다.

### B.1 이벤트 기록 항목

| 항목 | 내용 | 예시 |
|:---|:---|:---|
| 누가 (userIdentity) | 호출 주체 — SSO 사용자, 역할, 서비스 | `SandboxDeveloper` 권한세트의 과제 수행자 |
| 언제 (eventTime) | UTC 타임스탬프 | 2026-07-10T09:12:33Z |
| 어디서 (sourceIPAddress) | 호출 발신 IP | 사내망 IP 또는 AWS 서비스 |
| 무엇을 (eventName) | API 액션 | `RunInstances`(EC2 생성), `DeleteBucket` |
| 대상 (resources) | 어떤 리소스에 | 특정 S3 버킷, RDS 인스턴스 |
| 결과 | 성공/실패, 거부 사유 | `AccessDenied` 포함 — 시도 자체도 기록됨 |

### B.2 이벤트 종류

1. **관리 이벤트 (Management Events)** — 기본 제공. 리소스 생성·수정·삭제, 콘솔 로그인, IAM 권한 변경 등 제어 영역 작업. 대부분의 감사 요구를 충족한다.
2. **데이터 이벤트 (Data Events)** — 선택 활성화(추가 비용). S3 객체 단위 읽기/쓰기, Lambda 함수 실행 등 고빈도 작업. "데이터 사용 이력 전수 보존" 정책상 민감 버킷(Landing 버킷 등)에는 활성화가 필요하다.
3. **Insights 이벤트** — API 호출량의 비정상 급증 등 이상 패턴 자동 탐지(선택).

### B.3 "전 계정 CloudTrail 기록"의 의미 — Organization Trail

- 관리 계정(또는 위임된 Shared Services 계정)에서 조직 트레일(Organization Trail) 하나를 구성하면 Shared Services / Top-down / Bottom-up Sandbox **전 멤버 계정의 로그가 자동 수집**되며, 신규 계정 생성 시에도 자동 포함된다.
- 로그는 중앙 S3 버킷(로그 전용 계정 권장)에 저장되며, **멤버 계정(샌드박스 사용자)은 트레일을 중지하거나 로그를 수정·삭제할 수 없다.** 과제 수행자가 자신의 흔적을 지울 수 없다는 점이 감사 실효성의 핵심이다.
- 무결성 보장: 로그 파일 검증(digest 파일 기반 변조 탐지), KMS 암호화, 필요 시 S3 Object Lock으로 보존 기간 내 삭제 불가 처리 — 5.2의 "로그 보존 기간" 협의 항목과 연결된다.

### B.4 다른 구성 요소와의 관계

| 구성 요소 | 관계 |
|:---|:---|
| GuardDuty (5.1) | CloudTrail 이벤트를 입력으로 위협 탐지(비정상 IP의 API 호출, 자격 증명 탈취 의심 등). CloudTrail이 기록하고 GuardDuty가 해석 |
| Athena (3.1) | S3에 적재된 로그를 SQL로 조회. "지난 분기 특정 버킷 접근자 전체 목록" 같은 감사 질의에 활용 |
| CloudWatch | 역할 구분에 유의 — CloudWatch는 "시스템이 어떻게 돌고 있나"(지표·앱 로그, 운영 모니터링), CloudTrail은 "누가 무엇을 했나"(감사). 9.1의 사용량 모니터링은 CloudWatch, 2.3의 감사는 CloudTrail 담당 |
| 부록 A (접근 통제) | A.2~A.3이 사전 통제(인증·인가)라면 CloudTrail은 사후 추적. 최소권한을 벗어난 시도(`AccessDenied`)도 기록되므로 권한 설계 허점을 발견하는 피드백 자료가 됨 |

### B.5 본 샌드박스에서의 역할

1. **실데이터 금지 정책의 증빙** — Macie 탐지 시 CloudTrail로 "누가 언제 해당 데이터를 반입했는지" 역추적
2. **보안 사고 포렌식** — 사고 타임라인 재구성의 유일한 원천
3. **격상 심사 자료** — 과제의 실제 자원 사용 패턴 검증
4. **감사 대응** — 정보보호팀 정기 점검(2.3) 및 대외 감사 시 전수 이력 제시

## 부록 C. 과제 앱(ECS/Fargate) 상세 해설

그림 1의 Bottom-up Sandbox 계정 내 "과제 앱(ECS/Fargate)"은 **승인된 바텀업 과제의 애플리케이션이 사내 사용자에게 서비스되는 컨테이너 기반 실행 환경**이다.

### C.1 과제 앱의 정의와 표준 스택

과제 앱은 시티즌 개발자가 만든 바텀업 과제의 실제 서비스(예: 설비 점검 일지 자동 요약 대시보드)가 실행되는 곳이다. 승인 워크플로를 통과하면 Terraform이 과제별 표준 스택 4종을 자동 생성하며, 과제 앱은 그 중 서비스 실행을 담당한다.

| 구성 요소 | 역할 |
|:---|:---|
| **과제 앱 (ECS/Fargate)** | 완성된 앱이 실제 서비스로 실행되는 곳 |
| 개발 서버 (EC2) | 개발자가 코드를 작성·테스트하는 작업 공간 |
| S3 | 데이터·산출물 저장 |
| RDS | 앱이 사용하는 데이터베이스 |

생애주기 흐름: 개발 서버에서 개발 → CI/CD 파이프라인(7장) 통과 → 과제 앱(ECS/Fargate)에 배포 → 사내 사용자가 내부 ALB를 통해 접속.

### C.2 ECS/Fargate 개념

- **ECS (Elastic Container Service)**: AWS의 컨테이너 실행·관리 서비스. 앱을 컨테이너(Docker 이미지)로 포장해 올리면 배포·재시작·확장을 AWS가 관리한다.
- **Fargate**: ECS의 실행 방식 중 하나로, 서버(EC2) 없이 컨테이너만 실행하는 **서버리스 방식**. "0.5 vCPU / 1GB 메모리로 이 컨테이너를 실행"처럼 선언하면 해당 자원만 할당되고, 하부 서버·OS는 AWS가 운영한다.

### C.3 Fargate 선택 사유 — 운영 정책과의 정합성

1. **시티즌 개발자에게 서버 관리를 요구하지 않음** — OS 패치, 보안 업데이트 등 운영 부담이 없어 전문 인프라 지식 없이도 앱을 서비스로 배포할 수 있다.
2. **쿼터 강제가 용이** — 태스크당 자원 상한(0.5 vCPU/1GB 등)을 선언적으로 고정할 수 있어 2.3의 "과제별 쿼터" 정책이 자연스럽게 구현된다. 11.2 비용표의 "상시 태스크 10개"는 과제 약 10개의 앱이 각각 1개 태스크로 실행되는 규모를 의미한다.
3. **선셋(회수)이 즉각적** — 관리할 서버가 없으므로 태스크 정의 삭제만으로 자원이 즉시 회수된다. Terraform 자동 생성·회수 체계와 정합적이다.
4. **과제 간 격리** — 컨테이너 단위로 분리되어 한 과제 앱의 장애·부하가 다른 과제에 영향을 주지 않는다.

---

[^1]: AI 기반 심사 자동화 유사 사례: ① AWS는 Bedrock Agents로 서류 검증·리스크 평가를 수행한 뒤 적격 건은 자동 승인하고 복잡한 건은 인적 검토로 회부하는 모기지 심사 자동화 아키텍처를 공개 — 본 기획의 3단계 분류(승인 권고/조건부/보드 검토) 및 HITL 구조와 동일 패턴 ([Autonomous mortgage processing using Amazon Bedrock Data Automation and Amazon Bedrock Agents, AWS ML Blog](https://aws.amazon.com/blogs/machine-learning/autonomous-mortgage-processing-using-amazon-bedrock-data-automation-and-amazon-bedrock-agents/)). ② 멀티 에이전트 워크플로로 대규모 콘텐츠의 정확성 검증·근거 조회·개선 권고를 자동화한 콘텐츠 심사 사례 ([Scaling content review operations with multi-agent workflow, AWS ML Blog](https://aws.amazon.com/blogs/machine-learning/scaling-content-review-operations-with-multi-agent-workflow/)). ③ 국내 사례로 KCC는 Bedrock Tool Use 기반 멀티 에이전트 플랫폼을 구축해 부서별 반복 판단 업무를 자동화 ([KCC의 Amazon Bedrock Tool Use를 활용한 Multi Agent 플랫폼 구축 사례, AWS 기술 블로그](https://aws.amazon.com/ko/blogs/tech/kcc-aws-bedrock-tool-use-multi-agent-platform/)). 승인 전 인적 확인(HITL) 구현 패턴은 [Implement human-in-the-loop confirmation with Amazon Bedrock Agents (AWS ML Blog)](https://aws.amazon.com/blogs/machine-learning/implement-human-in-the-loop-confirmation-with-amazon-bedrock-agents/) 참고.

[^2]: AI 기반 리포트·모니터링 자동화 유사 사례: ① BGL은 Claude Agent SDK와 Bedrock AgentCore로 사내 데이터 분석·리포트 생성을 자동화하여 비개발 부서도 BI를 활용하도록 확산 ([Democratizing business intelligence: BGL's journey with Claude Agent SDK and Amazon Bedrock AgentCore, AWS ML Blog](https://aws.amazon.com/blogs/machine-learning/democratizing-business-intelligence-bgls-journey-with-claude-agent-sdk-and-amazon-bedrock-agentcore/)). ② SK텔레콤은 Bedrock 기반 Claude 파인튜닝으로 상담 품질 평가·상담 후처리(요약) 업무를 자동화해 저품질 응답 68% 감소, 후처리 품질 인간 상담사 대비 약 89% 달성 ([SK Telecom 고객 사례, Anthropic](https://claude.com/customers/skt) / [SK Telecom improves telco-specific Q&A by fine-tuning Anthropic's Claude models in Amazon Bedrock, AWS ML Blog](https://aws.amazon.com/blogs/machine-learning/sk-telecom-improves-telco-specific-qa-by-fine-tuning-anthropics-claude-models-in-amazon-bedrock/)).
