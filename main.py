"""Flask 驱动 Landing Page + VitePress 文档站点"""
import os
import shutil
from pathlib import Path

from flask import Flask, send_from_directory, abort, redirect

ROOT = Path(__file__).parent
DIST = ROOT / "docs" / ".vitepress" / "dist"
DOCS = ROOT / "docs"
VITEPRESS = ROOT / "docs" / ".vitepress"
VP_ICONS = ROOT / "node_modules" / "vitepress" / "dist" / "client" / "theme-default" / "styles" / "icons.css"

# VitePress 文档路由 → 对应 Markdown 源文件映射
VP_ROUTES = {
    "guide": DOCS / "guide" / "index.md",
    "guide/features": DOCS / "guide" / "features.md",
    "guide/structure": DOCS / "guide" / "structure.md",
    "guide/menu": DOCS / "guide" / "menu.md",
    "deploy": DOCS / "deploy" / "index.md",
    "deploy/linux": DOCS / "deploy" / "linux.md",
    "deploy/termux": DOCS / "deploy" / "termux.md",
    "deploy/cluster": DOCS / "deploy" / "cluster.md",
    "changelog": DOCS / "changelog.md",
    "privacy": DOCS / "privacy.md",
    "contact": DOCS / "contact.md",
    "sponsor": DOCS / "sponsor.md",
}

EXTRAS = {
    "style.css": (VITEPRESS, "style.css"),
    "logo.svg": (DOCS, "logo.svg"),
    "vp-icons.css": (VP_ICONS.parent, VP_ICONS.name),
}


def ensure_static_files():
    for target_path, (src_dir, src_name) in EXTRAS.items():
        dst = DIST / target_path
        if not dst.exists():
            src = src_dir / src_name
            if src.exists():
                dst.parent.mkdir(parents=True, exist_ok=True)
                if src.is_file():
                    shutil.copy2(src, dst)
                    print(f"[flask] 已复制: {target_path}")


app = Flask(__name__)


@app.route("/")
def landing():
    """首页 Landing Page"""
    lp = DIST / "landing.html"
    if lp.exists():
        return send_from_directory(DIST, "landing.html")
    return "<h2>首页文件不存在</h2>", 404


@app.route("/docs/") 
@app.route("/docs")
def docs_index():
    return redirect("/guide/")


@app.route("/<path:path>")
def serve(path: str):
    """处理所有其他路径"""
    if not DIST.exists():
        return "<h2>dist 目录不存在</h2>", 500

    ensure_static_files()

    # 1. 具体文件优先
    file_path = DIST / path
    if file_path.is_file():
        return send_from_directory(DIST, path)

    # 2. VitePress SPA 回退：页面路由交给 app.html 处理
    app_html = DIST / "app.html"
    if app_html.exists():
        return send_from_directory(DIST, "app.html")

    # 3. VitePress 未构建时的回退：直接渲染 Markdown 源文件为简易 HTML
    normalized = path.rstrip("/")
    if normalized in VP_ROUTES:
        md_file = VP_ROUTES[normalized]
        if md_file.exists():
            content = md_file.read_text(encoding="utf-8")
            html = md_to_html(content, title=normalized)
            return html

    # 4. 404 回退到 landing 页（SPA 风格）
    lp = DIST / "landing.html"
    if lp.exists():
        return send_from_directory(DIST, "landing.html")

    abort(404)


def md_to_html(md_text: str, title: str = "") -> str:
    """简易 Markdown → HTML 渲染器（无外部依赖）"""
    import re
    
    lines = md_text.split("\n")
    html_lines = []
    in_code_block = False
    code_lang = ""
    code_lines = []
    
    def flush_code():
        nonlocal code_lines
        if code_lines:
            lang_attr = f' class="language-{code_lang}"' if code_lang else ""
            code = "\n".join(code_lines)
            code = code.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            html_lines.append(f"<pre><code{lang_attr}>{code}</code></pre>")
            code_lines = []
    
    for line in lines:
        # Code blocks
        if line.startswith("```"):
            if in_code_block:
                flush_code()
                in_code_block = False
                code_lang = ""
            else:
                code_lang = line[3:].strip()
                in_code_block = True
            continue
        
        if in_code_block:
            code_lines.append(line)
            continue
        
        # Headings
        if line.startswith("# "):
            h1_text = line[2:].strip()
            if not title:
                title = h1_text
            html_lines.append(f'<h1>{h1_text}</h1>')
        elif line.startswith("## "):
            html_lines.append(f'<h2>{line[3:].strip()}</h2>')
        elif line.startswith("### "):
            html_lines.append(f'<h3>{line[4:].strip()}</h3>')
        elif line.startswith("#### "):
            html_lines.append(f'<h4>{line[5:].strip()}</h4>')
        # Blockquote
        elif line.startswith("> "):
            html_lines.append(f'<blockquote>{inline_md(line[2:].strip())}</blockquote>')
        # Horizontal rule
        elif line.strip() == "---":
            html_lines.append("<hr>")
        # Unordered list
        elif re.match(r"^\s*[-*+]\s+", line):
            indent = len(line) - len(line.lstrip())
            item = re.sub(r"^\s*[-*+]\s+", "", line)
            html_lines.append(f'<li style="margin-left:{indent+20}px">{inline_md(item)}</li>')
        # Ordered list
        elif re.match(r"^\s*\d+\.\s+", line):
            item = re.sub(r"^\s*\d+\.\s+", "", line)
            html_lines.append(f'<li style="margin-left:20px">{inline_md(item)}</li>')
        # Image
        elif re.match(r"^!\[.*\]\(.*\)$", line):
            m = re.match(r"^!\[(.*)\]\((.*)\)$", line)
            if m:
                alt, src = m.groups()
                html_lines.append(f'<p><img src="{src}" alt="{alt}" style="max-width:100%;border-radius:8px;"></p>')
        # Empty line
        elif line.strip() == "":
            html_lines.append("<br>")
        # Paragraph / inline HTML
        else:
            html_lines.append(f"<p>{inline_md(line)}</p>")
    
    flush_code()
    
    body = "\n".join(html_lines)
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — bilibili_learning_bot</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{
    font-family: 'Inter', -apple-system, sans-serif;
    background: #0D0D0D; color: #F5F5F5;
    max-width: 800px; margin: 0 auto; padding: 80px 40px 60px;
    line-height: 1.7;
  }}
  h1 {{ font-size: 2.2em; font-weight: 200; letter-spacing: -1px; margin-bottom: 24px; border-bottom: 1px solid #2A2A2A; padding-bottom: 16px; }}
  h2 {{ font-size: 1.5em; font-weight: 400; margin: 36px 0 14px; color: #E8916A; }}
  h3 {{ font-size: 1.15em; font-weight: 500; margin: 24px 0 10px; }}
  h4 {{ font-size: 1em; font-weight: 600; margin: 20px 0 8px; }}
  p {{ font-size: 15px; color: #999; margin-bottom: 12px; }}
  a {{ color: #E8916A; text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}
  code {{ background: #1A1A1A; padding: 2px 6px; border-radius: 4px; font-size: 13px; color: #E8916A; }}
  pre {{ background: #1A1A1A; padding: 20px; border-radius: 8px; overflow-x: auto; margin: 16px 0; border: 1px solid #2A2A2A; }}
  pre code {{ background: none; padding: 0; color: #CCC; }}
  blockquote {{ border-left: 2px solid #E8916A; padding: 8px 16px; margin: 16px 0; color: #888; font-style: italic; }}
  hr {{ border: none; border-top: 1px solid #2A2A2A; margin: 32px 0; }}
  li {{ font-size: 15px; color: #999; margin-bottom: 6px; }}
  img {{ max-width: 100%; border-radius: 8px; }}
  .back-link {{ display: inline-block; margin-bottom: 30px; font-size: 13px; color: #666; }}
  .back-link:hover {{ color: #E8916A; }}
</style>
</head>
<body>
<a href="/" class="back-link">← 返回首页</a>
{body}
</body>
</html>"""


def inline_md(text: str) -> str:
    """处理行内 Markdown：粗体、斜体、行内代码、链接"""
    import re
    # Bold
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    # Italic
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    # Inline code
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    # Links
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    return text


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    host = os.environ.get("HOST", "127.0.0.1")
    debug = os.environ.get("DEBUG", "0") == "1"

    if not DIST.exists():
        print("[flask] 错误: dist 目录不存在，请先运行 npm run docs:build")
        exit(1)

    ensure_static_files()
    print(f"[flask] 站点已启动:")
    print(f"  首页:      http://{host}:{port}/")
    print(f"  文档入口:  http://{host}:{port}/docs/")
    print(f"  PPT 讲解:  http://{host}:{port}/bilibili_learning_bot_slides.html")
    print(f"  OpenBiliClaw: http://{host}:{port}/openbiliclaw.html")
    app.run(host=host, port=port, debug=debug)
