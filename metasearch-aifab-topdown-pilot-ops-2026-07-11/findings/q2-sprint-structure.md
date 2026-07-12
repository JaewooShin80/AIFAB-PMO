# 3주 단기 스프린트로 배포까지 완성하는 프로그램의 주차별 운영 구조

## 핵심 발견

- **3주 스프린트의 가장 검증된 패턴은 "1주 계획·정제 + 2주 순수 개발"** 구조다. 1주차에 모든 회의·스토리 정제·기술 탐색을 집중하고, 2-3주차는 맥락 전환(context switching) 없이 개발에만 몰두한다. ([John Wakeling Blog](https://www.johnwakeling.co.uk/posts/3-week-sprints/), 날짜 미상)

- **Agile-Stage-Gate 하이브리드 모델**은 스프린트 종료 시점에 게이트(Go/Kill/Hold/Recycle)를 배치하여 애자일 개발 속도와 기업 거버넌스 요구를 동시에 충족한다. 의사결정 및 근거 발행 목표는 "24~48시간 이내"로 설정한다. ([Umbrex Stage-Gate Innovation Process](https://umbrex.com/resources/frameworks/strategy-frameworks/stage-gate-innovation-process/), 날짜 미상)

- **Agile-Stage-Gate에서 스프린트 길이는 1~4주**가 표준이며, 각 스프린트 종료 시 경영진이 검토할 수 있는 데모 가능한 산출물(working product)을 제출한다. 게이트는 고객 성과, 기능 증분, 지표 등 스프린트 증거를 평가한다. ([Profit.co Stage-Gate vs Agile](https://www.profit.co/blog/stage-gate-process/stage-gate-vs-agile-methodology-comparison-and-hybrid-models/), 날짜 미상)

- **해커톤·부트캠프 멀티위크 프로그램의 공통 체크포인트 3종**: 킥오프 콜(Kickoff call) → 중간 AMA(Mid-event check-in) → 최종 데모 세션(Final demo session). 중간 체크포인트는 팀이 방향을 피벗할 수 있는 공식 기회를 제공한다. ([Hackathon Guide](https://hackathon.guide/), 날짜 미상)

- **해커톤 이후 프로덕션 전환에 대한 사전 계획 필수**: 데모데이와 수상만으로 끝나면 "아이디어가 공유 드라이브에서 죽는다." 수상작의 다음 단계 경로(파일럿, 액셀러레이터 편입)를 해커톤 시작 전에 미리 합의해 두어야 한다. ([Klipfolio Hackathon Guide](https://www.klipfolio.com/blog/run-hackathon), 날짜 미상)

- **Google GV Design Sprint(5일) → 구현 스프린트(2~3주) 연계 구조**: 디자인 스프린트는 Day1 이해·Day2 스케치·Day3 결정·Day4 프로토타입·Day5 사용자 테스트로 구성되며, 스프린트 종료 후 "무엇을 다음에 할지"가 확정된다. 구현 스프린트는 별도 2~4주 추가 운영이 일반적이다. ([GV Sprint](https://www.gv.com/sprint/), 날짜 미상; [Google Design](https://design.google/library/design-sprints), 날짜 미상)

- **Design Sprint 3.0**은 스프린트 주 전에 "Problem Framing" 단계를 필수화하여 비즈니스 목표·이해관계자와 연결하고, 스프린트를 4일로 단축했다. 기업(enterprise) 팀 수백 개에서 검증된 진화 버전이다. ([Design Sprint 3.0 Academy](https://www.designsprint.academy/blog/design-sprint-3-0), 날짜 미상)

- **스프린트 플래닝 시간 기준**: 스크럼 가이드 표준은 "스프린트 1주당 플래닝 2시간". 3주 스프린트라면 킥오프 플래닝에 최대 6시간을 배정한다. ([Atlassian Scrum Sprints](https://www.atlassian.com/ko/agile/scrum/sprints), 날짜 미상)

- **국내 사례 - 부산 DX 스프린트 해커톤**: 2주 집중 운영으로 사전심사 선발 → 팀빌딩 → 개발 → 동작 시연·발표 심사까지 진행, 실제 서비스 출시를 목표로 함. ([파이낸셜뉴스](https://www.fnnews.com/news/202307171837050284), 2023-07-17)

- **AI App Bootcamp(12일 구조)** 사례: Day1-2 아이디어·설정, Day3-6 핵심 기능 개발, Day7-8 UI 디자인, Day9-10 배포·최종 조정, Day11-12 커스텀 통합. 주 단위 오피스 아워, 그룹 체크포인트, "MVP 로스트(Roast My MVP)" 피드백 세션을 구조화. ([AI Build Accelerator](https://build.starterstory.com/build/ai-build-accelerator), 날짜 미상)

## 정량 데이터

| 항목 | 수치 | 출처 | 시점 |
|---|---|---|---|
| 3주 스프린트 플래닝 권장 시간 | 6시간 (주당 2시간 × 3주) | [Atlassian Scrum Sprints](https://www.atlassian.com/ko/agile/scrum/sprints) | 날짜 미상 |
| Agile-Stage-Gate 게이트 결정 목표 시간 | 24~48시간 이내 | [Umbrex Stage-Gate](https://umbrex.com/resources/frameworks/strategy-frameworks/stage-gate-innovation-process/) | 날짜 미상 |
| Agile-Stage-Gate 스프린트 표준 기간 | 1~4주 | [Profit.co](https://www.profit.co/blog/stage-gate-process/stage-gate-vs-agile-methodology-comparison-and-hybrid-models/) | 날짜 미상 |
| SKT AI 액셀러레이터 2기 전체 기간 | 6개월, 참가 15팀(15:1 경쟁) | [더구루](https://www.theguru.co.kr/news/article.html?no=83646) | 날짜 미상 |
| 데모데이 팀당 발표 시간 | 5~10분 (내부 해커톤 기준) | [Klipfolio](https://www.klipfolio.com/blog/run-hackathon) | 날짜 미상 |
| 1337 Ventures Corporate Innovation Sprint 빈도 | 주 2회 세션, 총 4주 | [1337.ventures](https://1337.ventures/corporate-innovation-sprint/) | 날짜 미상 |
| 국내 DX 스프린트 해커톤 기간 | 2주(개발~출시까지) | [파이낸셜뉴스](https://www.fnnews.com/news/202307171837050284) | 2023-07-17 |
| MLH Fellowship 전체 기간 | 12주, 팟당 약 10명 | [MLH Fellowship](https://fellowship.mlh.com/) | 날짜 미상 |

## W1/W2/W3 구조 설계 종합 참고 프레임워크

조사 결과를 종합하면, 3주 스프린트 W1/W2/W3 구조는 다음 세 가지 패턴으로 수렴된다:

### 패턴 A: 계획-개발-검증 분리형 (Scrum 기반)
- **W1 (킥오프 + 계획)**: 스프린트 플래닝(~6h), 백로그 정제, 기술 탐색, 목표 정의
- **W2 (개발 집중)**: 맥락 전환 없는 순수 개발, 일일 스탠드업, 기능 증분 완성
- **W3 (완성 + 게이트)**: 통합 테스트, 스프린트 데모, 이해관계자 게이트 리뷰(Go/Kill), 배포, 회고

### 패턴 B: 디자인 스프린트 + 구현 스프린트 연계형 (GV 기반)
- **W1 (디자인 스프린트)**: 5일 집중 — 이해→스케치→결정→프로토타입→사용자 테스트
- **W2 (구현 스프린트 1)**: MVP 개발, 핵심 기능 구현, 중간 체크포인트
- **W3 (구현 스프린트 2 + 배포)**: 완성·UI 개선, 배포 승인 게이트, 데모데이, 회고

### 패턴 C: Agile-Stage-Gate 하이브리드형 (기업 거버넌스 필요 시)
- **W1 (Gate 0 → 스프린트 1)**: 킥오프, 요구사항 확정, Gate 0(착수 승인), 1차 스프린트 실행
- **W2 (스프린트 2 + 중간 게이트)**: 기능 증분 데모, Gate 1(중간 리뷰), 피벗 여부 결정
- **W3 (스프린트 3 + Gate 2 + 배포)**: 최종 완성, Gate 2(배포 승인), 프로덕션 배포, 데모데이, 이관 계획

## 한계

- 3주 스프린트로 실제 프로덕션 배포까지 완성한 사내 시티즌 개발자 프로그램의 주차별 공개 사례(국내 대기업 포함)를 1차 출처로 확보하지 못함
- W1/W2/W3 레이블을 명시적으로 사용하는 공개 프로그램 매뉴얼 미확보
- 해커톤→프로덕션 전환의 "배포 승인 게이트" 기준(체크리스트·KPI)에 대한 정량 데이터 미확보
- AI 코딩 도구(Claude Code 등) 활용 시 3주 스프린트 효율 차이에 대한 실증 데이터 미확보
- 국내 SKT·KT·삼성·LG 등 대기업의 사내 시티즌 개발자 단기 스프린트 운영 사례는 비공개로 추정됨

## 출처

- https://www.johnwakeling.co.uk/posts/3-week-sprints/ (John Wakeling Blog, 날짜 미상)
- https://umbrex.com/resources/frameworks/strategy-frameworks/stage-gate-innovation-process/ (Umbrex Stage-Gate Innovation Process, 날짜 미상)
- https://www.profit.co/blog/stage-gate-process/stage-gate-vs-agile-methodology-comparison-and-hybrid-models/ (Profit.co Stage-Gate vs Agile, 날짜 미상)
- https://hackathon.guide/ (Hackathon Guide, 날짜 미상)
- https://www.klipfolio.com/blog/run-hackathon (Klipfolio Corporate Hackathon Guide, 날짜 미상)
- https://www.gv.com/sprint/ (GV Design Sprint, 날짜 미상)
- https://design.google/library/design-sprints (Google Design Sprints, 날짜 미상)
- https://www.designsprint.academy/blog/design-sprint-3-0 (Design Sprint 3.0 Academy, 날짜 미상)
- https://www.atlassian.com/ko/agile/scrum/sprints (Atlassian Scrum Sprints KR, 날짜 미상)
- https://www.fnnews.com/news/202307171837050284 (파이낸셜뉴스 DX 스프린트 해커톤, 2023-07-17)
- https://build.starterstory.com/build/ai-build-accelerator (AI Build Accelerator, 날짜 미상)
- https://1337.ventures/corporate-innovation-sprint/ (1337 Ventures Corporate Innovation Sprint, 날짜 미상)
- https://www.theguru.co.kr/news/article.html?no=83646 (더구루 SKT AI 액셀러레이터, 날짜 미상)
- https://fellowship.mlh.com/ (MLH Fellowship, 날짜 미상)
- https://theinnovationmode.com/the-innovation-blog/how-to-run-a-successful-corporate-hackathon (Innovation Mode Corporate Hackathon Guide, 날짜 미상)
