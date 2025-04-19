import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  build: {
    rollupOptions: {
      external: ['react-dom/client'], // "react-dom/client" modulini tashqi bog'liq qilib belgilash
    },
  },
})
