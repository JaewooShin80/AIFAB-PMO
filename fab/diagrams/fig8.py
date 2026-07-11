from diagrams import Diagram, Cluster, Edge
from diagrams.aws.general import Users
from diagrams.aws.compute import Fargate
from diagrams.aws.devtools import Codepipeline, Codebuild
from diagrams.aws.security import Inspector
from diagrams.aws.management import Cloudwatch
from diagrams.onprem.vcs import Gitlab

FONT = "AppleGothic"
graph_attr = {
    "fontname": FONT,
    "fontsize": "16",
    "bgcolor": "white",
    "pad": "0.4",
    "nodesep": "0.7",
    "ranksep": "0.9",
}
node_attr = {"fontname": FONT, "fontsize": "11"}
edge_attr = {"fontname": FONT, "fontsize": "10"}

with Diagram(
    "탑다운 CI/CD 및 배포 구조 (스테이징 → 승인 게이트 → 운영)",
    filename="fig8-topdown-cicd",
    outformat="png",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
):
    with Cluster("탑다운 파이프라인 (Top-down 계정)"):
        git = Gitlab("Git 저장소\n(과제별 리포지토리)")
        pipe = Codepipeline("CodePipeline")
        build = Codebuild("CodeBuild\n(빌드·테스트·시크릿 검출)")
        scan = Inspector("이미지 스캔\n(ECR·Inspector)")
        stg = Fargate("스테이징 배포·검증\n(기능·성능·정책 준수)")

        git >> Edge(label="머지(PR)") >> pipe >> build >> scan
        scan >> Edge(label="스캔 통과") >> stg
        scan >> Edge(
            label="실패 시 차단·반려",
            style="dashed",
            color="red",
            fontcolor="red",
        ) >> git

    gate = Users("승인 게이트\n(AI Board·정보보호팀)")

    with Cluster("운영 환경 (상시 가동 · Multi-AZ)"):
        prod = Fargate("운영 배포\n(Blue/Green · 무중단)")
        mon = Cloudwatch("모니터링\n(SLO·오류율·알람)")
        prod >> mon

    stg >> Edge(label="검증 통과") >> gate
    gate >> Edge(label="승인 시") >> prod
    mon >> Edge(
        label="이상 시 자동 롤백",
        style="dashed",
        color="firebrick",
        fontcolor="firebrick",
    ) >> prod
