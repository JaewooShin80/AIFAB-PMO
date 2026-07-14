"""T2Y 구축 여정 간트차트 (경영 보고용) — 9/1 파일럿 오픈 기준"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.patches import FancyBboxPatch
from datetime import date

plt.rcParams["font.family"] = "AppleGothic"
plt.rcParams["axes.unicode_minus"] = False

NAVY = "#1f2a44"
ACCENT = "#ea002c"
MUTED = "#5b6472"
LINE = "#e3e7ee"

D = mdates.date2num

# 4개 단계 레인: (이름, 시작, 끝, 색, 핵심 내용, 기간표기)
phases = [
    ("준비", date(2026, 6, 29), date(2026, 7, 10), "#9aa8c4",
     "인원 구성 · 물리 환경 조사 · AWS 품의 · 웹 IDE 확정(EC2+Coder)", "2주 · 완료"),
    ("기반 구축", date(2026, 7, 13), date(2026, 8, 28), NAVY,
     "리드타임 4건 신청 · Landing Zone · Coder 플랫폼 · 골든 패스 7종 · 골든 AMI · E2E 통합 · 선발·온보딩 · 드라이런 → 8/28 Readiness", "7주"),
    ("통합 검증·파일럿", date(2026, 9, 1), date(2026, 9, 25), ACCENT,
     "스프린트 #1 — T2Y 에이전트 제작 · 운영 배포(9/17) · 데모데이(9/18) · 판정(9/25)", "4주"),
    ("확산", date(2026, 10, 1), date(2026, 12, 18), "#2b8a3e",
     "최종 보고(10/2) · 격상 이관(4~6주) · 지속 사이클 #2(10/19~)·#3(11/23~) — 연 6~8회 정례화", "4분기"),
]

milestones = [
    (date(2026, 7, 17), "착수 보고", 0),
    (date(2026, 8, 7), "중간 점검", 1),
    (date(2026, 8, 14), "선발 확정", 0),
    (date(2026, 8, 28), "Readiness\nGo/No-Go", 1),
    (date(2026, 9, 17), "운영 배포", 0),
    (date(2026, 9, 25), "판정", 1),
    (date(2026, 10, 2), "최종 보고\n(확대 결정)", 0),
]

X0, X1 = D(date(2026, 6, 21)), D(date(2026, 12, 28))
LABEL_X = X0 + 1  # 좌측 레인 라벨 위치

fig, ax = plt.subplots(figsize=(16, 8))

# ── 월 배경 밴드 (짝수 달 옅은 음영) + 월 라벨 헤더 ──
month_bounds = [date(2026, 7, 1), date(2026, 8, 1), date(2026, 9, 1),
                date(2026, 10, 1), date(2026, 11, 1), date(2026, 12, 1), date(2026, 12, 28)]
Y_TOP, Y_BOT = 8.6, 0.0
for i in range(len(month_bounds) - 1):
    x_s, x_e = D(month_bounds[i]), D(month_bounds[i + 1])
    if i % 2 == 1:
        ax.axvspan(x_s, x_e, ymin=0, ymax=1, color="#f4f6fa", zorder=0)
    ax.text((x_s + x_e) / 2, Y_TOP - 0.25, f"{month_bounds[i].month}월",
            fontsize=15, fontweight="bold", color=MUTED, ha="center", va="center")
    ax.plot([x_s, x_s], [Y_BOT, Y_TOP - 0.6], color=LINE, linewidth=1, zorder=1)

# 헤더 구분선
ax.plot([X0, X1], [Y_TOP - 0.6, Y_TOP - 0.6], color="#c9d1de", linewidth=1.4, zorder=2)

# ── 마일스톤 타임라인 레인 ──
ML_Y = 6.9
ax.plot([D(date(2026, 7, 10)), D(date(2026, 10, 12))], [ML_Y, ML_Y],
        color="#c9d1de", linewidth=2, zorder=2)
for d, label, level in milestones:
    x = D(d)
    ax.scatter([x], [ML_Y], marker="D", s=130, color=NAVY, zorder=5,
               edgecolors="white", linewidths=1.6)
    ly = ML_Y + (0.42 if level == 0 else 0.98)
    ax.plot([x, x], [ML_Y + 0.12, ly - 0.08], color="#aab4c4", linewidth=1, zorder=3)
    ax.text(x, ly, f"{d.month}/{d.day} {label}", fontsize=11.5, fontweight="bold",
            color=NAVY, ha="center", va="bottom", linespacing=1.15)

# ── 단계 레인 (막대 5개, 위→아래) ──
BAR_H = 0.66
for i, (name, s, e, color, desc, dur) in enumerate(phases):
    yc = 5.7 - i * 1.5
    x_s, w = D(s), D(e) - D(s) + 0.8
    # 레인 라벨 (좌측)
    ax.text(LABEL_X, yc, name, fontsize=15, fontweight="bold", color=color,
            ha="left", va="center")
    # 라운드 막대
    bar = FancyBboxPatch((x_s, yc - BAR_H / 2), w, BAR_H,
                         boxstyle="round,pad=0,rounding_size=0.18",
                         facecolor=color, edgecolor="none", zorder=3,
                         mutation_aspect=1 / ((X1 - X0) / (Y_TOP * 2)))
    ax.add_patch(bar)
    range_txt = f"{s.month}/{s.day} ~ {e.month}/{e.day}"
    if w < 16:
        # 짧은 막대: 라벨을 막대 오른쪽 바깥에
        ax.text(x_s + w + 1.0, yc, f"{range_txt} · {dur}", fontsize=11,
                fontweight="bold", color=color, ha="left", va="center", zorder=4)
    else:
        ax.text(x_s + 1.2, yc, range_txt, fontsize=11, fontweight="bold",
                color="white", ha="left", va="center", zorder=4)
        ax.text(x_s + w - 1.2, yc, dur, fontsize=11, fontweight="bold",
                color="white", ha="right", va="center", zorder=4)
    # 핵심 내용 (막대 아래)
    ax.text(x_s + 0.3, yc - BAR_H / 2 - 0.10, desc, fontsize=10.5, color=MUTED,
            ha="left", va="top", zorder=4)

# ── 9/1 파일럿 오픈 기준선 ──
open_x = D(date(2026, 9, 1))
ax.axvline(open_x, color=ACCENT, linewidth=3, zorder=6)
ax.text(open_x + 1.6, Y_TOP + 0.18, "▶ 9/1 파일럿 오픈", fontsize=17, fontweight="bold",
        color="white", ha="left", va="bottom", zorder=7,
        bbox=dict(boxstyle="round,pad=0.45", facecolor=ACCENT, edgecolor="none"))
# 구축/운영 구간 표기 (최하단 전용 밴드)
ax.text((X0 + open_x) / 2, Y_BOT + 0.14, "◀ 준비·기반 구축 (9주, ~8월 말)", fontsize=12,
        fontweight="bold", color=MUTED, ha="center", va="bottom")
ax.text((open_x + X1) / 2, Y_BOT + 0.14, "통합 검증·파일럿 (9월) → 확산 (10월~) ▶",
        fontsize=12, fontweight="bold", color=MUTED, ha="center", va="bottom")

# ── 오늘 표시 (하단 축 바깥) ──
today_x = D(date(2026, 7, 14))
ax.axvline(today_x, color=MUTED, linewidth=1.3, linestyle=(0, (4, 3)), zorder=2)
ax.text(today_x, Y_BOT - 0.28, "▲ 오늘 7/14", fontsize=10.5, fontweight="bold",
        color=MUTED, ha="center", va="top")

# ── 축 정리 ──
ax.set_xlim(X0, X1)
ax.set_ylim(Y_BOT - 0.7, Y_TOP + 1.0)
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

ax.set_title("AIFAB T2Y 구축 여정 — 9/1 파일럿 오픈 기준",
             fontsize=21, fontweight="bold", color=NAVY, pad=22, loc="left")

plt.tight_layout()
plt.savefig("fig10-construction-gantt.png", dpi=150, bbox_inches="tight", facecolor="white")
print("saved")
