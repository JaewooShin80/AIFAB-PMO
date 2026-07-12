# [비판 관점 — 시티즌 개발자 프로덕션 배포 위험론] 발산 리서치

## 핵심 발견

- **AI 생성 코드는 인간 코드보다 취약점 밀도가 2.74배 높으며, 45%가 보안 결함 포함** — 씨앗의 "CI/CD 자동 검사"가 이를 100% 차단할 수 없음을 시사. XSS 방어 실패율 85%, 로그 인젝션 88% — **씨앗과의 관계: 상충** ([Veracode Spring 2026 GenAI Code Security Report](https://www.veracode.com/blog/spring-2026-genai-code-security/), 2026-04)

- **Fortune 50 기업 내 AI 코딩 도구 도입 후 월간 보안 발견 건수가 1,000건→10,000건(6개월, 10배 급증)** — 속도 4배 향상이 아키텍처 결함 322%, 권한 상승 경로 153% 증가와 동반; 자동화 SAST가 놓치는 아키텍처 계층 결함이 핵심 — **씨앗과의 관계: 신규** ([Apiiro, 4x Velocity 10x Vulnerabilities](https://apiiro.com/blog/4x-velocity-10x-vulnerabilities-ai-coding-assistants-are-shipping-more-risks/), 2025)

- **시티즌 개발 앱의 대부분은 아키텍처 검토·보안 테스트·변경 관리 절차를 전혀 거치지 않음** — "대부분의 비즈니스 구축 앱이 보안 검증을 받지 못한다"는 실태 보고; 씨앗의 "수동 승인 게이트"가 앱 계층 위험까지 커버하는지 불분명 — **씨앗과의 관계: 상충** ([Pluto Security, Citizen Development: When Apps Bypass Security Teams](https://pluto.security/blog/citizen-development-security-teams/), 2024)

- **GitClear 211M 라인 분석: AI 도구 채택 후 코드 중복 8배 증가(2024년), 리팩토링 활동 -60%(2021→2024)** — 3주 스프린트 이후의 유지보수성이 심각히 훼손될 수 있음; "6~12개월 후 유지보수 위기" 예측 — **씨앗과의 관계: 신규** ([GitClear AI Code Quality Research 2025](https://www.gitclear.com/ai_assistant_code_quality_2025_research ⚠(dead link)), 2025-02)

- **Vibe coding 기술 부채는 지수적으로 누적되며, PR 8.1M건 분석에서 AI 도구 채택 후 기술 부채 30~41% 증가 확인** — 비전문가가 컨텍스트 없이 AI 생성 코드를 반복 수정할수록 누적 속도가 가속 — **씨앗과의 관계: 신규** ([Pixelmojo, Vibe Coding Technical Debt Crisis 2026-2027](https://www.pixelmojo.io/blogs/vibe-coding-technical-debt-crisis-2026-2027), 2026)

- **IT 리더 73%가 시티즌 개발자 데이터 무결성 위험을, 69%가 보안 취약점을 주요 우려로 꼽음** — 씨앗 기획안의 CoE 2~5명 규모가 대규모 비전문가 앱 배포 통제에 충분한지 의문 — **씨앗과의 관계: 보강** ([Flosum, The Unintended Security Threat of Citizen Development](https://www.flosum.com/blog/the-unintended-security-threat-of-citizen-development), 2024)

- **자동화 CI/CD 스캔은 로직 결함·아키텍처 결함·비즈니스 로직 오류를 탐지하지 못함** — 인간 리뷰어가 필수적이나 씨앗의 CoE 멘토 2~5명으로 모든 PR을 심층 리뷰하는 것은 물리적으로 불가능 — **씨앗과의 관계: 상충** ([Checkmarx, 2025 CISO Guide to Securing AI-Generated Code](https://checkmarx.com/blog/ai-is-writing-your-code-whos-keeping-it-secure/), 2025)

- **보안 훈련은 시티즌 개발자 보안 문제를 해결하지 못함** — 규모·속도·다양성이 사용자 교육의 한계를 초과; 개발 경험 내 기술적 통제 임베딩이 필요하다는 주장. 씨앗의 "오피스아워·1:1 멘토링" 중심 지원 체계의 한계 — **씨앗과의 관계: 상충** ([TechNewsWorld, Why Training Won't Solve the Citizen Developer Security Problem](https://www.technewsworld.com/story/why-training-wont-solve-the-citizen-developer-security-problem-179877.html ⚠(dead link)), 2024)

- **단기 스프린트 압박은 구조적으로 기술 부채를 유발** — Scrum/Agile 연구: 타이트한 마감 압박 시 팀원들이 의도적으로 차선책 코드를 선택하며, 이는 이후 개발 속도를 저하시키고 팀 번아웃을 유발. 시티즌 개발자(비전문가)에게는 이 압박이 더 크게 작용 — **씨앗과의 관계: 신규** ([Everlaw, How Sprinting Slows You Down](https://www.everlaw.com/blog/ediscovery-software/how-sprinting-slows-you-down/), 2024)

- **AI 생성 코드의 아키텍처 수준 결함(CWE-131, CWE-190, CWE-916)은 시스템적 패턴이며, 단순 엣지 케이스가 아님** — 논문은 "AI 모델이 안정적으로 취약점 없는 코드를 생성하는 메커니즘이 없다"고 결론 — **씨앗과의 관계: 상충** ([arXiv, Broken by Default: Formal Verification Study of Security Vulnerabilities in AI-Generated Code](https://arxiv.org/pdf/2604.05292), 2026-04)

---

## 정량 데이터

| 항목 | 수치 | 출처 | 시점 |
|---|---|---|---|
| AI 생성 코드 보안 통과율 | 55% (45% 결함 포함) | Veracode Spring 2026 GenAI Report | 2026-04 |
| AI 코드 대비 인간 코드 취약점 밀도 | 2.74배 높음 | Veracode 2025 GenAI Code Security Report | 2025 |
| Fortune 50 월간 보안 발견 건수 변화 | 1,000건 → 10,000건 (6개월, +10배) | Apiiro Fortune 50 Research | 2025 |
| 아키텍처 결함(Privilege escalation) 증가 | +322% | Apiiro, AI 코딩 도구 도입 후 | 2025 |
| XSS 방어 실패율 | 85% (15% 통과) | Veracode Spring 2026 | 2026-04 |
| 로그 인젝션 실패율 | 87% (13% 통과) | Veracode Spring 2026 | 2026-04 |
| AI 도구 채택 후 코드 중복 증가 | 8배 (2024년) | GitClear, 211M 라인 분석 | 2025-02 |
| 리팩토링 활동 감소 | -60% (25% → 10%, 2021-2024) | GitClear | 2025-02 |
| AI 도구 채택 후 기술 부채 증가 | 30~41% | 8.1M PR 분석 (Pixelmojo 인용) | 2026 |
| IT 리더의 시티즌 개발자 데이터 무결성 우려 | 73% | Flosum 시티즌 개발 보안 보고서 | 2024 |
| IT 리더의 시티즌 개발자 보안 취약점 우려 | 69% | Flosum 시티즌 개발 보안 보고서 | 2024 |
| 공식 거버넌스 정책 보유 기업 (2024 기준) | 42% (2026: 78%로 증가) | Ainformat Citizen Developer Report | 2026 |
| GitHub Copilot 코드 보안 약점 포함 비율 | 29.5%(Python), 24.2%(JS) | 733 Copilot 스니펫 경험적 연구(2024) | 2024 |
| Vibe coding 보안 취약점 포함률 | 45% | Stack Overflow / Veracode 복수 출처 | 2025 |
| 개발자의 AI 출력 무검증 신뢰 비율 | 58% | 업계 조사 (devtechinsights) | 2025 |

---

## 씨앗 보고서와의 관계 요약

- **보강**: IT 리더 다수(73%/69%)가 시티즌 개발자 데이터·보안 위험을 인식하고 있으며, 이는 씨앗의 수동 승인 게이트·CoE 지원 체계의 필요성을 뒷받침한다. 거버넌스 정책 보유 기업이 2024년 42%에서 2026년 78%로 증가하는 추세는 씨앗 접근 방식의 방향성과 일치한다.

- **상충**: (1) Veracode·Apiiro 연구는 CI/CD 자동 검사가 아키텍처 결함·XSS·로직 오류를 구조적으로 탐지하지 못함을 보여, 씨앗의 "Critical/High 취약점 0건" 자동 검사 게이트가 과신될 수 있음. (2) 보안 훈련(오피스아워·멘토링)이 규모·속도 문제 앞에서 불충분하다는 비판이 씨앗의 CoE 2~5명 체계를 직접 겨냥. (3) 시티즌 개발 앱 대부분이 보안 검증을 받지 못한다는 실태 보고는, 수동 승인 게이트가 실제로 작동하지 않는 환경적 압력을 시사.

- **신규**: (1) GitClear의 코드 중복 8배·리팩토링 -60% 데이터는 3주 스프린트 완료 후 장기 유지보수성 위기를 예측하는 새로운 근거. (2) Apiiro의 "속도 4배 = 아키텍처 결함 322%" 트레이드오프는 씨앗에서 다루지 않은 숨겨진 비용. (3) AI 기술 부채의 지수적 누적 메커니즘(컨텍스트 없이 반복 수정→6~12개월 후 유지보수 위기)은 파일럿 종료 후 이관팀이 부담을 떠안는 시나리오를 제기.

---

## 한계

- 3주 스프린트 + 시티즌 개발자 + AI 코딩 도구의 조합을 직접 평가한 대조 실험 연구를 찾지 못함 (씨앗과 동일한 한계).
- CoE 멘토링의 실효성에 대한 정량적 연구는 이번 조사 범위 내에서 미확보; CoE 성숙 주기(2~4년)와 3주 파일럿 간 시간 불일치에 대한 공개 데이터 부재.
- 시티즌 개발자 프로그램 종료 후 이관팀의 기술 부채 처리 비용에 대한 사례 연구 부재.
- Apiiro Fortune 50 데이터는 전문 개발자 대상이며, 비전문 시티즌 개발자에게는 더 불리한 결과가 예상되나 직접 비교 데이터 없음.

---

## 출처

- [Veracode, Spring 2026 GenAI Code Security Report](https://www.veracode.com/blog/spring-2026-genai-code-security/) (Veracode, 2026-04)
- [Apiiro, 4x Velocity 10x Vulnerabilities: AI Coding Assistants Are Shipping More Risks](https://apiiro.com/blog/4x-velocity-10x-vulnerabilities-ai-coding-assistants-are-shipping-more-risks/) (Apiiro, 2025)
- [Pluto Security, Citizen Development: When Apps Bypass Security Teams](https://pluto.security/blog/citizen-development-security-teams/) (Pluto Security, 2024)
- [GitClear, AI Copilot Code Quality: 2025 Data Suggests 4x Growth in Code Clones](https://www.gitclear.com/ai_assistant_code_quality_2025_research ⚠(dead link)) (GitClear, 2025-02)
- [Pixelmojo, Vibe Coding Technical Debt Crisis 2026-2027](https://www.pixelmojo.io/blogs/vibe-coding-technical-debt-crisis-2026-2027) (Pixelmojo, 2026)
- [Flosum, The Unintended Security Threat of Citizen Development](https://www.flosum.com/blog/the-unintended-security-threat-of-citizen-development) (Flosum, 2024)
- [Checkmarx, 2025 CISO Guide to Securing AI-Generated Code](https://checkmarx.com/blog/ai-is-writing-your-code-whos-keeping-it-secure/) (Checkmarx, 2025)
- [TechNewsWorld, Why Training Won't Solve the Citizen Developer Security Problem](https://www.technewsworld.com/story/why-training-wont-solve-the-citizen-developer-security-problem-179877.html ⚠(dead link)) (TechNewsWorld, 2024)
- [arXiv, Broken by Default: Formal Verification Study of Security Vulnerabilities in AI-Generated Code](https://arxiv.org/pdf/2604.05292) (arXiv, 2026-04)
- [arXiv, Faster Code, Deeper Debt? LLM-Assisted Software Development Technical Debt](https://arxiv.org/pdf/2606.14796) (arXiv, 2026-06)
- [Veracode Blog, AI-Generated Code Security Risks](https://www.veracode.com/blog/ai-generated-code-security-risks/) (Veracode, 2024)
- [SQ Magazine, AI Coding Security Vulnerability Statistics 2026](https://sqmagazine.co.uk/ai-coding-security-vulnerability-statistics/) (SQ Magazine, 2026)
- [Everlaw, How Sprinting Slows You Down](https://www.everlaw.com/blog/ediscovery-software/how-sprinting-slows-you-down/) (Everlaw, 2024)
- [Kissflow, Risks Associated with Citizen Development](https://kissflow.com/faq/risks-associated-with-citizen-development) (Kissflow, 2024)
- [Cybersierra, The Citizen Developer Problem: Managing Non-Technical AI Coders](https://cybersierra.co/blog/securing-ai-coders/ ⚠(dead link)) (Cybersierra, 2025)
