<template>
  <div class="info">
    <h2>User Info</h2>
    <p>Name: {{ name }}</p>
    <p>Age: {{ age }}</p>
    <p>Status: {{ isActive ? 'Active' : 'Inactive' }}</p>
  </div>
</template>

<script lang="ts" setup>
import { defineProps, ref } from 'vue'

const props = defineProps<{
  name: string
  age: number
  isActive: boolean
}>()

// Dùng biến với type rõ ràng
const message: string = 'Welcome!'
const count = ref<number>(0)

function increment(): void {
  count.value++
}
</script>

<style scoped>
.info {
  border: 1px solid #ccc;
  padding: 10px;
  margin-top: 10px;
}
</style>
