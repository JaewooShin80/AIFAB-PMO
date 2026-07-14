"""백서 + 부록 7종 → 단일 자기완결 HTML (A4, 이미지 base64 임베딩, 앵커 링크, 뒤로가기)"""
import base64
import os
import re
import markdown

BASE = os.path.dirname(os.path.abspath(__file__))
WP = os.path.join(BASE, "AIFAB_AWS_환경구축_백서_최종_v1-0.md")
APPENDIX_DIR = os.path.join(BASE, "백서부록")
OUT = os.path.join(BASE, "AIFAB_AWS_환경구축_백서_최종_v1-0.html")


def md_to_html(text, with_toc=False):
    exts = ["tables", "fenced_code"]
    if with_toc:
        exts.append("toc")
    md = markdown.Markdown(extensions=exts)
    html = md.convert(text)
    toc_tokens = getattr(md, "toc_tokens", []) if with_toc else []
    return html, toc_tokens


def embed_images(html, md_dir):
    def repl(m):
        src = m.group(1)
        path = os.path.normpath(os.path.join(md_dir, src))
        if not os.path.exists(path):
            return m.group(0)
        with open(path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
        return m.group(0).replace(src, f"data:image/png;base64,{b64}")

    return re.sub(r'<img[^>]*?src="([^"]+)"', lambda m: repl(m), html)


# ── 백서 본문 ──
with open(WP, encoding="utf-8") as f:
    wp_md = f.read()
wp_html, toc = md_to_html(wp_md, with_toc=True)
wp_html = embed_images(wp_html, BASE)
# 부록N 텍스트 → 앵커 링크 (본문 한정)
wp_html = re.sub(r"부록([1-7])", r'<a class="axlink" href="#appendix-\1">부록\1</a>', wp_html)

# ── 부록 7종 ──
appendix_sections = []
appendix_titles = []
for name in sorted(os.listdir(APPENDIX_DIR)):
    if not name.endswith(".md"):
        continue
    n = re.match(r"부록(\d)\. (.+)\.md", name)
    num, title = n.group(1), n.group(2)
    with open(os.path.join(APPENDIX_DIR, name), encoding="utf-8") as f:
        a_md = f.read()
    a_html, _ = md_to_html(a_md)
    a_html = embed_images(a_html, APPENDIX_DIR)
    appendix_titles.append((num, title))
    appendix_sections.append(
        f'<section class="appendix" id="appendix-{num}">'
        f'<div class="ax-head"><span class="ax-badge">부록 {num}</span><h1>{title}</h1>'
        f'<a class="ax-top" href="#top">▲ 백서 처음으로</a></div>{a_html}</section>'
    )

# ── 목차 ──
def toc_html(tokens):
    items = []
    for t in tokens:
        if t["level"] > 2:
            continue
        items.append(f'<li class="lv{t["level"]}"><a href="#{t["id"]}">{t["name"]}</a></li>')
    for num, title in appendix_titles:
        items.append(f'<li class="lv2 ax"><a href="#appendix-{num}">부록{num}. {title}</a></li>')
    return "<ul>" + "".join(items) + "</ul>"


TEMPLATE = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AIFAB AWS 환경 구축 백서 (최종 v1-0)</title>
<style>
  :root {{
    --ink:#14181f; --muted:#5b6472; --accent:#ea002c; --accent-soft:#fdeef1;
    --navy:#1f2a44; --line:#e3e7ee; --card:#f8fafc;
  }}
  * {{ box-sizing:border-box; }}
  html {{ scroll-behavior:smooth; }}
  body {{
    margin:0; background:#eef1f5; color:var(--ink);
    font-family:"Pretendard","Apple SD Gothic Neo","Malgun Gothic","Noto Sans KR",sans-serif;
    font-size:14.5px; line-height:1.75; word-break:keep-all;
  }}
  .page {{
    max-width:210mm; margin:0 auto; background:#fff; padding:22mm 18mm;
    box-shadow:0 6px 24px rgba(20,24,31,.10); min-height:297mm;
  }}
  h1 {{ font-size:26px; color:var(--navy); line-height:1.35; margin:1.6em 0 .5em;
       border-bottom:3px solid var(--navy); padding-bottom:.35em; }}
  h1:first-of-type {{ margin-top:0; font-size:30px; border-bottom:none; }}
  h1:first-of-type::after {{ content:""; display:block; width:64px; height:4px;
       background:var(--accent); border-radius:2px; margin-top:12px; }}
  h2 {{ font-size:20px; color:var(--navy); margin:2.1em 0 .5em; padding-left:12px;
       border-left:5px solid var(--accent); page-break-after:avoid; }}
  h3 {{ font-size:16.5px; color:var(--navy); margin:1.7em 0 .4em; page-break-after:avoid; }}
  h4 {{ font-size:15px; color:var(--navy); margin:1.4em 0 .3em; }}
  p {{ margin:.55em 0; }}
  strong {{ color:var(--navy); }}
  table {{ width:100%; border-collapse:collapse; font-size:12.8px; margin:.8em 0 1.1em;
          page-break-inside:avoid; }}
  th,td {{ border:1px solid var(--line); padding:7px 10px; text-align:left;
          vertical-align:top; line-height:1.55; }}
  thead th {{ background:var(--navy); color:#fff; font-weight:600; }}
  tbody tr:nth-child(even) {{ background:var(--card); }}
  code {{ background:var(--card); border:1px solid var(--line); border-radius:4px;
         padding:1px 5px; font-size:.88em; color:var(--navy);
         font-family:"SF Mono",Menlo,Consolas,monospace; }}
  pre {{ background:var(--card); border:1px solid var(--line); border-radius:8px;
        padding:14px 16px; overflow-x:auto; font-size:12px; line-height:1.55;
        page-break-inside:avoid; }}
  pre code {{ background:none; border:none; padding:0; }}
  img {{ max-width:100%; height:auto; display:block; margin:14px auto;
        border:1px solid var(--line); border-radius:6px; page-break-inside:avoid; }}
  em {{ color:var(--muted); }}
  blockquote {{ margin:.9em 0; padding:10px 16px; background:var(--accent-soft);
               border-left:4px solid var(--accent); border-radius:0 8px 8px 0; }}
  blockquote p {{ margin:.25em 0; }}
  hr {{ border:none; border-top:1.5px solid var(--line); margin:2.2em 0; }}
  ul,ol {{ padding-left:1.5em; }}
  li {{ margin:.28em 0; }}
  a {{ color:var(--accent); text-decoration:none; font-weight:600; }}
  a:hover {{ text-decoration:underline; }}
  a.axlink {{ background:var(--accent-soft); border-radius:5px; padding:0 5px; }}

  /* 목차 */
  .toc {{ background:var(--card); border:1px solid var(--line); border-radius:10px;
         padding:18px 24px; margin:1.4em 0 2em; }}
  .toc h2 {{ border:none; padding:0; margin:0 0 .5em; font-size:17px; }}
  .toc ul {{ list-style:none; padding:0; margin:0; column-count:2; column-gap:34px; }}
  .toc li {{ margin:.22em 0; break-inside:avoid; }}
  .toc li.lv1 a {{ color:var(--navy); }}
  .toc li.lv2 {{ padding-left:14px; font-size:13px; }}
  .toc li.lv2 a {{ color:var(--muted); font-weight:500; }}
  .toc li.ax a {{ color:var(--accent); }}

  /* 부록 */
  section.appendix {{ margin-top:3.5em; border-top:4px double var(--navy);
                     padding-top:1.5em; page-break-before:always; }}
  .ax-head {{ margin-bottom:1em; }}
  .ax-badge {{ display:inline-block; background:var(--navy); color:#fff; font-size:13px;
              font-weight:700; border-radius:999px; padding:4px 14px; }}
  .ax-head h1 {{ margin:.45em 0 .2em; border-bottom:2px solid var(--line); font-size:23px; }}
  .ax-top {{ font-size:12.5px; }}

  /* 플로팅 내비게이션 */
  .float-nav {{ position:fixed; right:26px; bottom:26px; display:flex; flex-direction:column;
               gap:8px; z-index:99; }}
  .float-nav button {{
    background:var(--navy); color:#fff; border:none; border-radius:999px;
    padding:11px 18px; font-size:13.5px; font-weight:700; cursor:pointer;
    box-shadow:0 4px 14px rgba(20,24,31,.25); font-family:inherit;
  }}
  .float-nav button:hover {{ background:var(--accent); }}
  .float-nav .toc-btn {{ background:#5b6472; }}

  @media print {{
    body {{ background:#fff; }}
    .page {{ box-shadow:none; padding:0; max-width:100%; }}
    .float-nav {{ display:none; }}
    @page {{ size:A4; margin:15mm; }}
  }}
</style>
</head>
<body>
<div class="page" id="top">
<div class="toc"><h2>목차</h2>{toc}</div>
{body}
{appendices}
</div>
<div class="float-nav">
  <button onclick="history.back()" title="이전에 보던 위치로 돌아갑니다">← 뒤로가기</button>
  <button class="toc-btn" onclick="location.hash='top'">▲ 목차</button>
</div>
</body>
</html>
"""

result = TEMPLATE.format(toc=toc_html(toc), body=wp_html, appendices="".join(appendix_sections))
with open(OUT, "w", encoding="utf-8") as f:
    f.write(result)
print(f"saved: {OUT} ({os.path.getsize(OUT) / 1024 / 1024:.1f} MB)")
print(f"부록 {len(appendix_sections)}종, 이미지 임베딩 {result.count('data:image/png;base64')}건")
