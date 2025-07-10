<script setup>
const config = useRuntimeConfig()
const email = ref('')
const password = ref('')
const result = ref('')
const loading = ref(false)

async function handleLogin() {
  loading.value = true
  result.value = ''

  console.log('Gọi đến:', `${config.public.apiBase}/login`)

  try {
    const res = await $fetch(`${config.public.apiBase}/login`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': config.public.apiKey   // Thêm dòng này để gửi API key
      },
      body: {
        email: email.value,
        password: password.value
      }
    })

    result.value = `✅ Login thành công:\n${JSON.stringify(res, null, 2)}`
  } catch (err) {
    result.value = `❌ Lỗi đăng nhập: ${err.data?.error || err.message}`
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div style="max-width: 400px; margin: auto; padding: 30px">
    <h2>Đăng nhập</h2>

    <label>Email:</label>
    <input v-model="email" type="email" placeholder="john@doe.com" />

    <label>Password:</label>
    <input v-model="password" type="password" placeholder="******" />

    <button @click="handleLogin" :disabled="loading">
      {{ loading ? 'Đang gửi...' : 'Đăng nhập' }}
    </button>

    <p style="margin-top: 10px; white-space: pre-line;">{{ result }}</p>
  </div>
</template>

<style scoped>
input {
  display: block;
  margin-bottom: 10px;
  padding: 6px;
  width: 100%;
}
button {
  padding: 8px 12px;
}
</style>
