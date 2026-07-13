from diagrams import Diagram, Cluster, Edge
from diagrams.aws.general import Users
from diagrams.aws.compute import EC2, Fargate, ECR
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
    "CI/CD 및 배포 구조 (바텀업: dev 배포까지 · 운영급 배포는 격상 후 탑다운)",
    filename="fig5-cicd",
    outformat="png",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
):
    with Cluster("바텀업 파이프라인 (Bottom-up Sandbox 계정 · 시간제 가동)"):
        git = Gitlab("Git 저장소\n(과제별 리포지토리)")
        pipe = Codepipeline("CodePipeline")
        build = Codebuild("CodeBuild\n(빌드·테스트·시크릿 검출)")
        ecr = ECR("ECR\n(이미지 저장소·Tag 불변)")
        scan = Inspector("이미지 스캔\n(Inspector)")
        dev = Fargate("dev 배포\n(샌드박스 Fargate · 자동)")
        mon = Cloudwatch("배포 후 모니터링\n(오류율·사용량 알람)")

        git >> Edge(label="머지(PR)") >> pipe >> build >> Edge(label="이미지 push") >> ecr >> scan
        scan >> Edge(label="스캔 통과") >> dev >> mon
        scan >> Edge(
            label="실패 시 차단·반려",
            style="dashed",
            color="red",
            fontcolor="red",
        ) >> git

    with Cluster("격상 시에만 (탑다운 이관)"):
        gate = Users("승인 게이트\n(AI Board·정보보호팀)")
        prod = EC2("탑다운 운영 배포\n(상시 가동)")

        gate >> Edge(label="승인 시") >> prod

    dev >> Edge(
        label="격상 심의\n(상시 가용성 필요 시)",
        style="dashed",
        color="firebrick",
        fontcolor="firebrick",
        penwidth="2",
    ) >> gate
