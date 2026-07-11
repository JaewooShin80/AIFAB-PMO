from diagrams import Diagram, Cluster, Edge
from diagrams.aws.general import General, Users
from diagrams.aws.compute import Lambda, Fargate
from diagrams.aws.security import Macie
from diagrams.aws.storage import S3
from diagrams.aws.database import RDS
from diagrams.aws.management import Cloudwatch
from diagrams.onprem.analytics import Databricks

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
    "ranksep": "0.8",
}
node_attr = {"fontname": FONT, "fontsize": "11"}
edge_attr = {"fontname": FONT, "fontsize": "10"}

with Diagram(
    "데이터 흐름도 (반입 → 사용 → 텔레메트리 → 리포트)",
    filename="fig6-data-flow",
    outformat="png",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
):
    with Cluster("사내 데이터 원천"):
        src = General("운영 데이터\n(원본 반출 금지)")
        mask = Lambda("마스킹·비식별 처리\n(반입 승인 절차)")
        src >> mask

    with Cluster("샌드박스 데이터 영역"):
        macie = Macie("Macie\n실데이터 유입 탐지")
        landing = S3("Landing 버킷\n(KMS 암호화)")
        app = Fargate("과제 앱")
        db = RDS("과제 DB")

        macie >> Edge(style="dashed") >> landing
        landing >> app >> db

    external = General("사외 접근·반출")

    mask >> Edge(label="승인된 반입") >> landing
    landing >> Edge(label="차단(Block)", style="dashed", color="red", fontcolor="red") >> external

    with Cluster("텔레메트리·리포트"):
        cw = Cloudwatch("사용량·로그 수집")
        logs = S3("로그 버킷")
        dbx = Databricks("Databricks\n(집계·분석)")
        report = Bedrock("주간 리포트 생성")

        cw >> logs >> dbx >> report

    board = Users("보드·경영진")

    app >> Edge(label="사용 로그·텔레메트리") >> cw
    report >> board
