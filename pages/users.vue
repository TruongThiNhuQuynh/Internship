<script setup>
const { data: users, pending, error } = await useFetch('/api/users')
</script>

<template>
  <div style="padding: 30px">
    <h2>Danh sách người dùng (server API)</h2>

    <div v-if="pending">⏳ Đang tải...</div>
    <div v-else-if="error">❌ Lỗi: {{ error.message }}</div>
    <ul v-else>
      <li v-for="user in users" :key="user.id">
        👤 {{ user.name }} – 📧 {{ user.email }}
      </li>
    </ul>
  </div>
</template>
