from diagrams import Diagram, Cluster, Edge
from diagrams.aws.general import Users, TraditionalServer
from diagrams.aws.integration import Eventbridge, SNS
from diagrams.aws.engagement import SES
from diagrams.aws.analytics import Athena
try:
    from diagrams.aws.analytics import AmazonOpensearchService as OpenSearchNode
except ImportError:
    from diagrams.aws.analytics import ElasticsearchService as OpenSearchNode
from diagrams.aws.storage import S3
from diagrams.aws.database import Dynamodb
from diagrams.onprem.iac import Terraform

try:
    from diagrams.aws.ml import Bedrock
except ImportError:
    from diagrams.aws.ml import Sagemaker as Bedrock

FONT = "AppleGothic"
graph_attr = {
    "fontname": FONT,
    "fontsize": "16",
    "bgcolor": "white",
    "pad": "0.4",
    "nodesep": "0.6",
    "ranksep": "0.9",
}
node_attr = {"fontname": FONT, "fontsize": "11"}
edge_attr = {"fontname": FONT, "fontsize": "10"}

with Diagram(
    "AI Agent 아키텍처 (가이드 챗봇 — 도구 추천·심사 판정 + 주간 리포트)",
    filename="fig4-ai-agent",
    outformat="png",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
):
    applicant = Users("신청자")

    with Cluster("가이드 챗봇 (도구 추천·심사 판정)"):
        portal = TraditionalServer("AI Portal")
        bot = Bedrock("가이드 챗봇 (Claude)\n대화형 상담 + Guardrails")
        ddb = Dynamodb("판정 결과·대화 로그")

        with Cluster("Knowledge Base (RAG)"):
            kb = S3("사내 AI 도구 카탈로그\n정책·사용법 가이드·판정 사례")
            oss = OpenSearchNode("OpenSearch\n(벡터 검색)")
            kb >> oss

        portal >> bot
        oss >> Edge(label="근거 조회", style="dashed") >> bot
        bot >> ddb

    notify = SNS("보드 알림")
    board = Users("운영 보드\n(승인 결정, HITL)")
    tf = Terraform("Terraform\n(Sandbox 배정·프로비저닝)")

    applicant >> Edge(label="AI Portal 접속") >> portal
    bot >> Edge(
        label="대화형 질문·답변\n(개인/팀 용도·데이터 현황 확인)",
        style="dashed",
        dir="both",
    ) >> applicant

    bot >> Edge(
        label="① 상용 툴 추천 + 사용법 가이드\n(A.Biz·MS Copilot·Copilot Studio·Databricks)",
        color="darkgreen",
        fontcolor="darkgreen",
    ) >> applicant
    bot >> Edge(
        label="② 자격 미충족: 교육 안내\n(Green Belt 이상·VS Code 사용 요건)",
        color="darkorange",
        fontcolor="darkorange",
        style="dashed",
    ) >> applicant
    bot >> Edge(label="③ AI 최종 판정: 승인/미승인/보류\n(근거 리포트 송부)") >> notify >> board
    board >> Edge(label="승인 결정 시\nSandbox 배정·진입") >> tf
    board >> Edge(label="판정 피드백\n(기준 보정)", style="dashed") >> ddb

    with Cluster("주간 리포트 에이전트"):
        sched = Eventbridge("EventBridge\n(주간 스케줄)")
        agg = Athena("사용량 집계\n(CloudWatch·Athena·Databricks)")
        summ = Bedrock("Bedrock (Claude)\n리포트 요약 생성")
        mail = SES("SES 메일 발송\n·사내 위키 게시")
        sched >> agg >> summ >> mail
