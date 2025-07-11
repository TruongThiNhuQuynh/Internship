<script setup>
const count = useState('count', () => 0)
</script>

<template>
  <h3>Global Count: {{ count }}</h3>
  <button @click="count++">Tăng</button>
</template>
