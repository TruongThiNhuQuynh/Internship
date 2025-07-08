<script setup>
import { reactive } from 'vue'

const form = reactive({
  name: '',
  email: ''
})

function submitForm() {
  alert(`Name: ${form.name}, Email: ${form.email}`)
}
</script>

<template>
  <div>
    <input v-model="form.name" placeholder="Name" />
    <input v-model="form.email" placeholder="Email" />
    <button @click="submitForm">Submit</button>
  </div>
</template>
