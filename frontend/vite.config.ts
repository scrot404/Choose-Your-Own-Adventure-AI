import { defineConfig, loadEnv } from 'vite'
import react from '@vitejs/plugin-react'
import dotenv from 'dotenv'

// https://vite.dev/config/
export default defineConfig(({ mode }) => {
  const dotenvResult = dotenv.config({
    path: [`.env.${mode}.local`, `.env.${mode}`, '.env.local', '.env']
  })
  if (dotenvResult.error && dotenvResult.error.code !== 'ENOENT') {
    throw dotenvResult.error
  }
  const env = loadEnv(mode, process.cwd(), 'VITE_')

  return {
    plugins: [react()],
    server: {
      ...(env.VITE_DEBUG !== 'false' && {
        proxy: {
          '/api': {
            target: env.VITE_PROXY_TARGET || 'http://localhost:8000',
            changeOrigin: true,
            secure: false
          }
        }
      })
    }
  }
})