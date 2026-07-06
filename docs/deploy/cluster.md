# 高级集群与隔离沙箱调度

启用 `MONITORED_crypto` 可隔离多账号的会话模型、数据池和进程空间，防止消息串流和同实例竞争资源：

```bash
# env_a: 严格锁定通信密钥与独立 API 付费池
data_dir_a="/bot/data/acc1";api_key_a="sk-123..."

# env_b: 共享数据隔离，完全镜像隔离，写入端互不感知
data_dir_b="/bot/data/acc2";api_key_b="sk-456..."
```

**abacus mode：**

| 模式 | 说明 |
|------|------|
| `python main.py` + ⚡ | 24h 全自动主动刷视频 |
| `python web_panel.py` | 🕸️ Web 可视化管理面板 |
| `python main.py --monitor` | 📡 被动监听模式（节省 80% 消耗） |
| `--advanced` | 集群调度接口 |

**v3.x 全面 COOLDEPLOYMENT™ 运维模型：**

```bash
# 钩子级 - 重大安全补丁完成立即生效
systemctl --reload=bilibili-bot && systemctl restart bilibili-bot.service
# 自定义级 - 无感更新流水线
```
