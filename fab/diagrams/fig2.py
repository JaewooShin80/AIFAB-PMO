from diagrams import Diagram, Cluster, Edge
from diagrams.aws.general import Users
from diagrams.aws.network import (
    DirectConnect,
    TransitGateway,
    ElbApplicationLoadBalancer,
    NATGateway,
    Endpoint,
    InternetGateway,
)
from diagrams.aws.compute import Fargate, Lambda, EC2
from diagrams.aws.database import RDS
from diagrams.aws.storage import S3

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
    "네트워크(VPC/Subnet) 구성도",
    filename="fig2-network-vpc",
    outformat="png",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
):
    with Cluster("사내 네트워크"):
        user = Users("사내 사용자")

    dx = DirectConnect("Direct Connect\n/ VPN")
    tgw = TransitGateway("Transit Gateway")

    with Cluster("Bottom-up Sandbox VPC  (예: 10.20.0.0/16, 2 AZ)"):
        with Cluster("Public Subnet"):
            alb = ElbApplicationLoadBalancer("내부 ALB\n(사내망 전용)")
            nat = NATGateway("NAT Gateway\n(허용 목록 egress)")

        with Cluster("Private Subnet - App"):
            app = Fargate("ECS/Fargate\n과제 앱")
            fn = Lambda("Lambda")
            dev = EC2("개발 서버")

        with Cluster("Private Subnet - Data"):
            rds = RDS("RDS\n(KMS 암호화)")

        vpce = Endpoint("VPC Endpoints\n(S3·ECR·Bedrock·Logs)")

        alb >> app
        app >> Edge(label="화이트리스트 통신", style="dashed") >> nat
        app >> rds
        fn >> rds
        app >> vpce

    s3 = S3("S3\n(Gateway Endpoint 경유)")
    igw = InternetGateway("IGW\n(아웃바운드 전용)")

    user >> dx >> tgw >> Edge(label="인바운드는 사내망만") >> alb
    vpce >> s3
    nat >> igw
