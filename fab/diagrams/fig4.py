from diagrams import Diagram, Cluster, Edge
from diagrams.aws.general import Users, TraditionalServer
from diagrams.aws.network import APIGateway
from diagrams.aws.compute import Lambda
from diagrams.aws.integration import StepFunctions, Eventbridge, SNS
from diagrams.aws.engagement import SES
from diagrams.aws.analytics import Athena, ElasticsearchService
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
    "AI Agent 아키텍처 (다각도 심사·트리아지 + 주간 리포트)",
    filename="fig4-ai-agent",
    outformat="png",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
):
    applicant = Users("신청자")

    with Cluster("심사 에이전트 (다각도 심사·트리아지)"):
        portal = TraditionalServer("신청 포털")
        apigw = APIGateway("API Gateway")
        intake = Lambda("접수 처리\n(필수 항목 검증)")
        wf = StepFunctions("심사 워크플로\n(Step Functions)")
        agent = Bedrock("Bedrock (Claude)\n다각도 판단·트리아지\n+ Guardrails")
        ddb = Dynamodb("심사 결과·판단 로그")

        with Cluster("Knowledge Base (RAG)"):
            kb = S3("정책·과제 카탈로그\n사내 AI 도구 카탈로그·심사 사례")
            oss = ElasticsearchService("OpenSearch\n(벡터 검색)")
            kb >> oss

        portal >> apigw >> intake >> wf >> agent
        oss >> Edge(label="근거 조회", style="dashed") >> agent
        agent >> ddb

    notify = SNS("보드 알림")
    board = Users("운영 보드\n(최종 승인, HITL)")
    tf = Terraform("Terraform\n(자원 프로비저닝)")

    applicant >> portal
    wf >> Edge(label="대화형 질문·답변", style="dashed", dir="both") >> applicant

    agent >> Edge(
        label="① 기존 도구 안내\n(A.Biz·Copilot 등 + 활용 가이드)",
        color="darkgreen",
        fontcolor="darkgreen",
    ) >> applicant
    agent >> Edge(
        label="③ 역량 준비 안내\n(사내 교육 후 재신청)",
        color="darkorange",
        fontcolor="darkorange",
        style="dashed",
    ) >> applicant
    agent >> Edge(label="② 샌드박스 배정 권고\n④ 보드 검토 회부") >> notify >> board
    board >> Edge(label="승인 시") >> tf
    board >> Edge(label="판정 피드백\n(기준 보정)", style="dashed") >> ddb

    with Cluster("주간 리포트 에이전트"):
        sched = Eventbridge("EventBridge\n(주간 스케줄)")
        agg = Athena("사용량 집계\n(CloudWatch·Athena·Databricks)")
        summ = Bedrock("Bedrock (Claude)\n리포트 요약 생성")
        mail = SES("SES 메일 발송\n·사내 위키 게시")
        sched >> agg >> summ >> mail
