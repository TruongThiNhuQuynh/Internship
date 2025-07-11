<script setup>
const { data: posts } = await useAsyncData('posts', () =>
  $fetch('https://jsonplaceholder.typicode.com/posts')
)
</script>

<template>
  <h1>Bài viết (AsyncData)</h1>
  <ul>
    <li v-for="post in posts" :key="post.id">
      {{ post.title }}
    </li>
  </ul>
</template>
