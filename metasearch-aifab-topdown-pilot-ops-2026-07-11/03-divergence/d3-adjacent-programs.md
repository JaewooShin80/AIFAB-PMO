# [인접 도메인 — GSoC·사내벤처·부트캠프 캡스톤 운영 구조] 발산 리서치

> 담당 축: 선발→단기 집중 개발→데모·이관 구조를 가진 인접 도메인 프로그램 운영 설계
> 조사 기준일: 2026-07-11

---

## 핵심 발견

1. **GSoC는 3주 단위 중간 게이트를 운영하지 않으며, 12주 코딩 기간 중 6주 시점 단 1회의 중간 평가(Midterm Evaluation)만 존재한다.** 중간 평가 통과 기준은 "40~50% 완료"이며, 한계 수준으로 평가받은 참가자의 80% 이상이 최종 실패한다. — **씨앗과의 관계: 상충** (씨앗은 3주 파일럿에 매주 Gate를 설정했으나, GSoC는 12주에 게이트 1회) ([GSoC Evaluations Guide](https://google.github.io/gsocguides/mentor/evaluations), 2025)

2. **GSoC 멘토 대 참가자 비율은 약 1.64:1로, 멘토가 참가자보다 많다.** 2025년 기준 2,100명 이상의 멘토가 1,280명의 참가자를 지원했으며, 멘토의 2/3는 4년 이상 경력을 보유한다. — **씨앗과의 관계: 신규** ([GSoC 2025 Statistics](https://opensource.googleblog.com/2025/08/google-summer-of-code-2025-contributor-statistics.html), 2025-08)

3. **GSoC는 코딩 시작 전 3~4주간 '커뮤니티 본딩 기간(Community Bonding Period)'을 의무화한다.** 이 기간 참가자는 코드를 작성하지 않고 조직·멘토와 라포를 형성하고 계획을 수립한다. 씨앗의 "W1 킥오프"는 이 구조와 유사하나, GSoC는 본딩 기간을 독립 단계로 분리한다. — **씨앗과의 관계: 보강** ([GSoC Timeline 2026](https://developers.google.com/open-source/gsoc/timeline), 2026)

4. **삼성 C-Lab Inside는 1년 과제 기간 후 3개월 스핀오프 준비 지원으로 구성된 2단계 종료 구조를 사용한다.** 1년 내 경영진 평가에서 사업성을 인정받은 과제에 한해 법무·세무·투자 실무 교육 및 법인 설립 지원이 3개월 제공된다. 2015년 도입 이후 2025년 2월까지 총 959개 과제 육성. — **씨앗과의 관계: 신규** ([Samsung Sustainability](https://www.samsung.com/sec/sustainability/popup/popup_doc/AYUBw0_6ArQAIx8i/), 2025)

5. **LG전자 스튜디오341은 외부 액셀러레이터(블루포인트파트너스)와 협업해 기존 1년 이상 소요되던 선발 기간을 약 6개월로 절반 단축했다.** 110개 아이디어 → 1차 심사 13팀 → 2차 심사 6팀의 2단계 깔때기 선발 구조를 사용한다. — **씨앗과의 관계: 신규** ([LG전자 뉴스룸](https://live.lge.co.kr/venture/), 2024)

6. **SK하이닉스 HiGarage(하이개라지) 사내벤처는 2년 육성 기간 동안 "창업" 또는 "사내 사업화" 중 선택하는 이중 출구(Dual-Exit) 구조를 채택한다.** 연간 ~240건 아이디어 접수 후 6팀 선발, 총 12억 원 지원 (팀당 약 2억 원). — **씨앗과의 관계: 신규** ([디일렉](https://www.thelec.kr/news/articleView.html?idxno=614 ⚠(dead link)), 2024)

7. **Meta 엔지니어링 부트캠프는 6주간 L1~L5의 5단계 과제 복잡도 사다리를 사용하며, 부트캠프 종료 후 "팀 매칭 이벤트"로 팀을 선택한다.** 멘토 1명당 멘티 2~3명의 비율이며, 팀 이동 권한은 참가자에게 있다. — **씨앗과의 관계: 신규** ([AutomationHacks Newsletter](https://newsletter.automationhacks.io/p/engineering-practices-meta-3-conduct), 2024)

8. **네이버 부스트캠프는 베이직(2주) → 챌린지(4주) → 멤버십(약 24주)의 3단계 깔때기 구조로, 각 단계 진입은 절대 기준 평가를 통해 결정되며 정해진 합격 인원 상한이 없다.** 전체 과정 80% 이상 출석 시 수료증 발급, 수료 후 이력서 특강·모의면접·현업자 멘토링을 제공한다. — **씨앗과의 관계: 신규** ([부스트캠프 공식 안내](https://boostcamp.connect.or.kr/guide_wm.html), 2025)

9. **카카오 신입 개발자 온보딩은 Pre-온보딩 → 공통 온보딩 → 기술 온보딩의 3단계, 총 약 2개월 구조이며, 버디(선배 개발자)와의 개인 과제 수행이 핵심 메커니즘이다.** 발표 과제와 부서 기술 스터디를 통해 지식 공유를 구조화한다. — **씨앗과의 관계: 보강** ([카카오 테크](https://tech.kakao.com/posts/379), 2020)

10. **기업 내부 해커톤은 72시간~5일 형식이 일반적이며, 배포 가능한 성과를 위해서는 '30일 이상의 사후 인큐베이션 단계'가 필수적이라는 실무 가이드라인이 존재한다.** "해커톤의 가장 중요한 예산 항목은 사후 리소스"라는 점이 강조된다. — **씨앗과의 관계: 상충** (씨앗은 3주 스프린트 안에 배포까지 완성하는 구조를 가정하나, 해커톤 실무에서는 배포 전 30일+ 인큐베이션을 권고) ([AngelHack AI Internal Hackathon Playbook](https://angelhack.com/blog/ai-internal-hackathon/), 2024)

---

## 정량 데이터

| 항목 | 수치 | 출처 | 시점 |
|---|---|---|---|
| GSoC 2025 멘토 수 | 2,100명+ | GSoC 2025 Statistics | 2025-08 |
| GSoC 2025 참가자 수 | 1,280명 | GSoC 2025 Statistics | 2025-08 |
| GSoC 멘토:참가자 비율 | 약 1.64:1 | GSoC 2025 Statistics | 2025-08 |
| GSoC 중간 평가 통과 기준 | 프로젝트 40~50% 완료 (6주 시점) | GSoC Evaluations Guide | 2025 |
| GSoC 한계 평가 → 최종 실패 확률 | 80%+ | GSoC Evaluations Guide | 2025 |
| GSoC 커뮤니티 본딩 기간 | 3주 (코딩 전) | GSoC Timeline 2026 | 2026 |
| GSoC 코딩 기간 (표준) | 12주 | GSoC Timeline 2026 | 2026 |
| 삼성 C-Lab 누적 육성 과제 수 | 959개 (사내 423, 사외 536) | Samsung Sustainability | 2025-02 |
| 삼성 C-Lab Inside 기간 | 1년 + 스핀오프 준비 3개월 | Samsung Newsroom | 2025 |
| LG 스튜디오341 선발 깔때기 | 110팀 → 13팀 → 6팀 (입과율 약 5.5%) | LG전자 뉴스룸 | 2024 |
| LG 스튜디오341 육성 기간 | 약 6개월 | LG전자 뉴스룸 | 2024 |
| SK하이닉스 HiGarage 연간 지원 | 12억 원 (6팀, 팀당 약 2억 원) | 디일렉 | 2024 |
| SK하이닉스 HiGarage 아이디어 접수 | ~240건/년 | 디일렉 | 2024 |
| SK하이닉스 HiGarage 육성 기간 | 2년 | 디일렉 | 2024 |
| Meta 엔지니어링 부트캠프 기간 | 6주 | AutomationHacks Newsletter | 2024 |
| Meta 멘토:멘티 비율 | 1:2~3 | AutomationHacks Newsletter | 2024 |
| 네이버 부스트캠프 베이직 기간 | 2주 | 부스트캠프 공식 안내 | 2025 |
| 네이버 부스트캠프 챌린지 기간 | 4주 | 부스트캠프 공식 안내 | 2025 |
| 네이버 부스트캠프 멤버십 기간 | 약 24주 | 부스트캠프 공식 안내 | 2025 |
| 네이버 부스트캠프 수료 기준 | 전체 기간의 80% 이상 출석 | 부스트캠프 공식 안내 | 2025 |
| 카카오 신입 개발자 온보딩 기간 | 약 2개월 | 카카오 테크 | 2020 |
| 해커톤 사후 인큐베이션 권고 기간 | 30일+ | AngelHack Playbook | 2024 |
| Amazon Prime Video AI 스프린트 | 10일, 개발자 6명, 556 커밋 | AWS Korea Blog | 2025 |
| Amazon AI 스프린트 성과 | 90주 예상 → 24주로 단축 | AWS Korea Blog | 2025 |

---

## 씨앗 보고서와의 관계 요약

- **보강**: GSoC의 커뮤니티 본딩(3주)은 씨앗의 W1 킥오프 주간이 단순 오리엔테이션을 넘어 라포 형성과 계획 수립에 충분한 시간을 배정해야 한다는 점을 뒷받침한다. 카카오 온보딩의 3단계(Pre→공통→기술) 구조도 씨앗의 선발→온보딩→스프린트 분리 설계와 방향이 일치한다.

- **상충**: (1) 씨앗은 3주 파일럿 내 매주 Gate를 설정했으나, GSoC는 12주 기간 중 단 1회 중간 평가를 운영하며, 해커톤 실무 가이드라인은 배포 수준의 성과를 위해 30일+ 사후 인큐베이션을 별도로 권고한다. 이는 "3주 스프린트 안에 배포까지"라는 씨앗의 전제가 타 도메인에서 검증된 사례가 희박함을 시사한다. (2) GSoC에서 중간 평가를 "한계 통과"한 참가자의 80% 이상이 최종 실패한다는 점은, 중간 Gate에서의 조기 경보 시스템(early warning)이 단순 통과/실패 판정보다 정교해야 함을 시사한다.

- **신규**: (1) 멘토:참가자 비율 1.64:1(GSoC), 1:2~3(Meta)으로 상이한 설계 모델이 존재한다. 씨앗은 이 비율을 명시하지 않았으나, 집중 단기 파일럿에서는 멘토 밀도가 높아야 한다는 근거가 마련된다. (2) 사내벤처 프로그램(삼성 C-Lab, LG 스튜디오341, SK HiGarage)의 "이중 출구(스핀오프/사내 사업화)"와 "게이트 통과 실패 시 현업 복귀"라는 이관 처리 구조는 씨앗에 없는 종료 설계 옵션으로 AI FAB 파일럿 종료 시 "이관/폐기/현업복귀" 3방향 출구 설계에 직접 이식 가능하다. (3) 네이버 부스트캠프의 "절대 기준 평가(합격 인원 상한 없음)" 모델은 씨앗의 고정 인원(20~30명) 파일럿 그룹 가정과 다른 접근법을 제시한다.

---

## 한계

- **GSoC 멘토 선발 기준**: 멘토 자격 요건(기술 수준, 경력 연차 등)의 구체적 기준이 공식 문서에 명시되어 있지 않아 AI FAB 코치/멘토 선발 기준 설계에 직접 적용하기 어렵다.
- **사내벤처 중간 평가 세부 구조**: 삼성 C-Lab, LG 스튜디오341 모두 1년 과제 기간 중 분기별·월별 중간 체크포인트 구조가 외부 공개 자료에 상세히 기술되어 있지 않다.
- **3주 단기 스프린트 + 실배포 선행 사례**: 씨앗의 한계와 동일하게, 비전문 개발자(시티즌 개발자)가 3주 만에 운영환경 배포까지 완성한 직접 사례는 이번 조사에서도 확인되지 않았다. Amazon Prime Video 사례(10일, 전문 개발자 6명)가 가장 인접하지만 대상이 시니어 엔지니어다.
- **한국 대기업 사내 AI 파일럿 3주 프로그램**: 공개된 구체적 운영 구조 데이터 부재. SK플래닛 GitHub Copilot 실험(30명, 4개월)은 배포 단계까지의 Gate 구조가 공개되지 않았다.

---

## 출처

- https://google.github.io/gsocguides/mentor/evaluations (GSoC Evaluations Guide, 2025)
- https://developers.google.com/open-source/gsoc/timeline (GSoC Timeline 2026, 2026)
- https://opensource.googleblog.com/2025/08/google-summer-of-code-2025-contributor-statistics.html (GSoC 2025 Contributor Statistics, 2025-08)
- https://google.github.io/gsocguides/mentor/selecting-students-and-mentors (GSoC Selecting Contributors and Mentors, 2025)
- https://www.samsung.com/sec/sustainability/popup/popup_doc/AYUBw0_6ArQAIx8i/ (Samsung C-Lab Sustainability, 2025)
- https://news.samsung.com/kr/%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90-c%EB%9E%A9-%EA%B3%BC%EC%A0%9C-4%EA%B0%9C-%EC%8A%A4%ED%83%80%ED%8A%B8%EC%97%85-%EC%B0%BD%EC%97%85-%EC%A7%80%EC%9B%90 ⚠(dead link) (Samsung Newsroom C-Lab 스핀오프, 2025)
- https://live.lge.co.kr/venture/ (LG전자 뉴스룸 사내벤처, 2024)
- https://live.lge.co.kr/2409-lg-studio341/ (LG전자 스튜디오341 탐방기, 2024-09)
- https://www.thelec.kr/news/articleView.html?idxno=614 ⚠(dead link) (디일렉 SK하이닉스 HiGarage, 2024)
- https://newsletter.automationhacks.io/p/engineering-practices-meta-3-conduct (AutomationHacks: Meta Engineering Bootcamp, 2024)
- https://boostcamp.connect.or.kr/guide_wm.html (네이버 부스트캠프 웹·모바일 공식 안내, 2025)
- https://tech.kakao.com/posts/379 (카카오 테크: 신입 개발자 온보딩, 2020)
- https://angelhack.com/blog/ai-internal-hackathon/ (AngelHack: AI Internal Hackathon Playbook, 2024)
- https://aws.amazon.com/ko/blogs/korea/how-frontier-teams-are-reinventing-ai-native-development/ (AWS Korea Blog: AI-Native Development, 2025)
- https://ideawake.com/hackathon-the-2026-enterprise-guide-to-high-impact-innovation/ ⚠(dead link) (IdeaWake: Enterprise Hackathon Guide, 2026)
