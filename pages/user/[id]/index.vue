<!-- pages/user/[id]/index.vue -->
<template>
  <div>
    <h1>Trang thông tin người dùng</h1>
    <p>ID người dùng: {{ id }}</p>
  </div>
</template>

<script setup>
const route = useRoute()
const id = route.params.id
</script>
