<template>
  <div class="container">
    <h1>Hello Vue 3!</h1>
    <MyButton>Click me!</MyButton>

    <section class="demo">
      <OptionsDemo />
    </section>
  </div>
</template>

<script setup>
import MyButton from './components/MyButton.vue'
import OptionsDemo from './components/OptionsDemo.vue'
</script>

<style scoped>
.container {
  padding: 1rem;
  max-width: 800px;
  margin: auto;
}

.demo {
  margin-top: 2rem;
  border-top: 1px solid #ccc;
  padding-top: 1rem;
}
</style>
