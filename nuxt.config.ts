// https://nuxt.com/docs/api/configuration/nuxt-config
// export default defineNuxtConfig({
//   compatibilityDate: '2025-05-15',
//   devtools: { enabled: true }
// })

// export default defineNuxtConfig({
//   runtimeConfig: {
//     public: {
//       apiBase: 'https://reqres.in/api',
//       apiKey: 'reqres-free-v1' 
//     },
//     privateKey: 'THIS_IS_SECRET'
//   }
// })

// export default defineNuxtConfig({
//   runtimeConfig: {
//     // Biến này chỉ dùng được ở server (backend)
//     privateApiKey: process.env.NUXT_PRIVATE_API_KEY,

//     public: {
//       // Biến public dùng được cả trong client
//       apiBase: process.env.NUXT_PUBLIC_API_BASE || 'http://localhost:3000/api'
//     }
//   }
// })

import { defineNuxtConfig } from 'nuxt/config'

export default defineNuxtConfig({
  // Kích hoạt DevTools nếu cần
  devtools: { enabled: true },

  // Biến môi trường runtime
  runtimeConfig: {
    public: {
      apiBase: process.env.NUXT_PUBLIC_API_BASE || 'https://reqres.in/api',
      apiKey: process.env.NUXT_PUBLIC_API_KEY || 'reqres-free-v1'
    },
    privateKey: process.env.PRIVATE_KEY || 'THIS_IS_SECRET'
  },

  // Optional: Nếu có dùng TypeScript strict
  typescript: {
    strict: true
  }
})



