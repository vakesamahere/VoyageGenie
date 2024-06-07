const { defineConfig } = require('@vue/cli-service')
const Markdown = require('unplugin-vue-markdown/webpack')
const prism = require('markdown-it-prism')

module.exports = defineConfig({
  transpileDependencies: true,
  parallel: false,
  chainWebpack: (config) => {
    config.module
      .rule('vue')
      .test(/\.(vue|md)$/)

    config
      .plugin('markdown')
      .use(Markdown({
        markdownItUses: [
          prism,
        ],
      }))
  },
  devServer: {
    proxy: {
      '/api': {
        target: 'https://dashscope.aliyuncs.com',
        changeOrigin: true,
        pathRewrite: {
          '^/api': ''
        },
        logLevel:"debug",
        onProxyReq: function(proxyReq, req, res) {
          // 请求被代理时打印当前时间
          console.log('Received HTML request at', new Date().toLocaleTimeString());
        }
      }
    }
  }
})