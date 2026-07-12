# 시티즌 개발자 파일럿 기간의 지원 체계

## 핵심 발견

- **CoE(Center of Excellence)는 2~5명의 소규모 전담팀**으로 구성하는 것이 모범 사례이며, 프로그램 프레임워크 소유, 사용 사례 승인, 플랫폼 표준 유지, 시티즌 개발자 안내·검수 역할을 담당한다. ([Kissflow, Citizen Developer Program, 2026](https://kissflow.com/no-code/citizen-developer-program/))

- **멘토링은 경험 있는 전문 개발자가 시티즌 개발자에게 1:1 페어링**하는 방식이 권장된다. ISG는 "자동화 CoE에서 경험 많은 개발자를 멘토로 지정해 시티즌 개발자의 시간가치(time to value)를 가속하라"고 명시했다. ([ISG, The Automation Center of Excellence and Citizen Developers, 날짜 미상](https://isg-one.com/articles/the-automation-center-of-excellence-and-citizen-developers-not-the-wild-wild-west!))

- **공동 개발(Co-development) 프로젝트 모델**: CoE와 사업부가 파트너십으로 프로젝트를 수행하며, 초기에는 CoE 50% : 사업부 50%로 시작해, 시간이 지남에 따라 CoE 0~2% : 사업부 98~100%로 점감하는 참여 구조를 권장한다. ([Microsoft Learn, Fabric Adoption Roadmap - Mentoring and User Enablement, 2024-12-30 업데이트](https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap-mentoring-and-user-enablement))

- **오피스아워(Office Hours)는 주 1회 이상, 정기적·빈번하게** 운영하는 것이 권장된다(예: 매주 화·목). CoE 전문가가 최소한의 절차로 지역 사회 구성원과 실시간 상담이 가능한 구조이며, "Power Hour", "Fabric Fridays" 등 브랜드명으로 운영하는 사례가 있다. ([Microsoft Learn, Fabric Adoption Roadmap - Mentoring and User Enablement, 2024-12-30 업데이트](https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap-mentoring-and-user-enablement))

- **허브-앤-스포크(Hub-and-Spoke) 구조**가 확장 시 효과적: CoE(허브)가 플랫폼 거버넌스·훈련 자료·프로그램 표준 유지하고, 각 사업부에 1~3명의 인증된 시티즌 개발자 챔피언(스포크)이 동료의 첫 번째 연락 창구 역할을 담당한다. ([Kissflow, Citizen Developer Program, 2026](https://kissflow.com/no-code/citizen-developer-program/))

- **Wesco 사례**: 직원 20,000명 이상 조직에서 "오피스아워 및 1:1 지원"을 제공하고, CoE 전문 개발자가 시티즌 개발자 프로젝트에 참여·검수. 시티즌 개발자를 "자동화 대사(automation ambassador)"로 정의하고 사용 사례 발굴 및 프로그램 홍보 역할도 부여한다. ([UiPath Blog, Successful citizen developer programs: Lessons from META, ConocoPhillips, 날짜 미상](https://www.uipath.com/blog/automation/citizen-development-lessons-from-meta-conocophillips-and-more))

- **H&M 그룹 CoE 사례**: 4명의 직원(Microsoft 365 Solution Architect, Cross Delivery Coordinator 포함)이 CoE를 주도하며, 자동화된 환영 이메일을 통한 온라인 교육 자료 제공, Yammer 온라인 커뮤니티 운영, SharePoint 성공 사례 카탈로그 공유 방식으로 1,500개 앱·30,000명 이상의 사용자 커뮤니티를 지원했다. ([Microsoft Power Platform Blog, H&M Group enables citizen development at scale, 날짜 미상](https://www.microsoft.com/en-us/power-platform/blog/power-apps/hmgroup/))

- **Deloitte의 Claude CoE 사례**: 470,000명 이상의 직원에게 Claude(Anthropic AI) 배포 시 Claude Center of Excellence를 설립, 표준화된 구현 추진. 약 15,000명의 실무자를 GenAI(특히 Anthropic 모델)로 인증했다. ([IntuitionLabs, Claude Enterprise Deployment & Training Guide 2026, 날짜 미상](https://intuitionlabs.ai/articles/claude-enterprise-deployment-training-guide-2026))

- **교육 지원 채널 구성**: 핸즈온 워크숍, 멘토링 프로그램, 온라인 포럼/채팅(Slack·Teams) 채널, 튜토리얼·모범 사례 지식 베이스, 중앙화된 포털(SharePoint/Teams 위키) 조합이 권장된다. ([Superblocks Blog, 6-Step Framework for Citizen Developer Governance 2026, 2026](https://www.superblocks.com/blog/citizen-developer-governance))

- **AI 코딩 도구 도입 시 단계적 파일럿 접근**: 20~30명의 소규모 파일럿 그룹으로 시작 후 전사 롤아웃이 90일 채택률을 높이는 것으로 보고되며, 기업들은 온라인 과정과 실습 워크숍 조합으로 온보딩을 진행한다. ([IntuitionLabs, Claude Enterprise Deployment & Training Guide 2026, 날짜 미상](https://intuitionlabs.ai/articles/claude-enterprise-deployment-training-guide-2026))

- **전임 개발자 대비 시티즌 개발자 생산성**: 전임 개발자는 연간 4~6건 자동화를 완료하는 반면, 25% 시간 할당 시티즌 개발자는 연간 1~2건 수준. CoE가 이 생산성 갭을 고려해 지원 강도를 설계해야 한다. ([ISG, The Automation Center of Excellence and Citizen Developers, 날짜 미상](https://isg-one.com/articles/the-automation-center-of-excellence-and-citizen-developers-not-the-wild-wild-west!))

## 정량 데이터

| 항목 | 수치 | 출처 | 시점 |
|---|---|---|---|
| 기업 CoE 권장 전담 인원 | 2~5명 | Kissflow, Citizen Developer Program | 2026 |
| H&M 그룹 CoE 실제 운원 | 4명 | Microsoft Power Platform Blog | 날짜 미상 |
| 오피스아워 최소 권장 빈도 | 주 1회 이상 | Microsoft Learn Fabric Adoption Roadmap | 2024-12-30 |
| Co-development 초기 CoE 참여 비율 | 50% → 0~2%로 점감 | Microsoft Learn Fabric Adoption Roadmap | 2024-12-30 |
| 챔피언(스포크) 권장 배치 수 | 사업부당 1~3명 | Kissflow, Citizen Developer Program | 2026 |
| Deloitte AI CoE 인증 인력 | 15,000명 (전체 470,000명 중) | IntuitionLabs Claude Enterprise Guide | 날짜 미상 |
| 파일럿 그룹 권장 규모 | 20~30명 | IntuitionLabs Claude Enterprise Guide | 날짜 미상 |
| 전임 개발자 연간 자동화 완료 건수 | 4~6건 | ISG | 날짜 미상 |
| 25% 할당 시티즌 개발자 연간 완료 건수 | 1~2건 | ISG | 날짜 미상 |
| IT 거버넌스 정책 보유 기업 비율 | 78% (2024년 42%에서 상승) | Gartner (via Kissflow) | 2026 |
| 커뮤니티 중 자발적 교육 참여 비율 | 10~20% | Microsoft Learn Fabric Adoption Roadmap | 2024-12-30 |
| Gartner 전망: 시티즌 개발자 대 전문 개발자 비율 | 4:1 (2023년 기준) | Gartner (via Quandary CG) | 2021년 전망 |

## 한계

- CoE 인원 대비 시티즌 개발자 수의 **명확한 지원 비율**(예: 1명 CoE 당 몇 명 지원)에 관한 1차 출처 데이터를 확보하지 못했다.
- 오피스아워의 **평균 참여자 수, 세션 길이, 월간 운영 횟수** 등 세부 운영 지표는 확인되지 않았다.
- **AI 코딩 도구(Claude Code, GitHub Copilot) 전용 시티즌 개발자 파일럿 지원 체계**에 관한 사례는 일반 low-code/no-code 사례에 비해 1차 출처가 매우 제한적이다.
- Gartner·Forrester 원문 보고서(유료 게이트)는 직접 접근이 불가했으며 2차 인용 데이터에 의존했다.
- 국내 기업(한국)의 시티즌 개발자 CoE·멘토링 운영 사례는 공개 출처에서 발견되지 않았다.

## 출처

- https://kissflow.com/no-code/citizen-developer-program/ (Kissflow, Citizen Developer Program, 2026)
- https://isg-one.com/articles/the-automation-center-of-excellence-and-citizen-developers-not-the-wild-wild-west! (ISG, The Automation CoE and Citizen Developers, 날짜 미상)
- https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap-mentoring-and-user-enablement (Microsoft Learn, Fabric Adoption Roadmap: Mentoring and User Enablement, 2024-12-30 업데이트)
- https://www.uipath.com/blog/automation/citizen-development-lessons-from-meta-conocophillips-and-more (UiPath Blog, Successful citizen developer programs, 날짜 미상)
- https://www.microsoft.com/en-us/power-platform/blog/power-apps/hmgroup/ (Microsoft Power Platform Blog, H&M Group enables citizen development at scale, 날짜 미상)
- https://intuitionlabs.ai/articles/claude-enterprise-deployment-training-guide-2026 (IntuitionLabs, Claude Enterprise Deployment & Training Guide 2026, 날짜 미상)
- https://www.superblocks.com/blog/citizen-developer-governance (Superblocks, 6-Step Framework for Citizen Developer Governance, 2026)
- https://www.deloitte.com/us/en/services/consulting/articles/5-keys-to-success-with-citizen-developers.html (Deloitte US, Citizen development: five keys to success, 날짜 미상)
- https://www.quandarycg.com/citizen-developer-statistics/ (Quandary CG, 50+ Current Citizen Developer Statistics, 2024)
- https://kissflow.com/low-code/empowering-citizen-developers-low-code-program/ (Kissflow, Empowering Citizen Developers, 날짜 미상)
- https://www.weweb.io/blog/citizen-developer-tools-governance-guide (WeWeb, Citizen Developer: What It Is, Tools & Governance, 2026)
