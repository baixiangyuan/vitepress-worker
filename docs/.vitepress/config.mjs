import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'bilibili_learning_bot',
  description: '全自动 B 站 AI 学习互动机器人手册',
  base: '/',
  lang: 'zh-CN',
  appearance: true,

  head: [
    ['link', { rel: 'preconnect', href: 'https://fonts.googleapis.com' }],
    ['link', { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' }],
    ['link', { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap' }],
    ['link', { rel: 'stylesheet', href: '/style.css' }],
    ['link', { rel: 'icon', type: 'image/jpeg', href: 'https://phototestbxybilibili.bxya.top' }],
    ['script', { charset: 'UTF-8', id: 'LA_COLLECT', src: '//sdk.51.la/js-sdk-pro.min.js' }],
    ['script', {}, `LA.init({id:"3QFckgiZTB513DZG",ck:"3QFckgiZTB513DZG",hashMode:true,screenRecord:true})`]
  ],

  themeConfig: {
    logo: '/logo.svg',

    nav: [
      { text: '指南', link: '/guide/' },
      { text: '部署', link: '/deploy/' },
      { text: '日志', link: '/changelog' },
      { text: '隐私', link: '/privacy' },
      { text: '联系我们', link: '/contact' },
      { text: '💰 赞助', link: '/sponsor' }
    ],

    sidebar: [
      {
        text: '📖 项目指南',
        items: [
          { text: '项目简介', link: '/guide/' },
          { text: '功能特点', link: '/guide/features' },
          { text: '项目结构', link: '/guide/structure' },
          { text: '主菜单', link: '/guide/menu' }
        ]
      },
      {
        text: '💻 部署指南',
        items: [
          { text: '快速开始', link: '/deploy/' },
          { text: 'Linux 配置', link: '/deploy/linux' },
          { text: 'Termux 安卓', link: '/deploy/termux' },
          { text: '高级集群', link: '/deploy/cluster' }
        ]
      },
      {
        text: '📜 更新日志',
        link: '/changelog'
      },
      {
        text: '🔒 隐私安全',
        link: '/privacy'
      },
      {
        text: '📮 联系我们',
        link: '/contact'
      },
      {
        text: '💰 赞助支持',
        link: '/sponsor'
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/xiaoyaya191/bilibili_learning_bot' }
    ],

    footer: {
      message: '基于 MIT License 开源',
      copyright: 'Copyright © 2026'
    },

    search: {
      provider: 'local'
    }
  }
})
