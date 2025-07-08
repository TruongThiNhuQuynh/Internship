<template>
  <div>
    <h2>Composition API Demo</h2>
    <input v-model="name" placeholder="Enter your name" />
    <p>Hello, {{ upperName }}</p>
    <button @click="reset">Reset</button>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const name = ref('')

const upperName = computed(() => name.value.toUpperCase())

function reset() {
  name.value = ''
}
</script>

<style scoped>
input {
  margin-bottom: 10px;
}
</style>
