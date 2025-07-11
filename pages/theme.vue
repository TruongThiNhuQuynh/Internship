<script setup>
const appConfig = useAppConfig()

// Đọc mode: light/dark
const mode = ref(appConfig.theme.mode)

// Chuyển mode
function toggleTheme() {
  mode.value = mode.value === 'light' ? 'dark' : 'light'
}
</script>

<template>
  <div>
    <!-- Khối nền theo màu chính -->
    <div
      :style="{
        backgroundColor: appConfig.theme.primaryColor,
        color: '#fff',
        padding: '20px'
      }"
    >
      <h2>Nền theo màu chính: {{ appConfig.theme.primaryColor }}</h2>
    </div>

    <!-- Khối nền chuyển đổi theme -->
    <div
      :style="{
        backgroundColor: mode === 'light' ? appConfig.theme.backgroundLight : appConfig.theme.backgroundDark,
        color: mode === 'light' ? appConfig.theme.textLight : appConfig.theme.textDark,
        minHeight: 'calc(100vh - 80px)',
        padding: '20px'
      }"
    >
      <h1>Theme hiện tại: {{ mode }}</h1>
      <p>Màu chính: <strong>{{ appConfig.theme.primaryColor }}</strong></p>
      <button @click="toggleTheme">
        Chuyển sang {{ mode === 'light' ? 'Dark' : 'Light' }} Mode
      </button>
    </div>
  </div>
</template>
