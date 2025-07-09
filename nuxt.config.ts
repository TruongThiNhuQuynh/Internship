// https://nuxt.com/docs/api/configuration/nuxt-config
// export default defineNuxtConfig({
//   compatibilityDate: '2025-05-15',
//   devtools: { enabled: true }
// })
export default defineNuxtConfig({
  runtimeConfig: {
    public: {
      apiBase: 'https://reqres.in/api',
      apiKey: 'reqres-free-v1' 
    },
    privateKey: 'THIS_IS_SECRET'
  }
})
