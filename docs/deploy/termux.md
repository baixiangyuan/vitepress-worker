# Android Termux 智能手机挂机配置

在 Android 手机利用 Termux 长期挂机的核心配置：

```bash
# 1. 克隆仓库
git clone https://github.com/xiaoyaya191/bilibili_learning_bot.git
cd bilibili_learning_bot

# 2. 安装依赖（优先用轻量换源源）
pip install -r requirements.txt

# 3. 启动监听模式（CPU 最低，省流量）
python main.py --monitor
```

::: tip 省电建议
- 系统关闭监控模式、各类动态壁纸与自启动管理器
- 将设备接入有线电源，保持 "保持唤醒状态"
- 优先使用 `--monitor` 监听模式而非完整扫描
:::
