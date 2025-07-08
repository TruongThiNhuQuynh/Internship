<template>
  <div :class="$style.wrapper">
    <h2 :class="$style.title">CSS Modules Example</h2>
    <button :class="$style.button" @click="toggle">Toggle Status</button>
    <p :class="[isActive ? $style.active : $style.inactive]">
      {{ isActive ? 'Active' : 'Inactive' }}
    </p>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const isActive = ref(false)
const toggle = () => (isActive.value = !isActive.value)
</script>

<style module>
.wrapper {
  padding: 20px;
  border: 2px dashed #ccc;
  text-align: center;
  margin-top: 20px;
}

.title {
  color: #2c3e50;
  font-size: 24px;
}

.button {
  padding: 10px 20px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}

.active {
  color: green;
  font-weight: bold;
}

.inactive {
  color: red;
  font-style: italic;
}
</style>
