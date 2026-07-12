# 결론 보고서 — AI FAB 탑다운 과제 파일럿 운영 방안: 시티즌 개발자 선발부터 3주 스프린트 배포·종료까지 운영 시나리오

> 생성: 2026-07-11 | 메타서치 단계 5 산출물 | 입력: 04-convergence.md

---

## 1. Executive Summary

3주 타임박스 안에 시티즌 개발자가 운영 배포를 완성하려면 **킥오프 4~6주 전에 골든 패스(AWS 6대 템플릿)가 완비**되어 있어야 한다는 것이 수렴 연구의 핵심 결론이다. 이 전제가 없으면 GenAI 파일럿 실패율 88~95%(MIT NANDA)·기업 AI 이니셔티브 포기율 42%(S&P Global)가 그대로 재현된다. 골든 패스가 갖춰지면 온보딩 시간 30~60% 단축, 첫 배포 1시간 미만이 실현 가능하다(Tasrie IT 2026, Spotify Backstage).

파일럿 운영 구조는 **Agile-Stage-Gate 하이브리드(W1 Gate 0 → W2 중간 Gate → W3 Gate 2+배포)** 가 기업 거버넌스와 스프린트 속도를 동시에 충족하는 현재 근거상 가장 방어 가능한 구조로 판정되었으며(비교 대안별 성과 데이터 부재로 '최적' 단정 보류), 배포 게이트는 3-lane 위험 분류(Green/Yellow/Red)와 rubber-stamping 방지 장치를 반드시 포함해야 한다(metacto 2026-07-08; arXiv 2606.22721).

CoE 선행 구축(2~5명)이 파일럿 성공률에 핵심 영향을 미치며, 거버넌스 있는 조직의 **비용 절감 성공률**이 77% vs 없는 조직 39%로 2배다(KPMG Belgium 2024; 이 수치는 거버넌스 유무 조직 간 비용 절감 성공률 차이를 가리키며, 파일럿 전체 성공률로 일반화하지 않는다). 에이전틱 도구 10주 지속 사용률이 10% 미만(DORA 2025)이므로 챔피언 프로그램 없이는 지속 사용 리스크가 커 구조적 개입이 필요하다.

**추가 리스크**: 내부 기획안(AWS_기반_탑다운_AIFAB_과제_운영환경_구축운영_기획안_v1-0.md §2)은 탑다운 과제 수행 주체를 '지정된 개발·운영 조직'으로 전제하며 시티즌 개발자 파일럿을 직접 다루지 않는다. 시티즌 개발자가 탑다운 과제를 수행하는 파일럿은 기획안의 전제와 구조적으로 불일치하므로, 파일럿 착수 전 기획안 개정 또는 파일럿 예외 규정 합의가 필요하다.

종료·이관은 소유권 단일 책임자 사전 지정 + 3방향 출구(이관/폐기/현업복귀) + 자동 Frozen·보드 최종 결정 하이브리드로 설계하고, 파일럿 착수 전 KPI·Go/No-Go 스코어카드를 동결하는 것이 필수다. Go/No-Go 임계값 0.605는 Visual Paradigm의 범용 예시값이며, AI FAB의 보안·기술부채·이관 비용을 반영한 자체 가중치·임계값 산식을 파일럿 착수 전 수립해야 한다.

**핵심 리스크**: 파일럿 종료 후 이관팀이 AI 생성 코드의 기술 부채(기술 부채 30~41% 증가, 코드 중복 8배, GitClear·Pixelmojo)를 수용하는 기준이 내부·외부 모두 미정의이며, 이관 거부 시 Pilot Purgatory(SoftwareSeni)가 재현될 가능성이 높다.

---

## 2. 우선순위 매트릭스

### 2A. 2축 좌표 요약

| 권고 번호 | 제목 | 실행용이성 | 영향도 | 분류 |
|---|---|---|---|---|
| R1 | 골든 패스 사전 완비 (킥오프 4~6주 전) | 하 | 상 | 전략 과제 |
| R2 | 킥오프 전 KPI·Go/No-Go 스코어카드 동결 | 상 | 상 | Quick Win |
| R3 | Agile-Stage-Gate 하이브리드 운영 구조 채택 | 상 | 상 | Quick Win |
| R4 | 3-lane 위험 분류 기반 배포 게이트 설계 | 하 | 상 | 전략 과제 |
| R5 | CoE 선행 구축 + 초기 고밀도 멘토링 (co-dev 50%) | 하 | 상 | 전략 과제 |
| R6 | 챔피언 프로그램 + 3단계 체크인 구조 도입 | 상 | 중 | 선택 과제 |
| R7 | 자동 Frozen + 보드 심의 하이브리드 종료 설계 | 상 | 중 | 선택 과제 |
| R8 | 보안 통제 기술 내재화 (SAST·골든 패스 임베딩) | 중 | 상 | 전략 과제 |
| R9 | 킥오프 전 선발 절차 확정 (부서·팀·과제 2단계 검토) | 상 | 상 | Quick Win |

### 2B. 우선순위 매트릭스 표

| 영향도 \ 실행용이성 | 상 | 중 | 하 |
|---|---|---|---|
| **상** | R2 KPI 동결, R3 Agile-Stage-Gate, R9 선발 절차 확정 | R8 보안 내재화 | R1 골든 패스, R4 게이트 설계, R5 CoE |
| **중** | R6 챔피언 프로그램, R7 종료 하이브리드 | — | — |
| **하** | — | — | — |

### 2C. 분류별 목록

| 분류 | 권고 | 요약 |
|---|---|---|
| Quick Win | R2 KPI·Go/No-Go 스코어카드 동결 | 킥오프 전 측정 기준 합의—비용 없음, 효과 즉시 |
| Quick Win | R3 Agile-Stage-Gate 하이브리드 운영 구조 | W1/W2/W3 게이트 구조 문서화—추가 리소스 불필요 |
| 전략 과제 | R1 골든 패스 사전 완비 | 파일럿 전 4~6주 AWS 6대 템플릿 준비—기간·공수 필요 |
| 전략 과제 | R4 3-lane 배포 게이트 설계 | Red lane 3인 승인 + rubber-stamping 방지 체계 구축 |
| 전략 과제 | R5 CoE 선행 구축 + 고밀도 멘토링 | 2~5명 CoE 사전 편성, 초기 co-development 50% 비율 |
| 전략 과제 | R8 보안 통제 기술 내재화 | SAST·골든 패스 내장으로 COE 전수 리뷰 부담 제거 |
| 선택 과제 | R6 챔피언 프로그램 + 3단계 체크인 | 25~50명당 챔피언 1명, 주 30분 오피스아워 |
| 선택 과제 | R7 자동 Frozen + 보드 심의 하이브리드 | 비용 임계값 자동 차단, 최종 폐쇄는 보드 결정 |
| Quick Win | R9 킥오프 전 선발 절차 확정 | 파일럿 부서 2~3개(챔피언 보유·백로그 명확), 팀당 3~5명 혼합팀, CoE 주관 2단계 과제 검토 |

---

## 3. 권고별 상세

### 3.1 R1 골든 패스 사전 완비 (킥오프 4~6주 전) — 전략 과제

| 기준 | 등급 | 근거 |
|---|---|---|
| 실행 가능성 | 중 | IDP MVP 정석 16주(8+8) vs 3주 파일럿의 시간 긴장 존재. 파일럿 이전 별도 준비 기간 확보 필요 (https://platformengineering.org/blog/how-to-set-up-an-internal-developer-platform) |
| 영향 | 상 | 골든 패스 미비 시 AI 생성 코드 변경 실패율 +30%·PR당 인시던트 +23.5%(Cortex 2025). IDP 성숙 조직 온보딩 30~60% 단축·첫 배포 1시간 미만 (https://tasrieit.com/blog/golden-paths-platform-engineering-guide-2026, https://backstage.spotify.com/discover/blog/how-we-measure-backstage-success-at-spotify) |
| 비용 | 상 | AI 인프라팀 4~6주 선행 투입 필요. AWS 6대 템플릿 구축 공수 존재 (https://www.thecloudplaybook.com/p/first-6-golden-paths-aws-platform-teams) |
| 리스크 | 중 | 골든 패스 문헌이 전문 개발자 대상이며 시티즌 개발자 특화 검증 미완 (내부: 탑다운 기획안 §5, 내부 자료 독립 검증 불가) |
| 시급성 | 상 | 킥오프 전에 반드시 완비되어야 하므로 파일럿 일정 역산 시 즉시 착수 필요. DORA 2025 "플랫폼 없이 AI 단독 도입=안정성 저하" (https://platformengineering.com/features/dora-2025-ai-wont-save-you-without-a-solid-platform/) |

- **2축 환산**: 실행용이성 **하** (실행 가능성 중 기준; 비용 상 → 한 단계 하향 → 하), 영향도 **상** (영향 상 기준; 시급성 상 → 상한이 '상'이므로 유지) → **전략 과제** (실행용이성 하 × 영향도 상)
- **첫 실행 단계**: AI 인프라팀이 파일럿 킥오프 D-42일 이전에 ECS on Fargate·Lambda·RDS·비용태그·관측성·Secrets Manager 6대 템플릿 완비 여부를 체크리스트로 확인. 시티즌 개발자가 폼 입력만으로 CI/CD·IAM·모니터링 포함 레포를 자동 생성할 수 있는 상태를 킥오프 전 완성 게이트로 설정.

---

### 3.2 R2 킥오프 전 KPI·Go/No-Go 스코어카드 동결 — Quick Win

| 기준 | 등급 | 근거 |
|---|---|---|
| 실행 가능성 | 상 | 문서화 작업이므로 추가 인프라 불필요. Traction Technology: Go/No-Go 스코어카드 합의 및 결정 권한자 사전 지정이 모범 사례 (https://www.tractiontechnology.com/blog/how-to-run-a-successful-pilot-with-a-startup-frameworks-kpis-enterprise-best-practices) |
| 영향 | 상 | KPI 미사전 정의는 Pilot Purgatory의 핵심 원인 (https://www.softwareseni.com/the-enterprise-ai-pilot-purgatory-problem-what-the-statistics-actually-tell-us/). Anthropic 공식 6개 KPI(WAU 70%·주당 메시지 25+건·만족도 4.0/5.0+·시간 절감 3시간+) 기준 제공 (https://claude.com/resources/tutorials/claude-enterprise-administrator-guide) |
| 비용 | 하 | 문서 작성 및 합의 미팅 외 추가 비용 없음 (추정: 기존 회의 체계 내 처리 가능) |
| 리스크 | 하 | KPI 동결 자체의 리스크는 없음. 다만 내부 정치적 합의 실패 가능성은 별도 관리 필요 (추정: 조직 내 합의 난이도는 맥락 의존) |
| 시급성 | 상 | 킥오프 전에 완료해야 하며 이후 변경 시 파일럿 평가 무력화. Go/No-Go 스코어카드(기술 40%·재무 30%·시장 20%·자원 10%, 임계값 0.605) 사전 합의 (https://guides.visual-paradigm.com/making-informed-decisions-with-a-go-no-go-checklist-for-agile-projects-a-scoring-approach/) ※ 0.605는 Visual Paradigm의 범용 예시값이며, AI FAB의 보안·기술부채·이관 비용을 반영한 자체 가중치·임계값 산식을 파일럿 착수 전 수립해야 함 |

- **2축 환산**: 실행용이성 **상** (실행 가능성 상 기준; 비용 하·리스크 하 → 하향 없음), 영향도 **상** (영향 상 기준; 시급성 상 → 상한 '상' 유지)
- **첫 실행 단계**: 파일럿 착수 전 AI Board 킥오프 회의에서 ①배포 완성 건수 ②WAU 70% ③참여자 만족도 4.0/5.0+ ④사이클 타임 단축률 ⑤거버넌스 준수율 5개 KPI와 Go/No-Go 임계값(0.605는 Visual Paradigm 범용 예시값—자체 가중치·산식 사전 수립 필요)을 문서화하고 결정 권한자(named decision owner)를 지정.

---

### 3.3 R3 Agile-Stage-Gate 하이브리드 운영 구조 채택 — Quick Win

| 기준 | 등급 | 근거 |
|---|---|---|
| 실행 가능성 | 상 | 기존 내부 기획안 §5 배포 게이트·격상 절차와 직접 연계 가능. Agile-Stage-Gate 게이트 결정 24~48시간 이내 목표로 속도 저해 최소화 (https://umbrex.com/resources/frameworks/strategy-frameworks/stage-gate-innovation-process/) |
| 영향 | 상 | GSoC 중간 평가에서 "한계 통과" 참가자 80%+가 최종 실패 → 중간 Gate 없이는 조기 경보 불가 (https://google.github.io/gsocguides/mentor/evaluations). KPMG Belgium: 거버넌스 있는 조직의 **비용 절감 성공률** 77% vs 없는 조직 39%—이 수치는 비용 절감 성공률 차이이며 파일럿 전체 성공률로 일반화하지 않음 (https://kpmg.com/be/en/home/insights/2024/11/ta-transforming-business-value-creation-with-citizen-development.html) |
| 비용 | 하 | 기존 조직 구조(AI Board·CoE) 내 역할 정의 수준으로 처리 가능. 추가 시스템 불필요 (내부: 탑다운 기획안 §5, 내부 자료 독립 검증 불가) |
| 리스크 | 하 | 구조 채택 자체의 리스크는 낮음. 게이트 경직화로 Shadow AI 촉진 가능성은 R4에서 별도 관리 (https://www.elegantsoftwaresolutions.com/blog/vibe-coding-enterprise-adoption) |
| 시급성 | 상 | 킥오프 전 운영 구조 확정이 필수. 이후 변경 시 참가자 혼선 유발 |

- **2축 환산**: 실행용이성 **상** (실행 가능성 상; 비용 하·리스크 하 → 하향 없음), 영향도 **상** (영향 상; 시급성 상 → 상한 '상' 유지)
- **Quick Win 범위 한정**: R3의 Quick Win 분류는 "Agile-Stage-Gate 구조 문서화·사전 합의" 범위에 한정된다. 게이트 실운영(3-lane 리뷰 실제 가동)과 CoE 주관 리뷰 체계 가동은 R4(3-lane 게이트 설계)·R5(CoE 선행 구축)의 선행 이행에 의존하며, R4·R5가 완료되지 않으면 R3 구조 문서화만으로 게이트 실효성을 확보할 수 없다.
- **첫 실행 단계**: W1(Day 1~7): Gate 0 킥오프 체크리스트(골든 패스 완비·KPI 동결·소유권 지정) → W2(Day 8~14): 중간 Gate(조기 경보 3개 이상 과제 멘토 집중 배치) → W3(Day 15~21): Gate 2 배포 승인(3-lane 리뷰) → 배포 후 D+7 회고 구조를 운영 매뉴얼에 문서화.

---

### 3.4 R4 3-lane 위험 분류 기반 배포 게이트 설계 — 전략 과제

| 기준 | 등급 | 근거 |
|---|---|---|
| 실행 가능성 | 중 | 3-lane 분류 기준 정의 및 리뷰어 로테이션 체계 설계 필요. Semgrep AI-SAST 도입 시 부분 자동화 가능 (https://semgrep.dev/blog/2025/ai-powered-detection-with-semgrep/). metacto 2026-07-08 3-lane 프레임워크 참조 가능 (https://www.metacto.com/blogs/establishing-code-review-standards-for-ai-generated-code) |
| 영향 | 상 | AI 코드 취약점 밀도 2.74배(Veracode). XSS 방어 실패 85%·로그 인젝션 실패 87%(Veracode Spring 2026). rubber-stamping: 승인율 +14.5%p·코멘트 -22% 실증(arXiv 2606.22721) (https://arxiv.org/pdf/2606.22721, https://www.veracode.com/blog/spring-2026-genai-code-security/) |
| 비용 | 중 | 리뷰어 3인 체계(Red lane) 운영 공수 발생. SLA 차등화(피어 리뷰 4h, 아키텍처 리뷰 24h) 관리 필요 (https://gotranscript.com/en/blog/turnaround-time-vs-quality-set-slas-without-increasing-risk) |
| 리스크 | 상 | 복잡한 승인 프로세스가 Shadow AI 사용을 촉진할 수 있다는 역설 존재 (https://www.elegantsoftwaresolutions.com/blog/vibe-coding-enterprise-adoption). 3-lane × 3인 리뷰가 3주 타임박스 안에서 소화 가능한지 실증 데이터 없음 (04 §4 미해결 쟁점 4) |
| 시급성 | 상 | Gate 2(W3 배포 승인) 전에 체계가 완비되어야 하며, 보안 게이트 없이 배포 시 취약점 리스크 즉시 현실화 |

- **2축 환산**: 실행용이성 **하** (실행 가능성 중 기준; 리스크 상 → 한 단계 하향 → 하), 영향도 **상** (영향 상; 시급성 상 → 상한 '상' 유지) → **전략 과제** (실행용이성 하 × 영향도 상)
- **첫 실행 단계**: 킥오프 4주 전까지 Green(내부 UI·문서·테스트)/Yellow(비즈니스 로직·API)/Red(Auth·PII·인프라) 3-lane 분류 기준표 작성. Red lane 리뷰어 풀 최소 6명 확보(로테이션 고려). 서면 정당화 양식 및 rubber-stamping 모니터링 지표(승인 소요 시간·코멘트 수) 사전 정의.

---

### 3.5 R5 CoE 선행 구축 + 초기 고밀도 멘토링 (co-dev 50%) — 전략 과제

| 기준 | 등급 | 근거 |
|---|---|---|
| 실행 가능성 | 중 | CoE 2~5명 선발 및 역할 정의 필요. H&M 4명 CoE로 1,500개 앱 지원(Microsoft Power Platform Blog)이 가능성을 보여주나 파일럿 특화 초기 고밀도 설계 필요 (https://www.microsoft.com/en-us/power-platform/blog/power-apps/hmgroup/) |
| 영향 | 상 | KPMG Belgium: 거버넌스 있는 조직의 **비용 절감 성공률** 77% vs 없는 조직 39%—이 수치는 비용 절감 성공률 차이이며 파일럿 전체 성공률로 일반화하지 않음 (https://kpmg.com/be/en/home/insights/2024/11/ta-transforming-business-value-creation-with-citizen-development.html). BCG 10-20-70: AI 성공의 70%는 사람·프로세스·문화 (https://www.forbes.com/sites/joemckendrick/2026/01/26/why-ais-10-20-70-principle-should-matter-to-ceos-and-everyone-else/) |
| 비용 | 상 | CoE 인력 사전 배치 + 초기 50% co-development 비율은 상당한 멘토 투입 공수를 의미. GSoC 멘토:참가자 1.64:1(역방향), Meta 1:2~3 참조 (https://opensource.googleblog.com/2025/08/google-summer-of-code-2025-contributor-statistics.html) |
| 리스크 | 중 | "CoE 2~5인으로 모든 PR 심층 리뷰는 물리적으로 불가"(Checkmarx 2025). 보안 훈련만으로 시티즌 개발자 보안 문제를 해결하지 못함(TechNewsWorld) (https://checkmarx.com/blog/ai-is-writing-your-code-whos-keeping-it-secure/) |
| 시급성 | 상 | 킥오프 전 CoE 완편이 필수. 파일럿 중 구성하면 프레임워크 공백 발생 |

- **2축 환산**: 실행용이성 **하** (실행 가능성 중 기준; 비용 상 → 한 단계 하향 → 하), 영향도 **상** (영향 상; 시급성 상 → 상한 '상' 유지) → **전략 과제** (실행용이성 하 × 영향도 상)
- **첫 실행 단계**: 파일럿 킥오프 D-28일 이전에 CoE 2~5명(프로그램 프레임워크·과제 검토·챔피언 운영·비즈니스+기술 2단계 과제 검토 담당)을 확정. 초기 2주(W1·W2) co-development 비율을 50%로 설정하고 W3부터 단계적 감소 계획 수립.

---

### 3.6 R6 챔피언 프로그램 + 3단계 체크인 구조 도입 — 선택 과제

| 기준 | 등급 | 근거 |
|---|---|---|
| 실행 가능성 | 상 | Anthropic 공식 Champion Kit 활용 가능(챔피언 주 40분 예산·30일 4주 플레이북·3원칙 share/ask/circle). 추가 도구 없이 기존 커뮤니케이션 채널로 운영 가능 (https://code.claude.com/docs/en/champion-kit) |
| 영향 | 중 | 챔피언 2.1배 지속 사용률(Worklytics via AI Assembly Lines)·채택률 62→85%(Adoptify.ai)는 단일 출처이며 독립 검증 없어 신뢰도 중간 (https://aiassemblylines.com/post/ai-champions-program-enterprise-adoption). 에이전틱 도구 10주 지속 사용률 <10%(DORA 2025) — 챔피언 없이는 효과 소멸 (https://jellyfish.co/blog/2025-dora-report/) |
| 비용 | 중 | 챔피언 1인당 주 40분 예산. 25~50명당 1명 배치(Anthropic Cowork). 3단계 체크인(30~60일 오피스아워·3개월 회고·분기 비즈니스 리뷰) 운영 공수 (https://claude.com/resources/tutorials/scaling-workflows-with-claude-cowork-at-your-organization) |
| 리스크 | 하 | 챔피언 프로그램 자체의 리스크는 낮음. Worklytics·Adoptify.ai 수치 독립 검증 부재가 투자 판단 불확실성 유발 (04 §4 미해결 쟁점 5) |
| 시급성 | 중 | 파일럿 기간 내보다는 이후 지속 사용 정착이 목적. 파일럿 W3 종료 전 챔피언 지정 필요 |

- **2축 환산**: 실행용이성 **상** (실행 가능성 상; 비용 중·리스크 하 → 하향 없음), 영향도 **중** (영향 중; 시급성 중 → 상향 없음) → **선택 과제** (실행용이성 상 × 영향도 중)
- **첫 실행 단계**: W2 종료 전(Day 14)까지 파일럿 참가 그룹에서 챔피언 후보를 1명 이상 지정. Anthropic Champion Kit 플레이북(30일 4주)을 파일럿 종료 후 즉시 시작하도록 일정 수립.

---

### 3.7 R7 자동 Frozen + 보드 심의 하이브리드 종료 설계 — 선택 과제

| 기준 | 등급 | 근거 |
|---|---|---|
| 실행 가능성 | 상 | AWS Innovation Sandbox 자동 Frozen 기능 활용 가능(Entry→Frozen→CleanUp 상태머신). 내부 기획안 보드 심의 원칙과 통합 가능 (https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/account-lifecycle-in-isb.html, 내부: 탑다운 기획안 §7, 내부 자료 독립 검증 불가) |
| 영향 | 중 | 소유권 공백이 파일럿-프로덕션 전환 최대 장애(SoftwareSeni). 자동 Frozen으로 비용 통제, 보드 심의로 사업 판단 병행 (https://www.softwareseni.com/the-enterprise-ai-pilot-purgatory-problem-what-the-statistics-actually-tell-us/) |
| 비용 | 하 | AWS 기존 Innovation Sandbox 기능 활용. 보드 심의는 기존 AI Board 체계 내 처리 가능 (내부: 탑다운 기획안 §7, 내부 자료 독립 검증 불가) |
| 리스크 | 중 | AI 생성 코드의 기술 부채 이관 기준 미정의로 이관팀 거부 가능성 존재 (04 §4 미해결 쟁점 2). 이관 거부 시 Pilot Purgatory 재현 위험 |
| 시급성 | 중 | W3 종료 전 출구 경로(이관/폐기/현업복귀) 및 Go/No-Go 임계값 사전 합의 필요 |

- **2축 환산**: 실행용이성 **상** (실행 가능성 상; 비용 하·리스크 중 → 하향 없음), 영향도 **중** (영향 중; 시급성 중 → 상향 없음) → **선택 과제** (실행용이성 상 × 영향도 중)
- **첫 실행 단계**: 파일럿 착수 전 AWS Innovation Sandbox 비용 임계값(자동 Frozen 트리거) 설정. 3방향 출구(이관/폐기/현업복귀) 판단 기준과 보드 심의 일정을 파일럿 킥오프 문서에 명시. 종료 시 클로저 레코드(15~20분, 4개 항목) 양식 사전 준비.

---

### 3.8 R8 보안 통제 기술 내재화 (SAST·골든 패스 임베딩) — 전략 과제

| 기준 | 등급 | 근거 |
|---|---|---|
| 실행 가능성 | 중 | Semgrep AI-SAST 도입으로 IDOR·인가 오류 부분 자동화 가능(완전 대체 불가). CI/CD 파이프라인 내 SAST·lint 임베딩은 기술적으로 표준 방식 (https://semgrep.dev/blog/2025/ai-powered-detection-with-semgrep/) |
| 영향 | 상 | CI/CD 자동검사만으로는 아키텍처·로직 결함 탐지 불가(Checkmarx 2025). AI 코드 취약점 밀도 2.74배(Veracode). 보안 교육만으로 해결 불가—"규모·속도·다양성이 교육 한계 초과"(TechNewsWorld) (https://checkmarx.com/blog/ai-is-writing-your-code-whos-keeping-it-secure/, https://www.flosum.com/blog/the-unintended-security-threat-of-citizen-development) |
| 비용 | 중 | Semgrep 라이선스 비용 + CI/CD 파이프라인 통합 공수 발생. 골든 패스 내장 정책 설계 추가 공수 |
| 리스크 | 중 | Semgrep AI-SAST가 아키텍처·로직 결함을 탐지하지 못하므로 "보안 완료"로 오인할 위험. 수동 게이트(R4)와 병행 필수 |
| 시급성 | 상 | 골든 패스 완비(R1)와 동시에 구축해야 하므로 파일럿 킥오프 전 완료 필요 |

- **2축 환산**: 실행용이성 **중** (실행 가능성 중; 비용 중·리스크 중 → 추가 하향 없음 — 둘 다 '상'이 아니므로 하향 조건 미충족), 영향도 **상** (영향 상; 시급성 상 → 상한 '상' 유지) → **전략 과제** (실행용이성 중 × 영향도 상)
- **첫 실행 단계**: R1 골든 패스 템플릿 내에 Semgrep SAST·의존성 취약점 스캔·시크릿 스캔을 CI/CD 단계로 내장. 보안 정책 위반 시 자동 빌드 실패 설정. CoE 전수 PR 리뷰 의존에서 "기술 차단선 → CoE 예외 처리"로 역할 재정의.

---

### 3.9 R9 킥오프 전 선발 절차 확정 — Quick Win

| 기준 | 등급 | 근거 |
|---|---|---|
| 실행 가능성 | 상 | 선발 기준 문서화 및 합의는 추가 인프라 없이 CoE 주관으로 처리 가능. Kissflow·Innovation Mode: 파일럿 부서 2~3개 선발이 업계 표준 출발점 (https://kissflow.com/no-code/citizen-developer-program/, https://theinnovationmode.com/corporate-hackathon-template). IntuitionLabs: 팀당 3~5명 혼합팀 구성 권고 (https://intuitionlabs.ai/articles/claude-enterprise-deployment-training-guide-2026) |
| 영향 | 상 | 부적합 팀/과제가 파일럿에 진입하면 3주 타임박스 안에 회복이 불가능. CoE 주관 과제 검토 2단계(비즈니스 타당성 → 기술 실현성)로 초기 리스크 제거 가능 (04 §2.2 일치 증거: Kissflow·Innovation Mode·IntuitionLabs; 04 §3.3 과제 검토 2단계) |
| 비용 | 하 | 선발 기준 작성 및 CoE 주관 2단계 검토 미팅 외 추가 비용 없음 (추정: 기존 기획 미팅 체계 내 처리 가능) |
| 리스크 | 하 | 선발 기준 사전 확정의 리스크는 낮음. 단, 선발 기준이 사후 정치적으로 완화될 가능성은 내부 합의 강도로 관리 (추정: 조직 내 합의 난이도는 맥락 의존) |
| 시급성 | 상 | 킥오프 전에 선발이 완료되어야 하며, 이후 변경 시 파일럿 구조 전체가 흔들림. 선발 절차 미확정 상태에서 킥오프하면 참가 자격 분쟁 발생 가능 |

- **2축 환산**: 실행용이성 **상** (실행 가능성 상 기준; 비용 하·리스크 하 → 하향 없음), 영향도 **상** (영향 상 기준; 시급성 상 → 상한 '상' 유지) → **Quick Win** (실행용이성 상 × 영향도 상)
- **첫 실행 단계**: 파일럿 킥오프 D-14일 이전에 CoE 주관으로 (1) 참가 부서 2~3개 선정(챔피언 보유 여부·구체적 백로그 명확성 기준), (2) 팀당 3~5명 혼합팀(비즈니스 도메인 지식 보유자 + 기술 보조자) 구성, (3) 과제 2단계 검토(1단계: 비즈니스 타당성·ROI 명확성, 2단계: 기술 실현성·3주 범위 적합성)를 완료하고 참가 명단을 문서화.

---

## 4. 조건부 권고·추가 조사 항목

> 04-convergence.md §4 미해결 쟁점·리스크 매핑

| 항목 | 유형 | 전제 조건 / 조사 질문 | 근거 (04 §4 항목) |
|---|---|---|---|
| 파일럿 코호트 규모 정의 | 조건부 권고 | 비전문 시티즌 개발자 특화 벤치마크 부재로 현재 판정 불가(미해결). 조건부 승격 조건: ① 내부 목적 정의(AI 도구 채택 확산 vs 탑다운 과제 완성) + ② 파일럿 드라이런 또는 사내 벤치마크 수립 후 실증 확보. 이 절차 완료 후 권고로 승격 가능. 참고 수치 50~100명(채택 확산) / 3~5명(과제 완성)는 1차 가설값이며 내부 재검증 필요 | 04 §4 미해결 쟁점 1 |
| AI 생성 코드 이관 기술 부채 수용 기준 수립 | 조건부 권고 | 이관팀과 파일럿 종료 전(W3 D+7 회고 시점)까지 기술 부채 수용 조건(코드 중복 허용 임계값·리팩토링 의무 범위)을 사전 합의하면, 자동 이관 원칙으로 승격 가능 | 04 §4 미해결 쟁점 2 |
| 시티즌 개발자 3주 배포 완성 실증 데이터 확보 | 추가 조사 | 비전문 개발자가 골든 패스 + AI 코딩 도구 조합으로 3주 내 운영환경 배포를 완성한 사례의 배포 완성률·실패율 벤치마크가 존재하는가? 국내외 사내 해커톤·부트캠프 운영 기관(NIPA·AWS·MS) 사례 조사 필요 | 04 §4 미해결 쟁점 3 |
| 3-lane 리뷰 3주 타임박스 적용 가능성 검증 | 추가 조사 | Red lane 3인 승인 체계가 3주 스프린트 안에서 실제로 소화 가능한지, 상시 개발 조직 사례가 아닌 단기 파일럿 조직 기준 SLA 데이터가 존재하는가? 사내 파일럿 드라이런(dry-run) 1회 시뮬레이션으로 측정 가능 | 04 §4 미해결 쟁점 4 |
| 챔피언 프로그램 정량 효과 독립 검증 | 추가 조사 | Worklytics "2.1배 지속 사용률"·Adoptify.ai "62→85%" 수치를 동료 검토 연구 또는 사내 파일럿 후 측정값으로 검증 가능한가? 파일럿 종료 후 90일 WAU 추적으로 내부 기준값 수립 가능 | 04 §4 미해결 쟁점 5 |
| 복잡한 게이트 → Shadow AI 역설 임계점 파악 | 추가 조사 | 게이트 복잡도와 Shadow AI 발생률 간 임계점 데이터가 존재하는가? 파일럿 기간 중 비공식 AI 도구 사용 현황 모니터링 지표를 설계하여 추적 필요 | 04 §4 미해결 쟁점 6 |
| **내부 기획안 주체 불일치** | **구조적 리스크** | 내부 기획안(AWS_기반_탑다운_AIFAB_과제_운영환경_구축운영_기획안_v1-0.md §2)은 탑다운 과제 수행 주체를 '지정된 개발·운영 조직'으로 전제하며 시티즌 개발자 파일럿을 직접 다루지 않는다(내부 자료, 독립 검증 불가). 시티즌 개발자가 탑다운 과제를 수행하는 파일럿은 기획안의 전제와 구조적으로 불일치하므로, 파일럿 착수 전 기획안 개정 또는 파일럿 예외 규정 합의가 필요하다. | 내부: 탑다운 기획안 §2 |

---

## 5. 검증 이력

| Layer | 결과 |
|---|---|
| Layer 1 — URL 검증 | 통과 — alive 53 / dead 0 (초판·수정판 각 1회, 2026-07-12) |
| Layer 2 — Critic 비평 (opus) | 수정 1회 반영 후 재확인 통과 — R1·R4·R5 실행용이성 환산 정정(매트릭스 재배치), 코호트 규모 조건부 권고에 실증 절차 명시 (2026-07-12) |
| Layer 3 — Codex 교차 검증 | 채택 6건 / 기각 3건 — 채택: 단정 표현 완화, KPMG 지표 전환 오류 정정, 0.605 예시값 명시, 내부 기획안 주체 불일치 리스크 신설, 선발 권고(R9) 신설, R3 범위 한정. 기각: 미래 출처 주장(사실 오인), 기술부채 기준 권고 승격(04 미해결 쟁점 유지), 코호트 기본안(기반영) (2026-07-12) |
| 출구 게이트 | 승인 — 2026-07-12, 반영 의견 없음. 후속 지시: 결론 기반 구축 타임라인(9월 초 운영 시작)·3주 스프린트 운영 시간표를 실무용·경영보고용 2버전으로 작성 |

---

## 6. Sources

- https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/ (Fortune / MIT NANDA, 2025-08-18)
- https://fluidlabs.com/resources/why-42-percent-enterprise-ai-abandoned-2025 (Fluidlabs / S&P Global, 2025)
- https://www.softwareseni.com/the-enterprise-ai-pilot-purgatory-problem-what-the-statistics-actually-tell-us/ (SoftwareSeni, 날짜 미상)
- https://www.forbes.com/sites/joemckendrick/2026/01/26/why-ais-10-20-70-principle-should-matter-to-ceos-and-everyone-else/ (Forbes / BCG, 2026-01-26)
- https://www.veracode.com/blog/spring-2026-genai-code-security/ (Veracode Spring 2026 GenAI Code Security Report, 2026-04)
- https://arxiv.org/pdf/2606.22721 (arXiv: Habituation at the Gate, 2026-06-23)
- https://www.metacto.com/blogs/establishing-code-review-standards-for-ai-generated-code (metacto, 2026-07-08)
- https://checkmarx.com/blog/ai-is-writing-your-code-whos-keeping-it-secure/ (Checkmarx, 2025)
- https://www.pixelmojo.io/blogs/vibe-coding-technical-debt-crisis-2026-2027 (Pixelmojo, 2026)
- https://devops.com/ai-in-software-development-productivity-at-the-cost-of-code-quality-2/ (DevOps.com / Google DORA 2024, 2025)
- https://google.github.io/gsocguides/mentor/evaluations (GSoC Evaluations Guide, 2025)
- https://opensource.googleblog.com/2025/08/google-summer-of-code-2025-contributor-statistics.html (GSoC 2025 Statistics, 2025-08)
- https://www.samsung.com/sec/sustainability/popup/popup_doc/AYUBw0_6ArQAIx8i/ (Samsung C-Lab Sustainability, 2025)
- https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025 (DORA 2025 / Faros.ai, 2025-09)
- https://dora.dev/insights/balancing-ai-tensions/ (DORA Insights, 2025)
- https://systemprompt.io/guides/claude-code-organisation-rollout (systemprompt.io Claude Code Rollout Playbook, 날짜 미상)
- https://claude.com/resources/tutorials/claude-enterprise-administrator-guide (Claude Enterprise Administrator Guide, 날짜 미상)
- https://claude.com/resources/tutorials/scaling-workflows-with-claude-cowork-at-your-organization (Scaling workflows with Claude Cowork, 날짜 미상)
- https://code.claude.com/docs/en/champion-kit (Claude Code Champion Kit, 날짜 미상)
- https://aiassemblylines.com/post/ai-champions-program-enterprise-adoption (AI Assembly Lines, 2026)
- https://jellyfish.co/blog/2025-dora-report/ (Jellyfish DORA 2025, 2025)
- https://platformengineering.com/features/dora-2025-ai-wont-save-you-without-a-solid-platform/ (Platform Engineering / DORA 2025, 2025)
- https://platformengineering.org/blog/how-to-set-up-an-internal-developer-platform (platformengineering.org, 날짜 미상)
- https://www.thecloudplaybook.com/p/first-6-golden-paths-aws-platform-teams (The Cloud Playbook TCP#124, 날짜 미상)
- https://tasrieit.com/blog/golden-paths-platform-engineering-guide-2026 (Tasrie IT, 2026-01)
- https://backstage.spotify.com/discover/blog/how-we-measure-backstage-success-at-spotify (Spotify Backstage, 2020~)
- https://kpmg.com/be/en/home/insights/2024/11/ta-transforming-business-value-creation-with-citizen-development.html (KPMG Belgium, 2024-11)
- https://kissflow.com/no-code/citizen-developer-program/ (Kissflow, 날짜 미상)
- https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap-mentoring-and-user-enablement (Microsoft Learn, 2024-12-30)
- https://www.microsoft.com/en-us/power-platform/blog/power-apps/hmgroup/ (Microsoft Power Platform Blog / H&M, 날짜 미상)
- https://www.tractiontechnology.com/blog/how-to-run-a-successful-pilot-with-a-startup-frameworks-kpis-enterprise-best-practices (Traction Technology, 날짜 미상)
- https://guides.visual-paradigm.com/making-informed-decisions-with-a-go-no-go-checklist-for-agile-projects-a-scoring-approach/ (Visual Paradigm, 날짜 미상)
- https://marginlayer.app/blog/pilot-success-criteria-kpi-roi.html (MarginLayer, 날짜 미상)
- https://agility-at-scale.com/ai/strategy/roi-and-success-metrics/ (Agility at Scale, 날짜 미상)
- https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/account-lifecycle-in-isb.html (AWS Docs Innovation Sandbox, 날짜 미상)
- https://umbrex.com/resources/frameworks/strategy-frameworks/stage-gate-innovation-process/ (Umbrex Stage-Gate, 날짜 미상)
- https://www.elegantsoftwaresolutions.com/blog/vibe-coding-enterprise-adoption (Elegant Software Solutions, 2025)
- https://semgrep.dev/blog/2025/ai-powered-detection-with-semgrep/ (Semgrep, 2025)
- https://gotranscript.com/en/blog/turnaround-time-vs-quality-set-slas-without-increasing-risk (GoTranscript, 날짜 미상)
- https://www.flosum.com/blog/the-unintended-security-threat-of-citizen-development (Flosum, 2024)
- https://aws.amazon.com/ko/blogs/tech/cj-oliveyoung-aidlc-tech-blog/ (AWS 기술 블로그 CJ올리브영, 날짜 미상)
- https://aws.amazon.com/ko/blogs/korea/how-frontier-teams-are-reinventing-ai-native-development/ (AWS Korea Blog, 2025)
- https://isg-one.com/articles/the-automation-center-of-excellence-and-citizen-developers-not-the-wild-wild-west! (ISG, 날짜 미상)
- https://blog.exceeds.ai/enterprise-ai-adoption-metrics-2025/ (Exceeds.ai, 2025)
- https://www.index.dev/blog/ai-coding-assistants-roi-productivity (Index.dev, 2025)
- https://newsroom.ibm.com/2025-10-07-2025-ibm-and-anthropic-partner-to-advance-enterprise-software-development-with-proven-security-and-governance (IBM Newsroom, 2025-10-07)
- https://2023.platformcon.com/talks/how-toyota-saved-over-10m-and-optimized-developer-experience-through-platform-engineering (PlatformCon 2023, 2023-06)
- https://quixy.com/blog/citizen-development-kpis-and-roi/ (Quixy, 2024)
- https://intuitionlabs.ai/articles/claude-enterprise-deployment-training-guide-2026 (IntuitionLabs, 2026)
- https://theinnovationmode.com/corporate-hackathon-template (Innovation Mode, 날짜 미상)
- https://docs.aws.amazon.com/controltower/latest/userguide/decommissioning-process-overview.html (AWS Docs Control Tower, 날짜 미상)
- https://pluto.security/blog/citizen-development-security-teams/ (Pluto Security, 2024)
- https://apiiro.com/blog/4x-velocity-10x-vulnerabilities-ai-coding-assistants-are-shipping-more-risks/ (Apiiro, 2025-09-04)
