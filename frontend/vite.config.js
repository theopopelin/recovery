import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
    base: '/recovery/',

    plugins: [vue()],

    server: {
        watch: {
            usePolling: true,
        },
    },
})