<template>
  <button class="btn"><slot /></button>
</template>

<script>
export default {
  name: 'MyButton'
}
</script>

<style scoped>
.btn {
  padding: 8px 16px;
  background: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
}
</style>