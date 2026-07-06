# Cloudflare Workers 部署

## 文件结构

- `wrangler.toml` - Wrangler 配置文件
- `index.js` - Worker 入口脚本
- `public/` - 静态文件目录（VitePress 构建产物）
- `.github/workflows/deploy.yml` - GitHub Actions 自动部署

## 部署方式

### 方式一：GitHub Actions 自动部署

1. 在 GitHub 仓库 Settings > Secrets and variables > Actions 中添加：
   - `CF_API_TOKEN` - Cloudflare API Token
   - `CF_ACCOUNT_ID` - Cloudflare Account ID

2. 推送到 main 分支，自动触发部署

### 方式二：本地 Wrangler CLI

```bash
npm install -g wrangler
wrangler login
wrangler deploy
```

## 获取 Cloudflare Token

1. 访问 https://dash.cloudflare.com/profile/api-tokens
2. 点击 "Create Token"
3. 选择 "Edit Cloudflare Workers" 模板
4. 复制 Token 添加到 GitHub Secrets

## Account ID

在 Cloudflare 控制台右侧边栏查看 Account ID。
