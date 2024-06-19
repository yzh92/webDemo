import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
    server:{
        proxy:{
            //将以/api开头的请求代理到目标服务器
            '/api':{
            target:'http://localhost:5000',
            changeOrigin:true,
            rewrite:(path) => path.replace(/^\/api/,'')
        }
    }
}
})
