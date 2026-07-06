# bilibili_learning_bot 功能升级规划

> 灵感来源：
> - [BiliNote.net](https://www.bilinote.net/) — AI 视频转笔记工具（在线版）
> - [GitHub: JefferyHcool/BiliNote](https://github.com/JefferyHcool/BiliNote) — 开源版（⭐6.7k, v2.4.4）
>
> 核心原则：**所有功能都支持 config.json 自定义开关和参数**

---

## 🔬 BiliNote 开源版 vs bilibili_learning_bot 深度对比

### 产品定位差异

| 维度 | BiliNote (开源版) | bilibili_learning_bot |
|------|------------------|----------------------|
| **定位** | AI 视频→笔记工具（被动式） | 全自动学习机器人（主动式） |
| **工作模式** | 用户手动提交链接，一次性生成笔记 | 自动拉取推荐流，持续学习归档 |
| **输入** | 用户粘贴 URL / 浏览器插件一键 | bot 自主发现视频（推荐流/关注列表/@提及） |
| **输出** | 结构化 Markdown 笔记 | 评分→收藏投币→知识归档 |
| **交互** | Web UI + 浏览器插件 + 桌面客户端 | CLI + Web 面板（Flask） |
| **License** | AGPL-3.0（copyleft） | MIT（宽松） |
| **社区** | ⭐6.7k / Fork 863 | 较小 |
| **版本** | v2.4.4（2026-06-23） | 3.0.2 |

### 功能矩阵对比

| 功能 | BiliNote | 我们的 bot | 差距 |
|------|----------|-----------|------|
| **多平台** | B站/YouTube/抖音/快手/本地视频 | 仅 B 站 | ❌ 大 |
| **浏览器插件** | Chrome/Edge/Firefox，悬浮按钮+侧边栏+右键菜单 | 无 | ❌ 大 |
| **B站字幕直接抓取** | 插件利用用户 Cookie 直接抓 B站字幕，跳过转写 | API 获取 | ❌ 值得借鉴 |
| **RAG 问答** | 基于笔记内容 AI 问答，支持 Function Calling 查原文 | 无 | ❌ 值得借鉴 |
| **多模态理解** | 图像+音频多模态分析 | 仅文本（字幕） | ❌ 架构差异 |
| **多样化转写引擎** | Fast-Whisper/MLX-Whisper/Groq/BCut | 无本地转写，依赖 LLM | ❌ 可选借鉴 |
| **GPU 加速** | CUDA 加速 Faster-Whisper | 无 | N/A（无本地转写） |
| **桌面客户端** | Tauri (Windows/macOS) | Docker/CLI | ❌ 远期可选 |
| **全局代理** | 一处配置作用 AI/转写/下载 | 无 | ❌ 小改进 |
| **笔记风格定制** | 学术/口语/重点提取可选 | 固定风格 | ❌ 小改进 |
| **多版本记录** | 保留历史可回溯 | 无 | ❌ 小改进 |
| **思维导图** | 浏览器插件侧边栏 markmap | 无 | ❌ 已列入规划 |
| **多模型切换** | OpenAI/DeepSeek/Qwen 可选 | OpenAI 兼容 + fallback | 🟡 半覆盖 |
| **章节锁定** | 有（"章节锁定+内容追加"） | 无 | ❌ 已列入规划 |
| **多导出格式** | Markdown/PDF/Word/PPT | 仅 Markdown | ❌ 已列入规划 |
| **Docker 部署** | CPU + GPU 两种镜像 | 支持 Docker | ✅ 持平 |
| **自动学习流程** | 无 | ✅ 自动拉流→评分→投币→归档 | ✅ **独有优势** |
| **待机通知模式** | 无 | ✅ @bot 触发总结 | ✅ **独有优势** |
| **Web 面板** | 有（React 前端） | 有（Flask 内嵌） | 🟡 持平 |

### BiliNote 但我们没有的 🔥 亮点

| 亮点 | 描述 | 借鉴价值 |
|------|------|----------|
| **浏览器插件** | 悬浮按钮 + 侧边栏（Markdown/思维导图/AI问答）+ 右键菜单 | ⭐⭐⭐⭐⭐ 最佳用户体验入口 |
| **B站字幕直抓** | 插件用用户 Cookie 直接抓 B 站字幕，完全跳过音频转写 | ⭐⭐⭐⭐⭐ 零成本获取字幕 |
| **RAG 问答** | 对已生成笔记做 AI 问答，Function Calling 查原文 | ⭐⭐⭐⭐ 知识消费升级 |
| **多模态理解** | 同时分析视频画面+音频，不只看字幕 | ⭐⭐⭐⭐ 更深理解 |
| **笔记风格定制** | 学术严谨/口语化/重点提取 三种风格可选 | ⭐⭐⭐ 个性化体验 |
| **桌面客户端** | Tauri 打包 Windows/macOS，一键安装 | ⭐⭐⭐ 降低使用门槛 |
| **多版本记录** | 每次生成保留历史，可对比回溯 | ⭐⭐ 锦上添花 |

### 我们独有但 BiliNote 没有的 🔥 优势

| 优势 | 描述 |
|------|------|
| **全自动无人值守** | bot 自己发现视频、自己评分、自己决定看哪个，不需要人喂链接 |
| **互动闭环** | 看完视频自动收藏+投币+评论，真正模拟人类学习行为 |
| **待机通知模式** | 在任何视频下 @bot 即可触发总结，无需离开 B站 |
| **精力系统** | 模拟人类疲劳度，防止无限刷视频，更自然的学习节奏 |
| **MIT License** | 比 AGPL-3.0 更宽松，商用友好 |

---

## 📊 当前 vs 目标对照

| 功能 | 当前状态 | BiliNote | 目标 |
|------|---------|----------|------|
| 视频平台 | 仅 B 站 | B站/YouTube/抖音/快手/TikTok/小宇宙 | **全平台可配** |
| AI 模型 | OpenAI 兼容 + 双 fallback | GPT-4o/Claude/Gemini/DeepSeek | **保持已有 + 面板可切换** |
| 长视频策略 | 全量字幕一次性处理 | 章节锁定 + 内容追加 | **新增** |
| 导出格式 | 仅 Markdown (.md) | Markdown/PDF/Word/PPT/思维导图 | **新增思维导图** |
| 知识可视化 | 无 | markmap 思维导图 | **新增** |
| Landing SEO | 无结构化数据 | 4 种 JSON-LD | **新增 FAQPage** |
| 营销话术 | 基础描述 | "零信息丢失"技术承诺 | **优化文案** |
| 浏览器插件 | 无 | Chrome/Edge/Firefox 全功能插件 | **远期规划** |
| RAG 问答 | 无 | 基于笔记 AI 问答 + Function Calling | **中期规划** |
| 笔记风格 | 固定 | 学术/口语/重点提取可选 | **新增** |
| 多版本记录 | 无 | 保留生成历史可回溯 | **远期规划** |
| B站字幕直抓 | API 获取 | 插件 Cookie 直抓（零成本） | **远期规划** |

---

## 🗺️ 功能详细设计

### 一、多平台支持 ⭐⭐⭐

**现状**：深度绑定 B 站，所有视频来源走 `bilibili_api`。  
**目标**：插件化平台适配器，config 中按平台开关。

#### 1.1 新增模块结构

```
services/platforms/                # 平台适配器目录
├── __init__.py                    # 平台注册中心
├── base.py                        # 抽象基类 PlatformAdapter
├── bilibili.py                    # B站适配器（搬运现有逻辑）
├── youtube.py                     # YouTube 适配器
├── douyin.py                      # 抖音适配器
├── kuaishou.py                    # 快手适配器
└── xiaoyuzhou.py                  # 小宇宙 FM 适配器
```

#### 1.2 PlatformAdapter 抽象基类

```python
class PlatformAdapter(ABC):
    """平台适配器基类 — 所有功能可 config 开关"""
    
    # ── 平台标识 ──
    platform_id: str          # "bilibili" / "youtube" / "douyin"
    platform_name: str        # "哔哩哔哩"
    
    # ── 核心能力（子类必须实现）──
    async def get_recommendations(count: int) -> list[VideoInfo]
    async def get_subtitles(video_id: str) -> str | None
    async def get_video_info(video_id: str) -> VideoInfo
    async def download_video(video_id: str) -> Path
    
    # ── 互动能力（可选实现，config 控制开关）──
    async def add_favorite(video_id: str) -> bool
    async def add_coin(video_id: str) -> bool
    async def post_comment(video_id: str, text: str) -> bool
    async def send_like(video_id: str) -> bool
```

#### 1.3 config.json 新增段

```json
{
  "platforms": {
    "bilibili": {
      "enabled": true,
      "cookies_file": "Data/bilibili_cookies.json",
      "owner_mid": 123456,
      "refresh_token": "",
      "max_daily_videos": 30
    },
    "youtube": {
      "enabled": false,
      "api_key": "",
      "max_daily_videos": 20,
      "language": "zh-CN"
    },
    "douyin": {
      "enabled": false,
      "cookie_string": "",
      "max_daily_videos": 15
    },
    "kuaishou": {
      "enabled": false
    },
    "xiaoyuzhou": {
      "enabled": false,
      "note": "小宇宙 FM — 仅音频转录，无视频"
    }
  },

  "platform_priority": ["bilibili", "youtube"],
  "platform_round_robin": false
}
```

#### 1.4 实现路线

| 阶段 | 内容 | 工作量 |
|------|------|--------|
| P1 | 抽象 `PlatformAdapter` 基类 + 重构 B 站为插件 | 3-4h |
| P2 | YouTube 适配器（youtube-transcript-api + pytube） | 4-5h |
| P3 | 抖音适配器（douyin-tiktok-scraper） | 3-4h |
| P4 | 快手 / 小宇宙适配器 | 各 2-3h |

#### 1.5 设计要点

- **向后兼容**：B 站适配器直接复用现有 `_brain_video.py` / `_bilibili_*.py` 逻辑，不做破坏性改动
- **轮询模式**：`platform_round_robin: true` 时，主循环轮流从各平台拉取推荐流
- **独立精力消耗**：每个平台可配不同的精力和冷却时间
- **统一 VideoInfo**：各平台返回统一的 `VideoInfo` 数据类，屏蔽差异

---

### 二、章节锁定 + 内容追加算法 ⭐⭐⭐

**现状**：长视频字幕全文一次性给 AI，容易超 token 或细节丢失。  
**启发**：BiliNote 先生成章节大纲并锁定，后续只追加内容不改写已有章。

#### 2.1 算法流程

```
长视频字幕 (60min+)
    │
    ├─→ ① AI 生成章节大纲（只做一次）
    │     prompt: "分析以下视频字幕，生成章节大纲。每章包含:
    │              标题 + 起始时间 + 本章核心问题"
    │     输出: [{title, start_time, core_question}, ...]  ← 锁定
    │
    ├─→ ② 按章节切片字幕
    │     chapter_1_subtitles = subtitles[0:180]
    │     chapter_2_subtitles = subtitles[180:360]
    │     ...
    │
    └─→ ③ 逐章追加内容（不做改写）
          对每个章节:
            prompt: "已有章节大纲: {outline}
                     当前章节字幕: {chapter_subtitles}
                     请提取本章核心知识点和关键案例，追加到笔记中。
                     ⚠️ 不要改写的已有章节内容，只追加新内容。"
            → 累积追加到 Markdown
```

#### 2.2 config.json 配置

```json
{
  "chapter_lock": {
    "enabled": true,
    "min_duration_minutes": 15,
    "model": "auto",
    "max_chapters_per_video": 12,
    "chapter_strategy": "ai_split",
    "strategies": {
      "ai_split": "AI 根据内容语义切分章节",
      "time_interval": "每 N 分钟切一个章节",
      "natural_breaks": "检测字幕中的话题转换点"
    }
  }
}
```

#### 2.3 实现位置

- `brain/_chapter_lock.py` — 新文件，章节锁定核心逻辑
- `brain/_brain_learn.py` — 在 `learn_from_video()` 中调用，替代现有全量处理逻辑
- 不影响短视频（<15min）的原有处理流程

---

### 三、思维导图导出（markmap）⭐⭐⭐

**现状**：知识只存为 Markdown 文件，无可视化。  
**目标**：基于 markmap，将知识笔记一键转为交互式思维导图 HTML。

#### 3.1 技术方案

- 使用 [markmap](https://markmap.js.org/)（MIT 开源），纯前端渲染
- 将 Markdown 的 `#` `##` `###` 层级自动转为思维导图节点
- 生成自包含 HTML 文件（内联 JS/CSS）

#### 3.2 config.json 配置

```json
{
  "mindmap": {
    "enabled": true,
    "auto_generate": true,
    "output_dir": "Data/MindMaps/",
    "theme": "default",
    "themes": ["default", "dark", "colorful"],
    "max_depth": 3,
    "inline_assets": true
  }
}
```

#### 3.3 导出触发方式

- **自动**：每次知识归档后自动生成对应思维导图
- **手动**：Web 面板一键导出（/api/export/mindmap）
- **批量**：一键生成全部知识库的思维导图索引

#### 3.4 实现位置

- `services/mindmap_export.py` — 新文件，Markdown → markmap HTML 转换器
- `html_exports/` — 已有导出目录，思维导图也存入此处
- 依赖：零外部 Python 依赖，纯字符串模板生成 HTML

---

### 四、多模型可选（面板切换）⭐⭐

**现状**：已支持多模型（chat/vision/image/fast/embedding），配置在 config.json 中。  
**目标**：Web 面板加模型选择下拉框，支持一键切换 GPT-4o / Claude / Gemini / DeepSeek。

#### 4.1 已有能力（无需重做）

✅ OpenAI 兼容 API（已支持任意 base_url）  
✅ 模型级 fallback + 跨服务商降级  
✅ 分场景独立模型配置（chat / vision / image / fast / embedding）

#### 4.2 新增内容

```json
{
  "model_presets": {
    "gpt4o": {
      "chat": "gpt-4o",
      "vision": "gpt-4o",
      "fast": "gpt-4o-mini",
      "base_url": "https://api.openai.com/v1"
    },
    "claude": {
      "chat": "claude-sonnet-4-20250514",
      "vision": "claude-sonnet-4-20250514",
      "fast": "claude-haiku-3-5-20250514",
      "base_url": "https://api.anthropic.com/v1"
    },
    "gemini": {
      "chat": "gemini-2.5-pro",
      "vision": "gemini-2.5-pro",
      "fast": "gemini-2.5-flash",
      "base_url": "https://generativelanguage.googleapis.com/v1beta"
    },
    "deepseek": {
      "chat": "deepseek-chat",
      "vision": "deepseek-chat",
      "fast": "deepseek-chat",
      "base_url": "https://api.deepseek.com/v1"
    }
  },
  "active_preset": "gpt4o"
}
```

#### 4.3 Web 面板改动

- 新增"模型切换"卡片：下拉选择 preset → 即时切换
- 切换后自动更新 API base_url 和模型名
- 保留现有 fallback 机制（每个 preset 下依然有回退）

---

### 五、多导出格式扩展 ⭐

**现状**：仅 Markdown (.md)。  
**目标**：新增 PDF、思维导图，保留延展性给 Word/PPT。

#### 5.1 导出格式一览

| 格式 | 优先级 | 实现方式 | 依赖 |
|------|--------|---------|------|
| Markdown | ✅ 已有 | 直接写入 .md | 无 |
| 思维导图 | 🆕 P0 | markmap HTML | 无外部依赖 |
| PDF | 🆕 P1 | Markdown → HTML → PDF (weasyprint) | weasyprint |
| Word | 🔮 P2 | python-docx | python-docx |
| PPT | 🔮 P2 | python-pptx | python-pptx |

#### 5.2 config.json 配置

```json
{
  "export": {
    "formats": ["markdown", "mindmap"],
    "pdf": {
      "enabled": false,
      "page_size": "A4",
      "font_family": "Inter, sans-serif"
    },
    "auto_export_on_save": true
  }
}
```

---

### 七、RAG 知识库问答 ⭐⭐⭐⭐

**现状**：知识归档后只能通过文件系统查看，无交互式查询。  
**启发**：BiliNote 的 RAG 问答支持 Function Calling，用户可对已生成的笔记提问。

#### 7.1 技术方案

```
用户提问
    │
    ├─→ ① 向量检索（已有 embedding 能力）
    │     在知识库中检索相关笔记片段
    │
    ├─→ ② 构建 RAG 上下文
    │     prompt = 检索到的知识片段 + 用户问题
    │
    └─→ ③ LLM 生成回答
         支持 Function Calling 查阅原文
```

#### 7.2 接入方式

- **Web 面板**：知识库页面新增"AI 问答"输入框
- **B站评论区**：在任意视频下 @bot 提问（利用已有通知模式）
- **API**：`/api/knowledge/ask` 接口

#### 7.3 config.json 配置

```json
{
  "rag_qa": {
    "enabled": false,
    "model": "auto",
    "max_context_chunks": 5,
    "enable_function_calling": true,
    "sources": ["knowledge_base", "single_video"]
  }
}
```

#### 7.4 实现位置

- `services/rag_qa.py` — 新文件，RAG 检索 + 问答
- 复用现有 `embedding` 模型做向量化
- `web_panel.py` — 新增问答 UI
- `brain/standby.py` — 评论区 @bot 问答触发

---

### 八、浏览器插件 ⭐⭐⭐⭐⭐

**现状**：用户必须访问 Web 面板或 CLI 操作。  
**启发**：BiliNote 的浏览器插件是用户最便捷的交互入口——悬浮按钮、侧边栏、右键菜单、B站字幕直抓。

#### 8.1 插件核心功能

| 功能 | 描述 |
|------|------|
| **悬浮按钮** | B站视频页右下角浮窗，一键"总结此视频" |
| **侧边栏** | 视频旁侧边栏展示 Markdown 笔记 / 思维导图 / AI 问答 |
| **右键菜单** | 选中文字右键 → "向 bot 提问" |
| **B站字幕直抓** | 利用用户 Cookie 直接抓取 B站字幕接口，跳过 API 调用 |
| **快捷面板** | 查看 bot 状态、今日学习报告 |

#### 8.2 技术方案

- Manifest V3 规范（Chrome/Edge/Firefox 兼容）
- 插件通过 WebSocket 或 HTTP 与本地 bot 通信
- B站字幕直抓：拦截 B站 `player` API 的子幕接口，用用户 Cookie 鉴权

#### 8.3 config.json 配置

```json
{
  "browser_extension": {
    "enabled": false,
    "port": 9527,
    "auto_open_sidebar": false,
    "subtitle_direct_capture": true,
    "note": "需要配合浏览器插件使用，见 extension/ 目录"
  }
}
```

#### 8.4 实现位置

- `extension/` — 新目录，浏览器插件源码（Manifest V3 + Vue/原生JS）
- `main.py` — 新增 WebSocket 端点供插件连接
- 与现有通知模式互补：插件是主动触发，通知模式是被动监控

---

### 九、笔记风格定制 ⭐⭐⭐

**现状**：所有笔记用同一种 prompt 模板。  
**启发**：BiliNote 支持学术严谨 / 口语化 / 重点提取三种风格。

#### 9.1 可选风格

```json
{
  "note_style": {
    "enabled": true,
    "active_style": "balanced",
    "styles": {
      "academic": {
        "name": "学术严谨",
        "prompt_suffix": "请使用学术论文风格，引用原文数据，标注时间戳。",
        "output_language": "zh-CN"
      },
      "conversational": {
        "name": "口语化",
        "prompt_suffix": "请用通俗易懂的口语化表达，像朋友聊天一样解释概念。",
        "output_language": "zh-CN"
      },
      "key_points": {
        "name": "重点提取",
        "prompt_suffix": "只提取核心观点和关键数据，忽略铺垫和废话，用 bullet points。",
        "output_language": "zh-CN"
      },
      "balanced": {
        "name": "平衡模式（默认）",
        "prompt_suffix": "结构清晰、重点突出、适当保留细节。",
        "output_language": "zh-CN"
      }
    }
  }
}
```

#### 9.2 实现方式

- 在 `brain/_brain_learn.py` 的 prompt 模板末尾追加 `prompt_suffix`
- Web 面板加下拉框切换风格
- 不同风格的笔记存入不同子目录或加标签

---

### 十、多版本记录 ⭐⭐

**现状**：每次重新处理同一视频会覆盖旧笔记。  
**启发**：BiliNote 保留每次生成的历史版本，可对比回溯。

#### 10.1 实现方案

```
Data/Knowledge/
├── BV1xx_20260706_v1.md      # 第一版笔记
├── BV1xx_20260706_v2.md      # 用不同模型重新生成
└── BV1xx_latest.md           # symlink → 最新版本
```

#### 10.2 config.json 配置

```json
{
  "version_history": {
    "enabled": false,
    "max_versions": 5,
    "diff_on_regenerate": true,
    "note": "保留每次重新生成的笔记历史，可对比不同模型/风格的输出差异"
  }
}
```

---

### 六、Landing 页优化 ⭐

#### 6.1 "零信息丢失"话术升级

当前着陆页描述：
> 自动拉取推荐流，AI 深度理解视频内容，智能评分后收藏投币，知识自动归档入库。

优化为：
> **长视频零信息丢失**：章节锁定 + 内容追加算法，60 分钟视频每个观点、数据、案例全部保留，绝不因总结而遗漏。

在 Features 区域新增一个卡片：
> 🎯 **长视频零信息丢失**  
> AI 先生成章节大纲并锁定，后续逐章追加内容而非改写。确保 60 分钟以上的长视频所有知识点完整保留。

#### 6.2 FAQPage 结构化数据（SEO）

在 `landing.html` 的 `<head>` 中新增 JSON-LD：

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "bilibili_learning_bot 是什么？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "一个全自动的 B 站 AI 学习机器人，自动拉取推荐流、AI 深度理解视频内容、智能评分后收藏投币、知识自动归档入库。"
      }
    },
    {
      "@type": "Question",
      "name": "支持哪些 AI 模型？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "支持 GPT-4o、Claude、Gemini、DeepSeek 等主流大模型，通过 OpenAI 兼容 API 调用，可在 Web 面板中一键切换。"
      }
    },
    {
      "@type": "Question",
      "name": "如何部署？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "支持 Docker、Termux（安卓）、Linux 多平台部署。克隆仓库后配置 API Key，一行命令即可启动。"
      }
    },
    {
      "@type": "Question",
      "name": "长视频总结会丢失信息吗？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "不会。我们采用章节锁定 + 内容追加算法，先生成章节大纲并锁定，逐章追加内容，确保所有观点和细节完整保留。"
      }
    },
    {
      "@type": "Question",
      "name": "是免费的吗？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "项目基于 MIT License 完全开源免费。你需要自备 AI API Key（如 OpenAI），bot 本身不收取任何费用。"
      }
    }
  ]
}
</script>
```

---

## 📅 实施优先级

| 优先级 | 功能 | 理由 |
|--------|------|------|
| **P0 立即** | Landing FAQPage SEO | 零成本，立即提升搜索可见度 |
| **P0 立即** | Landing "零信息丢失"话术 | 不改代码，文案优化 |
| **P0 立即** | 章节锁定 + 内容追加 | 核心差异化功能，解决真实痛点 |
| **P1 本周** | 思维导图导出 | markmap 实现简单，效果惊艳 |
| **P1 本周** | 笔记风格定制 | 改动极小，只加 prompt_suffix，体验提升大 |
| **P1 本周** | Web 面板模型切换 | 复用已有面板，改动小效果好 |
| **P1 本周** | PlatformAdapter 抽象 + B 站重构 | 整理架构，为多平台铺路 |
| **P2 两周** | RAG 知识库问答 | 知识消费升级，Web 面板 + 评论区双入口 |
| **P2 两周** | YouTube 适配器 | 最大用户需求的第二平台 |
| **P2 两周** | 多版本记录 | 改动小，锦上添花 |
| **P3 远期** | 浏览器插件 | 工程量大但体验最佳，需要跨项目协作 |
| **P3 远期** | 桌面客户端 (Tauri) | 降低小白用户部署门槛 |
| **P3 远期** | 抖音/快手/小宇宙 | 低频需求，按需推进 |
| **P3 远期** | PDF/Word/PPT 导出 | 依赖第三方库，非核心 |
| **P3 远期** | 多模态视频理解 | 架构改动大，需图像+音频处理管线 |

---

## ⚙️ 配置文件完整预览（所有新增段）

```json
{
  "_comment": "=== 以下为本次规划新增配置段 ===",

  "platforms": {
    "bilibili": { "enabled": true, "max_daily_videos": 30 },
    "youtube":  { "enabled": false, "api_key": "", "max_daily_videos": 20 },
    "douyin":   { "enabled": false },
    "kuaishou": { "enabled": false },
    "xiaoyuzhou": { "enabled": false }
  },
  "platform_priority": ["bilibili"],
  "platform_round_robin": false,

  "model_presets": {
    "gpt4o":    { "chat": "gpt-4o", "fast": "gpt-4o-mini", "base_url": "https://api.openai.com/v1" },
    "claude":   { "chat": "claude-sonnet-4-20250514", "fast": "claude-haiku-3-5-20250514", "base_url": "https://api.anthropic.com/v1" },
    "gemini":   { "chat": "gemini-2.5-pro", "fast": "gemini-2.5-flash", "base_url": "..." },
    "deepseek": { "chat": "deepseek-chat", "fast": "deepseek-chat", "base_url": "https://api.deepseek.com/v1" }
  },
  "active_preset": "gpt4o",

  "chapter_lock": {
    "enabled": true,
    "min_duration_minutes": 15,
    "max_chapters_per_video": 12,
    "chapter_strategy": "ai_split"
  },

  "mindmap": {
    "enabled": true,
    "auto_generate": true,
    "output_dir": "Data/MindMaps/",
    "theme": "default",
    "max_depth": 3
  },

  "export": {
    "formats": ["markdown", "mindmap"],
    "auto_export_on_save": true
  },

  "note_style": {
    "enabled": true,
    "active_style": "balanced",
    "styles": {
      "academic":        { "prompt_suffix": "学术论文风格，引用原文数据，标注时间戳。" },
      "conversational":  { "prompt_suffix": "口语化表达，像朋友聊天一样解释概念。" },
      "key_points":      { "prompt_suffix": "只提取核心观点和关键数据，用 bullet points。" },
      "balanced":        { "prompt_suffix": "结构清晰、重点突出、适当保留细节。" }
    }
  },

  "rag_qa": {
    "enabled": false,
    "model": "auto",
    "max_context_chunks": 5,
    "enable_function_calling": true
  },

  "version_history": {
    "enabled": false,
    "max_versions": 5,
    "diff_on_regenerate": true
  },

  "browser_extension": {
    "enabled": false,
    "port": 9527,
    "subtitle_direct_capture": true
  }
}
```

---

> 📝 **审批后进入实施阶段，按 P0 → P1 → P2 → P3 顺序推进。**
