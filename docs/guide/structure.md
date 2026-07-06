# 项目结构

```
├── main.py               # 🚀 主程序唯一流启动入口
├── start_cli.py          # 💻 终端菜单兼容层
├── web_panel.py          # 🌐 Flask 可视化管理面板（支持亮暗主题切换）
├── api/                  # 🔌 B站 API 鉴权/流控/风控层
│   ├── client.py         # HTTP/2 连接复用、WBI签名缓存
│   └── subtitles.py      # 字幕获取与412风控降级 fallback
├── brain/                # 🧠 核心混入多重组合大脑
│   ├── agent_brain.py    # 55行纯委托类 (包含13个核心 Mixin)
│   ├── _brain_loop.py    # 主推荐流状态机轮巡核心
│   └── monitor.py        # 📡 实时独立被动监听引擎
├── cli/                  # 💻 交互菜单命令与终端界面
├── core/                 # ⚙️ 全局常量、环境变量及核心配置
├── knowledge/            # 📚 三层分类知识库、浏览、整理与重温
├── persona/              # 🎭 人格/心情/日记/进化管理系统
├── security/             # 🛡️ 内容安全审查防线
├── services/             # 🔧 外部服务与工具封装
└── templates/            # 🎨 内置 Claude 专业设计卡片规范模板
```
