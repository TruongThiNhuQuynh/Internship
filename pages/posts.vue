<script setup>
const { data: posts, pending, error } = await useFetch('/api/posts')
</script>

<template>
  <div style="padding: 30px">
    <h2>📰 Danh sách bài viết</h2>

    <div v-if="pending">⏳ Đang tải...</div>
    <div v-else-if="error">❌ Lỗi: {{ error.message }}</div>
    <ul v-else>
      <li v-for="post in posts" :key="post.id">
        📌 <strong>{{ post.title }}</strong> — ✍️ {{ post.author }}
      </li>
    </ul>
  </div>
</template>
