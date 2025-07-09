<script setup>
const router = useRouter()

function goToAbout() {
  router.push('/about')
}
</script>

<template>
  <button @click="goToAbout">
    Chuyển đến trang About
  </button>
</template>
