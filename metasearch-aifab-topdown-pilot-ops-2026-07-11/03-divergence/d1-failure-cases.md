# [반례·실패 사례 — 시티즌 개발자·AI 파일럿 실패 원인] 발산 리서치

## 핵심 발견

- **GenAI 파일럿의 88~95%가 프로덕션 진입 실패** — IDC·Lenovo 연구에서 관찰된 PoC 33개 중 4개(12%)만 생산 단계 진입. MIT NANDA 이니셔티브는 기업 GenAI 파일럿의 95%가 P&L 기여 없이 정체된다고 보고 — **씨앗과의 관계: 신규** ([MIT NANDA via Fortune](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/), 2025-08-18; [IDC via CIO Korea](https://www.cio.com/article/3854098/ai-%ED%8C%8C%EC%9D%BC%EB%9F%BF-88%EA%B0%80-%EC%8B%A4%EC%9A%A9%ED%99%94%EC%97%90-%EC%8B%A4%ED%8C%A8%C2%B7%C2%B7%C2%B7-%EC%9D%B4%EB%A9%B4%EC%9D%98-%EC%97%AD%ED%95%99%EC%9D%80.html), 날짜 미상)

- **S&P Global: 기업의 AI 프로젝트 포기율이 1년 만에 17% → 42%로 급등** — 1,000개 이상의 북미·유럽 기업 조사에서 2024년 17%였던 AI 이니셔티브 포기율이 2025년 42%로 급증. 평균적으로 PoC의 46%가 프로덕션 이전에 폐기됨 — **씨앗과의 관계: 신규** ([S&P Global Market Intelligence via Fluidlabs](https://fluidlabs.com/resources/why-42-percent-enterprise-ai-abandoned-2025), 2025; [S&P Global 원문](https://www.spglobal.com/market-intelligence/en/news-insights/research/2025/10/generative-ai-shows-rapid-growth-but-yields-mixed-results ⚠(dead link)), 2025-10)

- **Gartner: GenAI 프로젝트의 30%(2024 예측) → 50%(2026 실측) PoC 이후 폐기** — 주요 원인은 데이터 품질 불량, 부적절한 리스크 통제, 비용 급증, 불명확한 비즈니스 가치. 2026년까지 AI 프로젝트 60%가 AI-ready 데이터 미비로 중단 예측 — **씨앗과의 관계: 보강** ([Gartner Press Release](https://www.gartner.com/en/newsroom/press-releases/2024-07-29-gartner-predicts-30-percent-of-generative-ai-projects-will-be-abandoned-after-proof-of-concept-by-end-of-2025 ⚠(dead link)), 2024-07-29)

- **"Pilot Purgatory" — 파일럿이 취소도 배포도 안 된 채 6~18개월 표류하는 패턴** — 데모가 성공하면 Phase 2가 원칙적으로 승인되나, 이후 책임자 없이 수개월간 방치. Fortune 500 은행 CTO 사례: 18개월간 GenAI PoC 47개 착수 → 실제 프로덕션 진입 3개 — **씨앗과의 관계: 신규** ([SoftwareSeni](https://www.softwareseni.com/the-enterprise-ai-pilot-purgatory-problem-what-the-statistics-actually-tell-us/), 날짜 미상; [Astrafy](https://astrafy.io/the-hub/blog/technical/scaling-ai-from-pilot-purgatory-why-only-33-reach-production-and-how-to-beat-the-odds), 날짜 미상)

- **BCG 10-20-70 법칙: AI 실패의 70%는 사람·프로세스·문화 문제** — 알고리즘 10%, 데이터·기술 20%, 사람·프로세스 70%가 AI 성공의 결정 요인. 그러나 대부분 조직은 예산의 70%를 알고리즘·기술에 투입하고 사람·프로세스를 부록으로 취급 → 기술적 성공 선언 후 6개월 뒤 KPI 미이동 확인 — **씨앗과의 관계: 보강** ([Forbes via BCG](https://www.forbes.com/sites/joemckendrick/2026/01/26/why-ais-10-20-70-principle-should-matter-to-ceos-and-everyone-else/), 2026-01-26)

- **시티즌 개발 프로그램의 구조적 실패 원인 7가지** — 실제 비즈니스 문제의 복잡성, 확장성 취약(DigitalSamaritan 사례: 4일만에 출시 → 확장 시 완전 재구축 필요), 보안 취약, 시스템 통합 실패, 벤더 종속, 훈련 지원 부족, 전문 개발자 역할 과소평가 — **씨앗과의 관계: 신규** ([Blueprint Systems](https://www.blueprintsys.com/blog/7-reasons-why-citizen-developer-never-materialized), 날짜 미상; [ITWorld Korea](https://www.itworld.co.kr/article/3962268/%EB%85%B8%EC%BD%94%EB%93%9C-%EB%A1%9C%EC%9A%B0%EC%BD%94%EB%93%9C-%EB%8F%84%EA%B5%AC%EA%B0%80-%EC%8B%A4%ED%8C%A8%ED%95%98%EB%8A%94-7%EA%B0%80%EC%A7%80-%EC%9D%B4%EC%9C%A0.html), 날짜 미상)

- **거버넌스 없는 시티즌 개발 → Shadow IT 대규모화** — KPMG 715개 EMA 기업 조사: 로우코드 계획자 73%(사용자 65%)가 거버넌스 규칙 미정의. 미정의 상태에서 수백 개의 문서화되지 않은 워크플로우 생성, 핵심 시티즌 개발자 퇴사 시 앱 고아화 발생 — **씨앗과의 관계: 보강** ([Quandary CG](https://quandarycg.com/citizen-development-shadow-it/), 날짜 미상)

- **AI 코딩 도구가 시티즌 개발자 프로그램에 새로운 기술 부채 위험 추가** — AI 보조 코드에서 미해결 기술 부채가 2025년 초 수백 건 → 2026년 2월 11만 건 이상으로 폭증. AI 생성 코드의 30~40%에 CWE급 보안 취약점 포함(OWASP 연구). Google DORA 2024: AI 코딩 도구 사용 25% 증가 시 코드 리뷰는 빨라지나 배포 안정성 7.2% 감소 — **씨앗과의 관계: 신규** ([LeadDev](https://leaddev.com/technical-direction/how-ai-generated-code-accelerates-technical-debt), 날짜 미상; [DevOps.com via DORA 2024](https://devops.com/ai-in-software-development-productivity-at-the-cost-of-code-quality-2/), 2025)

- **소유권 공백(Ownership Vacuum)이 파일럿-프로덕션 전환의 최대 장애** — 성공 조직의 공통 구조적 특성: 빌드 환경과 배포 환경을 동시에 책임지는 단일 책임 소유자 존재. 실패 조직은 데이터 사이언티스트가 실험을 소유하나 프로덕션 결정을 책임지는 리더 부재 — **씨앗과의 관계: 신규** ([SoftwareSeni Pilot Purgatory](https://www.softwareseni.com/the-enterprise-ai-pilot-purgatory-problem-what-the-statistics-actually-tell-us/), 날짜 미상)

- **기업 내 해커톤·파일럿의 생산 전환 실패 구조적 패턴** — 이미 로드맵에서 우선순위 탈락한 아이디어가 해커톤을 통해 재부상하나 동일 이유로 후속 추진력 상실. 포스트-해커톤 인큐베이션 부재, 엔지니어링 소유권 미배정, 통합 작업 미예산 책정이 핵심 실패 원인. 성공 사례의 공통점: 동일 임원 스폰서가 실패와 성공 재시도를 연속 지원 — **씨앗과의 관계: 신규** ([Domo Enterprise AI Hackathons](https://www.domo.com/blog/enterprise-ai-hackathons-workflows ⚠(dead link)), 날짜 미상; [Medium Hackathon Trap](https://medium.com/@swsthik.nair/hackathon-trap-hackathon-hype-vs-production-reality-what-all-student-devs-should-know-a86098b14c5e ⚠(dead link)), 날짜 미상)

---

## 정량 데이터

| 항목 | 수치 | 출처 | 시점 |
|---|---|---|---|
| GenAI 파일럿 P&L 기여 실패율 | 95% | MIT NANDA (150 인터뷰, 350 직원 서베이, 300 공개 배포 분석) | 2025 |
| AI PoC → 프로덕션 전환 실패율 | 88% (33개 중 4개만 진입) | IDC·Lenovo 공동 연구 | 날짜 미상 |
| 기업 AI 이니셔티브 포기율 (2025) | 42% (2024년 17%에서 급등) | S&P Global Market Intelligence (1,000개+ 기업) | 2025 |
| PoC → 프로덕션 이전 폐기 비율 | 46% (평균) | S&P Global | 2025 |
| Gartner GenAI 프로젝트 폐기 예측 | 30%(2024 예측) → 50%(2026 실측) | Gartner | 2024-07, 2026-04 |
| 2026년까지 AI 프로젝트 중단 예측 (데이터 미비 이유) | 60% | Gartner | 2024 |
| 시티즌 개발 거버넌스 규칙 미정의 기업 (로우코드 계획자) | 73% | KPMG (715개 EMA 기업) | 날짜 미상 |
| AI 생성 코드 내 CWE급 보안 취약점 포함율 | 30~40% | OWASP/학술 연구 | 2024-2025 |
| BCG: AI 성공의 사람·프로세스·문화 기여 비중 | 70% | BCG | 2024-2026 |
| 내부 빌드 AI 파일럿 성공율 | ~33% (벤더 파트너십 67%의 절반) | MIT NANDA | 2025 |
| CEO: AI 투자 재무 성과 없음 응답 | 56% | PwC 2026 CEO Survey | 2026 |
| McKinsey: AI 명확한 전략 보유 기업 성공률 vs 미보유 | 80% vs 37% | McKinsey | 2025 |
| AI 코딩 도구 사용 시 배포 안정성 변화 | -7.2% | Google DORA Report 2024 | 2024 |
| AI 보조 코드 미해결 기술 부채 건수 (2025→2026.2) | 수백 건 → 110,000건+ | 복수 코드 분석 연구 | 2025-2026 |

---

## 씨앗 보고서와의 관계 요약

- **보강**: 씨앗 보고서의 "거버넌스 있는 조직 77% vs 없는 조직 39% 비용 절감 성공" (KPMG Belgium 2024) 결론과 일관되게, 거버넌스 부재가 시티즌 개발 프로그램을 Shadow IT로 전락시키고 파일럿을 Pilot Purgatory에 빠뜨리는 핵심 원인임이 다수 출처에서 확인됨. BCG 10-20-70 법칙은 씨앗의 CoE·KPI 설계가 올바른 방향임을 지지함.

- **상충**: 씨앗 보고서는 시티즌 개발자 프로그램의 성공 사례(CJ올리브영 5배 속도, 배포 속도 5~10배)를 강조하나, 현실에서는 파일럿의 88~95%가 프로덕션에 진입하지 못하고(MIT NANDA, IDC), 기업의 42%가 AI 이니셔티브를 포기(S&P Global 2025)하는 실패 현실과 대조됨. 씨앗의 "3주 배포 완성"이 극히 예외적 사례일 가능성이 높음. 또한 AI 코딩 도구(Claude Code 등)가 속도를 높이는 동시에 기술 부채와 배포 불안정성을 증가시킨다는 역효과 증거(DORA 2024)는 씨앗의 ROI 2.5~3.5배 주장과 조건부 상충.

- **신규**: ① "Pilot Purgatory" — 취소도 배포도 안 된 상태로 6~18개월 표류하는 패턴(단순 실패가 아닌 무책임 방치 패턴)이 새 개념으로 추가됨. ② 소유권 공백(Ownership Vacuum)이 기술 문제보다 더 치명적인 실패 원인임. ③ AI 코딩 도구 사용 자체가 기술 부채·보안 취약점을 양산하는 역설적 위험이 신규 확인됨. ④ 해커톤 프로젝트는 이미 로드맵에서 탈락한 아이디어의 재부상 경로인 경우가 많아 구조적으로 후속 추진력이 약함.

---

## 한계

- **국내(한국) 기업의 시티즌 개발자 프로그램 구체적 폐기 사례**: 한국어·영어 검색 모두에서 국내 기업의 구체적 실패 사례(기업명, 수치)를 담은 1차 출처를 확보하지 못함. 국내에서 로우코드/노코드 도입 자체가 아직 초기 단계라는 보도가 있어, 실패 사례 공개 자료가 부족한 것으로 추정됨.
- **"3주 스프린트 배포 완성" 프로그램의 직접 실패 사례**: 씨앗 보고서의 한계를 그대로 공유함. 동일 조건(3주 타임박스, AI 코딩 도구 활용, 비개발자 시티즌 팀)의 실패 벤치마크 데이터는 미확보.
- **실패 데이터의 생존 편향**: 성공 사례 위주로 발표되는 편향이 실패 통계에도 적용됨 — S&P Global이나 IDC 설문 기반 자료는 포기 기업이 자발적으로 응답하지 않을 가능성.
- **인용 수치의 정의 불일치**: "파일럿 실패"의 정의가 연구마다 상이(P&L 기여 없음 vs. 프로덕션 미진입 vs. 프로젝트 취소)하여 88%, 95%, 42% 등 수치 간 단순 비교는 주의 필요.

---

## 출처

- https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/ (Fortune / MIT NANDA, 2025-08-18)
- https://www.gartner.com/en/newsroom/press-releases/2024-07-29-gartner-predicts-30-percent-of-generative-ai-projects-will-be-abandoned-after-proof-of-concept-by-end-of-2025 ⚠(dead link) (Gartner Press Release, 2024-07-29)
- https://www.spglobal.com/market-intelligence/en/news-insights/research/2025/10/generative-ai-shows-rapid-growth-but-yields-mixed-results ⚠(dead link) (S&P Global Market Intelligence, 2025-10)
- https://fluidlabs.com/resources/why-42-percent-enterprise-ai-abandoned-2025 (Fluidlabs, 2025)
- https://astrafy.io/the-hub/blog/technical/scaling-ai-from-pilot-purgatory-why-only-33-reach-production-and-how-to-beat-the-odds (Astrafy, 날짜 미상)
- https://www.softwareseni.com/the-enterprise-ai-pilot-purgatory-problem-what-the-statistics-actually-tell-us/ (SoftwareSeni, 날짜 미상)
- https://www.blueprintsys.com/blog/7-reasons-why-citizen-developer-never-materialized (Blueprint Systems, 날짜 미상)
- https://www.itworld.co.kr/article/3962268/%EB%85%B8%EC%BD%94%EB%93%9C-%EB%A1%9C%EC%9A%B0%EC%BD%94%EB%93%9C-%EB%8F%84%EA%B5%AC%EA%B0%80-%EC%8B%A4%ED%8C%A8%ED%95%98%EB%8A%94-7%EA%B0%80%EC%A7%80-%EC%9D%B4%EC%9C%A0.html (ITWorld Korea, 날짜 미상)
- https://quandarycg.com/citizen-development-shadow-it/ (Quandary CG, 날짜 미상)
- https://www.cio.com/article/3854098/ai-%ED%8C%8C%EC%9D%BC%EB%9F%BF-88%EA%B0%80-%EC%8B%A4%EC%9A%A9%ED%99%94%EC%97%90-%EC%8B%A4%ED%8C%A8%C2%B7%C2%B7%C2%B7-%EC%9D%B4%EB%A9%B4%EC%9D%98-%EC%97%AD%ED%95%99%EC%9D%80.html (CIO Korea, 날짜 미상)
- https://www.forbes.com/sites/joemckendrick/2026/01/26/why-ais-10-20-70-principle-should-matter-to-ceos-and-everyone-else/ (Forbes / BCG, 2026-01-26)
- https://leaddev.com/technical-direction/how-ai-generated-code-accelerates-technical-debt (LeadDev, 날짜 미상)
- https://devops.com/ai-in-software-development-productivity-at-the-cost-of-code-quality-2/ (DevOps.com / Google DORA 2024, 2025)
- https://www.domo.com/blog/enterprise-ai-hackathons-workflows ⚠(dead link) (Domo, 날짜 미상)
- https://medium.com/@swsthik.nair/hackathon-trap-hackathon-hype-vs-production-reality-what-all-student-devs-should-know-a86098b14c5e ⚠(dead link) (Medium, 날짜 미상)
- https://pluto.security/blog/citizen-development-security-teams/ (Pluto Security, 날짜 미상)
