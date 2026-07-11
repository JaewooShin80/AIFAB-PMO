"""그림 7. 운영 프로세스 (BPMN 표기 기반) — 트리아지 분기 반영"""
import graphviz

FONT = "AppleGothic"

# 담당 주체별 색상
C_USER = "#cfe2f3"   # 과제 신청자 (파랑)
C_AGENT = "#fce5cd"  # AI 에이전트 (주황)
C_BOARD = "#d9ead3"  # 운영 보드 (초록)
C_AUTO = "#e4d7f5"   # 자동화(인프라) (보라)
C_GW = "#efefef"     # 게이트웨이 (회색)

g = graphviz.Digraph("fig7", format="png")
g.attr(
    label="운영 프로세스 (BPMN 표기 기반 · 트리아지 분기 포함)",
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


# 시작 ~ 심사
event("start", "시작")
task("apply", "신청서 작성·제출\n(목적·데이터·자원)", C_USER)
task("review", "AI 사전심사\n다각도 판단·트리아지", C_AGENT)
gateway("triage", "트리아지\n판정")

# 트리아지 분기
task("guide", "① 기존 사내 도구 안내\n(A.Biz·Copilot 등 + 활용 가이드)", C_AGENT)
event("end_tool", "도구 활용\n(샌드박스\n미배정)", end=True)
task("edu", "③ 사내 교육 과정 안내", C_AGENT)
task("approve", "보드 승인\n(②배정 권고·④검토 회부)", C_BOARD)
gateway("ok", "승인?")
task("reject", "보완 요청·반려 통보", C_BOARD)

# 승인 이후
task("prov", "자원 자동 프로비저닝\n(Terraform, 30분 이내)", C_AUTO)
task("dev", "개발·dev 배포\n(CI/CD: 빌드·보안 스캔 자동 차단)", C_USER)
task("mon", "운영·사용량 모니터링\n(주간 리포트 자동 생성)", C_AUTO)
gateway("usage", "사용량·성과\n판정")

# 격상 / 선셋
task("promote", "격상 심의\n(보드·정보보호팀 승인 게이트\n→ 탑다운 이관)", C_BOARD)
event("end_promote", "공식과제\n전환", end=True)
task("sunset_warn", "선셋 알람·유예\n(2주)", C_AUTO)
gateway("appeal", "유지\n소명?")
task("sunset", "선셋 실행\n자원 회수·데이터 파기", C_AUTO)
event("end_sunset", "종료", end=True)

# 흐름
g.edge("start", "apply")
g.edge("apply", "review")
g.edge("review", "apply", label="대화형 질문·답변", style="dashed", dir="both")
g.edge("review", "triage")

g.edge("triage", "guide", label="기존 도구로 가능")
g.edge("guide", "end_tool")
g.edge("triage", "edu", label="역량 요건 미충족")
g.edge("edu", "apply", label="이수 후 재신청", style="dashed")
g.edge("triage", "approve", label="샌드박스 배정 권고\n·보드 검토")

g.edge("approve", "ok")
g.edge("ok", "prov", label="승인")
g.edge("ok", "reject", label="반려/보완")
g.edge("reject", "apply", label="보완 후 재제출", style="dashed")

g.edge("prov", "dev")
g.edge("dev", "mon")
g.edge("mon", "usage")
g.edge("usage", "mon", label="유지(정상)", style="dashed")
g.edge("usage", "promote", label="우수·상시 가용성 필요")
g.edge("promote", "end_promote")
g.edge("usage", "sunset_warn", label="저활용")
g.edge("sunset_warn", "appeal")
g.edge("appeal", "mon", label="소명 인정(연장)", style="dashed")
g.edge("appeal", "sunset", label="미소명")
g.edge("sunset", "end_sunset")

# 범례
with g.subgraph(name="cluster_legend") as lg:
    lg.attr(label="담당 주체", fontname=FONT, fontsize="13", color="gray60", style="rounded")
    lg.attr("node", shape="box", style="rounded,filled", fontsize="11")
    lg.node("l1", "과제 신청자", fillcolor=C_USER)
    lg.node("l2", "AI 에이전트", fillcolor=C_AGENT)
    lg.node("l3", "운영 보드", fillcolor=C_BOARD)
    lg.node("l4", "자동화(인프라)", fillcolor=C_AUTO)
    lg.edge("l1", "l2", style="invis")
    lg.edge("l2", "l3", style="invis")
    lg.edge("l3", "l4", style="invis")

g.render(filename="fig7-bpmn-process", cleanup=True)
print("fig7-bpmn-process.png generated")
