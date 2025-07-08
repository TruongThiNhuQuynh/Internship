<script setup>
import { useCounter } from '../composables/useCounter'

const { count, increment, reset } = useCounter()
</script>

<template>
  <p>Count: {{ count }}</p>
  <button @click="increment">+</button>
  <button @click="reset">Reset</button>
</template>
