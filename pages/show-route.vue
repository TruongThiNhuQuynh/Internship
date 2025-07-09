<script setup>
const route = useRoute()
</script>

<template>
  <div>
    <h1>Thông tin Route hiện tại</h1>
    <p><strong>Path:</strong> {{ route.path }}</p>
    <p><strong>Query:</strong> {{ route.query }}</p>
  </div>
</template>
