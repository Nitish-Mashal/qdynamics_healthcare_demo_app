import fs from 'fs'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'
import { getProxyOptions } from 'frappe-ui/src/utils/vite-dev-server'
import { webserver_port } from '../../../sites/common_site_config.json'

const appRoot = path.resolve(__dirname, '..')
const appModuleDir = path.join(appRoot, path.basename(appRoot))
const outDir = path.join(appModuleDir, 'public', 'frontend')

function syncFrappeHomepage() {
  return {
    name: 'sync-frappe-homepage',
    apply: 'build',
    closeBundle() {
      const homepage = path.join(appModuleDir, 'www', 'index.html')
      fs.mkdirSync(path.dirname(homepage), { recursive: true })
      fs.copyFileSync(
        path.join(outDir, 'index.html'),
        homepage,
      )
    },
  }
}

// https://vitejs.dev/config/
export default defineConfig({
  base: process.env.NODE_ENV === 'production'
    ? '/assets/qdynamics_healthcare_demo_app/frontend/'
    : '/',
  plugins: [vue(), syncFrappeHomepage()],
  server: {
    port: 8080,
    proxy: getProxyOptions({ port: webserver_port }),
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
    },
  },
  build: {
    outDir,
    emptyOutDir: true,
    target: 'es2015',
  },
  optimizeDeps: {
    include: ['frappe-ui > feather-icons', 'showdown', 'engine.io-client'],
  },
})
