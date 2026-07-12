# 딥 리서치 보고서 — AI FAB 탑다운 과제 파일럿 운영 방안: 시티즌 개발자 선발부터 3주 스프린트 배포·종료까지 운영 시나리오

> 생성: 2026-07-11 | 메타서치 단계 2 산출물 | 브리프: 01-topic-brief.md

---

## 1. Executive Summary

AI FAB 탑다운 파일럿 운영의 엔드투엔드 시나리오는 **선발 → 3주 스프린트 → 배포 게이트 → 종료·이관**의 4단계 흐름으로 설계할 수 있다. 내부 기획안(탑다운 AIFAB v1-0)은 AWS 인프라·배포 파이프라인·격상 절차·SLO 운영을 구체적으로 정의하고 있으나, 시티즌 개발자 선발 기준, 3주 스프린트 주차별 구조, 멘토링·오피스아워 등 사람 중심 지원 체계, 파일럿 KPI는 직접 다루지 않아 외부 사례 보완이 필수다. 선발은 비즈니스 검토 → 기술 검토 2단계 심사(8개 가중 기준)를 거쳐 3~5명 혼합팀을 구성하는 것이 업계 모범 사례이며, 스프린트 구조는 Agile-Stage-Gate 하이브리드(W1 킥오프·Gate 0 → W2 개발·중간 게이트 → W3 완성·배포 승인 게이트)가 기업 거버넌스 요건에 가장 부합한다. 지원 체계는 CoE 2~5명 전담 + 주 1회 이상 오피스아워 + 1:1 멘토 페어링 구조가 표준이며, 거버넌스 있는 조직의 비용 절감 성공률(77%)이 없는 조직(39%)보다 2배 높아 파일럿 단계부터 CoE를 병행 운영해야 한다. KPI는 킥오프 전 동결하고 배포 완성 건수·사이클 타임·거버넌스 준수율·참여자 만족도를 3주 단위로 측정하며, 확대 판단은 DECIDE 프레임워크 4대 질문(결과 KPI 달성·비용 대비 가치·거버넌스 수용성·변화 관리 준비도)로 수행한다. 종료·이관 시에는 파일럿 시작 전 합의한 Go/No-Go 스코어카드(4영역 가중 점수 0.605 이상)를 기준으로 Scale/Stop/Redirect를 결정하고, 내부 기획안의 7단계 격상 체크리스트 및 AWS 계정 라이프사이클 자동화를 적용하면 리소스 회수·이관이 체계화된다.

---

## 2. 핵심 질문별 발견

### 2.1 시티즌 개발자 선발 기준·절차

**핵심 발견**

- **파일럿 부서 선정**: 강한 관심을 표명하고, 명확한 자동화/개발 백로그가 있으며, 내부 챔피언이 1명 이상인 2~3개 비즈니스 유닛을 우선 선정한다. ([Kissflow - Citizen Developer Program](https://kissflow.com/no-code/citizen-developer-program/), 날짜 미상)

- **팀 구성 원칙**: 팀 규모 3~6명(최적 3~5명), 최소 1명의 비엔지니어(도메인 전문가·디자이너·운영 담당) 포함 필수. 전사 기술직+비기술직 혼합 구성이 가장 강력한 결과를 낸다. ([Innovation Mode - Corporate Hackathon Template](https://theinnovationmode.com/corporate-hackathon-template), 날짜 미상)

- **참가자 자격 기준**: IT 비전공자 명시 환영, 스프레드시트 등 기존 도구 숙련, 업무 프로세스 전문성 보유, 노코드/로우코드 배우려는 의지 — 이 4가지가 이상적인 시티즌 개발자 후보의 특성이다. ([UiPath - What is Citizen Development](https://www.uipath.com/rpa/what-is-citizen-development), 날짜 미상)

- **부서장 승인 절차**: 직속 상사 승인을 통해 업무 시간 일정 부분을 파일럿 과제에 할당하는 것이 모범 사례이며, 경영진 후원(executive sponsorship) 확보가 프로그램 성공의 전제 조건이다. ([CIO.com - 성공적인 해커톤의 비밀](https://www.cio.com/article/3530262/), 날짜 미상)

- **과제 심사 2단계 구조**: 1단계(도메인 전문가 폐쇄형 점수화) → 2단계(상위 5팀 경영진 패널 공개 발표). 8개 가중 기준(문제 중요성, 전략 테마 부합도, 실현 가능성, 개념 효과성, 개발 용이성, 운영 단순성, 잠재적 영향력, 혁신 수준)으로 평가한다. ([Innovation Mode](https://theinnovationmode.com/corporate-hackathon-template), 날짜 미상)

- **CoE 과제 검토 프로세스**: 비즈니스 검토(넓은 사용자에게 이익이 되는지) → 기술 검토(코드 품질·확장 준비도) 2단계를 거쳐 CoE 또는 시티즌 개발자 승인으로 연결. 역할은 셀프 유저, 파워 유저, 비즈니스 검토자, 기술 검토자 4종으로 구분한다. ([UiPath Automation Hub - Citizen Developer Framework](https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/understanding-the-citizen-developer-framework ⚠(dead link)), 날짜 미상)

- **국내 사례 — LG유플러스**: 탑다운(핵심 과제 전담 개발자 육성)·바텀업(전 직원 자동화 과제 개발 장려) 이원화 방식으로 국내 최초 RPA 시민개발자 모델 도입. 선발 인원을 초급·중급·고급·특급 4등급으로 분류해 등급별 혜택 부여. 2년 후 170개 이상 RPA 개선 과제, 약 50명 양성. ([UiPath - LG유플러스 시민개발자 사례](https://www.uipath.com/ko/resources/automation-case-studies/lguplus), 날짜 미상)

- **내부 기획안 관점**: 탑다운 과제 수행 주체를 "지정된 개발·운영 조직"으로 전제하며 시티즌 개발자 선발 기준·절차를 직접 다루지 않는다. 파일럿 운영 시나리오 설계 시 외부 모범 사례를 기준으로 별도 선발 절차를 수립해야 한다. (내부: AWS_기반_탑다운_AIFAB_과제_운영환경_구축운영_기획안_v1-0.md §2. 바텀업 샌드박스와의 차이)

| 항목 | 수치 | 출처 | 시점 |
|---|---|---|---|
| 파일럿 대상 비즈니스 유닛 수 | 2~3개 | Kissflow | 날짜 미상 |
| 파일럿 기간 (업계 표준) | 90일 | Kissflow | 날짜 미상 |
| 부서당 최대 사용 사례 수 | 5개 | Kissflow | 날짜 미상 |
| 권장 팀 규모 | 3~6명(최적 3~5명) | Innovation Mode | 날짜 미상 |
| CoE 구성 인원 | 2~5명 | Kissflow | 날짜 미상 |
| 과제 심사 기준 항목 수 | 8개 가중 기준 | Innovation Mode | 날짜 미상 |
| 2단계 심사 진출 팀 수(예시) | 상위 5팀 | Innovation Mode | 날짜 미상 |
| LG유플러스 양성 RPA 개발자 수 | 약 50명 | UiPath LG유플러스 사례 | 날짜 미상 |
| LG유플러스 RPA 개선 과제 수(2년 후) | 170개 이상 | UiPath LG유플러스 사례 | 날짜 미상 |

---

### 2.2 3주 스프린트 주차별 운영 구조 (W1/W2/W3)

**핵심 발견**

- **3주 스프린트의 가장 검증된 패턴**: "1주 계획·정제 + 2주 순수 개발" 구조. 1주차에 모든 회의·스토리 정제·기술 탐색을 집중하고, 2~3주차는 맥락 전환 없이 개발에만 몰두한다. ([John Wakeling Blog](https://www.johnwakeling.co.uk/posts/3-week-sprints/), 날짜 미상)

- **Agile-Stage-Gate 하이브리드 모델**: 스프린트 종료 시점에 게이트(Go/Kill/Hold/Recycle)를 배치하여 애자일 개발 속도와 기업 거버넌스 요구를 동시에 충족. 게이트 의사결정 목표는 "24~48시간 이내". ([Umbrex Stage-Gate Innovation Process](https://umbrex.com/resources/frameworks/strategy-frameworks/stage-gate-innovation-process/), 날짜 미상)

- **기업 거버넌스 대응 패턴 C (Agile-Stage-Gate 하이브리드)** — AI FAB에 가장 적합한 구조로 판단:
  - **W1 (Gate 0 → 스프린트 1)**: 킥오프, 요구사항 확정, Gate 0(착수 승인), 1차 스프린트 실행. 스프린트 플래닝 최대 6시간(주당 2시간 × 3주 기준).
  - **W2 (스프린트 2 + 중간 게이트)**: 기능 증분 데모, Gate 1(중간 리뷰, 24~48h 내 결정), 피벗 여부 결정.
  - **W3 (스프린트 3 + Gate 2 + 배포)**: 최종 완성, Gate 2(배포 승인 — 내부 기획안의 AI Board·정보보호팀 수동 승인과 연계), 프로덕션 배포, 데모데이, 이관 계획 수립.

- **내부 기획안 배포 승인 게이트**: 스테이징 배포·검증 통과 후 AI Board·정보보호팀 승인 게이트(수동) → Blue/Green 또는 Rolling 무중단 배포 → 실패 시 자동 롤백. CI/CD 통과 기준: 단위 테스트 통과·하드코딩 시크릿 미검출(자동), Critical/High 취약점 0건(자동), 기능·성능 검증·정책 준수(자동+오너), 그 후 수동 승인 게이트. (내부: AWS_기반_탑다운_AIFAB_과제_운영환경_구축운영_기획안_v1-0.md §5. 개발·배포)

- **해커톤·부트캠프 공통 체크포인트 3종**: 킥오프 콜 → 중간 AMA(Mid-event check-in) → 최종 데모 세션. 중간 체크포인트는 팀이 방향을 피벗할 수 있는 공식 기회를 제공한다. ([Hackathon Guide](https://hackathon.guide/), 날짜 미상)

- **해커톤 이후 프로덕션 전환 사전 계획 필수**: 수상작의 다음 단계 경로(파일럿, 액셀러레이터 편입)를 해커톤 시작 전에 미리 합의해 두어야 한다. ([Klipfolio Hackathon Guide](https://www.klipfolio.com/blog/run-hackathon), 날짜 미상)

- **AI App Bootcamp 12일 구조 사례**: Day1-2 아이디어·설정, Day3-6 핵심 기능 개발, Day7-8 UI 디자인, Day9-10 배포·최종 조정, Day11-12 커스텀 통합. 주 단위 오피스아워, 그룹 체크포인트, "MVP Roast" 피드백 세션을 구조화. ([AI Build Accelerator](https://build.starterstory.com/build/ai-build-accelerator), 날짜 미상)

| 항목 | 수치 | 출처 | 시점 |
|---|---|---|---|
| 3주 스프린트 플래닝 권장 시간 | 6시간 (주당 2시간 × 3주) | Atlassian Scrum Sprints | 날짜 미상 |
| Agile-Stage-Gate 게이트 결정 목표 시간 | 24~48시간 이내 | Umbrex Stage-Gate | 날짜 미상 |
| Agile-Stage-Gate 스프린트 표준 기간 | 1~4주 | Profit.co | 날짜 미상 |
| 데모데이 팀당 발표 시간 (내부 해커톤) | 5~10분 | Klipfolio | 날짜 미상 |
| 국내 DX 스프린트 해커톤 기간 | 2주 (개발~출시까지) | 파이낸셜뉴스 | 2023-07-17 |
| CI/CD 취약점 통과 기준 | Critical/High 0건 | 내부 기획안 §5 | 2026.07.11 |

---

### 2.3 파일럿 기간 중 지원 체계

**핵심 발견**

- **CoE(Center of Excellence) 구성**: 2~5명 소규모 전담팀. 프로그램 프레임워크 소유, 사용 사례 승인, 플랫폼 표준 유지, 시티즌 개발자 안내·검수 담당. ([Kissflow - Citizen Developer Program](https://kissflow.com/no-code/citizen-developer-program/), 날짜 미상). H&M 그룹은 실제 4명으로 1,500개 앱·30,000명 이상 사용자 커뮤니티를 지원했다. ([Microsoft Power Platform Blog](https://www.microsoft.com/en-us/power-platform/blog/power-apps/hmgroup/), 날짜 미상)

- **멘토링 방식**: 경험 있는 전문 개발자가 시티즌 개발자에게 1:1 페어링하는 방식 권장. ISG는 "자동화 CoE에서 경험 많은 개발자를 멘토로 지정해 시티즌 개발자의 time-to-value를 가속하라"고 명시. ([ISG](https://isg-one.com/articles/the-automation-center-of-excellence-and-citizen-developers-not-the-wild-wild-west!), 날짜 미상)

- **공동 개발(Co-development) 모델**: 초기 CoE 50% : 사업부 50% → 시간 경과 후 CoE 0~2% : 사업부 98~100%로 점감하는 참여 구조 권장. ([Microsoft Learn - Fabric Adoption Roadmap](https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap-mentoring-and-user-enablement), 2024-12-30 업데이트)

- **오피스아워 운영**: 주 1회 이상 정기적·빈번하게 운영(예: 매주 화·목). CoE 전문가가 최소한의 절차로 실시간 상담이 가능한 구조. "Power Hour", "Fabric Fridays" 등 브랜드명으로 운영하는 사례 있음. ([Microsoft Learn - Fabric Adoption Roadmap](https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap-mentoring-and-user-enablement), 2024-12-30 업데이트)

- **허브-앤-스포크(Hub-and-Spoke) 구조**: CoE(허브)가 플랫폼 거버넌스·훈련 자료·프로그램 표준 유지하고, 각 사업부에 1~3명의 인증된 챔피언(스포크)이 동료의 첫 번째 연락 창구 역할 담당. ([Kissflow](https://kissflow.com/no-code/citizen-developer-program/), 날짜 미상)

- **교육 지원 채널 구성**: 핸즈온 워크숍, 멘토링 프로그램, 온라인 포럼/채팅(Slack·Teams) 채널, 튜토리얼·모범 사례 지식 베이스, 중앙화된 포털(SharePoint/Teams 위키) 조합 권장. ([Superblocks Blog](https://www.superblocks.com/blog/citizen-developer-governance), 2026)

- **AI 코딩 도구 도입 시 단계적 파일럿 접근**: 20~30명의 소규모 파일럿 그룹으로 시작 후 전사 롤아웃이 90일 채택률을 높이는 것으로 보고됨. ([IntuitionLabs - Claude Enterprise Guide](https://intuitionlabs.ai/articles/claude-enterprise-deployment-training-guide-2026), 날짜 미상)

- **생산성 갭 인지**: 전임 개발자는 연간 4~6건 자동화 완료 vs. 25% 시간 할당 시티즌 개발자는 연간 1~2건 수준. CoE가 이 갭을 고려해 지원 강도를 설계해야 한다. ([ISG](https://isg-one.com/articles/the-automation-center-of-excellence-and-citizen-developers-not-the-wild-wild-west!), 날짜 미상)

- **내부 기획안 인프라 지원 범위**: Landing Zone(IaC·CI/CD·IAM 등) 및 배포 파이프라인은 AI 인프라팀이 제공. 개발자 직접 멘토링·오피스아워는 내부 기획안 범위 밖이며 CoE 역할로 별도 설계 필요. (내부: AWS_기반_탑다운_AIFAB_과제_운영환경_구축운영_기획안_v1-0.md §3~§5)

| 항목 | 수치 | 출처 | 시점 |
|---|---|---|---|
| 기업 CoE 권장 전담 인원 | 2~5명 | Kissflow | 2026 |
| H&M 그룹 CoE 실제 운원 | 4명 | Microsoft Power Platform Blog | 날짜 미상 |
| 오피스아워 최소 권장 빈도 | 주 1회 이상 | Microsoft Learn Fabric Adoption Roadmap | 2024-12-30 |
| Co-development 초기 CoE 참여 비율 | 50% → 0~2%로 점감 | Microsoft Learn Fabric Adoption Roadmap | 2024-12-30 |
| 챔피언(스포크) 권장 배치 수 | 사업부당 1~3명 | Kissflow | 날짜 미상 |
| AI 코딩 도구 파일럿 그룹 권장 규모 | 20~30명 | IntuitionLabs | 날짜 미상 |
| 전임 개발자 연간 자동화 완료 건수 | 4~6건 | ISG | 날짜 미상 |
| 25% 할당 시티즌 개발자 연간 완료 건수 | 1~2건 | ISG | 날짜 미상 |
| IT 거버넌스 정책 보유 기업 비율 | 78% (2024년 42%에서 상승) | Gartner (via Kissflow) | 2026 |

---

### 2.4 배포 후 종료 처리 절차 (운영 이관 vs 폐기, 회고, 리소스 회수)

**핵심 발견**

- **이관 vs 폐기 판단**: 파일럿 시작 전에 성공 기준을 합의하고, 종료 시 Scale/Stop/Redirect 중 하나를 결정. 결정 권한자(named decision owner)를 사전에 지정하는 것이 핵심 거버넌스 요건. ([Traction Technology](https://www.tractiontechnology.com/blog/how-to-run-a-successful-pilot-with-a-startup-frameworks-kpis-enterprise-best-practices), 날짜 미상)

- **Go/No-Go 스코어카드**: 기술 40%, 재무 30%, 시장 20%, 자원 10% 가중치로 최종 점수를 산출하며, 임계값(예: 0.605 이상) 통과 시 운영 이관 승인. ([Visual Paradigm](https://guides.visual-paradigm.com/making-informed-decisions-with-a-go-no-go-checklist-for-agile-projects-a-scoring-approach/), 날짜 미상)

- **클로저 레코드 작성**: ①테스트 내용·파라미터, ②성공 기준 대비 실제 결과, ③Scale/Stop/Redirect 결정과 근거, ④향후 동일 기술 범주 평가에 적용할 2~3가지 학습 사항 포함. 15~20분 내 작성, 조직 소유 시스템에 영구 보존. ([Traction Technology](https://www.tractiontechnology.com/blog/how-to-run-a-successful-pilot-with-a-startup-frameworks-kpis-enterprise-best-practices), 날짜 미상)

- **운영 이관 4대 체크리스트**: ①이관 산출물 사전 합의(내용·시기·형식), ②운영팀의 조직적·운영적 준비 확인, ③문서 완비(운영 매뉴얼·트러블슈팅·교육 기록·안전 파일), ④이관 후 현장 지원 체계 구축. ([Owner Team Consultation](https://www.ownerteamconsult.com/effective-handover-of-projects-to-operations-teams/), 날짜 미상)

- **내부 기획안 격상 이관 절차(7단계)**: 코드 리뷰 → 문서화 → 실데이터 재설계 → 운영 조직 지정 → 환경 재프로비저닝 → 이관·검증 → 원 환경 정리. 격상의 실체는 "재프로비저닝 + 재배포"이며 애플리케이션 재작성 없이 수용하는 것이 핵심 원칙. (내부: AWS_기반_탑다운_AIFAB_과제_운영환경_구축운영_기획안_v1-0.md §6. 격상 유입 절차)

- **내부 기획안 과제 종료**: 사업 판단(보드 심의)으로 결정, 종료 시 데이터 파기·자원 회수 체크리스트 적용. 자동 선셋은 적용하지 않음. (내부: AWS_기반_탑다운_AIFAB_과제_운영환경_구축운영_기획안_v1-0.md §7. 운영·모니터링)

- **애플리케이션 폐기 판단 기준 5가지**: ①활성 사용자/트랜잭션이 임계값 미만, ②유지보수 비용이 비즈니스 가치 대비 과도, ③기술 스택 노후화, ④보안·컴플라이언스 미충족, ⑤다른 시스템이 동등 이상의 기능 제공. ([SparxSystems](https://www.sparxsystems.us/application-portfolio-management/application-lifecycle-states-sunset-policy/ ⚠(dead link)), 날짜 미상)

- **AWS Innovation Sandbox 계정 라이프사이클 자동화**: Entry→CleanUp→Available→Active→Frozen→CleanUp 상태 머신으로 관리. Frozen 상태 후 14일 자동 접근 회수, 21일 자동 리소스 삭제(관리자 보존 지정 없을 시). 이관 결정 계정은 Eject로 영구 분리 가능. ([AWS Docs - Innovation Sandbox](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/account-lifecycle-in-isb.html), 날짜 미상)

- **AWS Control Tower 해제 자동 처리**: SCP 제거, CloudFormation StackSet 삭제, Account Factory 레코드 삭제 자동 수행. 단, CloudWatch Logs 그룹 및 S3 예약 버킷 2개는 수동 삭제 필요. ([AWS Docs - Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/decommissioning-process-overview.html), 날짜 미상)

- **AWS 계정 폐쇄 제한**: 계정 폐쇄 후 90일 이내 복구 가능. 정리 대상 식별 기준: 3개월 연속 $100 미만 지출 계정. ([AWS Cloud Operations Blog](https://aws.amazon.com/blogs/mt/streamlining-aws-organizations-cleanup-strategies/), 날짜 미상)

- **회고 KPI**: 액션 아이템 완료율·참여율·팀 행복도·사이클 타임. 이전 회고 액션 아이템 완료율을 다음 회고 첫 번째 의제로 점검. ([Gulf Coast Trade Institute](https://gulfcoasttradeinstitute.com/measuring-retrospective-effectiveness/), 날짜 미상)

| 항목 | 수치 | 출처 | 시점 |
|---|---|---|---|
| 클로저 레코드 작성 소요 시간 | 15~20분 | Traction Technology | 날짜 미상 |
| 정체 감지 → 대응 기한 | 48시간 이내 | Traction Technology | 날짜 미상 |
| Go/No-Go 스코어카드 통과 임계값 예시 | 0.605 이상 (가중 점수) | Visual Paradigm | 날짜 미상 |
| Innovation Sandbox 자동 접근 회수 | Frozen 상태 후 14일 | AWS Publicsector Blog | 날짜 미상 |
| Innovation Sandbox 자동 리소스 삭제 | 21일 (보존 지정 없을 시) | AWS Publicsector Blog | 날짜 미상 |
| AWS 계정 폐쇄 후 복구 가능 기간 | 90일 이내 | AWS Cloud Operations Blog | 날짜 미상 |
| AWS 정리 대상 식별 비용 임계값 | 3개월 연속 $100 미만 | AWS Cloud Operations Blog | 날짜 미상 |
| 파일럿 단계적 확대 배율 | 5%→10%→20%→40%→80%→100% | LogRocket Blog | 날짜 미상 |
| 격상 이관 체크리스트 단계 수 | 7단계 | 내부 기획안 §6 | 2026.07.11 |

---

### 2.5 파일럿 성공 KPI와 본 사업 확대 판단 기준

**핵심 발견**

- **핵심 KPI 6종**: 운영 효율성, 시간 절감, 가치 실현 기간(time-to-value), 직원 참여도, 참여자 수, 후원 아이디어 수 — 이 여섯 지표를 복합 추적한 조직이 단일 지표에 집중한 조직보다 성과가 높음. ([KPMG Belgium](https://kpmg.com/be/en/home/insights/2024/11/ta-transforming-business-value-creation-with-citizen-development.html), 2024-11)

- **KPI 사전 동결 원칙**: 파일럿 시작 전(day 0)에 KPI 임계값을 동결하고, go/no-go 판단 기준 및 의사결정 담당자를 킥오프 전에 합의·문서화하는 것이 최우선 원칙. ([MarginLayer](https://marginlayer.app/blog/pilot-success-criteria-kpi-roi.html), 날짜 미상)

- **90일 파일럿 단계별 go/no-go 게이트 사례**:
  - 30일 차: 채택률 40% + DLP 위반 0건
  - 60일 차: 주간 활성 사용자율 50% + 생산성 향상 15%
  - 90일 차: 최종 판단
  ([Agility at Scale](https://agility-at-scale.com/ai/generative/pilot-implementation-with-real-metrics/), 날짜 미상)

- **AI 코딩 도구 파일럿 DORA 메트릭**: 배포 빈도, 변경 리드타임, 평균 복구시간(MTTR), 변경실패율 — "6~8주 파일럿에서 리드타임 또는 배포 빈도의 측정 가능한 개선이 없으면, 병목 해결 후 재시도"가 표준 권고. ([Index.dev](https://www.index.dev/blog/ai-coding-assistants-roi-productivity), 2025)

- **전사 확대 판단 DECIDE 프레임워크 4대 질문**: ① 결과 KPI 달성 여부, ② 비용 대비 가치 비율 적정성, ③ 거버넌스·리스크 확대 수용 가능성, ④ 조직 변화 관리 준비도 — 4개 모두 충족 시 확대 결정. ([Agility at Scale](https://agility-at-scale.com/ai/strategy/roi-and-success-metrics/), 날짜 미상)

- **거버넌스 체계 유무의 영향**: 거버넌스 있는 저코드 조직 77% 비용 절감 성공 vs. 거버넌스 없는 조직 39% — 파일럿 단계부터 거버넌스 구조 병행 구축이 필수. ([KPMG Belgium](https://kpmg.com/be/en/home/insights/2024/11/ta-transforming-business-value-creation-with-citizen-development.html), 2024-11)

- **META 파일럿 성과**: 첫 두 코호트에서 7개 비즈니스 팀 전반에 걸쳐 20개 이상 자동화 배포 달성 — 코호트 단위 배포 건수가 확대 판단의 정량 지표로 활용됨. ([UiPath Blog](https://www.uipath.com/blog/automation/citizen-development-lessons-from-meta-conocophillips-and-more), 날짜 미상)

- **국내 사례 — CJ올리브영 AI-DLC**: 일반 개발 대비 5배 빠른 속도, 5개 비즈니스 과제 3일 내 프로토타입 구현, 반복 업무 처리 시간 최대 30배 단축(건당 5분→10초 이내), 운영 지연 요인 40% 사전 차단. 이후 PM 조직·글로벌 개발 조직으로 단계적 확장 결정. ([AWS 기술 블로그](https://aws.amazon.com/ko/blogs/tech/cj-oliveyoung-aidlc-tech-blog/), 날짜 미상)

- **내부 기획안 SLO**: 가용성 99.5%, 오류율, 응답시간을 과제별로 보드가 확정. 이는 개별 과제 운영 수준 목표이며, 파일럿 프로그램 KPI와는 별도로 설계 필요. (내부: AWS_기반_탑다운_AIFAB_과제_운영환경_구축운영_기획안_v1-0.md §7. 운영·모니터링)

- **ROI 과대평가 주의**: 파일럿 ROI는 운영 환경 ROI를 구조적으로 과대평가하므로, 확대 전 반드시 "위험 조정 ROI"를 재계산해야 함. ([Agility at Scale](https://agility-at-scale.com/ai/generative/pilot-implementation-with-real-metrics/), 날짜 미상)

| 항목 | 수치 | 출처 | 시점 |
|---|---|---|---|
| 거버넌스 있는 조직 비용 절감 성공률 | 77% | KPMG Belgium | 2024-11 |
| 거버넌스 없는 조직 비용 절감 성공률 | 39% | KPMG Belgium | 2024-11 |
| 시티즌 개발 배포 속도 향상 | IT 대비 5~10배 빠름 | Quixy | 2024 |
| 내부 도구 배포 리드타임 단축 | 평균 60~70% 감소 | Kissflow | 2025 |
| 소프트웨어 개발 비용 절감 (low-code) | 평균 40% 감소 | Quixy | 2024 |
| AI 코딩 도구 주당 절감 시간 | 개발자 1인당 평균 3.6시간/주 | DX Research via Index.dev | 2025 |
| AI 코딩 도구 파일럿 작업 완료 수 향상 | 개인 작업 ~21% 증가 | Index.dev | 2025 |
| 건강한 AI 코딩 도구 ROI 범위 | 2.5~3.5배(평균), 상위 25% 조직 4~6배 | Exceeds.ai | 2025 |
| 30일 채택률 go 기준 (사례) | 40% 이상 | Agility at Scale | 날짜 미상 |
| 60일 주간 활성 사용자율 go 기준 (사례) | 50% 이상 | Agility at Scale | 날짜 미상 |
| 60일 생산성 향상 go 기준 (사례) | 15% 이상 | Agility at Scale | 날짜 미상 |
| META 파일럿 2개 코호트 배포 성과 | 7개 팀, 20개 이상 자동화 배포 | UiPath Blog | 날짜 미상 |
| CJ올리브영: 개발 속도 향상 | 일반 방식 대비 5배, 프로토타입 3일 완성 | AWS 기술 블로그 | 날짜 미상 |
| CJ올리브영: 반복 업무 처리 시간 | 건당 5분 → 10초 이내 (최대 30배 단축) | AWS 기술 블로그 | 날짜 미상 |
| 운영 가용성 SLO (내부 기획안) | 99.5% | 내부 기획안 §7 | 2026.07.11 |

---

## 3. 종합 시사점

### 3.1 내부 기획안과 외부 모범 사례의 역할 분리

내부 기획안(탑다운 AIFAB v1-0)은 AWS 인프라·배포 파이프라인·격상·SLO 운영의 기술적 기반을 충실히 정의하고 있다. 반면 시티즌 개발자 선발, 스프린트 주차별 운영, 멘토링·오피스아워, 프로그램 KPI는 전적으로 외부 사례에서 설계 근거를 가져와야 한다. 파일럿 운영 시나리오는 이 두 레이어를 결합하는 구조로 설계해야 한다: **외부 모범 사례(선발·스프린트·지원 체계·KPI)가 "What to do"를 제공하고, 내부 기획안(배포 게이트·격상 절차·리소스 회수)이 "How the infrastructure responds"를 제공**한다.

### 3.2 거버넌스와 속도의 균형 — Agile-Stage-Gate 하이브리드가 최적

단순 해커톤 구조(수상 후 프로덕션 전환 사전 계획 없음)는 AI FAB 탑다운 과제에 적합하지 않다. 기업 거버넌스(AI Board·정보보호팀 승인 게이트)와 3주 단기 스프린트 속도를 동시에 충족하려면 **Agile-Stage-Gate 하이브리드 패턴 C**가 가장 적합하다. Gate 0(착수 승인), Gate 1(중간 리뷰, 24~48h 결정), Gate 2(배포 승인 — 내부 기획안의 AI Board 수동 게이트와 직접 연계)를 3주 스프린트에 내재화한다.

### 3.3 CoE 선행 구축이 파일럿 성공률 결정

거버넌스 구조 유무에 따른 성공률 차이(77% vs 39%, KPMG Belgium 2024)는 CoE를 파일럿 실행과 동시에(또는 이전에) 구축해야 함을 강력히 시사한다. CoE 2~5명이 멘토링, 오피스아워(주 1회 이상), 과제 검토(비즈니스+기술 2단계), 커뮤니티 운영을 병행 수행하는 구조가 업계 표준이다. 3주 스프린트처럼 단기 과제에서는 CoE 참여 비율을 초기에 높게(50% 이상) 설정하고 이후 점감하는 Co-development 모델이 현실적이다.

### 3.4 KPI는 킥오프 전 동결, ROI는 위험 조정 후 재계산

"파일럿 성공 기준을 파일럿이 끝난 후 정의하면, 언제나 성공한다"는 함정을 피하기 위해 KPI 임계값(채택률·사이클 타임·배포 완성 건수·거버넌스 준수율)은 킥오프 전 문서화가 필수다. 또한 파일럿 ROI는 실제 운영 ROI를 과대평가하는 구조적 편향이 있으므로, 전사 확대 결정 전 반드시 위험 조정 ROI를 재계산해야 한다.

### 3.5 종료·이관의 상충 — 자동 선셋 vs 보드 심의

외부 사례(AWS Innovation Sandbox)는 임계값 초과 시 자동 Frozen·리소스 삭제(14~21일)를 권장하는 반면, 내부 기획안은 "자동 선셋 미적용, 사업 판단(보드 심의)으로 결정"을 원칙으로 명시한다. 이 두 접근은 상충한다. 파일럿 운영 시나리오에서는 **자동 Frozen(비용 임계값 초과 시 접근 차단)은 적용하되, 최종 리소스 삭제·계정 폐쇄는 보드 심의로 결정**하는 하이브리드 방식을 채택하는 것이 현실적 절충안이다.

### 3.6 3주 스프린트의 현실적 한계 — 배포 완성율 벤치마크 부재

업계 표준(Kissflow, Traction Technology)의 파일럿 기간은 60~90일이다. 3주(약 21일)로 "배포까지 완성"하는 구조는 사례 문헌에서 직접적인 벤치마크를 확보하지 못한 영역이다. AI 코딩 도구(Claude Code 등) 활용 시 개발 속도가 5~10배 향상된다는 데이터(Quixy 2024, CJ올리브영)가 3주 배포 완성의 현실적 근거로 활용될 수 있으나, 이를 직접 실증한 사례는 미확보 상태다.

---

## 4. 한계·추가 조사 필요 영역

### 4.1 내부 기획안 기반 한계 (q0)

- **시티즌 개발자 선발 기준·절차**: 내부 기획안은 탑다운 과제 수행 주체를 "지정된 개발·운영 조직"으로 전제하며, 시티즌 개발자 선발 기준·절차에 대한 내용 없음.
- **3주 스프린트 구조**: 내부 기획안에 3주 스프린트 구조(킥오프, 중간 점검, 심사·게이트 일정)가 존재하지 않음.
- **개발자 지원 체계(멘토링·오피스아워·AI 코딩 도구)**: 인프라·플랫폼 지원만 기술됨. 사람 중심 지원 체계는 별도 설계 필요.
- **파일럿 프로그램 KPI**: SLO(가용성 99.5% 등)는 개별 과제 운영 수준 목표이며 파일럿 프로그램 KPI는 아님.
- **바텀업 샌드박스 기획안(v2-1)**: 시티즌 개발자 선발·스프린트 구조 관련 내용이 있을 가능성이 있으나 미분석.

### 4.2 선발 관련 한계 (q1)

- 국내 대기업의 사내 시티즌 개발자/AI 코딩 파일럿 프로그램 내 구체적인 지원 자격 요건(직급, 경력 연수, 사전 기술 수준 등) 공개 자료 미확보.
- 부서장 승인 절차의 세부 단계(승인 양식, 시간 확보 비율, 승인 기간 등) 정량 데이터 미확보.
- Claude Code 등 AI 코딩 도구를 활용한 시티즌 개발자 파일럿 선발 사례 1차 출처 미확보.

### 4.3 스프린트 구조 관련 한계 (q2)

- 3주 스프린트로 실제 프로덕션 배포까지 완성한 사내 시티즌 개발자 프로그램 주차별 공개 사례 미확보.
- W1/W2/W3 레이블을 명시적으로 사용하는 공개 프로그램 매뉴얼 미확보.
- AI 코딩 도구 활용 시 3주 스프린트 효율 차이에 대한 실증 데이터 미확보.

### 4.4 지원 체계 관련 한계 (q3)

- CoE 인원 대비 시티즌 개발자 수의 명확한 지원 비율(1명 CoE 당 몇 명 지원) 1차 출처 미확보.
- AI 코딩 도구(Claude Code, GitHub Copilot) 전용 시티즌 개발자 파일럿 지원 체계 사례 제한적.
- 국내 기업의 시티즌 개발자 CoE·멘토링 운영 사례 공개 출처 미확보.

### 4.5 종료·이관 관련 한계 (q4)

- 사내 IT 파일럿(시티즌 개발자 대상) 특화 이관 기준 미확보. 대부분 스타트업-엔터프라이즈 파일럿 또는 대규모 인프라 폐기 사례 중심.
- 국내 기업의 파일럿 프로젝트 운영 이관 기준이나 AWS 리소스 회수 가이드라인 공개 1차 출처 미발견.
- AWS Control Tower 수동 정리 항목의 완전한 목록 미확보.

### 4.6 KPI·확대 판단 관련 한계 (q5)

- 파일럿 배포 완성률(deployment completion rate) 벤치마크 1차 출처 미확보.
- 참여자 역량 향상 지표 정량 데이터(스킬 향상 점수, 자격증 취득률 등) 미확보.
- 한국 기업의 명시적 go/no-go 기준 사례 미확보(CJ올리브영은 성과 수치는 확인됐으나 의사결정 기준 미공개).
- 30일·60일 채택률 임계값(40%, 50%, 15%)의 보편성 미확인 — Gartner/McKinsey 1차 원보고서에서 동일 수치 확인 불가.

### 4.7 추가 조사 권고 영역 (단계 3 발산 리서치 입력)

1. **바텀업 샌드박스 기획안(v2-1) 분석**: 시티즌 개발자 선발·스프린트 구조 관련 내용 확인 필요.
2. **SK 계열사 사내 AI 파일럿 운영 사례**: 비공개 추정이나 내부 인터뷰 가능 여부 탐색.
3. **AI 코딩 도구 활용 3주 스프린트 실증 데이터**: Claude Code·GitHub Copilot 활용 시 배포 완성율 실측값 확보.
4. **CoE 지원 비율 벤치마크**: 1명 CoE 당 최적 지원 시티즌 개발자 수 산업별 데이터 탐색.

---

## 5. Sources

### 웹 출처

| URL | 출처명 | 발행일 |
|---|---|---|
| https://kissflow.com/no-code/citizen-developer-program/ | Kissflow - Citizen Developer Program | 날짜 미상 (2026 업데이트) |
| https://www.uipath.com/rpa/what-is-citizen-development | UiPath - What is Citizen Development | 날짜 미상 |
| https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/understanding-the-citizen-developer-framework ⚠(dead link) | UiPath Automation Hub - Citizen Developer Framework | 날짜 미상 |
| https://www.uipath.com/ko/resources/automation-case-studies/lguplus | UiPath - LG유플러스 RPA 시민개발자 사례 | 날짜 미상 |
| https://www.uipath.com/blog/automation/citizen-development-lessons-from-meta-conocophillips-and-more | UiPath Blog - Citizen development lessons from META, ConocoPhillips | 날짜 미상 |
| https://theinnovationmode.com/corporate-hackathon-template | Innovation Mode - Corporate Hackathon Template | 날짜 미상 |
| https://www.cio.com/article/3530262/ | CIO.com - 성공적인 해커톤의 비밀 | 날짜 미상 |
| https://m.etnews.com/20200319000047 | 전자신문 - 5대 그룹 사내벤처 육성책 | 2020-03-19 |
| https://angelhack.com/blog/ai-internal-hackathon/ | AngelHack - AI Internal Hackathon Playbook | 날짜 미상 |
| https://www.quandarycg.com/citizen-developer-statistics/ | Quandary CG - Citizen Developer Statistics 2024 | 2024 |
| https://www.pmi.org/citizen-developer/ ⚠(dead link) | PMI - Citizen Developer Program | 날짜 미상 |
| https://www.forrester.com/report/case-study-globes-low-code-citizen-developer-program/RES177457 | Forrester - Globe's Low-Code Citizen Developer Program | 날짜 미상 |
| https://www.servicenow.com/solutions/creator-workflows/citizen-development-program.html ⚠(dead link) | ServiceNow - Citizen Development Program | 날짜 미상 |
| https://www.johnwakeling.co.uk/posts/3-week-sprints/ | John Wakeling Blog - 3-Week Sprints | 날짜 미상 |
| https://umbrex.com/resources/frameworks/strategy-frameworks/stage-gate-innovation-process/ | Umbrex - Stage-Gate Innovation Process | 날짜 미상 |
| https://www.profit.co/blog/stage-gate-process/stage-gate-vs-agile-methodology-comparison-and-hybrid-models/ ⚠(dead link) | Profit.co - Stage-Gate vs Agile | 날짜 미상 |
| https://hackathon.guide/ | Hackathon Guide | 날짜 미상 |
| https://www.klipfolio.com/blog/run-hackathon | Klipfolio - Corporate Hackathon Guide | 날짜 미상 |
| https://www.gv.com/sprint/ | GV Design Sprint | 날짜 미상 |
| https://design.google/library/design-sprints | Google Design Sprints | 날짜 미상 |
| https://www.designsprint.academy/blog/design-sprint-3-0 | Design Sprint 3.0 Academy | 날짜 미상 |
| https://www.atlassian.com/ko/agile/scrum/sprints | Atlassian Scrum Sprints (KR) | 날짜 미상 |
| https://www.fnnews.com/news/202307171837050284 | 파이낸셜뉴스 - 부산 DX 스프린트 해커톤 | 2023-07-17 |
| https://build.starterstory.com/build/ai-build-accelerator | AI Build Accelerator | 날짜 미상 |
| https://1337.ventures/corporate-innovation-sprint/ | 1337 Ventures - Corporate Innovation Sprint | 날짜 미상 |
| https://www.theguru.co.kr/news/article.html?no=83646 | 더구루 - SKT AI 액셀러레이터 | 날짜 미상 |
| https://fellowship.mlh.im/ ⚠(dead link) | MLH Fellowship | 날짜 미상 |
| https://theinnovationmode.com/the-innovation-blog/how-to-run-a-successful-corporate-hackathon | Innovation Mode - Corporate Hackathon Guide | 날짜 미상 |
| https://isg-one.com/articles/the-automation-center-of-excellence-and-citizen-developers-not-the-wild-wild-west! | ISG - The Automation CoE and Citizen Developers | 날짜 미상 |
| https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap-mentoring-and-user-enablement | Microsoft Learn - Fabric Adoption Roadmap: Mentoring and User Enablement | 2024-12-30 업데이트 |
| https://www.microsoft.com/en-us/power-platform/blog/power-apps/hmgroup/ | Microsoft Power Platform Blog - H&M Group | 날짜 미상 |
| https://intuitionlabs.ai/articles/claude-enterprise-deployment-training-guide-2026 | IntuitionLabs - Claude Enterprise Deployment & Training Guide 2026 | 날짜 미상 |
| https://www.superblocks.com/blog/citizen-developer-governance | Superblocks - 6-Step Framework for Citizen Developer Governance | 2026 |
| https://www.deloitte.com/us/en/services/consulting/articles/5-keys-to-success-with-citizen-developers.html | Deloitte US - Citizen development: five keys to success | 날짜 미상 |
| https://kissflow.com/low-code/empowering-citizen-developers-low-code-program/ | Kissflow - Empowering Citizen Developers | 날짜 미상 |
| https://www.weweb.io/blog/citizen-developer-tools-governance-guide | WeWeb - Citizen Developer: What It Is, Tools & Governance | 2026 |
| https://www.tractiontechnology.com/blog/how-to-run-a-successful-pilot-with-a-startup-frameworks-kpis-enterprise-best-practices | Traction Technology - How to Run a Successful Pilot | 날짜 미상 |
| https://guides.visual-paradigm.com/making-informed-decisions-with-a-go-no-go-checklist-for-agile-projects-a-scoring-approach/ | Visual Paradigm - Go/No-Go Checklist for Agile Projects | 날짜 미상 |
| https://www.ownerteamconsult.com/effective-handover-of-projects-to-operations-teams/ | Owner Team Consultation - Effective Handover of Projects | 날짜 미상 |
| https://www.sparxsystems.us/application-portfolio-management/application-lifecycle-states-sunset-policy/ ⚠(dead link) | SparxSystems - Application Lifecycle States: Sunset Policy | 날짜 미상 |
| https://www.archondatastore.com/blog/application-decommissioning-retirement/ | Archon Data Store - Application Decommissioning | 날짜 미상 |
| https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/account-lifecycle-in-isb.html | AWS Docs - Innovation Sandbox Account Lifecycle | 날짜 미상 |
| https://docs.aws.amazon.com/controltower/latest/userguide/decommissioning-process-overview.html | AWS Docs - Control Tower Decommissioning | 날짜 미상 |
| https://aws.amazon.com/blogs/mt/streamlining-aws-organizations-cleanup-strategies/ | AWS Cloud Operations Blog - AWS Organizations Cleanup | 날짜 미상 |
| https://aws.amazon.com/blogs/mt/best-practices-creating-managing-sandbox-accounts-aws/ | AWS Cloud Operations Blog - Sandbox Account Best Practices | 날짜 미상 |
| https://allcloud.io/blog/emea-il-key-concepts-for-sandbox-accounts-management/ | AllCloud Blog - Sandbox Accounts Management | 날짜 미상 |
| https://aws.amazon.com/blogs/publicsector/empowering-educators-how-innovation-sandbox-on-aws-accelerates-learning-objectives-through-secure-cost-effective-and-recyclable-sandbox-management/ | AWS Public Sector Blog - Innovation Sandbox | 날짜 미상 |
| https://blog.logrocket.com/product-management/pilot-project-guide/ | LogRocket Blog - Pilot Project Guide | 날짜 미상 |
| https://gulfcoasttradeinstitute.com/measuring-retrospective-effectiveness/ | Gulf Coast Trade Institute - Measuring Retrospective Effectiveness | 날짜 미상 |
| https://www.solix.com/products/answers/application-decommissioning-checklist/ | Solix Technologies - Application Decommissioning Checklist | 날짜 미상 |
| https://quixy.com/blog/citizen-development-kpis-and-roi/ | Quixy - Citizen Development KPIs and ROI | 2024 |
| https://kissflow.com/citizen-development/citizen-development-statistics-and-trends/ | Kissflow - Citizen Development Trends & Key Stats 2025 | 2025 |
| https://kpmg.com/be/en/home/insights/2024/11/ta-transforming-business-value-creation-with-citizen-development.html | KPMG Belgium - Transforming business value creation with Citizen Development | 2024-11 |
| https://agility-at-scale.com/ai/generative/pilot-implementation-with-real-metrics/ | Agility at Scale - Pilot Implementation with Real Metrics | 날짜 미상 |
| https://agility-at-scale.com/ai/strategy/roi-and-success-metrics/ | Agility at Scale - Enterprise AI ROI Measurement | 날짜 미상 |
| https://aveni.ai/blog/enterprise-ai-implementation-framework-moving-beyond-pilots-to-production/ | Aveni - Moving Beyond Pilots to Production | 날짜 미상 |
| https://www.index.dev/blog/ai-coding-assistants-roi-productivity | Index.dev - AI Coding Assistant ROI: Real Productivity Data 2025 | 2025 |
| https://blog.exceeds.ai/enterprise-ai-adoption-metrics-2025/ | Exceeds.ai - Enterprise AI Coding Adoption Metrics 2025 | 2025 |
| https://aws.amazon.com/ko/blogs/tech/cj-oliveyoung-aidlc-tech-blog/ | AWS 기술 블로그 - CJ올리브영 AI-DLC 실전 도입 사례 | 날짜 미상 |
| https://marginlayer.app/blog/pilot-success-criteria-kpi-roi.html | MarginLayer - Pilot success criteria, KPI, and ROI frame | 날짜 미상 |
| https://www.scirp.org/journal/paperinformation?paperid=132715 ⚠(dead link) | SCIRP - Critical Success Factors for Citizen Development | 날짜 미상 |

### 내부 문서

| 파일명 | 분석 섹션 |
|---|---|
| AWS_기반_탑다운_AIFAB_과제_운영환경_구축운영_기획안_v1-0.md | §2 바텀업 샌드박스와의 차이, §4.1 실데이터 취급, §5 개발·배포, §6 격상 유입 절차, §7 운영·모니터링, §8 단계별 구축 로드맵, §9 비용 산정 |
