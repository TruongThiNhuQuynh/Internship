<template>
  <form @submit.prevent="submitTask">
    <input v-model="newTask" placeholder="Add a new task..." />
    <button type="submit">Add</button>
  </form>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const emit = defineEmits<{
  (e: 'add', task: string): void
}>()

const newTask = ref('')

function submitTask() {
  if (newTask.value.trim()) {
    emit('add', newTask.value.trim())
    newTask.value = ''
  }
}
</script>

<style scoped>
input {
  padding: 6px;
  width: 70%;
}
button {
  padding: 6px 12px;
  margin-left: 10px;
}
</style>
