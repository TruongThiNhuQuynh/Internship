<script setup>
const { data: posts } = await useFetch('https://jsonplaceholder.typicode.com/posts')

useHead({
  title: 'Blog cá nhân',
  meta: [{ name: 'description', content: 'Blog mẫu sử dụng Nuxt composables' }]
})
</script>

<template>
  <h1>Blog Cá Nhân</h1>
  <ul>
    <li v-for="post in posts" :key="post.id">
      <h3>{{ post.title }}</h3>
      <p>{{ post.body }}</p>
    </li>
  </ul>
</template>
