# 更新日志

<script setup>
import { ref, onMounted } from 'vue'

const releases = ref([])
const loading = ref(true)
const error = ref('')

onMounted(async () => {
  try {
    const res = await fetch('https://api.github.com/repos/xiaoyaya191/bilibili_learning_bot/releases')
    if (!res.ok) throw new Error('获取失败')
    releases.value = await res.json()
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
})

// 简单的 markdown 转 HTML 函数
function mdToHtml(text) {
  if (!text) return ''
  
  return text
    // 换行
    .replace(/\n/g, '<br>')
    // 粗体
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    // 斜体
    .replace(/\*(.*?)\*/g, '<em>$1</em>')
    // 代码
    .replace(/`([^`]+)`/g, '<code style="background:rgba(217,119,87,0.1);padding:2px 6px;border-radius:4px;font-size:0.85em;">$1</code>')
    // 链接
    .replace(/\[(.*?)\]\((.*?)\)/g, '<a href="$2" target="_blank" style="color:var(--vp-c-brand-1);text-decoration:underline;">$1</a>')
    // 列表项
    .replace(/^- (.*)$/gm, '• $1')
    // 标题
    .replace(/^#{1,3}\s+(.*)$/gm, '<h4 style="margin:8px 0;color:var(--vp-c-brand-1);">$1</h4>')
}
</script>

<div v-if="loading" class="loading">加载中...</div>

<div v-else-if="error" class="warning">加载失败: {{ error }}</div>

<div v-else class="releases">
  <div v-for="release in releases.slice(0, 10)" :key="release.id" class="release-card">
    <div class="release-header">
      <h3>{{ release.name || release.tag_name }}</h3>
      <span class="release-date">{{ new Date(release.published_at).toLocaleDateString('zh-CN') }}</span>
    </div>
    <div class="release-body" v-html="mdToHtml(release.body)"></div>
    <a :href="release.html_url" target="_blank" class="release-link">查看详情 →</a>
  </div>
</div>

<style scoped>
.loading {
  text-align: center;
  padding: 2rem;
  color: var(--vp-c-text-2);
}

.warning {
  color: var(--vp-c-warning);
  padding: 1rem;
  border-radius: 8px;
  background: var(--vp-c-bg-alt);
}

.releases {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.release-card {
  padding: 1.5rem;
  border-radius: 12px;
  background: var(--vp-c-bg-alt);
  border: 1px solid var(--vp-c-border);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.release-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.06);
}

.release-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.release-header h3 {
  margin: 0;
  color: var(--vp-c-brand-1);
  font-size: 1.2rem;
}

.release-date {
  color: var(--vp-c-text-2);
  font-size: 0.85rem;
}

.release-body {
  color: var(--vp-c-text-2);
  line-height: 1.8;
  font-size: 0.9rem;
}

.release-body br {
  display: block;
  margin: 4px 0;
}

.release-link {
  display: inline-block;
  margin-top: 1rem;
  color: var(--vp-c-brand-1);
  text-decoration: none;
  font-size: 0.9rem;
  transition: color 0.2s ease;
}

.release-link:hover {
  color: var(--vp-c-brand-2);
}
</style>
