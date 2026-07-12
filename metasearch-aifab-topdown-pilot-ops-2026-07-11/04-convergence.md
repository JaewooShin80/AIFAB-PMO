# 수렴 보고서 — AI FAB 탑다운 과제 파일럿 운영 방안: 시티즌 개발자 선발부터 3주 스프린트 배포·종료까지 운영 시나리오

> 생성: 2026-07-11 | 메타서치 단계 4 산출물 | 입력: 02-deep-research.md + 03-divergence/*.md (d1~d5, deepdive 3종)

---

## 1. 수렴 개요

02(씨앗)는 선발→3주 스프린트→게이트→종료의 4단계 흐름을 긍정적으로 설계했으며, 외부 모범 사례(CoE·Agile-Stage-Gate·KPI 사전 동결)와 내부 기획안(배포 게이트·격상 절차·리소스 회수)의 역할을 분리하는 틀을 제시했다.

d1(실패 사례)은 GenAI 파일럿 88~95% 실패, Pilot Purgatory, 소유권 공백, AI 코딩 도구의 기술 부채·배포 안정성 역효과로 씨앗의 낙관론을 강하게 상충했다. d2(비판 관점)는 CI/CD 자동 검사가 아키텍처·로직 결함을 차단하지 못하며 수동 승인 게이트에 rubber-stamping 패턴이 존재함을 실증했다. d2-dd(게이트 deepdive)는 3-lane 리스크 기반 리뷰·SLA 차등화·rubber-stamping 방지 장치 등 씨앗에 없는 게이트 설계 원칙을 신규 제공했다.

d3(인접 프로그램)은 3주 배포 완성 선행 사례가 없음을 확인하면서도 GSoC 커뮤니티 본딩·메타 부트캠프·사내벤처 이중 출구 구조 등 운영 설계 참고점을 제공했다. d4(에이전틱 동향)는 에이전틱 도구 10주 지속 사용률 10% 미만, 복잡한 게이트가 Shadow AI를 촉진한다는 역설을 상충으로 제기했다. d4-dd(Anthropic deepdive)는 공식 Champion Kit·6개 KPI·챔피언 비율 등 씨앗의 지원 체계를 구체화했다. d5(골든 패스)는 "AI는 증폭기, 강한 플랫폼 없이는 안정성 저하"를 확인하며 사전 골든 패스 준비가 3주 배포의 현실적 전제임을 밝혔다. d5-dd(골든 패스 deepdive)는 IDP 정석 16주 vs. 3주 파일럿의 긴장을 구체 수치로 드러냈다.

총 6개 쟁점이 판정되었고(근거 우세 측 채택 4개·조건부 수렴 2개), 3개 쟁점은 현재 증거로 판정 불가하여 "미해결"로 표기했다.

---

## 2. 쟁점별 수렴 결과

### 2.1 3주 스프린트로 배포까지 완성이 현실적인가

| 구분 | 내용 | 출처 |
|---|---|---|
| 일치 증거 | AI 코딩 도구 활용 시 개발 속도 5~10배 향상 주장(Quixy 2024), CJ올리브영 5배 속도·3일 프로토타입(AWS 기술 블로그), Amazon Prime Video 10일·전문 개발자 6명·90주→24주 단축(AWS Korea Blog) | [Quixy](https://quixy.com/blog/citizen-development-kpis-and-roi/), [AWS 기술 블로그](https://aws.amazon.com/ko/blogs/tech/cj-oliveyoung-aidlc-tech-blog/), [AWS Korea Blog](https://aws.amazon.com/ko/blogs/korea/how-frontier-teams-are-reinventing-ai-native-development/) |
| 상충 증거 (A) | GenAI 파일럿 88~95% P&L 기여 없음(MIT NANDA·IDC), 기업 AI 이니셔티브 포기율 42%(S&P Global 2025), 인접 도메인 선행 사례(비전문 시티즌 개발자 3주 배포 완성)가 조사 범위 내 미발견 | [MIT NANDA via Fortune](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/), [S&P Global via Fluidlabs](https://fluidlabs.com/resources/why-42-percent-enterprise-ai-abandoned-2025), [GSoC Evaluations Guide](https://google.github.io/gsocguides/mentor/evaluations), [AngelHack](https://angelhack.com/blog/ai-internal-hackathon/) |
| 상충 증거 (B) | DORA 2025 "AI는 증폭기—강한 플랫폼 없이 AI 단독 도입은 안정성 저하"; IDP MVP 정석 16주(8+8), 카탈로그 위생 없이 AI 도입 시 변경 실패율 +30% | [DORA 2025 via platformengineering.com](https://platformengineering.com/features/dora-2025-ai-wont-save-you-without-a-solid-platform/), [platformengineering.org](https://platformengineering.org/blog/how-to-set-up-an-internal-developer-platform), [Cortex 2025 via Medium AI Transfer Lab](https://medium.com/@ai_transfer_lab/internal-developer-platforms-in-the-mcp-era-how-idp-teams-are-embedding-claude-as-a-list-class-846abc073117 ⚠(dead link)) |
| **판정** | **조건부 가능** — 사전 골든 패스(AWS 6대 템플릿) + CoE 병행 + 소유권 단일 책임자가 전제되어야만 현실성 확보. 전제 없이 "AI 도구만으로 3주 배포"는 실패 가능성이 압도적으로 높음. 인접 도메인 선행 사례가 없어 낙관적 ROI 수치를 그대로 채택하기 어려움. | - |

### 2.2 파일럿 코호트 규모

| 구분 | 내용 | 출처 |
|---|---|---|
| 일치 증거 | Kissflow·Innovation Mode 기준 파일럿은 2~3개 부서·팀당 3~5명. AI 코딩 도구 파일럿 20~30명 권고(IntuitionLabs) | [Kissflow](https://kissflow.com/no-code/citizen-developer-program/), [Innovation Mode](https://theinnovationmode.com/corporate-hackathon-template), [IntuitionLabs](https://intuitionlabs.ai/articles/claude-enterprise-deployment-training-guide-2026) |
| 상충 증거 | Anthropic 공식 Enterprise Administrator Guide: 파일럿 50~100명(SCIM 초기 그룹), 2~4주; systemprompt.io: 초기 3~5명 후 10~20명 확대; Anthropic Cowork 튜토리얼: 4단계 3~5→10~20→30~60→50~200+명 | [Claude Enterprise Administrator Guide](https://claude.com/resources/tutorials/claude-enterprise-administrator-guide), [systemprompt.io](https://systemprompt.io/guides/claude-code-organisation-rollout) |
| **판정** | **미해결** — Anthropic 공식(50~100명)·서드파티 가이드(3~5명 초기)·씨앗(20~30명)이 모두 다르며, 이는 대상(전문 개발자 vs 시티즌 개발자)·목적(AI 코딩 도구 확산 vs 탑다운 과제 파일럿)의 차이에서 기인한다. 비전문 시티즌 개발자 특화 AI 코딩 파일럿 규모 벤치마크 1차 출처가 없어 판정 불가. 단, d5 골든 패스 가이드 "초기 2~3개 자발 팀"은 팀 수 기준으로 규모 억제를 지지한다. | - |

### 2.3 게이트 설계의 실효성

| 구분 | 내용 | 출처 |
|---|---|---|
| 일치 증거 | 수동 승인 게이트 필요성 자체: IT 리더 73%(데이터 무결성 우려)·69%(보안 취약점 우려), 거버넌스 있는 조직 77% vs 없는 조직 39% 비용 절감 성공(KPMG Belgium 2024). AI 코드 취약점 밀도 2.74배 | [Flosum](https://www.flosum.com/blog/the-unintended-security-threat-of-citizen-development), [KPMG Belgium](https://kpmg.com/be/en/home/insights/2024/11/ta-transforming-business-value-creation-with-citizen-development.html), [Veracode 2025](https://www.veracode.com/blog/spring-2026-genai-code-security/) |
| 상충 증거 (A) | CI/CD 자동검사는 아키텍처·로직 결함 탐지 불가(Checkmarx 2025). AI 코드에 XSS 방어 실패 85%·로그 인젝션 실패 87%(Veracode Spring 2026). AI 코드 승인율 +14.5%p·코멘트 -22%로 rubber-stamping 실증(arXiv 2606.22721). Copilot PR 리뷰 시간 17.2시간(인간 3.9시간 대비 4.4배) | [Checkmarx](https://checkmarx.com/blog/ai-is-writing-your-code-whos-keeping-it-secure/), [Veracode Spring 2026](https://www.veracode.com/blog/spring-2026-genai-code-security/), [arXiv 2606.22721](https://arxiv.org/pdf/2606.22721), [Codacy Blog](https://blog.codacy.com/ai-breaking-code-review-how-engineering-teams-survive-pr-bottleneck) |
| 상충 증거 (B) | "복잡한 승인 프로세스가 Shadow AI 사용을 촉진"한다는 역설 — 도구 기준 게이트 대신 위험 기준(색상 분류) 게이트 권고 | [Elegant Software Solutions](https://www.elegantsoftwaresolutions.com/blog/vibe-coding-enterprise-adoption) |
| 대안 증거 | 3-lane 리스크 기반 리뷰(Green/Yellow/Red), Red에 3인 승인 필수(metacto 2026-07-08). Semgrep AI-Powered Detection으로 IDOR·인가 오류 부분 자동화 가능. Rubber-stamping 방지 3장치(서면 정당화·분산 배치·로테이션). 리스크 계층별 SLA 차등화(피어 리뷰 4h, 아키텍처 리뷰 24h) | [metacto](https://www.metacto.com/blogs/establishing-code-review-standards-for-ai-generated-code), [Semgrep](https://semgrep.dev/blog/2025/ai-powered-detection-with-semgrep/), [GoTranscript](https://gotranscript.com/en/blog/turnaround-time-vs-quality-set-slas-without-increasing-risk) |
| **판정** | **조건부 수렴** — 씨앗의 "CI/CD 자동검사 + AI Board·정보보호팀 수동 승인" 2단 게이트만으로는 불충분. 실효성 확보를 위해 (1) 3-lane 위험 분류, (2) Red lane 3인 승인, (3) rubber-stamping 방지 장치(서면 정당화·로테이션), (4) SLA 차등화를 추가 설계해야 함. Shadow AI 유발 역설을 방지하기 위해 게이트는 위험 기준으로 설계한다. Semgrep AI-SAST는 보조 수단(완전 대체 불가). | - |

### 2.4 AI 코딩 도구의 효과 — ROI vs 역효과

| 구분 | 내용 | 출처 |
|---|---|---|
| 일치 증거 | 건강한 ROI 범위 2.5~3.5배(평균), 상위 25% 조직 4~6배(Exceeds.ai 2025). 개인 작업 ~21% 증가(Index.dev 2025). PR 병합 +98%(DORA 2025). IBM 45% 생산성 향상(공식 뉴스룸, 6,000명 전문 개발자) | [Exceeds.ai](https://blog.exceeds.ai/enterprise-ai-adoption-metrics-2025/), [Index.dev](https://www.index.dev/blog/ai-coding-assistants-roi-productivity), [IBM Newsroom](https://newsroom.ibm.com/2025-10-07-2025-ibm-and-anthropic-partner-to-advance-enterprise-software-development-with-proven-security-and-governance) |
| 상충 증거 | 배포 안정성 -7.2%(DORA 2024). 기술 부채 30~41% 증가(8.1M PR 분석, Pixelmojo 2026). 코드 중복 8배·리팩토링 -60%(GitClear, 211M 라인, 2025-02). 에이전틱 도구 10주 지속 사용률 <10%(DORA 2025, 5,000명 응답). DORA "AI는 증폭기—강한 팀은 더 강해지고 취약 팀은 문제만 커진다" | [Google DORA 2024 via DevOps.com](https://devops.com/ai-in-software-development-productivity-at-the-cost-of-code-quality-2/), [Pixelmojo](https://www.pixelmojo.io/blogs/vibe-coding-technical-debt-crisis-2026-2027), [GitClear](https://www.gitclear.com/ai_assistant_code_quality_2025_research ⚠(dead link)), [Jellyfish DORA 2025](https://jellyfish.co/blog/2025-dora-report/) |
| **판정** | **조건부 보강** — ROI 수치는 개인 생산성(단기) 기준이며 조직 안정성·장기 유지보수성 관점에서는 역효과가 실증됨. "AI는 증폭기" 명제 수렴: 골든 패스·CoE·거버넌스가 강한 조직에서는 ROI 실현, 약한 조직에서는 부채·취약점 축적. 파일럿 ROI는 구조적으로 운영 ROI를 과대평가(위험 조정 ROI 재계산 필수). 시티즌 개발자 특화 ROI 데이터는 없으며 전문 개발자 수치를 그대로 적용 불가. | - |

### 2.5 종료·이관 방식 — 자동 선셋 vs 보드 심의

| 구분 | 내용 | 출처 |
|---|---|---|
| 일치 증거 | 파일럿 시작 전 Go/No-Go 스코어카드 합의 필수(Traction Technology). 결정 권한자(named decision owner) 사전 지정(Traction Technology). AWS Innovation Sandbox 계정 라이프사이클 자동화(Entry→Frozen→CleanUp 상태머신) | [Traction Technology](https://www.tractiontechnology.com/blog/how-to-run-a-successful-pilot-with-a-startup-frameworks-kpis-enterprise-best-practices), [AWS Docs Innovation Sandbox](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/account-lifecycle-in-isb.html) |
| 상충 증거 | 외부 사례: AWS Innovation Sandbox Frozen 후 14일 자동 접근 회수·21일 자동 리소스 삭제. 내부 기획안: "자동 선셋 미적용, 사업 판단(보드 심의)으로 결정" 원칙 (내부: AWS_기반_탑다운_AIFAB_과제_운영환경_구축운영_기획안_v1-0.md §7) (내부 자료, 독립 검증 불가) | [AWS Docs Innovation Sandbox](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/account-lifecycle-in-isb.html), (내부: 탑다운 기획안 §7) |
| 신규 증거 | d3 인접 프로그램의 3방향 출구(Scale/Stop/Redirect → 이관/폐기/현업복귀) 설계. 삼성 C-Lab "1년+스핀오프 3개월" 이중 출구. SK하이닉스 HiGarage "창업/사내 사업화" 이중 출구 | [Samsung Sustainability](https://www.samsung.com/sec/sustainability/popup/popup_doc/AYUBw0_6ArQAIx8i/), [디일렉 SK하이닉스](https://www.thelec.kr/news/articleView.html?idxno=614 ⚠(dead link)) |
| **판정** | **하이브리드 채택** — 자동 Frozen(비용 임계값 초과 시 접근 차단)은 AWS 자동화로 적용하되, 최종 리소스 삭제·계정 폐쇄는 보드 심의로 결정한다. 이는 내부 기획안 원칙(보드 심의)을 존중하되 비용 통제(자동 Frozen)를 병행하는 절충안으로, 양쪽 증거를 모순 없이 수용한다. 종료 출구는 이관/폐기/현업복귀 3방향으로 설계한다. | - |

### 2.6 지속 사용 정착 — 챔피언 프로그램 vs 자연 이탈

| 구분 | 내용 | 출처 |
|---|---|---|
| 일치 증거 | 에이전틱 도구 10주 지속 사용률 <10%(DORA 2025, 5,000명). 지속 사용 정착이 핵심 과제임을 다수 출처 확인 | [DORA 2025 via Jellyfish](https://jellyfish.co/blog/2025-dora-report/), [DORA 2025 via Faros.ai](https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025) |
| 상충 증거 | 챔피언 프로그램의 정량 효과: 하향식 대비 2.1배 지속 사용률(Worklytics via aiassemblylines.com 2026), 챔피언 시연 시 채택률 62%→85%(Adoptify.ai), 90일 WAU 47% 달성 | [AI Assembly Lines](https://aiassemblylines.com/post/ai-champions-program-enterprise-adoption) |
| 신규 증거 | Anthropic 공식 Champion Kit: 챔피언 주 40분 예산·30일 4주 플레이북·3원칙(share/ask/circle). 챔피언 비율 25~50명당 1명(Cowork). 3단계 체크인(30~60일 주간 오피스아워 → 3개월 회고 → 분기 비즈니스 리뷰). CHI 2026 행동 설계 4원칙 | [Claude Code Champion Kit](https://code.claude.com/docs/en/champion-kit), [Scaling Claude Cowork](https://claude.com/resources/tutorials/scaling-workflows-with-claude-cowork-at-your-organization), [CHI 2026](https://dl.acm.org/doi/full/10.1145/3772363.3799043 ⚠(dead link)) |
| **판정** | **챔피언 프로그램 채택** — 10% 미만 자연 지속 사용률은 구조적 개입 없이는 파일럿 효과가 소멸함을 의미한다. 챔피언 2.1배 효과(Worklytics)·62→85% 채택률(Adoptify.ai)은 단일 출처이며 독립 검증이 없어 신뢰도는 중간 수준이나, Anthropic 공식 설계와 방향이 일치한다. 챔피언 프로그램 + 3단계 체크인 구조를 채택한다. 단, Worklytics·Adoptify.ai 수치는 "내부 자료 수준" 신뢰도로 취급하며 독립 검증이 필요하다. | - |

### 2.7 골든 패스 사전 준비의 필수성

| 구분 | 내용 | 출처 |
|---|---|---|
| 일치 증거 | DORA 2025 "플랫폼 없이 AI 단독 도입=안정성 저하". 골든 패스 MVP 목표 제로→스테이징 배포 <1시간(Tasrie IT 2026). IDP 도입 후 온보딩 30~60% 단축 | [DORA 2025 via platformengineering.com](https://platformengineering.com/features/dora-2025-ai-wont-save-you-without-a-solid-platform/), [Tasrie IT](https://tasrieit.com/blog/golden-paths-platform-engineering-guide-2026) |
| 상충 증거 | IDP 정석 MVP 16주(8+8) vs 3주 파일럿의 시간 긴장. 카탈로그 위생 없이 AI 도입 시 변경 실패율 +30%·PR당 인시던트 +23.5%(Cortex 2025). 골든 패스 문헌은 전문 개발자 대상이며 시티즌 개발자 특화 사례 미발견 | [platformengineering.org](https://platformengineering.org/blog/how-to-set-up-an-internal-developer-platform), [Cortex 2025 via Medium AI Transfer Lab](https://medium.com/@ai_transfer_lab/internal-developer-platforms-in-the-mcp-era-how-idp-teams-are-embedding-claude-as-a-first-class-846abc073117 ⚠(dead link)) |
| **판정** | **필수 전제 채택** — 3주 파일럿에서 배포 완성이 가능하려면 골든 패스(AWS 6대 템플릿: ECS on Fargate·Lambda·RDS·비용태그·관측성·Secrets Manager)가 파일럿 킥오프 전에 완비되어야 한다. IDP 정석 16주와 3주 파일럿의 긴장은 "파일럿 이전 선행 준비 기간"으로 해소한다. 카탈로그 정확도가 낮으면 AI 도입 자체가 리스크를 높이므로 사전 위생 점검이 필수다. | - |

### 2.8 멘토·CoE 체계의 규모와 실효성

| 구분 | 내용 | 출처 |
|---|---|---|
| 일치 증거 | CoE 2~5명 구성이 업계 표준(Kissflow·ISG·d2-dd). H&M 4명으로 1,500개 앱·30,000명 지원(Microsoft Power Platform Blog). Co-development 초기 CoE 50%→ 0~2% 점감(Microsoft Learn). 오피스아워 주 1회 이상 | [Kissflow](https://kissflow.com/no-code/citizen-developer-program/), [Microsoft Power Platform Blog](https://www.microsoft.com/en-us/power-platform/blog/power-apps/hmgroup/), [Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap-mentoring-and-user-enablement) |
| 상충 증거 | "CoE 2~5인으로 모든 PR 심층 리뷰는 물리적으로 불가"(Checkmarx 2025). 보안 훈련은 시티즌 개발자 보안 문제를 해결하지 못함—규모·속도·다양성이 교육 한계 초과(TechNewsWorld). GSoC 멘토:참가자 1.64:1(역방향), Meta 1:2~3. 단기 파일럿에서는 멘토 밀도가 높아야 한다는 인접 사례 근거 | [Checkmarx](https://checkmarx.com/blog/ai-is-writing-your-code-whos-keeping-it-secure/), [TechNewsWorld](https://www.technewsworld.com/story/why-training-wont-solve-the-citizen-developer-security-problem-179877.html ⚠(dead link)), [GSoC 2025 Statistics](https://opensource.googleblog.com/2025/08/google-summer-of-code-2025-contributor-statistics.html), [AutomationHacks](https://newsletter.automationhacks.io/p/engineering-practices-meta-3-conduct) |
| **판정** | **CoE 선행 구축 + 기술 통제 내재화 채택** — CoE 2~5명은 "프로그램 프레임워크·승인·커뮤니티 운영"을 담당하되, "모든 PR 심층 보안 리뷰"까지 담당하는 것은 현실적으로 불가능하다. 보안은 개발 경험 내 기술적 통제(SAST·lint·골든 패스 내장 정책) 임베딩으로 보완해야 한다. 3주 파일럿의 단기 집중 특성상 초기 멘토 밀도를 높게(co-development 50% 비율) 설정한다. | - |

### 2.9 파일럿 종료 이후 기술 부채의 이관 부담

| 구분 | 내용 | 출처 |
|---|---|---|
| 일치 증거 | 3주 스프린트 이후 AI 생성 코드의 장기 유지보수성 우려 존재(GitClear·Pixelmojo). 파일럿 종료 후 이관팀이 기술 부채를 떠안는 시나리오 제기(d2) | [GitClear](https://www.gitclear.com/ai_assistant_code_quality_2025_research ⚠(dead link)), [Pixelmojo](https://www.pixelmojo.io/blogs/vibe-coding-technical-debt-crisis-2026-2027) |
| 상충 증거 | 기술 부채 처리 비용·이관팀 수용 의사에 대한 사례 연구 부재. 내부 기획안 7단계 격상 절차는 "재작성 없이 수용"을 원칙으로 하나, AI 생성 코드의 기술 부채를 고려한 수용 기준이 없음(내부 자료, 독립 검증 불가) | (내부: 탑다운 기획안 §6) |
| **판정** | **미해결** — 이관팀이 AI 생성 코드의 기술 부채를 수용하는 조건·비용 기준이 내부에도 외부에도 없다. 파일럿 종료 전 이관팀과 기술 부채 수용 기준을 사전 합의하는 절차가 필요하나, 이를 뒷받침할 사례 근거가 없어 판정 불가. | - |

---

## 3. 통합 논리 구조

1. **3주 배포 완성은 "골든 패스 사전 완비" 없이는 비현실적이며, 있어도 조건부 가능이다.**
   - 근거: DORA 2025 "AI는 증폭기, 강한 플랫폼 없이 안정성 저하" ([DORA 2025 via platformengineering.com](https://platformengineering.com/features/dora-2025-ai-wont-save-you-without-a-solid-platform/)); GenAI 파일럿 실패율 88~95% ([MIT NANDA via Fortune](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/)); 골든 패스 없이는 AI 생성 코드 변경 실패율 +30% ([Cortex 2025 via Medium AI Transfer Lab](https://medium.com/@ai_transfer_lab/internal-developer-platforms-in-the-mcp-era-how-idp-teams-are-embedding-claude-as-a-first-class-846abc073117 ⚠(dead link))); 역으로 IDP 성숙 조직의 온보딩 67% 단축·첫 배포 1시간 미만([Spotify Backstage](https://backstage.spotify.com/discover/blog/how-we-measure-backstage-success-at-spotify), [Tasrie IT](https://tasrieit.com/blog/golden-paths-platform-engineering-guide-2026))
   - **운영 함의**: 킥오프 최소 4~6주 전에 AI 인프라팀이 AWS 6대 골든 패스(ECS on Fargate·Lambda·RDS·비용태그·관측성·Secrets Manager) 완비 ([The Cloud Playbook TCP#124](https://www.thecloudplaybook.com/p/first-6-golden-paths-aws-platform-teams)); 시티즌 개발자는 폼 입력만으로 CI/CD·IAM·모니터링 포함 레포 자동 생성

2. **파일럿 운영 구조는 Agile-Stage-Gate 하이브리드(W1 Gate 0 → W2 중간 Gate → W3 Gate 2+배포)가 기업 거버넌스와 스프린트 속도를 동시에 충족하는 최적 구조다.**
   - 근거: Agile-Stage-Gate 게이트 결정 24~48시간 이내 ([Umbrex Stage-Gate](https://umbrex.com/resources/frameworks/strategy-frameworks/stage-gate-innovation-process/)); 내부 기획안 AI Board·정보보호팀 수동 승인 게이트와 직접 연계(내부: 탑다운 기획안 §5, 내부 자료 독립 검증 불가); GSoC 중간 평가 "한계 통과" 참가자 80%+ 최종 실패 → 중간 Gate는 단순 통과/실패보다 정교한 조기 경보 필요([GSoC Evaluations Guide](https://google.github.io/gsocguides/mentor/evaluations))
   - **운영 함의**: Gate 2(배포 승인)는 3-lane 위험 분류 기반으로 설계: Green(내부 UI·문서·테스트) 표준 승인, Yellow(비즈니스 로직·API) 시니어 사인오프, Red(Auth·PII·인프라) 3인 승인(주 리뷰어+시니어+보안 오너) ([metacto 2026-07-08](https://www.metacto.com/blogs/establishing-code-review-standards-for-ai-generated-code)); rubber-stamping 방지를 위해 서면 정당화·로테이션 의무화

3. **CoE 선행 구축이 파일럿 성공률을 결정한다. 거버넌스 구조 유무에 따른 성공률 차이가 2배(77% vs 39%)이며, 단기 파일럿일수록 초기 멘토 밀도를 높여야 한다.**
   - 근거: KPMG Belgium 2024([KPMG Belgium](https://kpmg.com/be/en/home/insights/2024/11/ta-transforming-business-value-creation-with-citizen-development.html)); BCG 10-20-70 법칙—AI 성공의 70%는 사람·프로세스·문화([Forbes via BCG](https://www.forbes.com/sites/joemckendrick/2026/01/26/why-ais-10-20-70-principle-should-matter-to-ceos-and-everyone-else/)); Co-development 초기 CoE 50%→ 점감([Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap-mentoring-and-user-enablement))
   - **운영 함의**: 2~5명 CoE가 프로그램 프레임워크·과제 검토(비즈니스+기술 2단계)·챔피언 운영을 담당. 보안 리뷰는 개발 경험 내 SAST·골든 패스 내장 정책으로 내재화(CoE의 전수 PR 리뷰는 물리적 불가)

4. **KPI는 킥오프 전 동결하고, ROI는 위험 조정 후 재계산해야 한다. 에이전틱 도구 10주 지속 사용률 <10%는 챔피언 프로그램 없이는 파일럿 효과가 소멸함을 의미한다.**
   - 근거: KPI 사전 동결 원칙([MarginLayer](https://marginlayer.app/blog/pilot-success-criteria-kpi-roi.html)); Anthropic 공식 6개 KPI(WAU 70%, 주당 메시지 25+건, 만족도 4.0/5.0+, 시간 절감 3시간+)([Claude Enterprise Administrator Guide](https://claude.com/resources/tutorials/claude-enterprise-administrator-guide)); DORA 2025 <10% 지속 사용([DORA 2025 via Jellyfish](https://jellyfish.co/blog/2025-dora-report/)); 챔피언 2.1배 효과([AI Assembly Lines](https://aiassemblylines.com/post/ai-champions-program-enterprise-adoption))
   - **운영 함의**: 파일럿 KPI: 배포 완성 건수·WAU·사이클 타임·거버넌스 준수율·참여자 만족도를 킥오프 전 문서화. 챔피언 25~50명당 1명 배치([Anthropic Cowork](https://claude.com/resources/tutorials/scaling-workflows-with-claude-cowork-at-your-organization)), 주 30분 오피스아워·월간 부서간 데모데이 운영. 전사 확대 전 DECIDE 4대 질문으로 판단([Agility at Scale](https://agility-at-scale.com/ai/strategy/roi-and-success-metrics/))

5. **종료·이관은 소유권 단일 책임자 사전 지정 + 3방향 출구(이관/폐기/현업복귀) + 자동 Frozen·보드 최종 결정 하이브리드로 설계한다.**
   - 근거: 소유권 공백이 파일럿-프로덕션 전환 최대 장애([SoftwareSeni](https://www.softwareseni.com/the-enterprise-ai-pilot-purgatory-problem-what-the-statistics-actually-tell-us/)); AWS Innovation Sandbox 자동 Frozen→14일 접근 회수·21일 자동 삭제([AWS Docs Innovation Sandbox](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/account-lifecycle-in-isb.html)); 내부 기획안 7단계 격상 체크리스트·보드 심의 종료 원칙(내부: 탑다운 기획안 §6·§7, 내부 자료 독립 검증 불가); 사내벤처 이중 출구([Samsung Sustainability](https://www.samsung.com/sec/sustainability/popup/popup_doc/AYUBw0_6ArQAIx8i/))
   - **운영 함의**: 파일럿 착수 전 Go/No-Go 스코어카드(기술 40%·재무 30%·시장 20%·자원 10%, 임계값 0.605)와 결정 권한자 지정([Visual Paradigm](https://guides.visual-paradigm.com/making-informed-decisions-with-a-go-no-go-checklist-for-agile-projects-a-scoring-approach/), [Traction Technology](https://www.tractiontechnology.com/blog/how-to-run-a-successful-pilot-with-a-startup-frameworks-kpis-enterprise-best-practices)). 종료 시 클로저 레코드(15~20분 작성, 4개 항목) 작성 후 영구 보존

---

## 4. 미해결 쟁점·리스크

> 단계 5(정규화·결론)의 입력

1. **파일럿 코호트 규모(쟁점 2.2)**: Anthropic 공식 50~100명 vs 씨앗 20~30명 vs systemprompt.io 3~5명 초기. 비전문 시티즌 개발자 특화 AI 코딩 파일럿 규모 벤치마크 1차 출처가 없어 판정 불가. 내부에서 파일럿 목적(AI 도구 채택 확산 vs 탑다운 과제 완성)에 따라 규모를 별도 정의해야 한다.

2. **AI 생성 코드의 이관 기술 부채 수용 기준(쟁점 2.9)**: 파일럿 종료 후 이관팀이 AI 생성 코드의 기술 부채(기술 부채 30~41% 증가, 코드 중복 8배)를 수용하는 조건·비용 기준이 내부·외부 모두 미정의. 이관 거부 시 Pilot Purgatory 재현 위험.

3. **3주 배포 완성의 시티즌 개발자 실증 데이터 부재**: 비전문 개발자가 3주 만에 운영환경 배포까지 완성한 직접 사례가 조사 범위 내 확인되지 않음. 골든 패스 사전 완비 + AI 코딩 도구 조합의 배포 완성률·실패율 벤치마크 미확보.

4. **Rubber-stamping 방지 장치의 3주 사이클 적용 가능성**: 3-lane × 3인 리뷰 체제가 3주 타임박스 안에서 소화 가능한지 실증 데이터 없음. 대부분 사례는 상시 개발 조직 기준.

5. **챔피언 프로그램 정량 효과의 독립 검증 부재**: Worklytics "2.1배 지속 사용률"·Adoptify.ai "62→85%" 수치가 단일 출처이며 동료 검토 연구가 아닌 업계 보고서 기반. 신뢰도 중간 수준.

6. **복잡한 승인 게이트 → Shadow AI 촉진 역설의 관리**: 엄격한 3-lane 게이트가 오히려 비공식 AI 도구 사용을 조장할 수 있다는 역설([Elegant Software Solutions](https://www.elegantsoftwaresolutions.com/blog/vibe-coding-enterprise-adoption)). 게이트 복잡도와 Shadow AI 발생률 간의 임계점 데이터 미확보.

---

## 5. Sources

### 웹 출처 (주요)

- https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/ (Fortune / MIT NANDA, 2025-08-18)
- https://fluidlabs.com/resources/why-42-percent-enterprise-ai-abandoned-2025 (Fluidlabs / S&P Global, 2025)
- https://www.gartner.com/en/newsroom/press-releases/2024-07-29-gartner-predicts-30-percent-of-generative-ai-projects-will-be-abandoned-after-proof-of-concept-by-end-of-2025 ⚠(dead link) (Gartner Press Release, 2024-07-29)
- https://www.softwareseni.com/the-enterprise-ai-pilot-purgatory-problem-what-the-statistics-actually-tell-us/ (SoftwareSeni, 날짜 미상)
- https://www.forbes.com/sites/joemckendrick/2026/01/26/why-ais-10-20-70-principle-should-matter-to-ceos-and-everyone-else/ (Forbes / BCG, 2026-01-26)
- https://www.veracode.com/blog/spring-2026-genai-code-security/ (Veracode Spring 2026 GenAI Code Security Report, 2026-04)
- https://apiiro.com/blog/4x-velocity-10x-vulnerabilities-ai-coding-assistants-are-shipping-more-risks/ (Apiiro, 2025-09-04)
- https://arxiv.org/pdf/2606.22721 (arXiv: Habituation at the Gate, 2026-06-23)
- https://www.metacto.com/blogs/establishing-code-review-standards-for-ai-generated-code (metacto, 2026-07-08)
- https://checkmarx.com/blog/ai-is-writing-your-code-whos-keeping-it-secure/ (Checkmarx, 2025)
- https://www.gitclear.com/ai_assistant_code_quality_2025_research ⚠(dead link) (GitClear, 2025-02)
- https://www.pixelmojo.io/blogs/vibe-coding-technical-debt-crisis-2026-2027 (Pixelmojo, 2026)
- https://devops.com/ai-in-software-development-productivity-at-the-cost-of-code-quality-2/ (DevOps.com / Google DORA 2024, 2025)
- https://google.github.io/gsocguides/mentor/evaluations (GSoC Evaluations Guide, 2025)
- https://opensource.googleblog.com/2025/08/google-summer-of-code-2025-contributor-statistics.html (GSoC 2025 Statistics, 2025-08)
- https://angelhack.com/blog/ai-internal-hackathon/ (AngelHack, 2024)
- https://www.samsung.com/sec/sustainability/popup/popup_doc/AYUBw0_6ArQAIx8i/ (Samsung C-Lab Sustainability, 2025)
- https://live.lge.co.kr/venture/ (LG전자 뉴스룸 사내벤처, 2024)
- https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025 (DORA 2025 / Faros.ai, 2025-09)
- https://dora.dev/insights/balancing-ai-tensions/ (DORA Insights, 2025)
- https://systemprompt.io/guides/claude-code-organisation-rollout (systemprompt.io Claude Code Rollout Playbook, 날짜 미상)
- https://claude.com/resources/tutorials/claude-enterprise-administrator-guide (Claude Enterprise Administrator Guide, 날짜 미상)
- https://claude.com/resources/tutorials/scaling-workflows-with-claude-cowork-at-your-organization (Scaling workflows with Claude Cowork, 날짜 미상)
- https://code.claude.com/docs/en/champion-kit (Claude Code Champion Kit, 날짜 미상)
- https://newsroom.ibm.com/2025-10-07-2025-ibm-and-anthropic-partner-to-advance-enterprise-software-development-with-proven-security-and-governance (IBM Newsroom, 2025-10-07)
- https://aiassemblylines.com/post/ai-champions-program-enterprise-adoption (AI Assembly Lines, 2026)
- https://jellyfish.co/blog/2025-dora-report/ (Jellyfish DORA 2025, 2025)
- https://platformengineering.com/features/dora-2025-ai-wont-save-you-without-a-solid-platform/ (Platform Engineering / DORA 2025, 2025)
- https://platformengineering.org/blog/how-to-set-up-an-internal-developer-platform (platformengineering.org, 날짜 미상)
- https://www.thecloudplaybook.com/p/first-6-golden-paths-aws-platform-teams (The Cloud Playbook TCP#124, 날짜 미상)
- https://tasrieit.com/blog/golden-paths-platform-engineering-guide-2026 (Tasrie IT, 2026-01)
- https://backstage.spotify.com/discover/blog/how-we-measure-backstage-success-at-spotify (Spotify Backstage, 2020~)
- https://2023.platformcon.com/talks/how-toyota-saved-over-10m-and-optimized-developer-experience-through-platform-engineering (PlatformCon 2023, 2023-06)
- https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1814498/full (Frontiers in Computer Science, 2026)
- https://kpmg.com/be/en/home/insights/2024/11/ta-transforming-business-value-creation-with-citizen-development.html (KPMG Belgium, 2024-11)
- https://kissflow.com/no-code/citizen-developer-program/ (Kissflow, 날짜 미상)
- https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap-mentoring-and-user-enablement (Microsoft Learn, 2024-12-30)
- https://isg-one.com/articles/the-automation-center-of-excellence-and-citizen-developers-not-the-wild-wild-west! (ISG, 날짜 미상)
- https://www.tractiontechnology.com/blog/how-to-run-a-successful-pilot-with-a-startup-frameworks-kpis-enterprise-best-practices (Traction Technology, 날짜 미상)
- https://guides.visual-paradigm.com/making-informed-decisions-with-a-go-no-go-checklist-for-agile-projects-a-scoring-approach/ (Visual Paradigm, 날짜 미상)
- https://marginlayer.app/blog/pilot-success-criteria-kpi-roi.html (MarginLayer, 날짜 미상)
- https://agility-at-scale.com/ai/strategy/roi-and-success-metrics/ (Agility at Scale, 날짜 미상)
- https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/account-lifecycle-in-isb.html (AWS Docs Innovation Sandbox, 날짜 미상)
- https://docs.aws.amazon.com/controltower/latest/userguide/decommissioning-process-overview.html (AWS Docs Control Tower, 날짜 미상)
- https://umbrex.com/resources/frameworks/strategy-frameworks/stage-gate-innovation-process/ (Umbrex Stage-Gate, 날짜 미상)
- https://www.elegantsoftwaresolutions.com/blog/vibe-coding-enterprise-adoption (Elegant Software Solutions, 2025)
- https://blog.exceeds.ai/enterprise-ai-adoption-metrics-2025/ (Exceeds.ai, 2025)
- https://www.index.dev/blog/ai-coding-assistants-roi-productivity (Index.dev, 2025)
- https://semgrep.dev/blog/2025/ai-powered-detection-with-semgrep/ (Semgrep, 2025)
- https://gotranscript.com/en/blog/turnaround-time-vs-quality-set-slas-without-increasing-risk (GoTranscript, 날짜 미상)
- https://www.flosum.com/blog/the-unintended-security-threat-of-citizen-development (Flosum, 2024)
- https://pluto.security/blog/citizen-development-security-teams/ (Pluto Security, 2024)
- https://aws.amazon.com/ko/blogs/tech/cj-oliveyoung-aidlc-tech-blog/ (AWS 기술 블로그 CJ올리브영, 날짜 미상)
- https://aws.amazon.com/ko/blogs/korea/how-frontier-teams-are-reinventing-ai-native-development/ (AWS Korea Blog, 2025)
- https://dl.acm.org/doi/full/10.1145/3772363.3799043 ⚠(dead link) (CHI 2026 Extended Abstracts, 2026)

### 내부 문서

| 파일명 | 분석 섹션 | 신뢰도 |
|---|---|---|
| AWS_기반_탑다운_AIFAB_과제_운영환경_구축운영_기획안_v1-0.md | §2 바텀업 차이, §5 개발·배포, §6 격상 절차, §7 운영·모니터링 | 내부 자료(독립 검증 불가) |
