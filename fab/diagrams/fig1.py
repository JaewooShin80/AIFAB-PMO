from diagrams import Diagram, Cluster, Edge
from diagrams.aws.general import Users, TraditionalServer, GenericFirewall
from diagrams.aws.security import SingleSignOn, Guardduty, SecurityHub
from diagrams.aws.compute import EC2, Fargate
from diagrams.aws.devtools import Codepipeline
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
# 기본: 가로 흐름 — 출발 도형의 오른쪽 변 중앙(e)에서 나가 도착 도형의 왼쪽 변 중앙(w)으로
edge_attr = {"fontname": FONT, "fontsize": "10", "tailport": "e", "headport": "w"}

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
            with Cluster(
                "AI Infra",
                graph_attr={
                    "labelloc": "b",
                    "fontsize": "14",
                    "style": "rounded",
                    "color": "#1f2a44",
                    "penwidth": "2",
                },
            ):
                sso = SingleSignOn("IAM Identity Center\n(SSO·최소권한)")
                agent = Bedrock("적합성 심사 AI Agent\n(Bedrock)")
                portal = TraditionalServer("신청 포털\n(Top-Down/Bottom-up 선택)")
                wf = StepFunctions("승인 워크플로\n(Step Functions)")

            board = Users("운영 보드\n(AI Board)")
            tf = Terraform("Terraform\n(자원 자동 생성)")

            # 2행 배치 — 1행: IAM → 적합성 심사 AI Agent / 2행: 신청 포털 → 승인 워크플로
            sso >> Edge(label="적합성 심사") >> agent
            agent >> Edge(label="샌드박스 안내", constraint="false", tailport="s", headport="n") >> portal
            portal >> wf
            wf >> board
            board >> Edge(label="승인 시") >> tf

        with Cluster("Top-down Account (공식 과제)"):
            td_dev = EC2("개발 서버\n(웹 IDE)")
            td_git = Gitlab("Git\n(형상관리)")
            td_pipe = Codepipeline("CodePipeline\n(빌드·이미지 스캔)")
            td_s3 = S3("S3")
            td_rds = RDS("RDS")
            td_app = Fargate("과제 앱\n(Fargate · dev 배포 · 확인용)")

            td_dev >> Edge(label="개발 시 활용", style="dashed") >> td_s3
            td_dev >> Edge(label="개발 시 활용", style="dashed") >> td_rds
            td_dev >> Edge(label="개발 후") >> td_git >> td_pipe >> Edge(label="스캔 통과 시\ndev 배포") >> td_app

            with Cluster(
                "사내 정보보안 프로세스 확인",
                graph_attr={"style": "rounded", "color": "#1f2a44", "penwidth": "2"},
            ):
                secproc = GenericFirewall("보드·정보보호팀\n승인 게이트")

            with Cluster(
                "운영 서버 (24h / 365D)",
                graph_attr={"style": "rounded", "color": "#1f2a44", "penwidth": "2"},
            ):
                prod = EC2("운영 서비스\n(상시 가동)")

            td_app >> Edge(label="검증 완료 후") >> secproc
            secproc >> Edge(label="승인 시 운영 배포") >> prod

        with Cluster("Bottom-up Sandbox Account (자율 과제 · 시간제 가동: 셧다운/웨이크업)"):
            bu_dev = EC2("개발 서버\n(웹 IDE)")
            bu_git = Gitlab("Git\n(형상관리)")
            bu_pipe = Codepipeline("CodePipeline\n(빌드·이미지 스캔)")
            s3 = S3("S3")
            rds = RDS("RDS")
            app = Fargate("과제 앱\n(Fargate · dev 배포)")

            bu_dev >> Edge(label="개발 시 활용", style="dashed") >> s3
            bu_dev >> Edge(label="개발 시 활용", style="dashed") >> rds
            bu_dev >> Edge(label="개발 후") >> bu_git >> bu_pipe >> Edge(label="스캔 통과 시\ndev 배포") >> app

        app >> Edge(
            label="격상 이관\n(보드·정보보호팀 승인 게이트)",
            style="dashed",
            color="firebrick",
            fontcolor="firebrick",
            penwidth="2",
        ) >> secproc

        with Cluster("보안·관측 (전 계정 공통)"):
            trail = Cloudtrail("CloudTrail")
            gd = Guardduty("GuardDuty")
            sh = SecurityHub("Security Hub")
            cw = Cloudwatch("CloudWatch")
            # 배치용 비가시 flat edge(역방향, head가 위로): CloudTrail(위)→CloudWatch(아래) 순서 고정
            cw >> Edge(minlen="0", style="invis") >> sh
            sh >> Edge(minlen="0", style="invis") >> gd
            gd >> Edge(minlen="0", style="invis") >> trail
            # 표시용 화살표 (배치에 영향 없음) — 세로 흐름: 아래 변 중앙(s) → 위 변 중앙(n)
            trail >> Edge(constraint="false", tailport="s", headport="n") >> gd
            gd >> Edge(constraint="false", tailport="s", headport="n") >> sh
            sh >> Edge(constraint="false", tailport="s", headport="n") >> cw

        # 열 위치 고정용 비가시 앵커 (CloudTrail 기준)
        prod >> Edge(style="invis") >> trail

        tf >> Edge(label="환경 자동 세팅") >> td_dev
        tf >> Edge(label="환경 자동 세팅") >> bu_dev
        prod >> Edge(label="로그·지표", style="dashed", constraint="false") >> cw
        app >> Edge(label="로그·지표", style="dashed", constraint="false") >> cw

    user >> sso
    user >> Edge(style="invis") >> portal  # 신청 포털을 SSO와 같은 열(2행)로 고정
    user >> Edge(label="접속(SSO)", style="dashed") >> td_dev
    user >> Edge(label="접속(SSO)", style="dashed") >> bu_dev
