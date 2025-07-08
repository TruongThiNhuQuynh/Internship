<template>
  <div>
    <h2>Built-in Components & Directives</h2>

    <!-- v-model, v-if, v-show -->
    <input v-model="username" placeholder="Enter your name" />
    <button @click="toggleShow">Toggle Welcome</button>

    <p v-if="username">👋 Hello, {{ username }}!</p>
    <p v-show="showMessage">This is a welcome message using v-show.</p>

    <!-- v-for + key -->
    <ul>
      <li v-for="(item, index) in items" :key="index">
        {{ item }}
      </li>
    </ul>

    <!-- Transition -->
    <button @click="toggleBox">Toggle Box</button>
    <transition name="fade">
      <div v-if="showBox" class="box">I'm a box with transition</div>
    </transition>

    <!-- Teleport -->
    <teleport to="body">
      <div class="teleport-box">This content is teleported to body!</div>
    </teleport>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const username = ref('')
const showMessage = ref(true)
const items = ref(['Vue.js', 'React', 'Angular'])
const showBox = ref(false)

const toggleBox = () => (showBox.value = !showBox.value)
const toggleShow = () => (showMessage.value = !showMessage.value)
</script>

<style scoped>
.box {
  width: 200px;
  height: 100px;
  background: lightgreen;
  margin-top: 10px;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
.teleport-box {
  position: fixed;
  bottom: 10px;
  right: 10px;
  background: #ffe9a7;
  padding: 10px;
  border: 1px solid #aaa;
}
</style>
