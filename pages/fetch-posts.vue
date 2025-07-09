<script setup>
const { data: posts, pending, error } = await useFetch('https://jsonplaceholder.typicode.com/posts')
</script>

<template>
  <h1>Danh sách bài viết</h1>
  <div v-if="pending">Đang tải...</div>
  <div v-else-if="error">Lỗi: {{ error.message }}</div>
  <ul>
    <li v-for="post in posts" :key="post.id">
      {{ post.title }}
    </li>
  </ul>
</template>
