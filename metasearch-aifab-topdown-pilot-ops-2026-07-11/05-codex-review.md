Reading additional input from stdin...
OpenAI Codex v0.143.0
--------
workdir: /Users/jaybee/lab/AIFAB-plan
model: gpt-5.5
provider: openai
approval: never
sandbox: read-only
reasoning effort: none
reasoning summaries: none
session id: 019f5249-19fc-7e11-a135-2e18f810fac7
--------
user
다음 파일의 결론 보고서를 독립적으로 검증하라: /Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md — 논리 결함, 근거 대비 과장된 주장, 핵심 누락을 구체적으로 지적하라. 한국어로 답하라.
codex
검증 대상 파일과 같은 폴더의 근거 파일 구성을 먼저 확인하겠습니다. 결론 자체만 보지 않고, 결론이 기대고 있는 주변 문서까지 대조해서 과장이나 누락을 잡겠습니다.
exec
/bin/zsh -lc "sed -n '1,240p' /Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md" in /Users/jaybee/lab/AIFAB-plan
 succeeded in 0ms:
# 결론 보고서 — AI FAB 탑다운 과제 파일럿 운영 방안: 시티즌 개발자 선발부터 3주 스프린트 배포·종료까지 운영 시나리오

> 생성: 2026-07-11 | 메타서치 단계 5 산출물 | 입력: 04-convergence.md

---

## 1. Executive Summary

3주 타임박스 안에 시티즌 개발자가 운영 배포를 완성하려면 **킥오프 4~6주 전에 골든 패스(AWS 6대 템플릿)가 완비**되어 있어야 한다는 것이 수렴 연구의 핵심 결론이다. 이 전제가 없으면 GenAI 파일럿 실패율 88~95%(MIT NANDA)·기업 AI 이니셔티브 포기율 42%(S&P Global)가 그대로 재현된다. 골든 패스가 갖춰지면 온보딩 시간 30~60% 단축, 첫 배포 1시간 미만이 실현 가능하다(Tasrie IT 2026, Spotify Backstage).

파일럿 운영 구조는 **Agile-Stage-Gate 하이브리드(W1 Gate 0 → W2 중간 Gate → W3 Gate 2+배포)** 가 기업 거버넌스와 스프린트 속도를 동시에 충족하는 최적 구조로 판정되었으며, 배포 게이트는 3-lane 위험 분류(Green/Yellow/Red)와 rubber-stamping 방지 장치를 반드시 포함해야 한다(metacto 2026-07-08; arXiv 2606.22721).

CoE 선행 구축(2~5명)이 파일럿 성공률을 결정하며, 거버넌스 유무에 따른 성공률 차이가 77% vs 39%(KPMG Belgium 2024)로 2배다. 에이전틱 도구 10주 지속 사용률이 10% 미만(DORA 2025)이므로 챔피언 프로그램이 없으면 파일럿 효과는 소멸한다.

종료·이관은 소유권 단일 책임자 사전 지정 + 3방향 출구(이관/폐기/현업복귀) + 자동 Frozen·보드 최종 결정 하이브리드로 설계하고, 파일럿 착수 전 KPI·Go/No-Go 스코어카드를 동결하는 것이 필수다.

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

### 2B. 우선순위 매트릭스 표

| 영향도 \ 실행용이성 | 상 | 중 | 하 |
|---|---|---|---|
| **상** | R2 KPI 동결, R3 Agile-Stage-Gate | R8 보안 내재화 | R1 골든 패스, R4 게이트 설계, R5 CoE |
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
| 시급성 | 상 | 킥오프 전에 완료해야 하며 이후 변경 시 파일럿 평가 무력화. Go/No-Go 스코어카드(기술 40%·재무 30%·시장 20%·자원 10%, 임계값 0.605) 사전 합의 (https://guides.visual-paradigm.com/making-informed-decisions-with-a-go-no-go-checklist-for-agile-projects-a-scoring-approach/) |

- **2축 환산**: 실행용이성 **상** (실행 가능성 상 기준; 비용 하·리스크 하 → 하향 없음), 영향도 **상** (영향 상 기준; 시급성 상 → 상한 '상' 유지)
- **첫 실행 단계**: 파일럿 착수 전 AI Board 킥오프 회의에서 ①배포 완성 건수 ②WAU 70% ③참여자 만족도 4.0/5.0+ ④사이클 타임 단축률 ⑤거버넌스 준수율 5개 KPI와 Go/No-Go 임계값(0.605)을 문서화하고 결정 권한자(named decision owner)를 지정.

---

### 3.3 R3 Agile-Stage-Gate 하이브리드 운영 구조 채택 — Quick Win

| 기준 | 등급 | 근거 |
|---|---|---|
| 실행 가능성 | 상 | 기존 내부 기획안 §5 배포 게이트·격상 절차와 직접 연계 가능. Agile-Stage-Gate 게이트 결정 24~48시간 이내 목표로 속도 저해 최소화 (https://umbrex.com/resources/frameworks/strategy-frameworks/stage-gate-innovation-process/) |
| 영향 | 상 | GSoC 중간 평가에서 "한계 통과" 참가자 80%+가 최종 실패 → 중간 Gate 없이는 조기 경보 불가 (https://google.github.io/gsocguides/mentor/evaluations). KPMG Belgium: 거버넌스 있는 조직 77% vs 없는 조직 39% 비용 절감 성공 (https://kpmg.com/be/en/home/insights/2024/11/ta-transforming-business-value-creation-with-citizen-development.html) |
| 비용 | 하 | 기존 조직 구조(AI Board·CoE) 내 역할 정의 수준으로 처리 가능. 추가 시스템 불필요 (내부: 탑다운 기획안 §5, 내부 자료 독립 검증 불가) |
| 리스크 | 하 | 구조 채택 자체의 리스크는 낮음. 게이트 경직화로 Shadow AI 촉진 가능성은 R4에서 별도 관리 (https://www.elegantsoftwaresolutions.com/blog/vibe-coding-enterprise-adoption) |
| 시급성 | 상 | 킥오프 전 운영 구조 확정이 필수. 이후 변경 시 참가자 혼선 유발 |

- **2축 환산**: 실행용이성 **상** (실행 가능성 상; 비용 하·리스크 하 → 하향 없음), 영향도 **상** (영향 상; 시급성 상 → 상한 '상' 유지)
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
| 영향 | 상 | KPMG Belgium: 거버넌스 있는 조직 77% vs 없는 조직 39% (https://kpmg.com/be/en/home/insights/2024/11/ta-transforming-business-value-creation-with-citizen-development.html). BCG 10-20-70: AI 성공의 70%는 사람·프로세스·문화 (https://www.forbes.com/sites/joemckendrick/2026/01/26/why-ais-10-20-70-principle-should-matter-to-ceos-and-everyone-else/) |
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

---

## 5. 검증 이력

| Layer | 결과 |
|---|---|
| Layer 1 — URL 검증 | (검증 대기) |
| Layer 2 — Critic 비평 | (검증 대기) |
| Layer 3 — Codex 교차 검증 | (검증 대기) |
| 출구 게이트 | (승인 대기) |

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

exec
/bin/zsh -lc 'pwd && rg --files /Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11' in /Users/jaybee/lab/AIFAB-plan
 succeeded in 0ms:
/Users/jaybee/lab/AIFAB-plan
/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-codex-review.md
/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/02-deep-research.md
/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/01-topic-brief.md
/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/03-divergence/d5-platform-golden-path.md
/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/03-divergence/d4-deepdive-agentic-coding.md
/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/03-divergence/d1-failure-cases.md
/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/03-divergence/d2-critical-view.md
/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/03-divergence/d4-agentic-coding-trends.md
/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/03-divergence/d2-deepdive-critical-view.md
/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/03-divergence/d3-adjacent-programs.md
/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/03-divergence/d5-deepdive-golden-path.md
/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/findings/q1-selection-criteria.md
/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/findings/q2-sprint-structure.md
/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/findings/q0-internal-docs.md
/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/findings/q3-support-system.md
/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/findings/q4-closure-handover.md
/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/findings/q5-kpi-scaling.md
/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md
/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/STATE.md
/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/04-convergence.md

codex
결론 문서 안에서 이미 “검증 대기”로 남은 항목이 보입니다. 이제 입력 산출물인 `04-convergence.md`와 교차검증/세부 findings를 대조해, 결론이 수렴 결과보다 더 강하게 말한 지점을 분리하겠습니다.
exec
/bin/zsh -lc "sed -n '1,260p' /Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/04-convergence.md" in /Users/jaybee/lab/AIFAB-plan
 succeeded in 0ms:
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

exec
/bin/zsh -lc "sed -n '1,260p' /Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-codex-review.md" in /Users/jaybee/lab/AIFAB-plan
 succeeded in 0ms:
Reading additional input from stdin...
OpenAI Codex v0.143.0
--------
workdir: /Users/jaybee/lab/AIFAB-plan
model: gpt-5.5
provider: openai
approval: never
sandbox: read-only
reasoning effort: none
reasoning summaries: none
session id: 019f5249-19fc-7e11-a135-2e18f810fac7
--------
user
다음 파일의 결론 보고서를 독립적으로 검증하라: /Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md — 논리 결함, 근거 대비 과장된 주장, 핵심 누락을 구체적으로 지적하라. 한국어로 답하라.
codex
검증 대상 파일과 같은 폴더의 근거 파일 구성을 먼저 확인하겠습니다. 결론 자체만 보지 않고, 결론이 기대고 있는 주변 문서까지 대조해서 과장이나 누락을 잡겠습니다.
exec
/bin/zsh -lc "sed -n '1,240p' /Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md" in /Users/jaybee/lab/AIFAB-plan
 succeeded in 0ms:
# 결론 보고서 — AI FAB 탑다운 과제 파일럿 운영 방안: 시티즌 개발자 선발부터 3주 스프린트 배포·종료까지 운영 시나리오

> 생성: 2026-07-11 | 메타서치 단계 5 산출물 | 입력: 04-convergence.md

---

## 1. Executive Summary

3주 타임박스 안에 시티즌 개발자가 운영 배포를 완성하려면 **킥오프 4~6주 전에 골든 패스(AWS 6대 템플릿)가 완비**되어 있어야 한다는 것이 수렴 연구의 핵심 결론이다. 이 전제가 없으면 GenAI 파일럿 실패율 88~95%(MIT NANDA)·기업 AI 이니셔티브 포기율 42%(S&P Global)가 그대로 재현된다. 골든 패스가 갖춰지면 온보딩 시간 30~60% 단축, 첫 배포 1시간 미만이 실현 가능하다(Tasrie IT 2026, Spotify Backstage).

파일럿 운영 구조는 **Agile-Stage-Gate 하이브리드(W1 Gate 0 → W2 중간 Gate → W3 Gate 2+배포)** 가 기업 거버넌스와 스프린트 속도를 동시에 충족하는 최적 구조로 판정되었으며, 배포 게이트는 3-lane 위험 분류(Green/Yellow/Red)와 rubber-stamping 방지 장치를 반드시 포함해야 한다(metacto 2026-07-08; arXiv 2606.22721).

CoE 선행 구축(2~5명)이 파일럿 성공률을 결정하며, 거버넌스 유무에 따른 성공률 차이가 77% vs 39%(KPMG Belgium 2024)로 2배다. 에이전틱 도구 10주 지속 사용률이 10% 미만(DORA 2025)이므로 챔피언 프로그램이 없으면 파일럿 효과는 소멸한다.

종료·이관은 소유권 단일 책임자 사전 지정 + 3방향 출구(이관/폐기/현업복귀) + 자동 Frozen·보드 최종 결정 하이브리드로 설계하고, 파일럿 착수 전 KPI·Go/No-Go 스코어카드를 동결하는 것이 필수다.

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

### 2B. 우선순위 매트릭스 표

| 영향도 \ 실행용이성 | 상 | 중 | 하 |
|---|---|---|---|
| **상** | R2 KPI 동결, R3 Agile-Stage-Gate | R8 보안 내재화 | R1 골든 패스, R4 게이트 설계, R5 CoE |
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
| 시급성 | 상 | 킥오프 전에 완료해야 하며 이후 변경 시 파일럿 평가 무력화. Go/No-Go 스코어카드(기술 40%·재무 30%·시장 20%·자원 10%, 임계값 0.605) 사전 합의 (https://guides.visual-paradigm.com/making-informed-decisions-with-a-go-no-go-checklist-for-agile-projects-a-scoring-approach/) |

- **2축 환산**: 실행용이성 **상** (실행 가능성 상 기준; 비용 하·리스크 하 → 하향 없음), 영향도 **상** (영향 상 기준; 시급성 상 → 상한 '상' 유지)
- **첫 실행 단계**: 파일럿 착수 전 AI Board 킥오프 회의에서 ①배포 완성 건수 ②WAU 70% ③참여자 만족도 4.0/5.0+ ④사이클 타임 단축률 ⑤거버넌스 준수율 5개 KPI와 Go/No-Go 임계값(0.605)을 문서화하고 결정 권한자(named decision owner)를 지정.

---

### 3.3 R3 Agile-Stage-Gate 하이브리드 운영 구조 채택 — Quick Win

| 기준 | 등급 | 근거 |
|---|---|---|
| 실행 가능성 | 상 | 기존 내부 기획안 §5 배포 게이트·격상 절차와 직접 연계 가능. Agile-Stage-Gate 게이트 결정 24~48시간 이내 목표로 속도 저해 최소화 (https://umbrex.com/resources/frameworks/strategy-frameworks/stage-gate-innovation-process/) |
| 영향 | 상 | GSoC 중간 평가에서 "한계 통과" 참가자 80%+가 최종 실패 → 중간 Gate 없이는 조기 경보 불가 (https://google.github.io/gsocguides/mentor/evaluations). KPMG Belgium: 거버넌스 있는 조직 77% vs 없는 조직 39% 비용 절감 성공 (https://kpmg.com/be/en/home/insights/2024/11/ta-transforming-business-value-creation-with-citizen-development.html) |
| 비용 | 하 | 기존 조직 구조(AI Board·CoE) 내 역할 정의 수준으로 처리 가능. 추가 시스템 불필요 (내부: 탑다운 기획안 §5, 내부 자료 독립 검증 불가) |
| 리스크 | 하 | 구조 채택 자체의 리스크는 낮음. 게이트 경직화로 Shadow AI 촉진 가능성은 R4에서 별도 관리 (https://www.elegantsoftwaresolutions.com/blog/vibe-coding-enterprise-adoption) |
| 시급성 | 상 | 킥오프 전 운영 구조 확정이 필수. 이후 변경 시 참가자 혼선 유발 |

- **2축 환산**: 실행용이성 **상** (실행 가능성 상; 비용 하·리스크 하 → 하향 없음), 영향도 **상** (영향 상; 시급성 상 → 상한 '상' 유지)
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
| 영향 | 상 | KPMG Belgium: 거버넌스 있는 조직 77% vs 없는 조직 39% (https://kpmg.com/be/en/home/insights/2024/11/ta-transforming-business-value-creation-with-citizen-development.html). BCG 10-20-70: AI 성공의 70%는 사람·프로세스·문화 (https://www.forbes.com/sites/joemckendrick/2026/01/26/why-ais-10-20-70-principle-should-matter-to-ceos-and-everyone-else/) |
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

---

## 5. 검증 이력

| Layer | 결과 |
|---|---|
| Layer 1 — URL 검증 | (검증 대기) |
| Layer 2 — Critic 비평 | (검증 대기) |
| Layer 3 — Codex 교차 검증 | (검증 대기) |
| 출구 게이트 | (승인 대기) |

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


exec
/bin/zsh -lc "sed -n '1,220p' /Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/01-topic-brief.md" in /Users/jaybee/lab/AIFAB-plan
 succeeded in 0ms:
# 주제 브리프 — AI FAB 탑다운 과제 파일럿 운영 방안: 시티즌 개발자 선발부터 3주 스프린트 배포·종료까지 운영 시나리오

> 생성: 2026-07-11 | 메타서치 단계 1 산출물

## 배경·목적
- AI FAB(사내 시티즌 개발자 육성 + 탑다운 AI 과제 수행 프로그램)에서 탑다운 과제의 **파일럿을 실행**하기 위한 운영 방안 수립 (가정)
- 산출물 용도: 시티즌 개발자 온보딩(선발)부터 3주 스프린트로 배포 완성, 배포 후 종료까지의 **엔드투엔드 운영 시나리오 md 문서** — 실제 파일럿 운영 매뉴얼의 기초 (가정)

## 핵심 질문
1. 시티즌 개발자 선발은 어떤 기준·절차로 하는가 — 유사 프로그램(사내 시티즌 개발 프로그램, 해커톤/부트캠프형 파일럿)의 선발 모범 사례는?
2. 3주 스프린트로 "배포까지 완성"하려면 주차별 운영 구조(W1/W2/W3)를 어떻게 설계해야 하는가 — 킥오프, 중간 점검, 심사·게이트, 배포 승인?
3. 파일럿 기간 중 지원 체계(멘토링, 오피스아워, 플랫폼·인프라 지원, AI 코딩 도구 활용)는 어떻게 구성하는가? (가정)
4. 배포 후 종료 처리(운영 이관 vs 폐기, 회고, 성과 측정, 리소스 회수)는 어떤 절차로 하는가?
5. 파일럿 성공 지표(KPI)와 본 사업 확대 판단 기준은 무엇으로 잡는가? (가정)

## 범위
### 포함
- 시티즌 개발자 대상 사내 개발 프로그램 운영 사례 (국내외) (가정)
- 3주(단기) 스프린트 기반 과제 수행 운영 모델 — 애자일 스프린트, 해커톤·부트캠프·액셀러레이터 운영 방식 (가정)
- 선발 → 온보딩 → 스프린트 실행 → 배포 → 종료(이관·회고)의 전체 라이프사이클 (가정)
- AWS 기반 샌드박스/운영환경에서의 배포·리소스 관리 관점 (가정)

### 제외
- 인프라 구축 상세 설계 (기존 기획안에서 이미 다룸 — 운영 시나리오 관점만 참조) (가정)
- 바텀업 샌드박스 과제 운영 (탑다운 파일럿에 집중) (가정)

## 성공 기준
- 핵심 질문 5개에 근거 있는 답을 확보하고, **시티즌 개발자 접수부터 배포 후 종료까지 단계별 운영 시나리오**(역할·산출물·게이트 포함)를 md 보고서로 작성할 수 있으면 성공 (가정)

## 주제 지형 (딥 모드)
- 해당 없음

## 참조 문서

| 파일명 | 절대경로 | 형식 |
|---|---|---|
| AWS_기반_탑다운_AIFAB_과제_운영환경_구축운영_기획안_v1-0.md | /Users/jaybee/lab/AIFAB-plan/fab/AWS_기반_탑다운_AIFAB_과제_운영환경_구축운영_기획안_v1-0.md | md |

> 내부 문서 내용은 최종 보고서에 인용될 수 있습니다.

codex
핵심 구조는 파악했습니다. 마지막으로 줄 번호를 붙여 검토 근거를 정확히 인용하고, 선발 기준·운영 시나리오 같은 원래 질문의 누락 여부를 확인하겠습니다.
exec
/bin/zsh -lc "nl -ba /Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md | sed -n '1,240p'" in /Users/jaybee/lab/AIFAB-plan
 succeeded in 0ms:
     1	# 결론 보고서 — AI FAB 탑다운 과제 파일럿 운영 방안: 시티즌 개발자 선발부터 3주 스프린트 배포·종료까지 운영 시나리오
     2	
     3	> 생성: 2026-07-11 | 메타서치 단계 5 산출물 | 입력: 04-convergence.md
     4	
     5	---
     6	
     7	## 1. Executive Summary
     8	
     9	3주 타임박스 안에 시티즌 개발자가 운영 배포를 완성하려면 **킥오프 4~6주 전에 골든 패스(AWS 6대 템플릿)가 완비**되어 있어야 한다는 것이 수렴 연구의 핵심 결론이다. 이 전제가 없으면 GenAI 파일럿 실패율 88~95%(MIT NANDA)·기업 AI 이니셔티브 포기율 42%(S&P Global)가 그대로 재현된다. 골든 패스가 갖춰지면 온보딩 시간 30~60% 단축, 첫 배포 1시간 미만이 실현 가능하다(Tasrie IT 2026, Spotify Backstage).
    10	
    11	파일럿 운영 구조는 **Agile-Stage-Gate 하이브리드(W1 Gate 0 → W2 중간 Gate → W3 Gate 2+배포)** 가 기업 거버넌스와 스프린트 속도를 동시에 충족하는 최적 구조로 판정되었으며, 배포 게이트는 3-lane 위험 분류(Green/Yellow/Red)와 rubber-stamping 방지 장치를 반드시 포함해야 한다(metacto 2026-07-08; arXiv 2606.22721).
    12	
    13	CoE 선행 구축(2~5명)이 파일럿 성공률을 결정하며, 거버넌스 유무에 따른 성공률 차이가 77% vs 39%(KPMG Belgium 2024)로 2배다. 에이전틱 도구 10주 지속 사용률이 10% 미만(DORA 2025)이므로 챔피언 프로그램이 없으면 파일럿 효과는 소멸한다.
    14	
    15	종료·이관은 소유권 단일 책임자 사전 지정 + 3방향 출구(이관/폐기/현업복귀) + 자동 Frozen·보드 최종 결정 하이브리드로 설계하고, 파일럿 착수 전 KPI·Go/No-Go 스코어카드를 동결하는 것이 필수다.
    16	
    17	**핵심 리스크**: 파일럿 종료 후 이관팀이 AI 생성 코드의 기술 부채(기술 부채 30~41% 증가, 코드 중복 8배, GitClear·Pixelmojo)를 수용하는 기준이 내부·외부 모두 미정의이며, 이관 거부 시 Pilot Purgatory(SoftwareSeni)가 재현될 가능성이 높다.
    18	
    19	---
    20	
    21	## 2. 우선순위 매트릭스
    22	
    23	### 2A. 2축 좌표 요약
    24	
    25	| 권고 번호 | 제목 | 실행용이성 | 영향도 | 분류 |
    26	|---|---|---|---|---|
    27	| R1 | 골든 패스 사전 완비 (킥오프 4~6주 전) | 하 | 상 | 전략 과제 |
    28	| R2 | 킥오프 전 KPI·Go/No-Go 스코어카드 동결 | 상 | 상 | Quick Win |
    29	| R3 | Agile-Stage-Gate 하이브리드 운영 구조 채택 | 상 | 상 | Quick Win |
    30	| R4 | 3-lane 위험 분류 기반 배포 게이트 설계 | 하 | 상 | 전략 과제 |
    31	| R5 | CoE 선행 구축 + 초기 고밀도 멘토링 (co-dev 50%) | 하 | 상 | 전략 과제 |
    32	| R6 | 챔피언 프로그램 + 3단계 체크인 구조 도입 | 상 | 중 | 선택 과제 |
    33	| R7 | 자동 Frozen + 보드 심의 하이브리드 종료 설계 | 상 | 중 | 선택 과제 |
    34	| R8 | 보안 통제 기술 내재화 (SAST·골든 패스 임베딩) | 중 | 상 | 전략 과제 |
    35	
    36	### 2B. 우선순위 매트릭스 표
    37	
    38	| 영향도 \ 실행용이성 | 상 | 중 | 하 |
    39	|---|---|---|---|
    40	| **상** | R2 KPI 동결, R3 Agile-Stage-Gate | R8 보안 내재화 | R1 골든 패스, R4 게이트 설계, R5 CoE |
    41	| **중** | R6 챔피언 프로그램, R7 종료 하이브리드 | — | — |
    42	| **하** | — | — | — |
    43	
    44	### 2C. 분류별 목록
    45	
    46	| 분류 | 권고 | 요약 |
    47	|---|---|---|
    48	| Quick Win | R2 KPI·Go/No-Go 스코어카드 동결 | 킥오프 전 측정 기준 합의—비용 없음, 효과 즉시 |
    49	| Quick Win | R3 Agile-Stage-Gate 하이브리드 운영 구조 | W1/W2/W3 게이트 구조 문서화—추가 리소스 불필요 |
    50	| 전략 과제 | R1 골든 패스 사전 완비 | 파일럿 전 4~6주 AWS 6대 템플릿 준비—기간·공수 필요 |
    51	| 전략 과제 | R4 3-lane 배포 게이트 설계 | Red lane 3인 승인 + rubber-stamping 방지 체계 구축 |
    52	| 전략 과제 | R5 CoE 선행 구축 + 고밀도 멘토링 | 2~5명 CoE 사전 편성, 초기 co-development 50% 비율 |
    53	| 전략 과제 | R8 보안 통제 기술 내재화 | SAST·골든 패스 내장으로 COE 전수 리뷰 부담 제거 |
    54	| 선택 과제 | R6 챔피언 프로그램 + 3단계 체크인 | 25~50명당 챔피언 1명, 주 30분 오피스아워 |
    55	| 선택 과제 | R7 자동 Frozen + 보드 심의 하이브리드 | 비용 임계값 자동 차단, 최종 폐쇄는 보드 결정 |
    56	
    57	---
    58	
    59	## 3. 권고별 상세
    60	
    61	### 3.1 R1 골든 패스 사전 완비 (킥오프 4~6주 전) — 전략 과제
    62	
    63	| 기준 | 등급 | 근거 |
    64	|---|---|---|
    65	| 실행 가능성 | 중 | IDP MVP 정석 16주(8+8) vs 3주 파일럿의 시간 긴장 존재. 파일럿 이전 별도 준비 기간 확보 필요 (https://platformengineering.org/blog/how-to-set-up-an-internal-developer-platform) |
    66	| 영향 | 상 | 골든 패스 미비 시 AI 생성 코드 변경 실패율 +30%·PR당 인시던트 +23.5%(Cortex 2025). IDP 성숙 조직 온보딩 30~60% 단축·첫 배포 1시간 미만 (https://tasrieit.com/blog/golden-paths-platform-engineering-guide-2026, https://backstage.spotify.com/discover/blog/how-we-measure-backstage-success-at-spotify) |
    67	| 비용 | 상 | AI 인프라팀 4~6주 선행 투입 필요. AWS 6대 템플릿 구축 공수 존재 (https://www.thecloudplaybook.com/p/first-6-golden-paths-aws-platform-teams) |
    68	| 리스크 | 중 | 골든 패스 문헌이 전문 개발자 대상이며 시티즌 개발자 특화 검증 미완 (내부: 탑다운 기획안 §5, 내부 자료 독립 검증 불가) |
    69	| 시급성 | 상 | 킥오프 전에 반드시 완비되어야 하므로 파일럿 일정 역산 시 즉시 착수 필요. DORA 2025 "플랫폼 없이 AI 단독 도입=안정성 저하" (https://platformengineering.com/features/dora-2025-ai-wont-save-you-without-a-solid-platform/) |
    70	
    71	- **2축 환산**: 실행용이성 **하** (실행 가능성 중 기준; 비용 상 → 한 단계 하향 → 하), 영향도 **상** (영향 상 기준; 시급성 상 → 상한이 '상'이므로 유지) → **전략 과제** (실행용이성 하 × 영향도 상)
    72	- **첫 실행 단계**: AI 인프라팀이 파일럿 킥오프 D-42일 이전에 ECS on Fargate·Lambda·RDS·비용태그·관측성·Secrets Manager 6대 템플릿 완비 여부를 체크리스트로 확인. 시티즌 개발자가 폼 입력만으로 CI/CD·IAM·모니터링 포함 레포를 자동 생성할 수 있는 상태를 킥오프 전 완성 게이트로 설정.
    73	
    74	---
    75	
    76	### 3.2 R2 킥오프 전 KPI·Go/No-Go 스코어카드 동결 — Quick Win
    77	
    78	| 기준 | 등급 | 근거 |
    79	|---|---|---|
    80	| 실행 가능성 | 상 | 문서화 작업이므로 추가 인프라 불필요. Traction Technology: Go/No-Go 스코어카드 합의 및 결정 권한자 사전 지정이 모범 사례 (https://www.tractiontechnology.com/blog/how-to-run-a-successful-pilot-with-a-startup-frameworks-kpis-enterprise-best-practices) |
    81	| 영향 | 상 | KPI 미사전 정의는 Pilot Purgatory의 핵심 원인 (https://www.softwareseni.com/the-enterprise-ai-pilot-purgatory-problem-what-the-statistics-actually-tell-us/). Anthropic 공식 6개 KPI(WAU 70%·주당 메시지 25+건·만족도 4.0/5.0+·시간 절감 3시간+) 기준 제공 (https://claude.com/resources/tutorials/claude-enterprise-administrator-guide) |
    82	| 비용 | 하 | 문서 작성 및 합의 미팅 외 추가 비용 없음 (추정: 기존 회의 체계 내 처리 가능) |
    83	| 리스크 | 하 | KPI 동결 자체의 리스크는 없음. 다만 내부 정치적 합의 실패 가능성은 별도 관리 필요 (추정: 조직 내 합의 난이도는 맥락 의존) |
    84	| 시급성 | 상 | 킥오프 전에 완료해야 하며 이후 변경 시 파일럿 평가 무력화. Go/No-Go 스코어카드(기술 40%·재무 30%·시장 20%·자원 10%, 임계값 0.605) 사전 합의 (https://guides.visual-paradigm.com/making-informed-decisions-with-a-go-no-go-checklist-for-agile-projects-a-scoring-approach/) |
    85	
    86	- **2축 환산**: 실행용이성 **상** (실행 가능성 상 기준; 비용 하·리스크 하 → 하향 없음), 영향도 **상** (영향 상 기준; 시급성 상 → 상한 '상' 유지)
    87	- **첫 실행 단계**: 파일럿 착수 전 AI Board 킥오프 회의에서 ①배포 완성 건수 ②WAU 70% ③참여자 만족도 4.0/5.0+ ④사이클 타임 단축률 ⑤거버넌스 준수율 5개 KPI와 Go/No-Go 임계값(0.605)을 문서화하고 결정 권한자(named decision owner)를 지정.
    88	
    89	---
    90	
    91	### 3.3 R3 Agile-Stage-Gate 하이브리드 운영 구조 채택 — Quick Win
    92	
    93	| 기준 | 등급 | 근거 |
    94	|---|---|---|
    95	| 실행 가능성 | 상 | 기존 내부 기획안 §5 배포 게이트·격상 절차와 직접 연계 가능. Agile-Stage-Gate 게이트 결정 24~48시간 이내 목표로 속도 저해 최소화 (https://umbrex.com/resources/frameworks/strategy-frameworks/stage-gate-innovation-process/) |
    96	| 영향 | 상 | GSoC 중간 평가에서 "한계 통과" 참가자 80%+가 최종 실패 → 중간 Gate 없이는 조기 경보 불가 (https://google.github.io/gsocguides/mentor/evaluations). KPMG Belgium: 거버넌스 있는 조직 77% vs 없는 조직 39% 비용 절감 성공 (https://kpmg.com/be/en/home/insights/2024/11/ta-transforming-business-value-creation-with-citizen-development.html) |
    97	| 비용 | 하 | 기존 조직 구조(AI Board·CoE) 내 역할 정의 수준으로 처리 가능. 추가 시스템 불필요 (내부: 탑다운 기획안 §5, 내부 자료 독립 검증 불가) |
    98	| 리스크 | 하 | 구조 채택 자체의 리스크는 낮음. 게이트 경직화로 Shadow AI 촉진 가능성은 R4에서 별도 관리 (https://www.elegantsoftwaresolutions.com/blog/vibe-coding-enterprise-adoption) |
    99	| 시급성 | 상 | 킥오프 전 운영 구조 확정이 필수. 이후 변경 시 참가자 혼선 유발 |
   100	
   101	- **2축 환산**: 실행용이성 **상** (실행 가능성 상; 비용 하·리스크 하 → 하향 없음), 영향도 **상** (영향 상; 시급성 상 → 상한 '상' 유지)
   102	- **첫 실행 단계**: W1(Day 1~7): Gate 0 킥오프 체크리스트(골든 패스 완비·KPI 동결·소유권 지정) → W2(Day 8~14): 중간 Gate(조기 경보 3개 이상 과제 멘토 집중 배치) → W3(Day 15~21): Gate 2 배포 승인(3-lane 리뷰) → 배포 후 D+7 회고 구조를 운영 매뉴얼에 문서화.
   103	
   104	---
   105	
   106	### 3.4 R4 3-lane 위험 분류 기반 배포 게이트 설계 — 전략 과제
   107	
   108	| 기준 | 등급 | 근거 |
   109	|---|---|---|
   110	| 실행 가능성 | 중 | 3-lane 분류 기준 정의 및 리뷰어 로테이션 체계 설계 필요. Semgrep AI-SAST 도입 시 부분 자동화 가능 (https://semgrep.dev/blog/2025/ai-powered-detection-with-semgrep/). metacto 2026-07-08 3-lane 프레임워크 참조 가능 (https://www.metacto.com/blogs/establishing-code-review-standards-for-ai-generated-code) |
   111	| 영향 | 상 | AI 코드 취약점 밀도 2.74배(Veracode). XSS 방어 실패 85%·로그 인젝션 실패 87%(Veracode Spring 2026). rubber-stamping: 승인율 +14.5%p·코멘트 -22% 실증(arXiv 2606.22721) (https://arxiv.org/pdf/2606.22721, https://www.veracode.com/blog/spring-2026-genai-code-security/) |
   112	| 비용 | 중 | 리뷰어 3인 체계(Red lane) 운영 공수 발생. SLA 차등화(피어 리뷰 4h, 아키텍처 리뷰 24h) 관리 필요 (https://gotranscript.com/en/blog/turnaround-time-vs-quality-set-slas-without-increasing-risk) |
   113	| 리스크 | 상 | 복잡한 승인 프로세스가 Shadow AI 사용을 촉진할 수 있다는 역설 존재 (https://www.elegantsoftwaresolutions.com/blog/vibe-coding-enterprise-adoption). 3-lane × 3인 리뷰가 3주 타임박스 안에서 소화 가능한지 실증 데이터 없음 (04 §4 미해결 쟁점 4) |
   114	| 시급성 | 상 | Gate 2(W3 배포 승인) 전에 체계가 완비되어야 하며, 보안 게이트 없이 배포 시 취약점 리스크 즉시 현실화 |
   115	
   116	- **2축 환산**: 실행용이성 **하** (실행 가능성 중 기준; 리스크 상 → 한 단계 하향 → 하), 영향도 **상** (영향 상; 시급성 상 → 상한 '상' 유지) → **전략 과제** (실행용이성 하 × 영향도 상)
   117	- **첫 실행 단계**: 킥오프 4주 전까지 Green(내부 UI·문서·테스트)/Yellow(비즈니스 로직·API)/Red(Auth·PII·인프라) 3-lane 분류 기준표 작성. Red lane 리뷰어 풀 최소 6명 확보(로테이션 고려). 서면 정당화 양식 및 rubber-stamping 모니터링 지표(승인 소요 시간·코멘트 수) 사전 정의.
   118	
   119	---
   120	
   121	### 3.5 R5 CoE 선행 구축 + 초기 고밀도 멘토링 (co-dev 50%) — 전략 과제
   122	
   123	| 기준 | 등급 | 근거 |
   124	|---|---|---|
   125	| 실행 가능성 | 중 | CoE 2~5명 선발 및 역할 정의 필요. H&M 4명 CoE로 1,500개 앱 지원(Microsoft Power Platform Blog)이 가능성을 보여주나 파일럿 특화 초기 고밀도 설계 필요 (https://www.microsoft.com/en-us/power-platform/blog/power-apps/hmgroup/) |
   126	| 영향 | 상 | KPMG Belgium: 거버넌스 있는 조직 77% vs 없는 조직 39% (https://kpmg.com/be/en/home/insights/2024/11/ta-transforming-business-value-creation-with-citizen-development.html). BCG 10-20-70: AI 성공의 70%는 사람·프로세스·문화 (https://www.forbes.com/sites/joemckendrick/2026/01/26/why-ais-10-20-70-principle-should-matter-to-ceos-and-everyone-else/) |
   127	| 비용 | 상 | CoE 인력 사전 배치 + 초기 50% co-development 비율은 상당한 멘토 투입 공수를 의미. GSoC 멘토:참가자 1.64:1(역방향), Meta 1:2~3 참조 (https://opensource.googleblog.com/2025/08/google-summer-of-code-2025-contributor-statistics.html) |
   128	| 리스크 | 중 | "CoE 2~5인으로 모든 PR 심층 리뷰는 물리적으로 불가"(Checkmarx 2025). 보안 훈련만으로 시티즌 개발자 보안 문제를 해결하지 못함(TechNewsWorld) (https://checkmarx.com/blog/ai-is-writing-your-code-whos-keeping-it-secure/) |
   129	| 시급성 | 상 | 킥오프 전 CoE 완편이 필수. 파일럿 중 구성하면 프레임워크 공백 발생 |
   130	
   131	- **2축 환산**: 실행용이성 **하** (실행 가능성 중 기준; 비용 상 → 한 단계 하향 → 하), 영향도 **상** (영향 상; 시급성 상 → 상한 '상' 유지) → **전략 과제** (실행용이성 하 × 영향도 상)
   132	- **첫 실행 단계**: 파일럿 킥오프 D-28일 이전에 CoE 2~5명(프로그램 프레임워크·과제 검토·챔피언 운영·비즈니스+기술 2단계 과제 검토 담당)을 확정. 초기 2주(W1·W2) co-development 비율을 50%로 설정하고 W3부터 단계적 감소 계획 수립.
   133	
   134	---
   135	
   136	### 3.6 R6 챔피언 프로그램 + 3단계 체크인 구조 도입 — 선택 과제
   137	
   138	| 기준 | 등급 | 근거 |
   139	|---|---|---|
   140	| 실행 가능성 | 상 | Anthropic 공식 Champion Kit 활용 가능(챔피언 주 40분 예산·30일 4주 플레이북·3원칙 share/ask/circle). 추가 도구 없이 기존 커뮤니케이션 채널로 운영 가능 (https://code.claude.com/docs/en/champion-kit) |
   141	| 영향 | 중 | 챔피언 2.1배 지속 사용률(Worklytics via AI Assembly Lines)·채택률 62→85%(Adoptify.ai)는 단일 출처이며 독립 검증 없어 신뢰도 중간 (https://aiassemblylines.com/post/ai-champions-program-enterprise-adoption). 에이전틱 도구 10주 지속 사용률 <10%(DORA 2025) — 챔피언 없이는 효과 소멸 (https://jellyfish.co/blog/2025-dora-report/) |
   142	| 비용 | 중 | 챔피언 1인당 주 40분 예산. 25~50명당 1명 배치(Anthropic Cowork). 3단계 체크인(30~60일 오피스아워·3개월 회고·분기 비즈니스 리뷰) 운영 공수 (https://claude.com/resources/tutorials/scaling-workflows-with-claude-cowork-at-your-organization) |
   143	| 리스크 | 하 | 챔피언 프로그램 자체의 리스크는 낮음. Worklytics·Adoptify.ai 수치 독립 검증 부재가 투자 판단 불확실성 유발 (04 §4 미해결 쟁점 5) |
   144	| 시급성 | 중 | 파일럿 기간 내보다는 이후 지속 사용 정착이 목적. 파일럿 W3 종료 전 챔피언 지정 필요 |
   145	
   146	- **2축 환산**: 실행용이성 **상** (실행 가능성 상; 비용 중·리스크 하 → 하향 없음), 영향도 **중** (영향 중; 시급성 중 → 상향 없음) → **선택 과제** (실행용이성 상 × 영향도 중)
   147	- **첫 실행 단계**: W2 종료 전(Day 14)까지 파일럿 참가 그룹에서 챔피언 후보를 1명 이상 지정. Anthropic Champion Kit 플레이북(30일 4주)을 파일럿 종료 후 즉시 시작하도록 일정 수립.
   148	
   149	---
   150	
   151	### 3.7 R7 자동 Frozen + 보드 심의 하이브리드 종료 설계 — 선택 과제
   152	
   153	| 기준 | 등급 | 근거 |
   154	|---|---|---|
   155	| 실행 가능성 | 상 | AWS Innovation Sandbox 자동 Frozen 기능 활용 가능(Entry→Frozen→CleanUp 상태머신). 내부 기획안 보드 심의 원칙과 통합 가능 (https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/account-lifecycle-in-isb.html, 내부: 탑다운 기획안 §7, 내부 자료 독립 검증 불가) |
   156	| 영향 | 중 | 소유권 공백이 파일럿-프로덕션 전환 최대 장애(SoftwareSeni). 자동 Frozen으로 비용 통제, 보드 심의로 사업 판단 병행 (https://www.softwareseni.com/the-enterprise-ai-pilot-purgatory-problem-what-the-statistics-actually-tell-us/) |
   157	| 비용 | 하 | AWS 기존 Innovation Sandbox 기능 활용. 보드 심의는 기존 AI Board 체계 내 처리 가능 (내부: 탑다운 기획안 §7, 내부 자료 독립 검증 불가) |
   158	| 리스크 | 중 | AI 생성 코드의 기술 부채 이관 기준 미정의로 이관팀 거부 가능성 존재 (04 §4 미해결 쟁점 2). 이관 거부 시 Pilot Purgatory 재현 위험 |
   159	| 시급성 | 중 | W3 종료 전 출구 경로(이관/폐기/현업복귀) 및 Go/No-Go 임계값 사전 합의 필요 |
   160	
   161	- **2축 환산**: 실행용이성 **상** (실행 가능성 상; 비용 하·리스크 중 → 하향 없음), 영향도 **중** (영향 중; 시급성 중 → 상향 없음) → **선택 과제** (실행용이성 상 × 영향도 중)
   162	- **첫 실행 단계**: 파일럿 착수 전 AWS Innovation Sandbox 비용 임계값(자동 Frozen 트리거) 설정. 3방향 출구(이관/폐기/현업복귀) 판단 기준과 보드 심의 일정을 파일럿 킥오프 문서에 명시. 종료 시 클로저 레코드(15~20분, 4개 항목) 양식 사전 준비.
   163	
   164	---
   165	
   166	### 3.8 R8 보안 통제 기술 내재화 (SAST·골든 패스 임베딩) — 전략 과제
   167	
   168	| 기준 | 등급 | 근거 |
   169	|---|---|---|
   170	| 실행 가능성 | 중 | Semgrep AI-SAST 도입으로 IDOR·인가 오류 부분 자동화 가능(완전 대체 불가). CI/CD 파이프라인 내 SAST·lint 임베딩은 기술적으로 표준 방식 (https://semgrep.dev/blog/2025/ai-powered-detection-with-semgrep/) |
   171	| 영향 | 상 | CI/CD 자동검사만으로는 아키텍처·로직 결함 탐지 불가(Checkmarx 2025). AI 코드 취약점 밀도 2.74배(Veracode). 보안 교육만으로 해결 불가—"규모·속도·다양성이 교육 한계 초과"(TechNewsWorld) (https://checkmarx.com/blog/ai-is-writing-your-code-whos-keeping-it-secure/, https://www.flosum.com/blog/the-unintended-security-threat-of-citizen-development) |
   172	| 비용 | 중 | Semgrep 라이선스 비용 + CI/CD 파이프라인 통합 공수 발생. 골든 패스 내장 정책 설계 추가 공수 |
   173	| 리스크 | 중 | Semgrep AI-SAST가 아키텍처·로직 결함을 탐지하지 못하므로 "보안 완료"로 오인할 위험. 수동 게이트(R4)와 병행 필수 |
   174	| 시급성 | 상 | 골든 패스 완비(R1)와 동시에 구축해야 하므로 파일럿 킥오프 전 완료 필요 |
   175	
   176	- **2축 환산**: 실행용이성 **중** (실행 가능성 중; 비용 중·리스크 중 → 추가 하향 없음 — 둘 다 '상'이 아니므로 하향 조건 미충족), 영향도 **상** (영향 상; 시급성 상 → 상한 '상' 유지) → **전략 과제** (실행용이성 중 × 영향도 상)
   177	- **첫 실행 단계**: R1 골든 패스 템플릿 내에 Semgrep SAST·의존성 취약점 스캔·시크릿 스캔을 CI/CD 단계로 내장. 보안 정책 위반 시 자동 빌드 실패 설정. CoE 전수 PR 리뷰 의존에서 "기술 차단선 → CoE 예외 처리"로 역할 재정의.
   178	
   179	---
   180	
   181	## 4. 조건부 권고·추가 조사 항목
   182	
   183	> 04-convergence.md §4 미해결 쟁점·리스크 매핑
   184	
   185	| 항목 | 유형 | 전제 조건 / 조사 질문 | 근거 (04 §4 항목) |
   186	|---|---|---|---|
   187	| 파일럿 코호트 규모 정의 | 조건부 권고 | 비전문 시티즌 개발자 특화 벤치마크 부재로 현재 판정 불가(미해결). 조건부 승격 조건: ① 내부 목적 정의(AI 도구 채택 확산 vs 탑다운 과제 완성) + ② 파일럿 드라이런 또는 사내 벤치마크 수립 후 실증 확보. 이 절차 완료 후 권고로 승격 가능. 참고 수치 50~100명(채택 확산) / 3~5명(과제 완성)는 1차 가설값이며 내부 재검증 필요 | 04 §4 미해결 쟁점 1 |
   188	| AI 생성 코드 이관 기술 부채 수용 기준 수립 | 조건부 권고 | 이관팀과 파일럿 종료 전(W3 D+7 회고 시점)까지 기술 부채 수용 조건(코드 중복 허용 임계값·리팩토링 의무 범위)을 사전 합의하면, 자동 이관 원칙으로 승격 가능 | 04 §4 미해결 쟁점 2 |
   189	| 시티즌 개발자 3주 배포 완성 실증 데이터 확보 | 추가 조사 | 비전문 개발자가 골든 패스 + AI 코딩 도구 조합으로 3주 내 운영환경 배포를 완성한 사례의 배포 완성률·실패율 벤치마크가 존재하는가? 국내외 사내 해커톤·부트캠프 운영 기관(NIPA·AWS·MS) 사례 조사 필요 | 04 §4 미해결 쟁점 3 |
   190	| 3-lane 리뷰 3주 타임박스 적용 가능성 검증 | 추가 조사 | Red lane 3인 승인 체계가 3주 스프린트 안에서 실제로 소화 가능한지, 상시 개발 조직 사례가 아닌 단기 파일럿 조직 기준 SLA 데이터가 존재하는가? 사내 파일럿 드라이런(dry-run) 1회 시뮬레이션으로 측정 가능 | 04 §4 미해결 쟁점 4 |
   191	| 챔피언 프로그램 정량 효과 독립 검증 | 추가 조사 | Worklytics "2.1배 지속 사용률"·Adoptify.ai "62→85%" 수치를 동료 검토 연구 또는 사내 파일럿 후 측정값으로 검증 가능한가? 파일럿 종료 후 90일 WAU 추적으로 내부 기준값 수립 가능 | 04 §4 미해결 쟁점 5 |
   192	| 복잡한 게이트 → Shadow AI 역설 임계점 파악 | 추가 조사 | 게이트 복잡도와 Shadow AI 발생률 간 임계점 데이터가 존재하는가? 파일럿 기간 중 비공식 AI 도구 사용 현황 모니터링 지표를 설계하여 추적 필요 | 04 §4 미해결 쟁점 6 |
   193	
   194	---
   195	
   196	## 5. 검증 이력
   197	
   198	| Layer | 결과 |
   199	|---|---|
   200	| Layer 1 — URL 검증 | (검증 대기) |
   201	| Layer 2 — Critic 비평 | (검증 대기) |
   202	| Layer 3 — Codex 교차 검증 | (검증 대기) |
   203	| 출구 게이트 | (승인 대기) |
   204	
   205	---
   206	
   207	## 6. Sources
   208	
   209	- https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/ (Fortune / MIT NANDA, 2025-08-18)
   210	- https://fluidlabs.com/resources/why-42-percent-enterprise-ai-abandoned-2025 (Fluidlabs / S&P Global, 2025)
   211	- https://www.softwareseni.com/the-enterprise-ai-pilot-purgatory-problem-what-the-statistics-actually-tell-us/ (SoftwareSeni, 날짜 미상)
   212	- https://www.forbes.com/sites/joemckendrick/2026/01/26/why-ais-10-20-70-principle-should-matter-to-ceos-and-everyone-else/ (Forbes / BCG, 2026-01-26)
   213	- https://www.veracode.com/blog/spring-2026-genai-code-security/ (Veracode Spring 2026 GenAI Code Security Report, 2026-04)
   214	- https://arxiv.org/pdf/2606.22721 (arXiv: Habituation at the Gate, 2026-06-23)
   215	- https://www.metacto.com/blogs/establishing-code-review-standards-for-ai-generated-code (metacto, 2026-07-08)
   216	- https://checkmarx.com/blog/ai-is-writing-your-code-whos-keeping-it-secure/ (Checkmarx, 2025)
   217	- https://www.pixelmojo.io/blogs/vibe-coding-technical-debt-crisis-2026-2027 (Pixelmojo, 2026)
   218	- https://devops.com/ai-in-software-development-productivity-at-the-cost-of-code-quality-2/ (DevOps.com / Google DORA 2024, 2025)
   219	- https://google.github.io/gsocguides/mentor/evaluations (GSoC Evaluations Guide, 2025)
   220	- https://opensource.googleblog.com/2025/08/google-summer-of-code-2025-contributor-statistics.html (GSoC 2025 Statistics, 2025-08)
   221	- https://www.samsung.com/sec/sustainability/popup/popup_doc/AYUBw0_6ArQAIx8i/ (Samsung C-Lab Sustainability, 2025)
   222	- https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025 (DORA 2025 / Faros.ai, 2025-09)
   223	- https://dora.dev/insights/balancing-ai-tensions/ (DORA Insights, 2025)
   224	- https://systemprompt.io/guides/claude-code-organisation-rollout (systemprompt.io Claude Code Rollout Playbook, 날짜 미상)
   225	- https://claude.com/resources/tutorials/claude-enterprise-administrator-guide (Claude Enterprise Administrator Guide, 날짜 미상)
   226	- https://claude.com/resources/tutorials/scaling-workflows-with-claude-cowork-at-your-organization (Scaling workflows with Claude Cowork, 날짜 미상)
   227	- https://code.claude.com/docs/en/champion-kit (Claude Code Champion Kit, 날짜 미상)
   228	- https://aiassemblylines.com/post/ai-champions-program-enterprise-adoption (AI Assembly Lines, 2026)
   229	- https://jellyfish.co/blog/2025-dora-report/ (Jellyfish DORA 2025, 2025)
   230	- https://platformengineering.com/features/dora-2025-ai-wont-save-you-without-a-solid-platform/ (Platform Engineering / DORA 2025, 2025)
   231	- https://platformengineering.org/blog/how-to-set-up-an-internal-developer-platform (platformengineering.org, 날짜 미상)
   232	- https://www.thecloudplaybook.com/p/first-6-golden-paths-aws-platform-teams (The Cloud Playbook TCP#124, 날짜 미상)
   233	- https://tasrieit.com/blog/golden-paths-platform-engineering-guide-2026 (Tasrie IT, 2026-01)
   234	- https://backstage.spotify.com/discover/blog/how-we-measure-backstage-success-at-spotify (Spotify Backstage, 2020~)
   235	- https://kpmg.com/be/en/home/insights/2024/11/ta-transforming-business-value-creation-with-citizen-development.html (KPMG Belgium, 2024-11)
   236	- https://kissflow.com/no-code/citizen-developer-program/ (Kissflow, 날짜 미상)
   237	- https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap-mentoring-and-user-enablement (Microsoft Learn, 2024-12-30)
   238	- https://www.microsoft.com/en-us/power-platform/blog/power-apps/hmgroup/ (Microsoft Power Platform Blog / H&M, 날짜 미상)
   239	- https://www.tractiontechnology.com/blog/how-to-run-a-successful-pilot-with-a-startup-frameworks-kpis-enterprise-best-practices (Traction Technology, 날짜 미상)
   240	- https://guides.visual-paradigm.com/making-informed-decisions-with-a-go-no-go-checklist-for-agile-projects-a-scoring-approach/ (Visual Paradigm, 날짜 미상)

exec
/bin/zsh -lc "nl -ba /Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/04-convergence.md | sed -n '1,240p'" in /Users/jaybee/lab/AIFAB-plan
 succeeded in 0ms:
     1	# 수렴 보고서 — AI FAB 탑다운 과제 파일럿 운영 방안: 시티즌 개발자 선발부터 3주 스프린트 배포·종료까지 운영 시나리오
     2	
     3	> 생성: 2026-07-11 | 메타서치 단계 4 산출물 | 입력: 02-deep-research.md + 03-divergence/*.md (d1~d5, deepdive 3종)
     4	
     5	---
     6	
     7	## 1. 수렴 개요
     8	
     9	02(씨앗)는 선발→3주 스프린트→게이트→종료의 4단계 흐름을 긍정적으로 설계했으며, 외부 모범 사례(CoE·Agile-Stage-Gate·KPI 사전 동결)와 내부 기획안(배포 게이트·격상 절차·리소스 회수)의 역할을 분리하는 틀을 제시했다.
    10	
    11	d1(실패 사례)은 GenAI 파일럿 88~95% 실패, Pilot Purgatory, 소유권 공백, AI 코딩 도구의 기술 부채·배포 안정성 역효과로 씨앗의 낙관론을 강하게 상충했다. d2(비판 관점)는 CI/CD 자동 검사가 아키텍처·로직 결함을 차단하지 못하며 수동 승인 게이트에 rubber-stamping 패턴이 존재함을 실증했다. d2-dd(게이트 deepdive)는 3-lane 리스크 기반 리뷰·SLA 차등화·rubber-stamping 방지 장치 등 씨앗에 없는 게이트 설계 원칙을 신규 제공했다.
    12	
    13	d3(인접 프로그램)은 3주 배포 완성 선행 사례가 없음을 확인하면서도 GSoC 커뮤니티 본딩·메타 부트캠프·사내벤처 이중 출구 구조 등 운영 설계 참고점을 제공했다. d4(에이전틱 동향)는 에이전틱 도구 10주 지속 사용률 10% 미만, 복잡한 게이트가 Shadow AI를 촉진한다는 역설을 상충으로 제기했다. d4-dd(Anthropic deepdive)는 공식 Champion Kit·6개 KPI·챔피언 비율 등 씨앗의 지원 체계를 구체화했다. d5(골든 패스)는 "AI는 증폭기, 강한 플랫폼 없이는 안정성 저하"를 확인하며 사전 골든 패스 준비가 3주 배포의 현실적 전제임을 밝혔다. d5-dd(골든 패스 deepdive)는 IDP 정석 16주 vs. 3주 파일럿의 긴장을 구체 수치로 드러냈다.
    14	
    15	총 6개 쟁점이 판정되었고(근거 우세 측 채택 4개·조건부 수렴 2개), 3개 쟁점은 현재 증거로 판정 불가하여 "미해결"로 표기했다.
    16	
    17	---
    18	
    19	## 2. 쟁점별 수렴 결과
    20	
    21	### 2.1 3주 스프린트로 배포까지 완성이 현실적인가
    22	
    23	| 구분 | 내용 | 출처 |
    24	|---|---|---|
    25	| 일치 증거 | AI 코딩 도구 활용 시 개발 속도 5~10배 향상 주장(Quixy 2024), CJ올리브영 5배 속도·3일 프로토타입(AWS 기술 블로그), Amazon Prime Video 10일·전문 개발자 6명·90주→24주 단축(AWS Korea Blog) | [Quixy](https://quixy.com/blog/citizen-development-kpis-and-roi/), [AWS 기술 블로그](https://aws.amazon.com/ko/blogs/tech/cj-oliveyoung-aidlc-tech-blog/), [AWS Korea Blog](https://aws.amazon.com/ko/blogs/korea/how-frontier-teams-are-reinventing-ai-native-development/) |
    26	| 상충 증거 (A) | GenAI 파일럿 88~95% P&L 기여 없음(MIT NANDA·IDC), 기업 AI 이니셔티브 포기율 42%(S&P Global 2025), 인접 도메인 선행 사례(비전문 시티즌 개발자 3주 배포 완성)가 조사 범위 내 미발견 | [MIT NANDA via Fortune](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/), [S&P Global via Fluidlabs](https://fluidlabs.com/resources/why-42-percent-enterprise-ai-abandoned-2025), [GSoC Evaluations Guide](https://google.github.io/gsocguides/mentor/evaluations), [AngelHack](https://angelhack.com/blog/ai-internal-hackathon/) |
    27	| 상충 증거 (B) | DORA 2025 "AI는 증폭기—강한 플랫폼 없이 AI 단독 도입은 안정성 저하"; IDP MVP 정석 16주(8+8), 카탈로그 위생 없이 AI 도입 시 변경 실패율 +30% | [DORA 2025 via platformengineering.com](https://platformengineering.com/features/dora-2025-ai-wont-save-you-without-a-solid-platform/), [platformengineering.org](https://platformengineering.org/blog/how-to-set-up-an-internal-developer-platform), [Cortex 2025 via Medium AI Transfer Lab](https://medium.com/@ai_transfer_lab/internal-developer-platforms-in-the-mcp-era-how-idp-teams-are-embedding-claude-as-a-list-class-846abc073117 ⚠(dead link)) |
    28	| **판정** | **조건부 가능** — 사전 골든 패스(AWS 6대 템플릿) + CoE 병행 + 소유권 단일 책임자가 전제되어야만 현실성 확보. 전제 없이 "AI 도구만으로 3주 배포"는 실패 가능성이 압도적으로 높음. 인접 도메인 선행 사례가 없어 낙관적 ROI 수치를 그대로 채택하기 어려움. | - |
    29	
    30	### 2.2 파일럿 코호트 규모
    31	
    32	| 구분 | 내용 | 출처 |
    33	|---|---|---|
    34	| 일치 증거 | Kissflow·Innovation Mode 기준 파일럿은 2~3개 부서·팀당 3~5명. AI 코딩 도구 파일럿 20~30명 권고(IntuitionLabs) | [Kissflow](https://kissflow.com/no-code/citizen-developer-program/), [Innovation Mode](https://theinnovationmode.com/corporate-hackathon-template), [IntuitionLabs](https://intuitionlabs.ai/articles/claude-enterprise-deployment-training-guide-2026) |
    35	| 상충 증거 | Anthropic 공식 Enterprise Administrator Guide: 파일럿 50~100명(SCIM 초기 그룹), 2~4주; systemprompt.io: 초기 3~5명 후 10~20명 확대; Anthropic Cowork 튜토리얼: 4단계 3~5→10~20→30~60→50~200+명 | [Claude Enterprise Administrator Guide](https://claude.com/resources/tutorials/claude-enterprise-administrator-guide), [systemprompt.io](https://systemprompt.io/guides/claude-code-organisation-rollout) |
    36	| **판정** | **미해결** — Anthropic 공식(50~100명)·서드파티 가이드(3~5명 초기)·씨앗(20~30명)이 모두 다르며, 이는 대상(전문 개발자 vs 시티즌 개발자)·목적(AI 코딩 도구 확산 vs 탑다운 과제 파일럿)의 차이에서 기인한다. 비전문 시티즌 개발자 특화 AI 코딩 파일럿 규모 벤치마크 1차 출처가 없어 판정 불가. 단, d5 골든 패스 가이드 "초기 2~3개 자발 팀"은 팀 수 기준으로 규모 억제를 지지한다. | - |
    37	
    38	### 2.3 게이트 설계의 실효성
    39	
    40	| 구분 | 내용 | 출처 |
    41	|---|---|---|
    42	| 일치 증거 | 수동 승인 게이트 필요성 자체: IT 리더 73%(데이터 무결성 우려)·69%(보안 취약점 우려), 거버넌스 있는 조직 77% vs 없는 조직 39% 비용 절감 성공(KPMG Belgium 2024). AI 코드 취약점 밀도 2.74배 | [Flosum](https://www.flosum.com/blog/the-unintended-security-threat-of-citizen-development), [KPMG Belgium](https://kpmg.com/be/en/home/insights/2024/11/ta-transforming-business-value-creation-with-citizen-development.html), [Veracode 2025](https://www.veracode.com/blog/spring-2026-genai-code-security/) |
    43	| 상충 증거 (A) | CI/CD 자동검사는 아키텍처·로직 결함 탐지 불가(Checkmarx 2025). AI 코드에 XSS 방어 실패 85%·로그 인젝션 실패 87%(Veracode Spring 2026). AI 코드 승인율 +14.5%p·코멘트 -22%로 rubber-stamping 실증(arXiv 2606.22721). Copilot PR 리뷰 시간 17.2시간(인간 3.9시간 대비 4.4배) | [Checkmarx](https://checkmarx.com/blog/ai-is-writing-your-code-whos-keeping-it-secure/), [Veracode Spring 2026](https://www.veracode.com/blog/spring-2026-genai-code-security/), [arXiv 2606.22721](https://arxiv.org/pdf/2606.22721), [Codacy Blog](https://blog.codacy.com/ai-breaking-code-review-how-engineering-teams-survive-pr-bottleneck) |
    44	| 상충 증거 (B) | "복잡한 승인 프로세스가 Shadow AI 사용을 촉진"한다는 역설 — 도구 기준 게이트 대신 위험 기준(색상 분류) 게이트 권고 | [Elegant Software Solutions](https://www.elegantsoftwaresolutions.com/blog/vibe-coding-enterprise-adoption) |
    45	| 대안 증거 | 3-lane 리스크 기반 리뷰(Green/Yellow/Red), Red에 3인 승인 필수(metacto 2026-07-08). Semgrep AI-Powered Detection으로 IDOR·인가 오류 부분 자동화 가능. Rubber-stamping 방지 3장치(서면 정당화·분산 배치·로테이션). 리스크 계층별 SLA 차등화(피어 리뷰 4h, 아키텍처 리뷰 24h) | [metacto](https://www.metacto.com/blogs/establishing-code-review-standards-for-ai-generated-code), [Semgrep](https://semgrep.dev/blog/2025/ai-powered-detection-with-semgrep/), [GoTranscript](https://gotranscript.com/en/blog/turnaround-time-vs-quality-set-slas-without-increasing-risk) |
    46	| **판정** | **조건부 수렴** — 씨앗의 "CI/CD 자동검사 + AI Board·정보보호팀 수동 승인" 2단 게이트만으로는 불충분. 실효성 확보를 위해 (1) 3-lane 위험 분류, (2) Red lane 3인 승인, (3) rubber-stamping 방지 장치(서면 정당화·로테이션), (4) SLA 차등화를 추가 설계해야 함. Shadow AI 유발 역설을 방지하기 위해 게이트는 위험 기준으로 설계한다. Semgrep AI-SAST는 보조 수단(완전 대체 불가). | - |
    47	
    48	### 2.4 AI 코딩 도구의 효과 — ROI vs 역효과
    49	
    50	| 구분 | 내용 | 출처 |
    51	|---|---|---|
    52	| 일치 증거 | 건강한 ROI 범위 2.5~3.5배(평균), 상위 25% 조직 4~6배(Exceeds.ai 2025). 개인 작업 ~21% 증가(Index.dev 2025). PR 병합 +98%(DORA 2025). IBM 45% 생산성 향상(공식 뉴스룸, 6,000명 전문 개발자) | [Exceeds.ai](https://blog.exceeds.ai/enterprise-ai-adoption-metrics-2025/), [Index.dev](https://www.index.dev/blog/ai-coding-assistants-roi-productivity), [IBM Newsroom](https://newsroom.ibm.com/2025-10-07-2025-ibm-and-anthropic-partner-to-advance-enterprise-software-development-with-proven-security-and-governance) |
    53	| 상충 증거 | 배포 안정성 -7.2%(DORA 2024). 기술 부채 30~41% 증가(8.1M PR 분석, Pixelmojo 2026). 코드 중복 8배·리팩토링 -60%(GitClear, 211M 라인, 2025-02). 에이전틱 도구 10주 지속 사용률 <10%(DORA 2025, 5,000명 응답). DORA "AI는 증폭기—강한 팀은 더 강해지고 취약 팀은 문제만 커진다" | [Google DORA 2024 via DevOps.com](https://devops.com/ai-in-software-development-productivity-at-the-cost-of-code-quality-2/), [Pixelmojo](https://www.pixelmojo.io/blogs/vibe-coding-technical-debt-crisis-2026-2027), [GitClear](https://www.gitclear.com/ai_assistant_code_quality_2025_research ⚠(dead link)), [Jellyfish DORA 2025](https://jellyfish.co/blog/2025-dora-report/) |
    54	| **판정** | **조건부 보강** — ROI 수치는 개인 생산성(단기) 기준이며 조직 안정성·장기 유지보수성 관점에서는 역효과가 실증됨. "AI는 증폭기" 명제 수렴: 골든 패스·CoE·거버넌스가 강한 조직에서는 ROI 실현, 약한 조직에서는 부채·취약점 축적. 파일럿 ROI는 구조적으로 운영 ROI를 과대평가(위험 조정 ROI 재계산 필수). 시티즌 개발자 특화 ROI 데이터는 없으며 전문 개발자 수치를 그대로 적용 불가. | - |
    55	
    56	### 2.5 종료·이관 방식 — 자동 선셋 vs 보드 심의
    57	
    58	| 구분 | 내용 | 출처 |
    59	|---|---|---|
    60	| 일치 증거 | 파일럿 시작 전 Go/No-Go 스코어카드 합의 필수(Traction Technology). 결정 권한자(named decision owner) 사전 지정(Traction Technology). AWS Innovation Sandbox 계정 라이프사이클 자동화(Entry→Frozen→CleanUp 상태머신) | [Traction Technology](https://www.tractiontechnology.com/blog/how-to-run-a-successful-pilot-with-a-startup-frameworks-kpis-enterprise-best-practices), [AWS Docs Innovation Sandbox](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/account-lifecycle-in-isb.html) |
    61	| 상충 증거 | 외부 사례: AWS Innovation Sandbox Frozen 후 14일 자동 접근 회수·21일 자동 리소스 삭제. 내부 기획안: "자동 선셋 미적용, 사업 판단(보드 심의)으로 결정" 원칙 (내부: AWS_기반_탑다운_AIFAB_과제_운영환경_구축운영_기획안_v1-0.md §7) (내부 자료, 독립 검증 불가) | [AWS Docs Innovation Sandbox](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/account-lifecycle-in-isb.html), (내부: 탑다운 기획안 §7) |
    62	| 신규 증거 | d3 인접 프로그램의 3방향 출구(Scale/Stop/Redirect → 이관/폐기/현업복귀) 설계. 삼성 C-Lab "1년+스핀오프 3개월" 이중 출구. SK하이닉스 HiGarage "창업/사내 사업화" 이중 출구 | [Samsung Sustainability](https://www.samsung.com/sec/sustainability/popup/popup_doc/AYUBw0_6ArQAIx8i/), [디일렉 SK하이닉스](https://www.thelec.kr/news/articleView.html?idxno=614 ⚠(dead link)) |
    63	| **판정** | **하이브리드 채택** — 자동 Frozen(비용 임계값 초과 시 접근 차단)은 AWS 자동화로 적용하되, 최종 리소스 삭제·계정 폐쇄는 보드 심의로 결정한다. 이는 내부 기획안 원칙(보드 심의)을 존중하되 비용 통제(자동 Frozen)를 병행하는 절충안으로, 양쪽 증거를 모순 없이 수용한다. 종료 출구는 이관/폐기/현업복귀 3방향으로 설계한다. | - |
    64	
    65	### 2.6 지속 사용 정착 — 챔피언 프로그램 vs 자연 이탈
    66	
    67	| 구분 | 내용 | 출처 |
    68	|---|---|---|
    69	| 일치 증거 | 에이전틱 도구 10주 지속 사용률 <10%(DORA 2025, 5,000명). 지속 사용 정착이 핵심 과제임을 다수 출처 확인 | [DORA 2025 via Jellyfish](https://jellyfish.co/blog/2025-dora-report/), [DORA 2025 via Faros.ai](https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025) |
    70	| 상충 증거 | 챔피언 프로그램의 정량 효과: 하향식 대비 2.1배 지속 사용률(Worklytics via aiassemblylines.com 2026), 챔피언 시연 시 채택률 62%→85%(Adoptify.ai), 90일 WAU 47% 달성 | [AI Assembly Lines](https://aiassemblylines.com/post/ai-champions-program-enterprise-adoption) |
    71	| 신규 증거 | Anthropic 공식 Champion Kit: 챔피언 주 40분 예산·30일 4주 플레이북·3원칙(share/ask/circle). 챔피언 비율 25~50명당 1명(Cowork). 3단계 체크인(30~60일 주간 오피스아워 → 3개월 회고 → 분기 비즈니스 리뷰). CHI 2026 행동 설계 4원칙 | [Claude Code Champion Kit](https://code.claude.com/docs/en/champion-kit), [Scaling Claude Cowork](https://claude.com/resources/tutorials/scaling-workflows-with-claude-cowork-at-your-organization), [CHI 2026](https://dl.acm.org/doi/full/10.1145/3772363.3799043 ⚠(dead link)) |
    72	| **판정** | **챔피언 프로그램 채택** — 10% 미만 자연 지속 사용률은 구조적 개입 없이는 파일럿 효과가 소멸함을 의미한다. 챔피언 2.1배 효과(Worklytics)·62→85% 채택률(Adoptify.ai)은 단일 출처이며 독립 검증이 없어 신뢰도는 중간 수준이나, Anthropic 공식 설계와 방향이 일치한다. 챔피언 프로그램 + 3단계 체크인 구조를 채택한다. 단, Worklytics·Adoptify.ai 수치는 "내부 자료 수준" 신뢰도로 취급하며 독립 검증이 필요하다. | - |
    73	
    74	### 2.7 골든 패스 사전 준비의 필수성
    75	
    76	| 구분 | 내용 | 출처 |
    77	|---|---|---|
    78	| 일치 증거 | DORA 2025 "플랫폼 없이 AI 단독 도입=안정성 저하". 골든 패스 MVP 목표 제로→스테이징 배포 <1시간(Tasrie IT 2026). IDP 도입 후 온보딩 30~60% 단축 | [DORA 2025 via platformengineering.com](https://platformengineering.com/features/dora-2025-ai-wont-save-you-without-a-solid-platform/), [Tasrie IT](https://tasrieit.com/blog/golden-paths-platform-engineering-guide-2026) |
    79	| 상충 증거 | IDP 정석 MVP 16주(8+8) vs 3주 파일럿의 시간 긴장. 카탈로그 위생 없이 AI 도입 시 변경 실패율 +30%·PR당 인시던트 +23.5%(Cortex 2025). 골든 패스 문헌은 전문 개발자 대상이며 시티즌 개발자 특화 사례 미발견 | [platformengineering.org](https://platformengineering.org/blog/how-to-set-up-an-internal-developer-platform), [Cortex 2025 via Medium AI Transfer Lab](https://medium.com/@ai_transfer_lab/internal-developer-platforms-in-the-mcp-era-how-idp-teams-are-embedding-claude-as-a-first-class-846abc073117 ⚠(dead link)) |
    80	| **판정** | **필수 전제 채택** — 3주 파일럿에서 배포 완성이 가능하려면 골든 패스(AWS 6대 템플릿: ECS on Fargate·Lambda·RDS·비용태그·관측성·Secrets Manager)가 파일럿 킥오프 전에 완비되어야 한다. IDP 정석 16주와 3주 파일럿의 긴장은 "파일럿 이전 선행 준비 기간"으로 해소한다. 카탈로그 정확도가 낮으면 AI 도입 자체가 리스크를 높이므로 사전 위생 점검이 필수다. | - |
    81	
    82	### 2.8 멘토·CoE 체계의 규모와 실효성
    83	
    84	| 구분 | 내용 | 출처 |
    85	|---|---|---|
    86	| 일치 증거 | CoE 2~5명 구성이 업계 표준(Kissflow·ISG·d2-dd). H&M 4명으로 1,500개 앱·30,000명 지원(Microsoft Power Platform Blog). Co-development 초기 CoE 50%→ 0~2% 점감(Microsoft Learn). 오피스아워 주 1회 이상 | [Kissflow](https://kissflow.com/no-code/citizen-developer-program/), [Microsoft Power Platform Blog](https://www.microsoft.com/en-us/power-platform/blog/power-apps/hmgroup/), [Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap-mentoring-and-user-enablement) |
    87	| 상충 증거 | "CoE 2~5인으로 모든 PR 심층 리뷰는 물리적으로 불가"(Checkmarx 2025). 보안 훈련은 시티즌 개발자 보안 문제를 해결하지 못함—규모·속도·다양성이 교육 한계 초과(TechNewsWorld). GSoC 멘토:참가자 1.64:1(역방향), Meta 1:2~3. 단기 파일럿에서는 멘토 밀도가 높아야 한다는 인접 사례 근거 | [Checkmarx](https://checkmarx.com/blog/ai-is-writing-your-code-whos-keeping-it-secure/), [TechNewsWorld](https://www.technewsworld.com/story/why-training-wont-solve-the-citizen-developer-security-problem-179877.html ⚠(dead link)), [GSoC 2025 Statistics](https://opensource.googleblog.com/2025/08/google-summer-of-code-2025-contributor-statistics.html), [AutomationHacks](https://newsletter.automationhacks.io/p/engineering-practices-meta-3-conduct) |
    88	| **판정** | **CoE 선행 구축 + 기술 통제 내재화 채택** — CoE 2~5명은 "프로그램 프레임워크·승인·커뮤니티 운영"을 담당하되, "모든 PR 심층 보안 리뷰"까지 담당하는 것은 현실적으로 불가능하다. 보안은 개발 경험 내 기술적 통제(SAST·lint·골든 패스 내장 정책) 임베딩으로 보완해야 한다. 3주 파일럿의 단기 집중 특성상 초기 멘토 밀도를 높게(co-development 50% 비율) 설정한다. | - |
    89	
    90	### 2.9 파일럿 종료 이후 기술 부채의 이관 부담
    91	
    92	| 구분 | 내용 | 출처 |
    93	|---|---|---|
    94	| 일치 증거 | 3주 스프린트 이후 AI 생성 코드의 장기 유지보수성 우려 존재(GitClear·Pixelmojo). 파일럿 종료 후 이관팀이 기술 부채를 떠안는 시나리오 제기(d2) | [GitClear](https://www.gitclear.com/ai_assistant_code_quality_2025_research ⚠(dead link)), [Pixelmojo](https://www.pixelmojo.io/blogs/vibe-coding-technical-debt-crisis-2026-2027) |
    95	| 상충 증거 | 기술 부채 처리 비용·이관팀 수용 의사에 대한 사례 연구 부재. 내부 기획안 7단계 격상 절차는 "재작성 없이 수용"을 원칙으로 하나, AI 생성 코드의 기술 부채를 고려한 수용 기준이 없음(내부 자료, 독립 검증 불가) | (내부: 탑다운 기획안 §6) |
    96	| **판정** | **미해결** — 이관팀이 AI 생성 코드의 기술 부채를 수용하는 조건·비용 기준이 내부에도 외부에도 없다. 파일럿 종료 전 이관팀과 기술 부채 수용 기준을 사전 합의하는 절차가 필요하나, 이를 뒷받침할 사례 근거가 없어 판정 불가. | - |
    97	
    98	---
    99	
   100	## 3. 통합 논리 구조
   101	
   102	1. **3주 배포 완성은 "골든 패스 사전 완비" 없이는 비현실적이며, 있어도 조건부 가능이다.**
   103	   - 근거: DORA 2025 "AI는 증폭기, 강한 플랫폼 없이 안정성 저하" ([DORA 2025 via platformengineering.com](https://platformengineering.com/features/dora-2025-ai-wont-save-you-without-a-solid-platform/)); GenAI 파일럿 실패율 88~95% ([MIT NANDA via Fortune](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/)); 골든 패스 없이는 AI 생성 코드 변경 실패율 +30% ([Cortex 2025 via Medium AI Transfer Lab](https://medium.com/@ai_transfer_lab/internal-developer-platforms-in-the-mcp-era-how-idp-teams-are-embedding-claude-as-a-first-class-846abc073117 ⚠(dead link))); 역으로 IDP 성숙 조직의 온보딩 67% 단축·첫 배포 1시간 미만([Spotify Backstage](https://backstage.spotify.com/discover/blog/how-we-measure-backstage-success-at-spotify), [Tasrie IT](https://tasrieit.com/blog/golden-paths-platform-engineering-guide-2026))
   104	   - **운영 함의**: 킥오프 최소 4~6주 전에 AI 인프라팀이 AWS 6대 골든 패스(ECS on Fargate·Lambda·RDS·비용태그·관측성·Secrets Manager) 완비 ([The Cloud Playbook TCP#124](https://www.thecloudplaybook.com/p/first-6-golden-paths-aws-platform-teams)); 시티즌 개발자는 폼 입력만으로 CI/CD·IAM·모니터링 포함 레포 자동 생성
   105	
   106	2. **파일럿 운영 구조는 Agile-Stage-Gate 하이브리드(W1 Gate 0 → W2 중간 Gate → W3 Gate 2+배포)가 기업 거버넌스와 스프린트 속도를 동시에 충족하는 최적 구조다.**
   107	   - 근거: Agile-Stage-Gate 게이트 결정 24~48시간 이내 ([Umbrex Stage-Gate](https://umbrex.com/resources/frameworks/strategy-frameworks/stage-gate-innovation-process/)); 내부 기획안 AI Board·정보보호팀 수동 승인 게이트와 직접 연계(내부: 탑다운 기획안 §5, 내부 자료 독립 검증 불가); GSoC 중간 평가 "한계 통과" 참가자 80%+ 최종 실패 → 중간 Gate는 단순 통과/실패보다 정교한 조기 경보 필요([GSoC Evaluations Guide](https://google.github.io/gsocguides/mentor/evaluations))
   108	   - **운영 함의**: Gate 2(배포 승인)는 3-lane 위험 분류 기반으로 설계: Green(내부 UI·문서·테스트) 표준 승인, Yellow(비즈니스 로직·API) 시니어 사인오프, Red(Auth·PII·인프라) 3인 승인(주 리뷰어+시니어+보안 오너) ([metacto 2026-07-08](https://www.metacto.com/blogs/establishing-code-review-standards-for-ai-generated-code)); rubber-stamping 방지를 위해 서면 정당화·로테이션 의무화
   109	
   110	3. **CoE 선행 구축이 파일럿 성공률을 결정한다. 거버넌스 구조 유무에 따른 성공률 차이가 2배(77% vs 39%)이며, 단기 파일럿일수록 초기 멘토 밀도를 높여야 한다.**
   111	   - 근거: KPMG Belgium 2024([KPMG Belgium](https://kpmg.com/be/en/home/insights/2024/11/ta-transforming-business-value-creation-with-citizen-development.html)); BCG 10-20-70 법칙—AI 성공의 70%는 사람·프로세스·문화([Forbes via BCG](https://www.forbes.com/sites/joemckendrick/2026/01/26/why-ais-10-20-70-principle-should-matter-to-ceos-and-everyone-else/)); Co-development 초기 CoE 50%→ 점감([Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap-mentoring-and-user-enablement))
   112	   - **운영 함의**: 2~5명 CoE가 프로그램 프레임워크·과제 검토(비즈니스+기술 2단계)·챔피언 운영을 담당. 보안 리뷰는 개발 경험 내 SAST·골든 패스 내장 정책으로 내재화(CoE의 전수 PR 리뷰는 물리적 불가)
   113	
   114	4. **KPI는 킥오프 전 동결하고, ROI는 위험 조정 후 재계산해야 한다. 에이전틱 도구 10주 지속 사용률 <10%는 챔피언 프로그램 없이는 파일럿 효과가 소멸함을 의미한다.**
   115	   - 근거: KPI 사전 동결 원칙([MarginLayer](https://marginlayer.app/blog/pilot-success-criteria-kpi-roi.html)); Anthropic 공식 6개 KPI(WAU 70%, 주당 메시지 25+건, 만족도 4.0/5.0+, 시간 절감 3시간+)([Claude Enterprise Administrator Guide](https://claude.com/resources/tutorials/claude-enterprise-administrator-guide)); DORA 2025 <10% 지속 사용([DORA 2025 via Jellyfish](https://jellyfish.co/blog/2025-dora-report/)); 챔피언 2.1배 효과([AI Assembly Lines](https://aiassemblylines.com/post/ai-champions-program-enterprise-adoption))
   116	   - **운영 함의**: 파일럿 KPI: 배포 완성 건수·WAU·사이클 타임·거버넌스 준수율·참여자 만족도를 킥오프 전 문서화. 챔피언 25~50명당 1명 배치([Anthropic Cowork](https://claude.com/resources/tutorials/scaling-workflows-with-claude-cowork-at-your-organization)), 주 30분 오피스아워·월간 부서간 데모데이 운영. 전사 확대 전 DECIDE 4대 질문으로 판단([Agility at Scale](https://agility-at-scale.com/ai/strategy/roi-and-success-metrics/))
   117	
   118	5. **종료·이관은 소유권 단일 책임자 사전 지정 + 3방향 출구(이관/폐기/현업복귀) + 자동 Frozen·보드 최종 결정 하이브리드로 설계한다.**
   119	   - 근거: 소유권 공백이 파일럿-프로덕션 전환 최대 장애([SoftwareSeni](https://www.softwareseni.com/the-enterprise-ai-pilot-purgatory-problem-what-the-statistics-actually-tell-us/)); AWS Innovation Sandbox 자동 Frozen→14일 접근 회수·21일 자동 삭제([AWS Docs Innovation Sandbox](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/account-lifecycle-in-isb.html)); 내부 기획안 7단계 격상 체크리스트·보드 심의 종료 원칙(내부: 탑다운 기획안 §6·§7, 내부 자료 독립 검증 불가); 사내벤처 이중 출구([Samsung Sustainability](https://www.samsung.com/sec/sustainability/popup/popup_doc/AYUBw0_6ArQAIx8i/))
   120	   - **운영 함의**: 파일럿 착수 전 Go/No-Go 스코어카드(기술 40%·재무 30%·시장 20%·자원 10%, 임계값 0.605)와 결정 권한자 지정([Visual Paradigm](https://guides.visual-paradigm.com/making-informed-decisions-with-a-go-no-go-checklist-for-agile-projects-a-scoring-approach/), [Traction Technology](https://www.tractiontechnology.com/blog/how-to-run-a-successful-pilot-with-a-startup-frameworks-kpis-enterprise-best-practices)). 종료 시 클로저 레코드(15~20분 작성, 4개 항목) 작성 후 영구 보존
   121	
   122	---
   123	
   124	## 4. 미해결 쟁점·리스크
   125	
   126	> 단계 5(정규화·결론)의 입력
   127	
   128	1. **파일럿 코호트 규모(쟁점 2.2)**: Anthropic 공식 50~100명 vs 씨앗 20~30명 vs systemprompt.io 3~5명 초기. 비전문 시티즌 개발자 특화 AI 코딩 파일럿 규모 벤치마크 1차 출처가 없어 판정 불가. 내부에서 파일럿 목적(AI 도구 채택 확산 vs 탑다운 과제 완성)에 따라 규모를 별도 정의해야 한다.
   129	
   130	2. **AI 생성 코드의 이관 기술 부채 수용 기준(쟁점 2.9)**: 파일럿 종료 후 이관팀이 AI 생성 코드의 기술 부채(기술 부채 30~41% 증가, 코드 중복 8배)를 수용하는 조건·비용 기준이 내부·외부 모두 미정의. 이관 거부 시 Pilot Purgatory 재현 위험.
   131	
   132	3. **3주 배포 완성의 시티즌 개발자 실증 데이터 부재**: 비전문 개발자가 3주 만에 운영환경 배포까지 완성한 직접 사례가 조사 범위 내 확인되지 않음. 골든 패스 사전 완비 + AI 코딩 도구 조합의 배포 완성률·실패율 벤치마크 미확보.
   133	
   134	4. **Rubber-stamping 방지 장치의 3주 사이클 적용 가능성**: 3-lane × 3인 리뷰 체제가 3주 타임박스 안에서 소화 가능한지 실증 데이터 없음. 대부분 사례는 상시 개발 조직 기준.
   135	
   136	5. **챔피언 프로그램 정량 효과의 독립 검증 부재**: Worklytics "2.1배 지속 사용률"·Adoptify.ai "62→85%" 수치가 단일 출처이며 동료 검토 연구가 아닌 업계 보고서 기반. 신뢰도 중간 수준.
   137	
   138	6. **복잡한 승인 게이트 → Shadow AI 촉진 역설의 관리**: 엄격한 3-lane 게이트가 오히려 비공식 AI 도구 사용을 조장할 수 있다는 역설([Elegant Software Solutions](https://www.elegantsoftwaresolutions.com/blog/vibe-coding-enterprise-adoption)). 게이트 복잡도와 Shadow AI 발생률 간의 임계점 데이터 미확보.
   139	
   140	---
   141	
   142	## 5. Sources
   143	
   144	### 웹 출처 (주요)
   145	
   146	- https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/ (Fortune / MIT NANDA, 2025-08-18)
   147	- https://fluidlabs.com/resources/why-42-percent-enterprise-ai-abandoned-2025 (Fluidlabs / S&P Global, 2025)
   148	- https://www.gartner.com/en/newsroom/press-releases/2024-07-29-gartner-predicts-30-percent-of-generative-ai-projects-will-be-abandoned-after-proof-of-concept-by-end-of-2025 ⚠(dead link) (Gartner Press Release, 2024-07-29)
   149	- https://www.softwareseni.com/the-enterprise-ai-pilot-purgatory-problem-what-the-statistics-actually-tell-us/ (SoftwareSeni, 날짜 미상)
   150	- https://www.forbes.com/sites/joemckendrick/2026/01/26/why-ais-10-20-70-principle-should-matter-to-ceos-and-everyone-else/ (Forbes / BCG, 2026-01-26)
   151	- https://www.veracode.com/blog/spring-2026-genai-code-security/ (Veracode Spring 2026 GenAI Code Security Report, 2026-04)
   152	- https://apiiro.com/blog/4x-velocity-10x-vulnerabilities-ai-coding-assistants-are-shipping-more-risks/ (Apiiro, 2025-09-04)
   153	- https://arxiv.org/pdf/2606.22721 (arXiv: Habituation at the Gate, 2026-06-23)
   154	- https://www.metacto.com/blogs/establishing-code-review-standards-for-ai-generated-code (metacto, 2026-07-08)
   155	- https://checkmarx.com/blog/ai-is-writing-your-code-whos-keeping-it-secure/ (Checkmarx, 2025)
   156	- https://www.gitclear.com/ai_assistant_code_quality_2025_research ⚠(dead link) (GitClear, 2025-02)
   157	- https://www.pixelmojo.io/blogs/vibe-coding-technical-debt-crisis-2026-2027 (Pixelmojo, 2026)
   158	- https://devops.com/ai-in-software-development-productivity-at-the-cost-of-code-quality-2/ (DevOps.com / Google DORA 2024, 2025)
   159	- https://google.github.io/gsocguides/mentor/evaluations (GSoC Evaluations Guide, 2025)
   160	- https://opensource.googleblog.com/2025/08/google-summer-of-code-2025-contributor-statistics.html (GSoC 2025 Statistics, 2025-08)
   161	- https://angelhack.com/blog/ai-internal-hackathon/ (AngelHack, 2024)
   162	- https://www.samsung.com/sec/sustainability/popup/popup_doc/AYUBw0_6ArQAIx8i/ (Samsung C-Lab Sustainability, 2025)
   163	- https://live.lge.co.kr/venture/ (LG전자 뉴스룸 사내벤처, 2024)
   164	- https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025 (DORA 2025 / Faros.ai, 2025-09)
   165	- https://dora.dev/insights/balancing-ai-tensions/ (DORA Insights, 2025)
   166	- https://systemprompt.io/guides/claude-code-organisation-rollout (systemprompt.io Claude Code Rollout Playbook, 날짜 미상)
   167	- https://claude.com/resources/tutorials/claude-enterprise-administrator-guide (Claude Enterprise Administrator Guide, 날짜 미상)
   168	- https://claude.com/resources/tutorials/scaling-workflows-with-claude-cowork-at-your-organization (Scaling workflows with Claude Cowork, 날짜 미상)
   169	- https://code.claude.com/docs/en/champion-kit (Claude Code Champion Kit, 날짜 미상)
   170	- https://newsroom.ibm.com/2025-10-07-2025-ibm-and-anthropic-partner-to-advance-enterprise-software-development-with-proven-security-and-governance (IBM Newsroom, 2025-10-07)
   171	- https://aiassemblylines.com/post/ai-champions-program-enterprise-adoption (AI Assembly Lines, 2026)
   172	- https://jellyfish.co/blog/2025-dora-report/ (Jellyfish DORA 2025, 2025)
   173	- https://platformengineering.com/features/dora-2025-ai-wont-save-you-without-a-solid-platform/ (Platform Engineering / DORA 2025, 2025)
   174	- https://platformengineering.org/blog/how-to-set-up-an-internal-developer-platform (platformengineering.org, 날짜 미상)
   175	- https://www.thecloudplaybook.com/p/first-6-golden-paths-aws-platform-teams (The Cloud Playbook TCP#124, 날짜 미상)
   176	- https://tasrieit.com/blog/golden-paths-platform-engineering-guide-2026 (Tasrie IT, 2026-01)
   177	- https://backstage.spotify.com/discover/blog/how-we-measure-backstage-success-at-spotify (Spotify Backstage, 2020~)
   178	- https://2023.platformcon.com/talks/how-toyota-saved-over-10m-and-optimized-developer-experience-through-platform-engineering (PlatformCon 2023, 2023-06)
   179	- https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1814498/full (Frontiers in Computer Science, 2026)
   180	- https://kpmg.com/be/en/home/insights/2024/11/ta-transforming-business-value-creation-with-citizen-development.html (KPMG Belgium, 2024-11)
   181	- https://kissflow.com/no-code/citizen-developer-program/ (Kissflow, 날짜 미상)
   182	- https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap-mentoring-and-user-enablement (Microsoft Learn, 2024-12-30)
   183	- https://isg-one.com/articles/the-automation-center-of-excellence-and-citizen-developers-not-the-wild-wild-west! (ISG, 날짜 미상)
   184	- https://www.tractiontechnology.com/blog/how-to-run-a-successful-pilot-with-a-startup-frameworks-kpis-enterprise-best-practices (Traction Technology, 날짜 미상)
   185	- https://guides.visual-paradigm.com/making-informed-decisions-with-a-go-no-go-checklist-for-agile-projects-a-scoring-approach/ (Visual Paradigm, 날짜 미상)
   186	- https://marginlayer.app/blog/pilot-success-criteria-kpi-roi.html (MarginLayer, 날짜 미상)
   187	- https://agility-at-scale.com/ai/strategy/roi-and-success-metrics/ (Agility at Scale, 날짜 미상)
   188	- https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/account-lifecycle-in-isb.html (AWS Docs Innovation Sandbox, 날짜 미상)
   189	- https://docs.aws.amazon.com/controltower/latest/userguide/decommissioning-process-overview.html (AWS Docs Control Tower, 날짜 미상)
   190	- https://umbrex.com/resources/frameworks/strategy-frameworks/stage-gate-innovation-process/ (Umbrex Stage-Gate, 날짜 미상)
   191	- https://www.elegantsoftwaresolutions.com/blog/vibe-coding-enterprise-adoption (Elegant Software Solutions, 2025)
   192	- https://blog.exceeds.ai/enterprise-ai-adoption-metrics-2025/ (Exceeds.ai, 2025)
   193	- https://www.index.dev/blog/ai-coding-assistants-roi-productivity (Index.dev, 2025)
   194	- https://semgrep.dev/blog/2025/ai-powered-detection-with-semgrep/ (Semgrep, 2025)
   195	- https://gotranscript.com/en/blog/turnaround-time-vs-quality-set-slas-without-increasing-risk (GoTranscript, 날짜 미상)
   196	- https://www.flosum.com/blog/the-unintended-security-threat-of-citizen-development (Flosum, 2024)
   197	- https://pluto.security/blog/citizen-development-security-teams/ (Pluto Security, 2024)
   198	- https://aws.amazon.com/ko/blogs/tech/cj-oliveyoung-aidlc-tech-blog/ (AWS 기술 블로그 CJ올리브영, 날짜 미상)
   199	- https://aws.amazon.com/ko/blogs/korea/how-frontier-teams-are-reinventing-ai-native-development/ (AWS Korea Blog, 2025)
   200	- https://dl.acm.org/doi/full/10.1145/3772363.3799043 ⚠(dead link) (CHI 2026 Extended Abstracts, 2026)
   201	
   202	### 내부 문서
   203	
   204	| 파일명 | 분석 섹션 | 신뢰도 |
   205	|---|---|---|
   206	| AWS_기반_탑다운_AIFAB_과제_운영환경_구축운영_기획안_v1-0.md | §2 바텀업 차이, §5 개발·배포, §6 격상 절차, §7 운영·모니터링 | 내부 자료(독립 검증 불가) |

exec
/bin/zsh -lc "for f in /Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/findings/*.md; do printf '%s\\n' \""'$f"; rg -n "선발|selection|criteria|코호트|3주|배포|KPI|Go/No-Go|이관|소유권|보안|멘토|CoE" "$f"; done' in /Users/jaybee/lab/AIFAB-plan
 succeeded in 0ms:
/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/findings/q0-internal-docs.md
7:- 탑다운 과제는 사업 계획으로 확정된 공식 과제이며, 수행 주체는 "지정된 개발·운영 조직"으로 명시됨. 바텀업의 "시티즌 개발자(교육 이수자)"와 명확히 구분됨 — **이 문서는 시티즌 개발자 선발·파일럿 운영 시나리오를 직접 다루지 않음** (내부: AWS_기반_탑다운_AIFAB_과제_운영환경_구축운영_기획안_v1-0.md §2. 바텀업 샌드박스와의 차이)
8:- 배포 승인 게이트는 스테이징 배포·검증 통과 후 "AI Board·정보보호팀 승인 게이트"(수동) → 무중단 배포(Blue/Green 또는 Rolling), 실패 시 자동 롤백 순서로 구성됨 (내부: AWS_기반_탑다운_AIFAB_과제_운영환경_구축운영_기획안_v1-0.md §5. 개발·배포)
9:- 운영 환경 직접 수정 경로는 없으며, 모든 변경은 Git 머지 → 파이프라인 재통과로만 반영 (불변 배포 원칙) (내부: AWS_기반_탑다운_AIFAB_과제_운영환경_구축운영_기획안_v1-0.md §5. 개발·배포)
10:- 바텀업 우수과제 격상은 분기 보드 심의로 확정되며, 7단계 체크리스트(코드 리뷰 → 문서화 → 실데이터 재설계 → 운영 조직 지정 → 환경 재프로비저닝 → 이관·검증 → 원 환경 정리)로 이관 처리됨 (내부: AWS_기반_탑다운_AIFAB_과제_운영환경_구축운영_기획안_v1-0.md §6. 격상 유입 절차)
11:- 격상의 실체는 "재프로비저닝 + 재배포"이며 애플리케이션 재작성 없이 수용하는 것이 핵심 원칙으로 명시됨 (내부: AWS_기반_탑다운_AIFAB_과제_운영환경_구축운영_기획안_v1-0.md §6. 격상 유입 절차)
14:- CI/CD 파이프라인 통과 기준: 단위 테스트 통과·하드코딩 시크릿 미검출(자동), Critical/High 취약점 0건(자동), 기능·성능 검증·정책 준수(자동+오너), 그 후 수동 승인 게이트 (내부: AWS_기반_탑다운_AIFAB_과제_운영환경_구축운영_기획안_v1-0.md §5. 개발·배포)
16:- 구축 로드맵은 M1~M6 4단계: 공통 기반(M1~M2) → 탑다운 표준화(M2~M3) → 배포 체계(M3~M4) → 격상 수용·정착(M4~M6) (내부: AWS_기반_탑다운_AIFAB_과제_운영환경_구축운영_기획안_v1-0.md §8. 단계별 구축 로드맵)
28:| 격상 이관 체크리스트 단계 수 | 7단계 | §6. 격상 유입 절차 | 2026.07.11 |
29:| CI/CD 취약점 기준 | Critical/High 0건 | §5. 개발·배포 | 2026.07.11 |
35:- **브리프 핵심 질문 1(시티즌 개발자 선발 기준·절차)**: 본 문서는 탑다운 운영환경 구축·운영 기획안이며, 수행 주체를 "지정된 개발·운영 조직"으로 전제함. 시티즌 개발자 선발 기준·절차에 대한 내용 없음.
36:- **브리프 핵심 질문 2(3주 스프린트 주차별 운영 구조)**: 본 문서에 3주 스프린트 구조(킥오프, 중간 점검, 심사·게이트 일정)가 존재하지 않음. 파일럿 스프린트 운영 시나리오는 다루지 않음.
37:- **브리프 핵심 질문 3(멘토링·오피스아워·AI 코딩 도구 지원)**: 개발자 지원 체계(멘토링, 오피스아워, AI 코딩 도구)에 대한 내용 없음. 인프라·플랫폼 지원(Landing Zone, IaC, CI/CD)만 기술됨.
38:- **브리프 핵심 질문 5(파일럿 성공 KPI와 확대 판단 기준)**: 정량적 KPI 및 프로그램 확대 판단 기준 없음. SLO(가용성 99.5% 등)는 개별 과제 운영 수준 목표이며 파일럿 프로그램 KPI는 아님.
39:- 관련 문서로 언급된 "샌드박스 기획안(바텀업, v2-1)"은 분석 목록에 없어 내용 미확인. 시티즌 개발자 선발·스프린트 구조 관련 내용이 해당 문서에 있을 가능성 있음.
/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/findings/q1-selection-criteria.md
1:# 시티즌 개발자 프로그램의 참가자 선발 기준·절차 모범 사례
15:- **과제 제출·검토 2단계**: UiPath Automation Hub 프레임워크 기준으로 과제는 비즈니스 검토(넓은 사용자에게 이익이 되는지 평가) → 기술 검토(코드 품질·확장 준비도 확인)의 2단계를 거쳐 CoE 또는 시티즌 개발자 승인으로 연결된다. 역할은 셀프 유저, 파워 유저, 비즈니스 검토자, 기술 검토자 4종으로 구분된다. ([UiPath Automation Hub - Citizen Developer Framework](https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/understanding-the-citizen-developer-framework), 날짜 미상)
17:- **CoE(Center of Excellence) 규모**: 프로그램 표준 수립, 사용 사례 승인, 플랫폼 관리, 교육, 커뮤니티 운영을 담당하는 CoE는 통상 IT+비즈니스 전문가 2~5명으로 구성하고, 신규 과제 제출 포털을 운영한다. ([Kissflow - Citizen Developer Program](https://kissflow.com/no-code/citizen-developer-program/), 날짜 미상)
21:- **LG유플러스 국내 사례**: 국내 최초 RPA 시민개발자 모델을 도입하여 탑다운(핵심 과제 전담 개발자 육성)·바텀업(전 직원 자동화 과제 개발 장려) 이원화 방식을 운영했다. 선발된 인원은 초급·중급·고급·특급 4등급으로 분류하여 등급별 혜택을 부여, 자발적 역량 향상을 유도했다. ([UiPath - LG유플러스 시민개발자 사례](https://www.uipath.com/ko/resources/automation-case-studies/lguplus), 날짜 미상)
33:| CoE 구성 인원 | 2~5명 | Kissflow | 날짜 미상 |
50:- Claude Code 등 AI 코딩 도구를 활용한 시티즌 개발자 파일럿 선발 사례는 공개된 1차 출처를 찾지 못함.
/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/findings/q2-sprint-structure.md
1:# 3주 단기 스프린트로 배포까지 완성하는 프로그램의 주차별 운영 구조
5:- **3주 스프린트의 가장 검증된 패턴은 "1주 계획·정제 + 2주 순수 개발"** 구조다. 1주차에 모든 회의·스토리 정제·기술 탐색을 집중하고, 2-3주차는 맥락 전환(context switching) 없이 개발에만 몰두한다. ([John Wakeling Blog](https://www.johnwakeling.co.uk/posts/3-week-sprints/), 날짜 미상)
15:- **Google GV Design Sprint(5일) → 구현 스프린트(2~3주) 연계 구조**: 디자인 스프린트는 Day1 이해·Day2 스케치·Day3 결정·Day4 프로토타입·Day5 사용자 테스트로 구성되며, 스프린트 종료 후 "무엇을 다음에 할지"가 확정된다. 구현 스프린트는 별도 2~4주 추가 운영이 일반적이다. ([GV Sprint](https://www.gv.com/sprint/), 날짜 미상; [Google Design](https://design.google/library/design-sprints), 날짜 미상)
19:- **스프린트 플래닝 시간 기준**: 스크럼 가이드 표준은 "스프린트 1주당 플래닝 2시간". 3주 스프린트라면 킥오프 플래닝에 최대 6시간을 배정한다. ([Atlassian Scrum Sprints](https://www.atlassian.com/ko/agile/scrum/sprints), 날짜 미상)
21:- **국내 사례 - 부산 DX 스프린트 해커톤**: 2주 집중 운영으로 사전심사 선발 → 팀빌딩 → 개발 → 동작 시연·발표 심사까지 진행, 실제 서비스 출시를 목표로 함. ([파이낸셜뉴스](https://www.fnnews.com/news/202307171837050284), 2023-07-17)
23:- **AI App Bootcamp(12일 구조)** 사례: Day1-2 아이디어·설정, Day3-6 핵심 기능 개발, Day7-8 UI 디자인, Day9-10 배포·최종 조정, Day11-12 커스텀 통합. 주 단위 오피스 아워, 그룹 체크포인트, "MVP 로스트(Roast My MVP)" 피드백 세션을 구조화. ([AI Build Accelerator](https://build.starterstory.com/build/ai-build-accelerator), 날짜 미상)
29:| 3주 스프린트 플래닝 권장 시간 | 6시간 (주당 2시간 × 3주) | [Atlassian Scrum Sprints](https://www.atlassian.com/ko/agile/scrum/sprints) | 날짜 미상 |
40:조사 결과를 종합하면, 3주 스프린트 W1/W2/W3 구조는 다음 세 가지 패턴으로 수렴된다:
45:- **W3 (완성 + 게이트)**: 통합 테스트, 스프린트 데모, 이해관계자 게이트 리뷰(Go/Kill), 배포, 회고
50:- **W3 (구현 스프린트 2 + 배포)**: 완성·UI 개선, 배포 승인 게이트, 데모데이, 회고
55:- **W3 (스프린트 3 + Gate 2 + 배포)**: 최종 완성, Gate 2(배포 승인), 프로덕션 배포, 데모데이, 이관 계획
59:- 3주 스프린트로 실제 프로덕션 배포까지 완성한 사내 시티즌 개발자 프로그램의 주차별 공개 사례(국내 대기업 포함)를 1차 출처로 확보하지 못함
61:- 해커톤→프로덕션 전환의 "배포 승인 게이트" 기준(체크리스트·KPI)에 대한 정량 데이터 미확보
62:- AI 코딩 도구(Claude Code 등) 활용 시 3주 스프린트 효율 차이에 대한 실증 데이터 미확보
/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/findings/q3-support-system.md
5:- **CoE(Center of Excellence)는 2~5명의 소규모 전담팀**으로 구성하는 것이 모범 사례이며, 프로그램 프레임워크 소유, 사용 사례 승인, 플랫폼 표준 유지, 시티즌 개발자 안내·검수 역할을 담당한다. ([Kissflow, Citizen Developer Program, 2026](https://kissflow.com/no-code/citizen-developer-program/))
7:- **멘토링은 경험 있는 전문 개발자가 시티즌 개발자에게 1:1 페어링**하는 방식이 권장된다. ISG는 "자동화 CoE에서 경험 많은 개발자를 멘토로 지정해 시티즌 개발자의 시간가치(time to value)를 가속하라"고 명시했다. ([ISG, The Automation Center of Excellence and Citizen Developers, 날짜 미상](https://isg-one.com/articles/the-automation-center-of-excellence-and-citizen-developers-not-the-wild-wild-west!))
9:- **공동 개발(Co-development) 프로젝트 모델**: CoE와 사업부가 파트너십으로 프로젝트를 수행하며, 초기에는 CoE 50% : 사업부 50%로 시작해, 시간이 지남에 따라 CoE 0~2% : 사업부 98~100%로 점감하는 참여 구조를 권장한다. ([Microsoft Learn, Fabric Adoption Roadmap - Mentoring and User Enablement, 2024-12-30 업데이트](https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap-mentoring-and-user-enablement))
11:- **오피스아워(Office Hours)는 주 1회 이상, 정기적·빈번하게** 운영하는 것이 권장된다(예: 매주 화·목). CoE 전문가가 최소한의 절차로 지역 사회 구성원과 실시간 상담이 가능한 구조이며, "Power Hour", "Fabric Fridays" 등 브랜드명으로 운영하는 사례가 있다. ([Microsoft Learn, Fabric Adoption Roadmap - Mentoring and User Enablement, 2024-12-30 업데이트](https://learn.microsoft.com/en-us/power-bi/guidance/fabric-adoption-roadmap-mentoring-and-user-enablement))
13:- **허브-앤-스포크(Hub-and-Spoke) 구조**가 확장 시 효과적: CoE(허브)가 플랫폼 거버넌스·훈련 자료·프로그램 표준 유지하고, 각 사업부에 1~3명의 인증된 시티즌 개발자 챔피언(스포크)이 동료의 첫 번째 연락 창구 역할을 담당한다. ([Kissflow, Citizen Developer Program, 2026](https://kissflow.com/no-code/citizen-developer-program/))
15:- **Wesco 사례**: 직원 20,000명 이상 조직에서 "오피스아워 및 1:1 지원"을 제공하고, CoE 전문 개발자가 시티즌 개발자 프로젝트에 참여·검수. 시티즌 개발자를 "자동화 대사(automation ambassador)"로 정의하고 사용 사례 발굴 및 프로그램 홍보 역할도 부여한다. ([UiPath Blog, Successful citizen developer programs: Lessons from META, ConocoPhillips, 날짜 미상](https://www.uipath.com/blog/automation/citizen-development-lessons-from-meta-conocophillips-and-more))
17:- **H&M 그룹 CoE 사례**: 4명의 직원(Microsoft 365 Solution Architect, Cross Delivery Coordinator 포함)이 CoE를 주도하며, 자동화된 환영 이메일을 통한 온라인 교육 자료 제공, Yammer 온라인 커뮤니티 운영, SharePoint 성공 사례 카탈로그 공유 방식으로 1,500개 앱·30,000명 이상의 사용자 커뮤니티를 지원했다. ([Microsoft Power Platform Blog, H&M Group enables citizen development at scale, 날짜 미상](https://www.microsoft.com/en-us/power-platform/blog/power-apps/hmgroup/))
19:- **Deloitte의 Claude CoE 사례**: 470,000명 이상의 직원에게 Claude(Anthropic AI) 배포 시 Claude Center of Excellence를 설립, 표준화된 구현 추진. 약 15,000명의 실무자를 GenAI(특히 Anthropic 모델)로 인증했다. ([IntuitionLabs, Claude Enterprise Deployment & Training Guide 2026, 날짜 미상](https://intuitionlabs.ai/articles/claude-enterprise-deployment-training-guide-2026))
21:- **교육 지원 채널 구성**: 핸즈온 워크숍, 멘토링 프로그램, 온라인 포럼/채팅(Slack·Teams) 채널, 튜토리얼·모범 사례 지식 베이스, 중앙화된 포털(SharePoint/Teams 위키) 조합이 권장된다. ([Superblocks Blog, 6-Step Framework for Citizen Developer Governance 2026, 2026](https://www.superblocks.com/blog/citizen-developer-governance))
25:- **전임 개발자 대비 시티즌 개발자 생산성**: 전임 개발자는 연간 4~6건 자동화를 완료하는 반면, 25% 시간 할당 시티즌 개발자는 연간 1~2건 수준. CoE가 이 생산성 갭을 고려해 지원 강도를 설계해야 한다. ([ISG, The Automation Center of Excellence and Citizen Developers, 날짜 미상](https://isg-one.com/articles/the-automation-center-of-excellence-and-citizen-developers-not-the-wild-wild-west!))
31:| 기업 CoE 권장 전담 인원 | 2~5명 | Kissflow, Citizen Developer Program | 2026 |
32:| H&M 그룹 CoE 실제 운원 | 4명 | Microsoft Power Platform Blog | 날짜 미상 |
34:| Co-development 초기 CoE 참여 비율 | 50% → 0~2%로 점감 | Microsoft Learn Fabric Adoption Roadmap | 2024-12-30 |
36:| Deloitte AI CoE 인증 인력 | 15,000명 (전체 470,000명 중) | IntuitionLabs Claude Enterprise Guide | 날짜 미상 |
46:- CoE 인원 대비 시티즌 개발자 수의 **명확한 지원 비율**(예: 1명 CoE 당 몇 명 지원)에 관한 1차 출처 데이터를 확보하지 못했다.
50:- 국내 기업(한국)의 시티즌 개발자 CoE·멘토링 운영 사례는 공개 출처에서 발견되지 않았다.
55:- https://isg-one.com/articles/the-automation-center-of-excellence-and-citizen-developers-not-the-wild-wild-west! (ISG, The Automation CoE and Citizen Developers, 날짜 미상)
/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/findings/q4-closure-handover.md
1:# 파일럿 과제 배포 후 종료 처리 절차
5:- **이관 vs 폐기 판단은 사전 정의된 성공 기준 기반 Go/No-Go 결정으로 수행**: 파일럿 시작 전에 성공 기준을 합의하고, 종료 시 조직된 증거(성공 기준 충족 여부)를 근거로 Scale/Stop/Redirect 중 하나를 결정한다. 결정 권한자(named decision owner)를 사전에 지정하는 것이 핵심 거버넌스 요건이다. ([Traction Technology, 날짜 미상](https://www.tractiontechnology.com/blog/how-to-run-a-successful-pilot-with-a-startup-frameworks-kpis-enterprise-best-practices))
9:- **Go/No-Go 스코어카드는 4개 영역(기술·재무·시장·자원) 가중 점수로 정량화**: 기술 40%, 재무 30%, 시장 20%, 자원 10% 등 가중치를 사전 배정하고 최종 점수 임계값(예: 0.605 이상)을 통과해야 운영 이관을 승인한다. ([Visual Paradigm, 날짜 미상](https://guides.visual-paradigm.com/making-informed-decisions-with-a-go-no-go-checklist-for-agile-projects-a-scoring-approach/))
11:- **운영 이관은 완료 날짜가 아닌 '전환 과정'으로 설계**: 이관 체크리스트는 ①이관 산출물 사전 합의(내용·시기·형식), ②운영팀의 조직적·운영적 준비 확인, ③문서(운영 매뉴얼·트러블슈팅 매뉴얼·교육 기록·안전 파일) 완비, ④이관 후 현장 지원 체계 구축 등 4개 핵심 항목으로 구성된다. ([Owner Team Consultation, 날짜 미상](https://www.ownerteamconsult.com/effective-handover-of-projects-to-operations-teams/))
13:- **애플리케이션 폐기(Decommissioning) 판단 기준**: ①활성 사용자 수 또는 트랜잭션이 정의된 임계값 미만, ②유지보수 비용이 비즈니스 가치 대비 과도, ③기술 스택 노후화(미지원 플랫폼), ④보안·컴플라이언스 기준 미충족, ⑤다른 시스템이 동등 이상의 기능 제공 등 5개 기준으로 결정한다. ([SparxSystems, 날짜 미상](https://www.sparxsystems.us/application-portfolio-management/application-lifecycle-states-sunset-policy/))
17:- **AWS Innovation Sandbox 솔루션의 계정 라이프사이클 자동화**: 계정은 Entry→CleanUp→Available→Active→Frozen→CleanUp의 상태 머신으로 관리되며, 임계값(비용 또는 기간) 초과 시 Frozen 상태로 자동 전환되어 사용자 접근이 차단된다. 정리 실패 시 Quarantine 상태로 격리되어 관리자 수동 복구가 필요하다. 운영 이관이 결정된 계정은 Eject(Exit OU로 이동)하여 계정 풀에서 영구 분리할 수 있다. ([AWS Docs, 날짜 미상](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/account-lifecycle-in-isb.html))
23:- **회고(Retrospective) KPI는 액션 아이템 완료율·참여율·팀 행복도·사이클 타임으로 정량화**: 매 스프린트 회고에서 팀원의 행복도 점수(임의 척도)를 기록하고 추세를 추적하며, 이전 회고 액션 아이템 완료율을 다음 회고 첫 번째 의제로 점검하는 것이 권장된다. ([Gulf Coast Trade Institute, 날짜 미상](https://gulfcoasttradeinstitute.com/measuring-retrospective-effectiveness/))
39:| Go/No-Go 스코어카드 통과 임계값 예시 | 0.605 이상 (가중 점수) | [Visual Paradigm](https://guides.visual-paradigm.com/making-informed-decisions-with-a-go-no-go-checklist-for-agile-projects-a-scoring-approach/) | 날짜 미상 |
44:- **사내 IT 파일럿(시티즌 개발자 대상) 특화 이관 기준 미확보**: 검색 결과는 대부분 스타트업-엔터프라이즈 파일럿 또는 대규모 인프라 폐기 사례 중심이며, AI 코딩 도구 활용 시티즌 개발자 파일럿의 이관 기준에 특화된 1차 출처는 부재하다.
45:- **한국어 1차 출처(국내 파일럿 이관 사례) 부재**: 국내 기업의 파일럿 프로젝트 운영 이관 기준이나 AWS 리소스 회수 가이드라인에 관한 공개 1차 출처를 발견하지 못했다.
/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/findings/q5-kpi-scaling.md
1:# 시티즌 개발자 파일럿의 성공 지표(KPI)와 본 사업 확대 판단 기준
5:- 시티즌 개발자 프로그램의 핵심 KPI 6종: 운영 효율성, 시간 절감, 가치 실현 기간, 직원 참여도, 참여자 수, 후원 아이디어 수 — 이 여섯 지표를 복합 추적한 조직이 단일 지표에 집중한 조직보다 성과가 높음 ([KPMG Belgium, "Transforming business value creation with Citizen Development"](https://kpmg.com/be/en/home/insights/2024/11/ta-transforming-business-value-creation-with-citizen-development.html), 2024-11)
7:- 파일럿 성공 기준은 **시작 전(day 0)에 KPI 임계값을 동결**해야 하며, go/no-go 판단 기준 및 의사결정 담당자를 킥오프 전에 합의·문서화하는 것이 최우선 원칙 ([MarginLayer, "Pilot success criteria, KPI, and ROI frame"](https://marginlayer.app/blog/pilot-success-criteria-kpi-roi.html), 날짜 미상)
11:- AI 코딩 도구 파일럿에서 DORA 메트릭(배포 빈도, 변경 리드타임, 평균 복구시간, 변경실패율)이 실측 기반 확대 판단의 핵심 지표 — "6~8주 파일럿에서 리드타임 또는 배포 빈도의 측정 가능한 개선이 없으면, 병목 해결 후 재시도"가 표준 권고 ([Index.dev, "AI Coding Assistant ROI: Real Productivity Data 2025"](https://www.index.dev/blog/ai-coding-assistants-roi-productivity), 2025)
13:- 전사 확대 여부를 판단하는 DECIDE 프레임워크 4대 질문: ① 결과 KPI 달성 여부, ② 비용 대비 가치 비율 적정성, ③ 거버넌스·리스크 확대 수용 가능성, ④ 조직 변화 관리 준비도 — 4개 모두 충족 시 확대 결정 ([Agility at Scale, "Enterprise AI ROI Measurement"](https://agility-at-scale.com/ai/strategy/roi-and-success-metrics/), 날짜 미상)
17:- META의 시티즌 개발자 파일럿 성과: 첫 두 코호트에서 7개 비즈니스 팀 전반에 걸쳐 20개 이상의 자동화 배포 달성 — 코호트 단위 배포 건수가 확대 판단의 정량 지표로 활용됨 ([UiPath, "Citizen development lessons from META, ConocoPhillips"](https://www.uipath.com/blog/automation/citizen-development-lessons-from-meta-conocophillips-and-more), 날짜 미상)
23:- Kissflow 기준 장기 KPI(확대 후): 90일 내 최소 1개 앱 배포한 활성 시티즌 개발자 수, 거버넌스 준수율(승인된 프로세스를 통한 앱 비율), 분기별 부서 만족도 설문 — CoE가 분기 평가 보고서를 작성해 경영진 확대 승인 기초자료로 제출 ([Kissflow, "Citizen Developer Program: How to Launch, Scale & Govern"](https://kissflow.com/no-code/citizen-developer-program/), 날짜 미상)
29:| 시티즌 개발 도입 시 배포 속도 향상 | 기존 IT 대비 5~10배 빠름 | [Quixy](https://quixy.com/blog/citizen-development-kpis-and-roi/) | 2024 |
30:| 내부 도구 배포 리드타임 단축 | 평균 60~70% 감소 | [Kissflow 통계](https://kissflow.com/citizen-development/citizen-development-statistics-and-trends/) | 2025 |
41:| META 파일럿 2개 코호트 배포 성과 | 7개 팀, 20개 이상 자동화 배포 | [UiPath Blog](https://www.uipath.com/blog/automation/citizen-development-lessons-from-meta-conocophillips-and-more) | 날짜 미상 |
51:- **파일럿 배포 완성률(deployment completion rate) 벤치마크**: 업계 표준 수치(예: "파일럿 중 X%가 배포까지 완료")를 제시하는 1차 출처를 확보하지 못함. 대부분의 자료가 속도·비용 절감에 집중하며 완성률 자체는 별도 측정하지 않음.
53:- **참여자 역량 향상 지표 정량 데이터 부재**: 시티즌 개발자 프로그램에서 역량 향상(스킬 향상 점수, 자격증 취득률 등)을 독립 KPI로 제시하는 1차 출처를 확보하지 못함.
55:- **한국 기업의 명시적 go/no-go 기준 사례 부재**: CJ올리브영 사례는 성과 수치는 확인됐으나 전사 확대 의사결정 기준을 공개한 자료가 없음. SK 계열사 등 국내 대기업의 구체적 파일럿 KPI 공개 사례도 확보하지 못함.
63:- https://quixy.com/blog/citizen-development-kpis-and-roi/ (Quixy, "Navigating Citizen Development KPIs and ROI", 2024)
74:- https://marginlayer.app/blog/pilot-success-criteria-kpi-roi.html (MarginLayer, "Pilot success criteria, KPI, and ROI frame", 날짜 미상)

codex
독립 검증 결과, 이 결론 보고서는 방향성은 대체로 수렴 보고서와 맞지만, “조건부 가능/미해결”이어야 할 내용을 “필수/최적/실현 가능”으로 끌어올린 곳이 많습니다. 특히 최종 운영 의사결정 문서로 쓰기에는 검증 이력 자체가 완료되지 않았고, 원래 질문인 “시티즌 개발자 선발부터 3주 배포·종료까지”의 일부 핵심이 빠져 있습니다.

**주요 결함**

1. **검증 완료 전제 자체가 성립하지 않음**  
   [05-conclusion.md:196](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md:196) 이하에 URL 검증, Critic 비평, Codex 교차 검증, 출구 게이트가 모두 “검증 대기”로 남아 있습니다. 따라서 이 문서는 “결론 보고서”라기보다 “미검증 결론 초안”으로 취급해야 합니다. 특히 여러 웹 출처가 날짜 미상, dead link, 미래 날짜 자료를 포함하는데도 최종 판단처럼 서술합니다.

2. **“골든 패스 없으면 실패율 88~95%가 그대로 재현”은 인과 과장**  
   [05-conclusion.md:9](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md:9)의 문장은 MIT NANDA/S&P 수치를 “골든 패스 부재”의 직접 결과처럼 연결합니다. 그러나 [04-convergence.md:26](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/04-convergence.md:26)는 GenAI 파일럿의 P&L 기여 실패와 포기율을 일반 상충 증거로 제시할 뿐, 골든 패스 부재 시 같은 실패율이 “그대로 재현”된다는 실증은 없습니다. 적절한 표현은 “유사한 실패 리스크가 커진다” 정도입니다.

3. **“골든 패스가 갖춰지면 첫 배포 1시간 미만”도 대상 전이가 큼**  
   [05-conclusion.md:9](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md:9), [66](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md:66)는 IDP/플랫폼 엔지니어링 문헌의 일반 효과를 시티즌 개발자 3주 운영 배포에 직접 적용합니다. 그런데 수렴 보고서는 “비전문 개발자가 3주 만에 운영환경 배포까지 완성한 직접 사례가 조사 범위 내 확인되지 않음”이라고 명시합니다([04-convergence.md:132](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/04-convergence.md:132)). 즉 “가능성 조건”이지 “실현 가능”으로 단정할 근거는 부족합니다.

4. **Agile-Stage-Gate를 “최적 구조”로 판정한 근거가 약함**  
   [05-conclusion.md:11](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md:11)는 “최적 구조”라고 하지만, [04-convergence.md:106](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/04-convergence.md:106)의 근거는 일반 Stage-Gate, 내부 기획안과의 정합성, GSoC 중간평가 유추입니다. 비교 대안별 성과 데이터가 없으므로 “최적”이 아니라 “현재 근거상 가장 방어 가능한 후보 구조”가 맞습니다.

5. **R3를 Quick Win으로 둔 것은 R4/R5의 무거운 전제와 충돌**  
   R3는 “추가 리소스 불필요”라고 합니다([05-conclusion.md:49](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md:49), [97](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md:97)). 그러나 같은 운영 구조가 W3 Gate 2의 3-lane 리뷰와 Red lane 3인 승인, CoE 선행 구축에 의존합니다([05-conclusion.md:102](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md:102), [117](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md:117), [132](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md:132)). 문서화 자체는 쉽지만 실제 운영은 Quick Win이 아닙니다.

6. **CoE가 “파일럿 성공률을 결정”한다는 표현은 과장**  
   [05-conclusion.md:13](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md:13)는 KPMG 77% vs 39%를 파일럿 성공률처럼 사용합니다. 하지만 수렴 보고서의 원 표현은 “거버넌스 있는 조직 vs 없는 조직의 비용 절감 성공”입니다([04-convergence.md:42](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/04-convergence.md:42)). 비용 절감 성공률을 3주 탑다운 파일럿 성공률로 바꾸는 것은 지표 전환 오류입니다.

7. **챔피언 프로그램 부재 시 “파일럿 효과는 소멸”은 인과가 약함**  
   [05-conclusion.md:13](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md:13), [141](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md:141)는 DORA의 10주 지속 사용률 <10%를 챔피언 프로그램 필요성으로 연결합니다. 그러나 [04-convergence.md:72](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/04-convergence.md:72)는 챔피언 효과 수치가 단일 출처이고 독립 검증이 없다고 밝힙니다. “소멸한다”보다 “지속 사용 리스크가 크므로 개입이 필요하다”가 타당합니다.

8. **Go/No-Go 임계값 0.605를 그대로 채택한 것은 부적절**  
   [05-conclusion.md:84](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md:84), [87](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md:87)는 Visual Paradigm 예시의 0.605를 실제 파일럿 임계값처럼 넣습니다. 이는 범용 예시이지 AI FAB의 위험, 보안, 기술부채, 운영 이관 비용을 반영한 산식이 아닙니다. 특히 findings에는 배포 완성률 벤치마크가 없다고 되어 있습니다([q5-kpi-scaling.md:51](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/findings/q5-kpi-scaling.md:51)).

9. **가장 큰 전제 충돌: 내부 기획안은 ‘시티즌 개발자 탑다운 파일럿’을 직접 다루지 않음**  
   [q0-internal-docs.md:7](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/findings/q0-internal-docs.md:7)는 탑다운 과제 수행 주체가 “지정된 개발·운영 조직”이고 시티즌 개발자와 구분된다고 합니다. 또한 [q0-internal-docs.md:35](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/findings/q0-internal-docs.md:35) 이하에서 선발 기준, 3주 스프린트, 멘토링, KPI가 내부 문서에 없다고 명시합니다. 결론 보고서는 이 구조적 불일치를 핵심 리스크로 올리지 않았습니다.

10. **시티즌 개발자 선발 기준이 사실상 결론에서 빠짐**  
   문서 제목은 “시티즌 개발자 선발부터”라고 하지만, 결론의 8개 권고에는 선발 기준·절차가 독립 권고로 없습니다. 별도 finding에는 과제 제출·검토 2단계, 역할 구분, LG유플러스 등 선발 관련 근거가 있습니다([q1-selection-criteria.md:15](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/findings/q1-selection-criteria.md:15), [21](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/findings/q1-selection-criteria.md:21)). 이 누락은 원래 핵심 질문 1에 대한 미응답입니다.

11. **기술 부채 이관 기준은 “핵심 리스크”라면서 권고 우선순위에는 없음**  
   [05-conclusion.md:17](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md:17)에서 핵심 리스크로 인정하지만, [25-34](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md:25) 우선순위 매트릭스에는 독립 권고가 없습니다. [188](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md:188)에 “조건부 권고”로만 밀려 있습니다. 실제로는 R7보다 우선도가 높아야 합니다. 이 기준 없이는 배포 성공 후 운영 이관이 막힐 수 있습니다.

12. **미래/불확실 출처 처리 미흡**  
   04 수렴 보고서의 소스에는 2026-09, 2026-10 등 보고서 생성일 2026-07-11 이후 자료가 포함되어 있습니다([04-convergence.md:164](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/04-convergence.md:164), [170](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/04-convergence.md:170)). 05 결론에도 2026 자료들이 섞여 있으나 URL 검증이 대기 상태입니다. 보고서 날짜 기준으로 존재 여부와 접근 가능성을 재검증하지 않으면, 출처 신뢰도가 크게 흔들립니다.

**핵심 누락**

- 선발 기준: 참가자 역량, 과제 난이도, 업무 도메인, 보안 권한, 선발/탈락 프로세스가 결론 권고에 없음.
- 코호트 규모: 미해결이라고만 두고 운영 가능한 기본안이 없음.
- 3주 운영 상세: W1/W2/W3 문구는 있지만 산출물, 책임자, 승인 SLA, 실패 시 조치가 부족함.
- 기술 부채 수용 기준: 중복률, 테스트 커버리지, 취약점 0건, 리팩토링 범위, 운영팀 거부권 같은 이관 조건이 없음.
- 내부 기획안과의 주체 불일치: “지정 개발·운영 조직” 대 “시티즌 개발자”의 충돌을 해소하지 않음.

**종합 판단**

이 결론은 “골든 패스 + CoE + 게이트 + KPI 동결”이라는 큰 방향은 방어 가능하지만, 현재 형태는 근거 대비 표현이 강합니다. 최종본으로 쓰려면 `최적/필수/실현 가능/결정한다/소멸한다` 같은 단정 표현을 `조건부 권고/가설/리스크 완화 수단`으로 낮추고, 선발 기준·코호트 규모·기술 부채 이관 기준을 독립 권고로 올려야 합니다.
tokens used
63,406
독립 검증 결과, 이 결론 보고서는 방향성은 대체로 수렴 보고서와 맞지만, “조건부 가능/미해결”이어야 할 내용을 “필수/최적/실현 가능”으로 끌어올린 곳이 많습니다. 특히 최종 운영 의사결정 문서로 쓰기에는 검증 이력 자체가 완료되지 않았고, 원래 질문인 “시티즌 개발자 선발부터 3주 배포·종료까지”의 일부 핵심이 빠져 있습니다.

**주요 결함**

1. **검증 완료 전제 자체가 성립하지 않음**  
   [05-conclusion.md:196](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md:196) 이하에 URL 검증, Critic 비평, Codex 교차 검증, 출구 게이트가 모두 “검증 대기”로 남아 있습니다. 따라서 이 문서는 “결론 보고서”라기보다 “미검증 결론 초안”으로 취급해야 합니다. 특히 여러 웹 출처가 날짜 미상, dead link, 미래 날짜 자료를 포함하는데도 최종 판단처럼 서술합니다.

2. **“골든 패스 없으면 실패율 88~95%가 그대로 재현”은 인과 과장**  
   [05-conclusion.md:9](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md:9)의 문장은 MIT NANDA/S&P 수치를 “골든 패스 부재”의 직접 결과처럼 연결합니다. 그러나 [04-convergence.md:26](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/04-convergence.md:26)는 GenAI 파일럿의 P&L 기여 실패와 포기율을 일반 상충 증거로 제시할 뿐, 골든 패스 부재 시 같은 실패율이 “그대로 재현”된다는 실증은 없습니다. 적절한 표현은 “유사한 실패 리스크가 커진다” 정도입니다.

3. **“골든 패스가 갖춰지면 첫 배포 1시간 미만”도 대상 전이가 큼**  
   [05-conclusion.md:9](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md:9), [66](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md:66)는 IDP/플랫폼 엔지니어링 문헌의 일반 효과를 시티즌 개발자 3주 운영 배포에 직접 적용합니다. 그런데 수렴 보고서는 “비전문 개발자가 3주 만에 운영환경 배포까지 완성한 직접 사례가 조사 범위 내 확인되지 않음”이라고 명시합니다([04-convergence.md:132](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/04-convergence.md:132)). 즉 “가능성 조건”이지 “실현 가능”으로 단정할 근거는 부족합니다.

4. **Agile-Stage-Gate를 “최적 구조”로 판정한 근거가 약함**  
   [05-conclusion.md:11](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md:11)는 “최적 구조”라고 하지만, [04-convergence.md:106](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/04-convergence.md:106)의 근거는 일반 Stage-Gate, 내부 기획안과의 정합성, GSoC 중간평가 유추입니다. 비교 대안별 성과 데이터가 없으므로 “최적”이 아니라 “현재 근거상 가장 방어 가능한 후보 구조”가 맞습니다.

5. **R3를 Quick Win으로 둔 것은 R4/R5의 무거운 전제와 충돌**  
   R3는 “추가 리소스 불필요”라고 합니다([05-conclusion.md:49](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md:49), [97](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md:97)). 그러나 같은 운영 구조가 W3 Gate 2의 3-lane 리뷰와 Red lane 3인 승인, CoE 선행 구축에 의존합니다([05-conclusion.md:102](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md:102), [117](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md:117), [132](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md:132)). 문서화 자체는 쉽지만 실제 운영은 Quick Win이 아닙니다.

6. **CoE가 “파일럿 성공률을 결정”한다는 표현은 과장**  
   [05-conclusion.md:13](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md:13)는 KPMG 77% vs 39%를 파일럿 성공률처럼 사용합니다. 하지만 수렴 보고서의 원 표현은 “거버넌스 있는 조직 vs 없는 조직의 비용 절감 성공”입니다([04-convergence.md:42](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/04-convergence.md:42)). 비용 절감 성공률을 3주 탑다운 파일럿 성공률로 바꾸는 것은 지표 전환 오류입니다.

7. **챔피언 프로그램 부재 시 “파일럿 효과는 소멸”은 인과가 약함**  
   [05-conclusion.md:13](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md:13), [141](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md:141)는 DORA의 10주 지속 사용률 <10%를 챔피언 프로그램 필요성으로 연결합니다. 그러나 [04-convergence.md:72](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/04-convergence.md:72)는 챔피언 효과 수치가 단일 출처이고 독립 검증이 없다고 밝힙니다. “소멸한다”보다 “지속 사용 리스크가 크므로 개입이 필요하다”가 타당합니다.

8. **Go/No-Go 임계값 0.605를 그대로 채택한 것은 부적절**  
   [05-conclusion.md:84](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md:84), [87](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md:87)는 Visual Paradigm 예시의 0.605를 실제 파일럿 임계값처럼 넣습니다. 이는 범용 예시이지 AI FAB의 위험, 보안, 기술부채, 운영 이관 비용을 반영한 산식이 아닙니다. 특히 findings에는 배포 완성률 벤치마크가 없다고 되어 있습니다([q5-kpi-scaling.md:51](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/findings/q5-kpi-scaling.md:51)).

9. **가장 큰 전제 충돌: 내부 기획안은 ‘시티즌 개발자 탑다운 파일럿’을 직접 다루지 않음**  
   [q0-internal-docs.md:7](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/findings/q0-internal-docs.md:7)는 탑다운 과제 수행 주체가 “지정된 개발·운영 조직”이고 시티즌 개발자와 구분된다고 합니다. 또한 [q0-internal-docs.md:35](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/findings/q0-internal-docs.md:35) 이하에서 선발 기준, 3주 스프린트, 멘토링, KPI가 내부 문서에 없다고 명시합니다. 결론 보고서는 이 구조적 불일치를 핵심 리스크로 올리지 않았습니다.

10. **시티즌 개발자 선발 기준이 사실상 결론에서 빠짐**  
   문서 제목은 “시티즌 개발자 선발부터”라고 하지만, 결론의 8개 권고에는 선발 기준·절차가 독립 권고로 없습니다. 별도 finding에는 과제 제출·검토 2단계, 역할 구분, LG유플러스 등 선발 관련 근거가 있습니다([q1-selection-criteria.md:15](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/findings/q1-selection-criteria.md:15), [21](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/findings/q1-selection-criteria.md:21)). 이 누락은 원래 핵심 질문 1에 대한 미응답입니다.

11. **기술 부채 이관 기준은 “핵심 리스크”라면서 권고 우선순위에는 없음**  
   [05-conclusion.md:17](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md:17)에서 핵심 리스크로 인정하지만, [25-34](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md:25) 우선순위 매트릭스에는 독립 권고가 없습니다. [188](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/05-conclusion.md:188)에 “조건부 권고”로만 밀려 있습니다. 실제로는 R7보다 우선도가 높아야 합니다. 이 기준 없이는 배포 성공 후 운영 이관이 막힐 수 있습니다.

12. **미래/불확실 출처 처리 미흡**  
   04 수렴 보고서의 소스에는 2026-09, 2026-10 등 보고서 생성일 2026-07-11 이후 자료가 포함되어 있습니다([04-convergence.md:164](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/04-convergence.md:164), [170](/Users/jaybee/lab/AIFAB-plan/metasearch-aifab-topdown-pilot-ops-2026-07-11/04-convergence.md:170)). 05 결론에도 2026 자료들이 섞여 있으나 URL 검증이 대기 상태입니다. 보고서 날짜 기준으로 존재 여부와 접근 가능성을 재검증하지 않으면, 출처 신뢰도가 크게 흔들립니다.

**핵심 누락**

- 선발 기준: 참가자 역량, 과제 난이도, 업무 도메인, 보안 권한, 선발/탈락 프로세스가 결론 권고에 없음.
- 코호트 규모: 미해결이라고만 두고 운영 가능한 기본안이 없음.
- 3주 운영 상세: W1/W2/W3 문구는 있지만 산출물, 책임자, 승인 SLA, 실패 시 조치가 부족함.
- 기술 부채 수용 기준: 중복률, 테스트 커버리지, 취약점 0건, 리팩토링 범위, 운영팀 거부권 같은 이관 조건이 없음.
- 내부 기획안과의 주체 불일치: “지정 개발·운영 조직” 대 “시티즌 개발자”의 충돌을 해소하지 않음.

**종합 판단**

이 결론은 “골든 패스 + CoE + 게이트 + KPI 동결”이라는 큰 방향은 방어 가능하지만, 현재 형태는 근거 대비 표현이 강합니다. 최종본으로 쓰려면 `최적/필수/실현 가능/결정한다/소멸한다` 같은 단정 표현을 `조건부 권고/가설/리스크 완화 수단`으로 낮추고, 선발 기준·코호트 규모·기술 부채 이관 기준을 독립 권고로 올려야 합니다.
