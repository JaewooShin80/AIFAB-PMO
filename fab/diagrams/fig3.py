from diagrams import Diagram, Cluster, Edge
from diagrams.aws.general import GenericFirewall
from diagrams.aws.management import Organizations, Cloudtrail, Config
from diagrams.aws.security import (
    SingleSignOn,
    IdentityAndAccessManagementIam,
    WAF,
    KMS,
    Macie,
    Inspector,
    Guardduty,
    SecurityHub,
)
from diagrams.aws.network import Privatelink
from diagrams.aws.storage import S3
from diagrams.aws.integration import SNS

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
    "보안 아키텍처 (4계층 + 통합 탐지)",
    filename="fig3-security-architecture",
    outformat="png",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
):
    with Cluster("계정·접근 통제"):
        scp = Organizations("Organizations SCP\n(금지 행위 차단)")
        sso = SingleSignOn("IAM Identity Center\n(SSO·권한세트)")
        iam = IdentityAndAccessManagementIam("IAM 역할\n(최소권한)")
        scp - sso - iam

    with Cluster("네트워크 보안"):
        waf = WAF("AWS WAF\n(내부 ALB 보호)")
        sg = GenericFirewall("보안그룹 / NACL")
        plink = Privatelink("PrivateLink\n(인터넷 미경유)")
        waf - sg - plink

    with Cluster("데이터 보호"):
        kms = KMS("KMS\n(전 구간 암호화)")
        macie = Macie("Macie\n(실데이터·PII 유입 탐지)")
        s3block = S3("S3 Block\nPublic Access")
        kms - macie - s3block

    with Cluster("위협 탐지·감사"):
        config = Config("Config Rules\n(정책 준수 점검)")
        trail = Cloudtrail("CloudTrail\n(Org 전체 기록)")
        inspector = Inspector("Inspector\n(이미지 취약점)")
        gd = Guardduty("GuardDuty")

    hub = SecurityHub("Security Hub\n(통합 대시보드)")
    sns = SNS("SNS 알림\n(보드·정보보호팀)")

    macie >> hub
    config >> hub
    trail >> hub
    inspector >> hub
    gd >> hub
    hub >> sns
