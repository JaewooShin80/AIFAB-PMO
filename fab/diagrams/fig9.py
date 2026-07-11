"""그림. 격상 유입 절차 (바텀업 → 탑다운 이관)"""
import graphviz

FONT = "AppleGothic"

C_OWNER = "#cfe2f3"  # 과제 오너 (파랑)
C_BOARD = "#d9ead3"  # 보드·정보보호팀 (초록)
C_AUTO = "#e4d7f5"   # AI 인프라팀·자동화 (보라)
C_GW = "#efefef"     # 게이트웨이 (회색)

g = graphviz.Digraph("fig9", format="png")
g.attr(
    label="격상 유입 절차 (바텀업 → 탑다운 이관)",
    labelloc="t",
    fontname=FONT,
    fontsize="20",
    bgcolor="white",
    pad="0.4",
    nodesep="0.5",
    ranksep="0.55",
)
g.attr("node", fontname=FONT, fontsize="12", color="gray40")
g.attr("edge", fontname=FONT, fontsize="11", color="gray30")


def task(name, label, fill):
    g.node(name, label, shape="box", style="rounded,filled", fillcolor=fill)


def gateway(name, label):
    g.node(name, label, shape="diamond", style="filled", fillcolor=C_GW)


def event(name, label, end=False):
    g.node(
        name, label, shape="doublecircle" if end else "circle",
        style="filled", fillcolor="white", fontsize="11",
    )


event("start", "시작")
task("confirm", "격상 확정\n(분기 보드 심의:\n성과 기준 또는 상시 가용성 필요)", C_BOARD)
task("codereview", "코드 리뷰\n(품질·보안·표준 준수)", C_OWNER)
task("docs", "문서화\n(아키텍처·운영 절차서 Runbook)", C_OWNER)
task("data", "실데이터 연동 재설계\n(보안 재심사·반입 승인)", C_BOARD)
task("org", "정식 운영 조직 지정", C_BOARD)
task("prov", "탑다운 계정 재프로비저닝\n(topdown-project 모듈·Multi-AZ)", C_AUTO)
task("verify", "Git 이관·스테이징 검증", C_OWNER)
gateway("gate", "승인 게이트\n(보드·정보보호팀)")
task("open", "운영 오픈\n(상시 가동·SLO 관리)", C_AUTO)
task("cleanup", "샌드박스 자원 회수\n·데이터 파기", C_AUTO)
event("done", "격상 완료", end=True)

g.edge("start", "confirm")
g.edge("confirm", "codereview")
g.edge("codereview", "docs")
g.edge("docs", "data")
g.edge("data", "org")
g.edge("org", "prov")
g.edge("prov", "verify")
g.edge("verify", "gate")
g.edge("gate", "open", label="승인")
g.edge("gate", "verify", label="보완 요청", style="dashed")
g.edge("open", "cleanup")
g.edge("cleanup", "done")

with g.subgraph(name="cluster_legend") as lg:
    lg.attr(label="담당 주체", fontname=FONT, fontsize="13", color="gray60", style="rounded")
    lg.attr("node", shape="box", style="rounded,filled", fontsize="11")
    lg.node("l1", "과제 오너", fillcolor=C_OWNER)
    lg.node("l2", "보드·정보보호팀", fillcolor=C_BOARD)
    lg.node("l3", "AI 인프라팀·자동화", fillcolor=C_AUTO)
    lg.edge("l1", "l2", style="invis")
    lg.edge("l2", "l3", style="invis")

g.render(filename="fig9-promotion-flow", cleanup=True)
print("fig9-promotion-flow.png generated")
