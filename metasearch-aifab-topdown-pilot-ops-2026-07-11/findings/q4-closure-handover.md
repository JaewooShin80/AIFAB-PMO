# 파일럿 과제 배포 후 종료 처리 절차

## 핵심 발견

- **이관 vs 폐기 판단은 사전 정의된 성공 기준 기반 Go/No-Go 결정으로 수행**: 파일럿 시작 전에 성공 기준을 합의하고, 종료 시 조직된 증거(성공 기준 충족 여부)를 근거로 Scale/Stop/Redirect 중 하나를 결정한다. 결정 권한자(named decision owner)를 사전에 지정하는 것이 핵심 거버넌스 요건이다. ([Traction Technology, 날짜 미상](https://www.tractiontechnology.com/blog/how-to-run-a-successful-pilot-with-a-startup-frameworks-kpis-enterprise-best-practices))

- **파일럿 종료 후 클로저 레코드(Closure Record) 15-20분 내 작성 필수**: ①테스트 내용·파라미터, ②성공 기준 대비 실제 결과, ③Scale/Stop/Redirect 결정과 근거, ④향후 동일 기술 범주 평가에 적용할 2-3가지 학습 사항을 포함하며, 팀 변경과 관계없이 조직 소유 시스템에 영구 보존해야 한다. ([Traction Technology, 날짜 미상](https://www.tractiontechnology.com/blog/how-to-run-a-successful-pilot-with-a-startup-frameworks-kpis-enterprise-best-practices))

- **Go/No-Go 스코어카드는 4개 영역(기술·재무·시장·자원) 가중 점수로 정량화**: 기술 40%, 재무 30%, 시장 20%, 자원 10% 등 가중치를 사전 배정하고 최종 점수 임계값(예: 0.605 이상)을 통과해야 운영 이관을 승인한다. ([Visual Paradigm, 날짜 미상](https://guides.visual-paradigm.com/making-informed-decisions-with-a-go-no-go-checklist-for-agile-projects-a-scoring-approach/))

- **운영 이관은 완료 날짜가 아닌 '전환 과정'으로 설계**: 이관 체크리스트는 ①이관 산출물 사전 합의(내용·시기·형식), ②운영팀의 조직적·운영적 준비 확인, ③문서(운영 매뉴얼·트러블슈팅 매뉴얼·교육 기록·안전 파일) 완비, ④이관 후 현장 지원 체계 구축 등 4개 핵심 항목으로 구성된다. ([Owner Team Consultation, 날짜 미상](https://www.ownerteamconsult.com/effective-handover-of-projects-to-operations-teams/))

- **애플리케이션 폐기(Decommissioning) 판단 기준**: ①활성 사용자 수 또는 트랜잭션이 정의된 임계값 미만, ②유지보수 비용이 비즈니스 가치 대비 과도, ③기술 스택 노후화(미지원 플랫폼), ④보안·컴플라이언스 기준 미충족, ⑤다른 시스템이 동등 이상의 기능 제공 등 5개 기준으로 결정한다. ([SparxSystems, 날짜 미상](https://www.sparxsystems.us/application-portfolio-management/application-lifecycle-states-sunset-policy/))

- **애플리케이션 폐기 9단계 절차**: ①계획·평가 → ②종속성 매핑 → ③데이터 분류·보존 정의 → ④데이터 추출·아카이빙 → ⑤테스트·검증(UAT) → ⑥사용자 커뮤니케이션 → ⑦시스템 단계적 종료 → ⑧문서화·거버넌스 증거 기록 → ⑨지속적 보존 관리(분기별 정책 재검토). ([Archon Data Store, 날짜 미상](https://www.archondatastore.com/blog/application-decommissioning-retirement/))

- **AWS Innovation Sandbox 솔루션의 계정 라이프사이클 자동화**: 계정은 Entry→CleanUp→Available→Active→Frozen→CleanUp의 상태 머신으로 관리되며, 임계값(비용 또는 기간) 초과 시 Frozen 상태로 자동 전환되어 사용자 접근이 차단된다. 정리 실패 시 Quarantine 상태로 격리되어 관리자 수동 복구가 필요하다. 운영 이관이 결정된 계정은 Eject(Exit OU로 이동)하여 계정 풀에서 영구 분리할 수 있다. ([AWS Docs, 날짜 미상](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/account-lifecycle-in-isb.html))

- **AWS Control Tower 해제(Decommissioning) 시 자동 처리 항목**: 탐지 제어(Detective Control) 비활성화, SCP 제거, CloudFormation StackSet·Stack 삭제, Account Factory 계정 레코드 삭제, AWS Service Catalog에서 계정·포트폴리오 제거가 자동으로 수행된다. 단, CloudWatch Logs 그룹(`aws-controltower/CloudTrailLogs`)과 S3 예약 버킷 2개는 **수동 삭제** 필요하다. ([AWS Docs - Control Tower, 날짜 미상](https://docs.aws.amazon.com/controltower/latest/userguide/decommissioning-process-overview.html))

- **AWS Organizations 계정 정리 시 30일 한도 및 90일 복구 기간 존재**: 계정 폐쇄 후 90일 이내 복구 가능하며, 30일 내 폐쇄 가능 계정 수는 규모에 따라 최대 10개(100개 미만 조직) ~ 전체의 10%(100~10,000개 조직) ~ 최대 1,000개(10,000개 초과)로 제한된다. 정리 대상 식별 기준은 3개월 연속 $100 미만 지출 계정이다. ([AWS Cloud Operations Blog, 날짜 미상](https://aws.amazon.com/blogs/mt/streamlining-aws-organizations-cleanup-strategies/))

- **회고(Retrospective) KPI는 액션 아이템 완료율·참여율·팀 행복도·사이클 타임으로 정량화**: 매 스프린트 회고에서 팀원의 행복도 점수(임의 척도)를 기록하고 추세를 추적하며, 이전 회고 액션 아이템 완료율을 다음 회고 첫 번째 의제로 점검하는 것이 권장된다. ([Gulf Coast Trade Institute, 날짜 미상](https://gulfcoasttradeinstitute.com/measuring-retrospective-effectiveness/))

## 정량 데이터

| 항목 | 수치 | 출처 | 시점 |
|---|---|---|---|
| 파일럿 표준 기간 | 60-90일 | [Traction Technology](https://www.tractiontechnology.com/blog/how-to-run-a-successful-pilot-with-a-startup-frameworks-kpis-enterprise-best-practices) | 날짜 미상 |
| 파일럿 마일스톤 체크포인트 | 4개 (킥오프·20-30일·40-50일·55-65일) | [Traction Technology](https://www.tractiontechnology.com/blog/how-to-run-a-successful-pilot-with-a-startup-frameworks-kpis-enterprise-best-practices) | 날짜 미상 |
| 클로저 레코드 작성 소요 시간 | 15-20분 | [Traction Technology](https://www.tractiontechnology.com/blog/how-to-run-a-successful-pilot-with-a-startup-frameworks-kpis-enterprise-best-practices) | 날짜 미상 |
| 정체 감지 → 대응 기한 | 48시간 이내 (2주 무응답 또는 1주 미해결 전제조건 발견 시) | [Traction Technology](https://www.tractiontechnology.com/blog/how-to-run-a-successful-pilot-with-a-startup-frameworks-kpis-enterprise-best-practices) | 날짜 미상 |
| Innovation Sandbox 자동 접근 회수 | Frozen 상태 후 14일 | [AWS Publicsector Blog](https://aws.amazon.com/blogs/publicsector/empowering-educators-how-innovation-sandbox-on-aws-accelerates-learning-objectives-through-secure-cost-effective-and-recyclable-sandbox-management/) | 날짜 미상 |
| Innovation Sandbox 자동 리소스 삭제 | 21일 (관리자 보존 지정 없을 시) | [AWS Publicsector Blog](https://aws.amazon.com/blogs/publicsector/empowering-educators-how-innovation-sandbox-on-aws-accelerates-learning-objectives-through-secure-cost-effective-and-recyclable-sandbox-management/) | 날짜 미상 |
| AWS 계정 폐쇄 후 복구 가능 기간 | 90일 이내 | [AWS Cloud Operations Blog](https://aws.amazon.com/blogs/mt/streamlining-aws-organizations-cleanup-strategies/) | 날짜 미상 |
| AWS 정리 대상 식별 비용 임계값 | 3개월 연속 $100 미만 | [AWS Cloud Operations Blog](https://aws.amazon.com/blogs/mt/streamlining-aws-organizations-cleanup-strategies/) | 날짜 미상 |
| 레거시 시스템이 IT 예산 점유율 | 60-80% | [Archon Data Store](https://www.archondatastore.com/blog/application-decommissioning-retirement/) | 날짜 미상 |
| 개별 앱 폐기 시 비용 절감률 | 80-90% | [Archon Data Store](https://www.archondatastore.com/blog/application-decommissioning-retirement/) | 날짜 미상 |
| Go/No-Go 스코어카드 통과 임계값 예시 | 0.605 이상 (가중 점수) | [Visual Paradigm](https://guides.visual-paradigm.com/making-informed-decisions-with-a-go-no-go-checklist-for-agile-projects-a-scoring-approach/) | 날짜 미상 |
| 파일럿 단계적 확대 배율 | 5%→10%→20%→40%→80%→100% | [LogRocket Blog](https://blog.logrocket.com/product-management/pilot-project-guide/) | 날짜 미상 |

## 한계

- **사내 IT 파일럿(시티즌 개발자 대상) 특화 이관 기준 미확보**: 검색 결과는 대부분 스타트업-엔터프라이즈 파일럿 또는 대규모 인프라 폐기 사례 중심이며, AI 코딩 도구 활용 시티즌 개발자 파일럿의 이관 기준에 특화된 1차 출처는 부재하다.
- **한국어 1차 출처(국내 파일럿 이관 사례) 부재**: 국내 기업의 파일럿 프로젝트 운영 이관 기준이나 AWS 리소스 회수 가이드라인에 관한 공개 1차 출처를 발견하지 못했다.
- **AWS Control Tower 수동 정리 항목의 완전한 목록 미확보**: 공식 문서에 일부 항목(CloudWatch Logs 그룹, S3 버킷)만 명시되어 있으며, 실제 환경에 따라 추가 수동 정리 항목이 존재할 수 있다.
- **비용 임계값 수치의 보편성 한계**: AWS가 제시한 $100 기준은 권고 기준이며 조직 규모·워크로드 특성에 따라 조정이 필요하다.

## 출처

- https://www.tractiontechnology.com/blog/how-to-run-a-successful-pilot-with-a-startup-frameworks-kpis-enterprise-best-practices (Traction Technology, 날짜 미상)
- https://guides.visual-paradigm.com/making-informed-decisions-with-a-go-no-go-checklist-for-agile-projects-a-scoring-approach/ (Visual Paradigm, 날짜 미상)
- https://www.ownerteamconsult.com/effective-handover-of-projects-to-operations-teams/ (Owner Team Consultation, 날짜 미상)
- https://www.sparxsystems.us/application-portfolio-management/application-lifecycle-states-sunset-policy/ (SparxSystems, 날짜 미상)
- https://www.archondatastore.com/blog/application-decommissioning-retirement/ (Archon Data Store, 날짜 미상)
- https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/account-lifecycle-in-isb.html (AWS Docs - Innovation Sandbox, 날짜 미상)
- https://docs.aws.amazon.com/controltower/latest/userguide/decommissioning-process-overview.html (AWS Docs - Control Tower, 날짜 미상)
- https://aws.amazon.com/blogs/mt/streamlining-aws-organizations-cleanup-strategies/ (AWS Cloud Operations Blog, 날짜 미상)
- https://aws.amazon.com/blogs/mt/best-practices-creating-managing-sandbox-accounts-aws/ (AWS Cloud Operations Blog, 날짜 미상)
- https://allcloud.io/blog/emea-il-key-concepts-for-sandbox-accounts-management/ (AllCloud Blog, 날짜 미상)
- https://aws.amazon.com/blogs/publicsector/empowering-educators-how-innovation-sandbox-on-aws-accelerates-learning-objectives-through-secure-cost-effective-and-recyclable-sandbox-management/ (AWS Public Sector Blog, 날짜 미상)
- https://blog.logrocket.com/product-management/pilot-project-guide/ (LogRocket Blog, 날짜 미상)
- https://gulfcoasttradeinstitute.com/measuring-retrospective-effectiveness/ (Gulf Coast Trade Institute, 날짜 미상)
- https://www.solix.com/products/answers/application-decommissioning-checklist/ (Solix Technologies, 날짜 미상)
