<script setup>
const { data: products, pending, error } = await useFetch('/api/products')
</script>

<template>
  <div style="padding: 30px">
    <h2>🛍 Danh sách sản phẩm</h2>

    <div v-if="pending">⏳ Đang tải...</div>
    <div v-else-if="error">❌ Lỗi: {{ error.message }}</div>
    <ul v-else>
      <li v-for="product in products" :key="product.id">
        🧾 {{ product.name }} — 💰 {{ product.price }}$
      </li>
    </ul>
  </div>
</template>
