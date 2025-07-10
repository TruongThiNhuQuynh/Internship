<script setup>
const config = useRuntimeConfig()
</script>

<template>
  <div style="padding: 30px">
    <h2>🔧 Environment Test</h2>
    <p>🌐 API Base: {{ config.public.apiBase }}</p>
  </div>
</template>
