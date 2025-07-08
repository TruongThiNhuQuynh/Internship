<template>
  <li :class="{ done: done }">
    <input type="checkbox" v-model="done" />
    {{ task }}
    <button @click="emit('remove')">❌</button>
  </li>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'

const props = defineProps<{
  task: string
}>()

const emit = defineEmits(['remove'])

const done = ref(false)

watch(done, (val) => {
  console.log(`Task "${props.task}" is ${val ? 'done' : 'not done'}.`)
})
</script>

<style scoped>
li {
  margin-bottom: 6px;
  list-style: none;
}
.done {
  text-decoration: line-through;
  color: gray;
}
</style>
