# 골든 패스 deepdive — 3주 파일럿 사전 준비 체크리스트·AI 결합 발산 리서치

## 핵심 발견

- **IDP MVP 표준 스케줄은 "8주 MVP + 8주 Production Readiness = 총 16주"**로, 3주(21일) 파일럿에 골든 패스까지 갖추려면 최소한의 스캐폴딩·CI/CD·관측성만 갖춘 압축형 MVP를 사전에 확보해야 함 — **씨앗과의 관계: 신규** ([platformengineering.org](https://platformengineering.org/blog/how-to-set-up-an-internal-developer-platform), 날짜 미상, 2026 시점 유효)
- **MVP 8주는 2~4명 풀타임 엔지니어를 요구**하며, 사전 준비(Weeks 1-2)에서 "Discovery, 파일럿 팀 선정(Force Ranking), 골든 패스 식별, 스코프 락인"을 완료해야 배포까지 스프린트가 가능 — **씨앗과의 관계: 신규** ([platformengineering.org](https://platformengineering.org/blog/how-to-set-up-an-internal-developer-platform), 날짜 미상)
- **AWS 플랫폼팀이 먼저 만들 6대 골든 패스 순서는 ECS on Fargate → Lambda → RDS → 비용태그 → 관측성 → Secrets Manager**로 정의되어 있으며, 컨테이너·서버리스·DB·태그·관측·시크릿의 6영역이 최소 사전 구성 대상 — **씨앗과의 관계: 보강** ([The Cloud Playbook TCP#124](https://www.thecloudplaybook.com/p/first-6-golden-paths-aws-platform-teams), 날짜 미상)
- **각 템플릿의 사전 내장 구성요소가 구체 명세**됨: ECS(Task Def·ALB·ExecRole 최소권한·CloudWatch 리텐션·비용태그), Lambda(런타임 기본값·에러율 알람), RDS(env별 인스턴스 가드레일·암호화·백업 리텐션·삭제 보호·프라이빗 서브넷), 관측성(X-Ray, p99 지연 알람, 대시보드), Secrets(로테이션 포함) — **씨앗과의 관계: 신규** ([The Cloud Playbook TCP#124](https://www.thecloudplaybook.com/p/first-6-golden-paths-aws-platform-teams), 날짜 미상)
- **골든 패스 MVP 벤치마크: "제로 → 스테이징 배포 <1시간, 프로덕션 배포 <2시간"** — 3주 파일럿에서 시티즌 개발자가 배포까지 도달하려면 이 벤치마크에 준하는 골든 패스가 사전에 있어야 실현 가능 — **씨앗과의 관계: 보강** ([Tasrie IT Services](https://tasrieit.com/blog/golden-paths-platform-engineering-guide-2026), 2026)
- **골든 패스 파일럿 권고 방식: "30일 파일럿 + 명명된 오너 + 리뷰 케이던스 + 가시적 예외 경로"**, 그리고 초기 롤아웃은 "2~3개 자발 파일럿 팀"으로 제한 — 3주 스프린트 파일럿 운영에 그대로 이식 가능한 프레임 — **씨앗과의 관계: 신규** ([Microsoft Community Hub](https://techcommunity.microsoft.com/blog/azurearchitectureblog/golden-paths-are-a-product-treat-them-like-one-/4533707 ⚠(dead link)), 날짜 미상 / [platformengineering.org](https://platformengineering.org/blog/how-to-pave-golden-paths-that-actually-go-somewhere), 날짜 미상)
- **비전문가용 추상화 원칙: "buffet of choices 금지 → 단일·의견 있는 경로", "intent(성능·가용성) 입력 → 플랫폼이 concrete config로 해석"**, 스마트 기본값 + 티켓 없이 발견 가능한 셀프서비스 — 시티즌 개발자용 UX 설계 원칙에 직접 적용 — **씨앗과의 관계: 신규** ([DZone Golden Paths](https://dzone.com/articles/golden-paths-idps ⚠(dead link)), 날짜 미상 / [platformengineering.org 정의](https://platformengineering.org/blog/what-are-golden-paths-a-guide-to-streamlining-developer-workflows), 날짜 미상)
- **Backstage 1.43(2025-09)이 MCP 토큰 지원 실험 도입 + `@backstage/plugin-mcp-actions-backend` 정식 플러그인 출시**: Scaffolder 액션을 Claude·Cursor에 MCP 툴로 노출. AI가 `scaffold_new_service`, `provision_dev_environment` 등을 직접 호출 — **씨앗과의 관계: 신규** ([Medium — AI Transfer Lab](https://medium.com/@ai_transfer_lab/internal-developer-platforms-in-the-mcp-era-how-idp-teams-are-embedding-claude-as-a-first-class-846abc073117 ⚠(dead link)), 2026 / [Backstage docs](https://backstage.io/api/next/modules/_backstage_plugin-mcp-actions-backend.html))
- **Spotify Portal MCP는 통합 HTTP 엔드포인트(`/api/mcp-actions/v1`) + Streamable HTTP + Bearer 토큰**, CIMD(OAuth) 베타로 시크릿 저장 불필요. Scaffolder·Catalog·TechDocs가 MCP 툴로 노출 — 시티즌 개발자용 IDE(Claude Code 등)에 Scaffolder 직접 호출 가능한 아키텍처 확보 — **씨앗과의 관계: 보강** ([Spotify Backstage Portal MCP docs](https://backstage.spotify.com/docs/portal/core-features-and-plugins/mcp/overview), 2026)
- **Port April 2026 "Skills" 출시**: 카탈로그에 정의된 skill이 role 기반 권한으로 모든 MCP 호환 클라이언트에 자동 배포. 6월 릴리스에서 외부 MCP 서버 연결·AI 에이전트 workflows 시각 빌더 오픈베타 — **씨앗과의 관계: 신규** ([Port June 2026 릴리스노트](https://www.port.io/blog/product-release-notes-june-2026), 2026-06)
- **AI+IDP 통합의 데이터 품질 하드 요건**: Cortex 2025 벤치마크에서 "카탈로그 위생 없이 AI 도입 시 변경 실패율 +30%, PR당 인시던트 +23.5%". 3주 파일럿 전 카탈로그 정확도 확보가 필수 전제 — **씨앗과의 관계: 상충(주의)** ([Medium — AI Transfer Lab](https://medium.com/@ai_transfer_lab/internal-developer-platforms-in-the-mcp-era-how-idp-teams-are-embedding-claude-as-a-first-class-846abc073117 ⚠(dead link)), 2026)
- **Vista/Cortex 통합 결과: "서비스 오너 식별 자신감 +43%"** — 골든 패스에 카탈로그 소유권·메타데이터 사전 등록이 필요함을 시사 — **씨앗과의 관계: 보강** ([Medium — AI Transfer Lab](https://medium.com/@ai_transfer_lab/internal-developer-platforms-in-the-mcp-era-how-idp-teams-are-embedding-claude-as-a-first-class-846abc073117 ⚠(dead link)), 2026)
- **MCP 보안 아키텍처 3원칙**: (1) 태스크 스코프 토큰 → 작업 종료 시 만료, (2) 카탈로그 데이터 품질 하드 의존(80% 정확도로는 부족), (3) HTTP가 아닌 MCP 툴 호출 레이어에서 구조화 로깅 — **씨앗과의 관계: 신규** ([Medium — AI Transfer Lab](https://medium.com/@ai_transfer_lab/internal-developer-platforms-in-the-mcp-era-how-idp-teams-are-embedding-claude-as-a-first-class-846abc073117 ⚠(dead link)), 2026)

## 정량 데이터

| 항목 | 수치 | 출처 | 시점 |
|---|---|---|---|
| IDP MVP 구축 기간 | 8주 | platformengineering.org 구현 가이드 | 날짜 미상(2026 유효) |
| IDP Production Readiness 기간 | 8주 (MVP 이후) | platformengineering.org | 날짜 미상 |
| IDP 총 첫 프로덕션 배포까지 | 16주 | platformengineering.org | 날짜 미상 |
| MVP 팀 규모 | 풀타임 엔지니어 2~4명 | platformengineering.org | 날짜 미상 |
| 골든 패스 MVP 목표: 제로→스테이징 배포 | <1시간 | Tasrie IT Services | 2026 |
| 프로덕션 배포 목표 | <2시간(중앙값) | Tasrie IT Services | 2026 |
| 백엔드 마이크로서비스 골든 패스 스테이징 도달 | <15분 | Tasrie IT Services | 2026 |
| 프로덕션 확장 | 1일 이내 | Tasrie IT Services | 2026 |
| 서비스 추가 소요(플랫폼 전→후) | 16h → 8h | platformengineering.org | 날짜 미상 |
| 신규 개발자 온보딩(플랫폼 전→후) | 80h → 16h | platformengineering.org | 날짜 미상 |
| AWS 첫 6대 골든 패스 | ECS, Lambda, RDS, 태그, 관측성, Secrets | The Cloud Playbook TCP#124 | 날짜 미상 |
| 골든 패스 파일럿 권장 팀 수 | 2~3개 자발 팀 | platformengineering.org | 날짜 미상 |
| 골든 패스 파일럿 최소 기간 프레임 | 30일 + 명명된 오너·리뷰 케이던스 | Microsoft Community Hub | 날짜 미상 |
| 채택 실패 임계 | 90일 내 60% 미만 시 마찰 감사 | The Cloud Playbook TCP#124 | 날짜 미상 |
| 카탈로그 위생 없이 AI 도입 시 변경실패율 | +30% | Cortex 2025 벤치마크 (via Medium) | 2025 |
| 위와 동일, PR당 인시던트 | +23.5% | Cortex 2025 벤치마크 (via Medium) | 2025 |
| Vista/Cortex 소유권 식별 자신감 향상 | +43% | Medium — AI Transfer Lab | 2026 |
| Backstage MCP 지원 도입 버전 | 1.43 (2025-09) | Medium — AI Transfer Lab | 2025-09 |
| Port Skills 출시 | 2026-04 | Medium — AI Transfer Lab | 2026-04 |
| Port 외부 MCP 서버 연결 | 2026-06 릴리스 | Port 공식 블로그 | 2026-06 |
| AI 코딩 어시스턴트 사용 엔지니어 예측 | 90% by 2028 (초 2024 <14%) | Gartner (via Tasrie) | 2026 |

## 씨앗 보고서와의 관계 요약

- **보강**: 씨앗의 "1~2시간 첫 배포"·"플랫폼 없이 AI 단독=안정성 저하" 명제가 (a) 골든 패스 MVP의 <1h/<2h 스테이징/프로덕션 벤치마크, (b) Cortex 2025의 30%/23.5% 악화 수치로 이중 확증됨. Spotify Portal의 MCP 통합 엔드포인트·CIMD OAuth는 씨앗의 "AI+IDP MCP" 패턴을 구체 아키텍처로 뒷받침.
- **상충**: 완전 상충은 아니나 **경보 신호**로 "카탈로그 정확도 80% 미만이면 AI 도입이 오히려 실패율을 높인다"는 조건은 씨앗의 "MCP 통합=신규 패턴" 톤보다 훨씬 강한 전제조건을 요구.
- **신규**: (1) IDP 정석 16주(8+8) 대비 3주 파일럿의 압축 로드맵, (2) AWS 6대 골든 패스 순서와 각 템플릿 사전 내장 구성요소 체크리스트, (3) MVP 팀 2~4 FTE, (4) 골든 패스 30일 파일럿 프레임(오너·리뷰 케이던스·예외 경로), (5) 60% 채택 임계, (6) MCP 보안 3원칙(태스크 스코프 토큰·데이터 품질 하드 의존·툴 레이어 로깅), (7) Backstage 1.43/Port April 2026 Skills 릴리스 타임라인.

## 한계

- **비개발자·시티즌 개발자가 실제로 골든 패스로 배포한 케이스의 정량 사례**를 찾지 못함. 골든 패스 문헌은 "developer"를 대상으로 함이 지배적. 시티즌 개발자 특화 성공 사례는 별도 조사가 필요.
- **3주(21일) 스프린트 파일럿에 골든 패스 사전 준비를 몇 명·몇 주 전에 시작해야 하는지의 직접 벤치마크는 없음**. 다만 16주 MVP 정석과 30일 파일럿 프레임을 조합해 역산 가능.
- **AI 에이전트가 MCP를 통해 실제로 프로덕션 배포까지 자동 수행한 성공 사례의 정량 데이터**(배포 시간 단축률 등)는 확보하지 못함. 대부분 카탈로그 조회·스캐폴딩 단계에 한정된 실험 사례.
- Backstage MCP 실제 프로덕션 사용 사례는 저자 스스로 "development environment only"로 스코프 제한을 명시.

## 출처

- https://platformengineering.org/blog/how-to-set-up-an-internal-developer-platform (platformengineering.org 구현 가이드, 날짜 미상)
- https://www.thecloudplaybook.com/p/first-6-golden-paths-aws-platform-teams (The Cloud Playbook TCP#124, 날짜 미상)
- https://tasrieit.com/blog/golden-paths-platform-engineering-guide-2026 (Tasrie IT Services, 2026)
- https://techcommunity.microsoft.com/blog/azurearchitectureblog/golden-paths-are-a-product-treat-them-like-one-/4533707 ⚠(dead link) (Microsoft Community Hub, 날짜 미상)
- https://platformengineering.org/blog/how-to-pave-golden-paths-that-actually-go-somewhere (platformengineering.org, 날짜 미상)
- https://platformengineering.org/blog/what-are-golden-paths-a-guide-to-streamlining-developer-workflows (platformengineering.org 정의, 날짜 미상)
- https://dzone.com/articles/golden-paths-idps ⚠(dead link) (DZone, 날짜 미상)
- https://medium.com/@ai_transfer_lab/internal-developer-platforms-in-the-mcp-era-how-idp-teams-are-embedding-claude-as-a-first-class-846abc073117 ⚠(dead link) (Medium — AI Transfer Lab, 2026)
- https://backstage.spotify.com/docs/portal/core-features-and-plugins/mcp/overview (Spotify Backstage Portal MCP 공식 문서, 2026)
- https://backstage.io/api/next/modules/_backstage_plugin-mcp-actions-backend.html (Backstage 공식 플러그인 API, 2026)
- https://www.port.io/blog/product-release-notes-june-2026 (Port 공식 릴리스 노트, 2026-06)
- https://nitin15j.medium.com/turning-backstage-into-an-ai-ready-platform-with-mcp-2412bf744a64 (Medium — Nitin Jain, 2026)
