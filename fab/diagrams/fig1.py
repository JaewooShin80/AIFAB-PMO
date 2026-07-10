from diagrams import Diagram, Cluster, Edge
from diagrams.aws.general import Users, TraditionalServer, GenericFirewall
from diagrams.aws.security import SingleSignOn, Guardduty, SecurityHub
from diagrams.aws.network import APIGateway
from diagrams.aws.compute import EC2, Lambda, Fargate
from diagrams.aws.integration import StepFunctions
from diagrams.aws.storage import S3
from diagrams.aws.database import RDS
from diagrams.aws.management import Cloudtrail, Cloudwatch, Organizations
from diagrams.onprem.iac import Terraform
from diagrams.onprem.vcs import Gitlab

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
    "AWS 전체 아키텍처 (Top-Down / Bottom-up 신청·프로비저닝·개발 흐름)",
    filename="fig1-aws-architecture",
    outformat="png",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
):
    user = Users("사내 사용자\n(사내망 전용 접근)")

    with Cluster("AWS Organization"):
        org = Organizations("Organizations\n(SCP 정책)")

        with Cluster("Shared Services Account (공통)"):
            sso = SingleSignOn("IAM Identity Center\n(SSO·최소권한)")
            portal = TraditionalServer("신청 포털\n(Top-Down/Bottom-up 선택)")
            apigw = APIGateway("API Gateway")
            intake = Lambda("접수 처리")
            wf = StepFunctions("승인 워크플로\n(Step Functions)")
            agent = Bedrock("Bedrock AI Agent\n(적합성 사전심사)")
            board = Users("운영 보드\n(AI Board)")
            tf = Terraform("Terraform\n(자원 자동 생성)")

            sso >> portal >> apigw >> intake >> wf
            wf >> Edge(label="Bottom-up: AI 사전심사") >> agent >> board
            wf >> Edge(label="Top-Down: AI 심사 바이패스", style="dashed") >> board
            board >> Edge(label="승인 시") >> tf

        with Cluster("Top-down Account (공식 과제)"):
            td_dev = EC2("개발 서버")
            gitlab = Gitlab("GitLab\nCI/CD")
            secproc = GenericFirewall("사내 정보보안\n프로세스 확인")
            prod = EC2("운영 서버\n(별도 구동)")

            td_dev >> Edge(label="개발 후") >> gitlab
            gitlab >> Edge(label="배포 전 확인") >> secproc >> prod

        with Cluster("Bottom-up Sandbox Account (자율 과제)"):
            bu_dev = EC2("개발 서버")
            s3 = S3("S3")
            rds = RDS("RDS")
            app = Fargate("과제 앱\n(ECS/Fargate)")

            bu_dev >> Edge(label="개발 시 활용", style="dashed") >> s3
            bu_dev >> Edge(label="개발 시 활용", style="dashed") >> rds
            bu_dev >> Edge(label="CI/CD 배포") >> app

        with Cluster("보안·관측 (전 계정 공통)"):
            trail = Cloudtrail("CloudTrail")
            gd = Guardduty("GuardDuty")
            sh = SecurityHub("Security Hub")
            cw = Cloudwatch("CloudWatch")
            trail >> gd >> sh >> cw

        tf >> Edge(label="환경 자동 세팅") >> td_dev
        tf >> Edge(label="환경 자동 세팅") >> bu_dev
        prod >> Edge(label="로그·지표", style="dashed") >> cw
        app >> Edge(label="로그·지표", style="dashed") >> cw

    user >> sso
    user >> Edge(label="접속(SSO)", style="dashed") >> td_dev
    user >> Edge(label="접속(SSO)", style="dashed") >> bu_dev
