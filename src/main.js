
import { createApp } from 'vue'
import App from './App.vue'
import MyButton from './components/MyButton.vue'

// Tạo instance app Vue
const app = createApp(App)

// Đăng ký component toàn cục
app.component('MyButton', MyButton)

// Mount app vào #app
app.mount('#app')