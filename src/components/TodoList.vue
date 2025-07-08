<template>
  <div>
    <TodoInput @add="addTask" />
    <ul>
      <TodoItem
        v-for="(task, index) in tasks"
        :key="index"
        :task="task"
        @remove="removeTask(index)"
      />
    </ul>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import TodoInput from './TodoInput.vue'
import TodoItem from './TodoItem.vue'

const tasks = ref<string[]>([])

function addTask(task: string) {
  tasks.value.push(task)
}

function removeTask(index: number) {
  tasks.value.splice(index, 1)
}
</script>

<style scoped>
ul {
  padding: 0;
}
</style>
