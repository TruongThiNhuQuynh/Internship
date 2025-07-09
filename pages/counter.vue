<script setup>
const count = useState('count', () => 0)
</script>

<template>
  <h1>Bộ đếm toàn cục</h1>
  <p>Giá trị hiện tại: {{ count }}</p>
  <button @click="count++">Tăng</button>
</template>
