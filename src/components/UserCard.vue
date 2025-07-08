<template>
  <div class="card">
    <img :src="avatar" alt="User avatar" />
    <h3>{{ name }}</h3>
    <p>{{ description }}</p>
  </div>
</template>

<script setup>
defineProps({
  name: String,
  description: String,
  avatar: String
})
</script>

<style scoped>
.card {
  width: 200px;
  padding: 15px;
  border-radius: 8px;
  border: 1px solid #ddd;
  text-align: center;
}
.card img {
  width: 100px;
  height: 100px;
  border-radius: 50%;
}
</style>
