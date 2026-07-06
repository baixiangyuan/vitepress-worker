# Linux 深度配置手册

要在一台 PC 或服务器上完成全自动长期挂机运行，推荐结合 **systemd 守护服务 + cron 定期重启** 部署：

```ini
[Unit]
Description=Bilibili Learning Bot
After=network.target

[Service]
Type=simple
User=bili
WorkingDirectory=/home/bili/bilibili_learning_bot
Environment="DISPLAY=:0"
ExecStart=/home/bili/.local/bin/pipenv run python main.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Atomic-Restart 脚本 `/usr/local/bin/bili-restart.sh`：

```bash
#!/bin/bash
cd /home/bili/bilibili_learning_bot
zip -r "$(date +%Y%m%d_%H%M).zip" Data/*.json
git pull --ff-only
pipenv install --deploy --ignore-pipfile
touch trigger_restart
systemctl restart bilibili-bot.service
```
