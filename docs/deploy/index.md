# 部署与快速开始

## 1. 安装运行环境依赖

::: warning
请确保安装最新的 `bilibili-api-python`（>=17.4.1），不要错装已被弃用的旧包。
:::

```bash
pip install -r requirements.txt
# 若之前环境混淆错装了旧包，请先执行清空：
# pip uninstall bilibili-api -y

# 推荐安装 ffmpeg 以便用于执行多模态视频视觉帧断点切片抽帧
# apt install ffmpeg     # Linux
# pkg install ffmpeg     # Termux
```

## 2. 初始化运行配置文件

```bash
cp config.example.json Data/config.json
# 打开 Data/config.json 并按需填入大模型 API Key（统一中转或兼容接口）
```

## 3. 呼叫控制端启动

| 启动模式 | 命令 | 说明 |
|----------|------|------|
| 单实例 | `python main.py` | 💻 终端菜单交互模式 |
| 后台监听 | `python main.py --monitor` | 📡 纯监听模式（CPU最低） |
| Web 面板 | `python web_panel.py` | 🌐 Flask 浏览器可视化管理 |
| Docker | `docker-compose up -d` | 🐳 一键容器化部署 |
