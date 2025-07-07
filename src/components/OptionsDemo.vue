<template>
  <div>
    <h2>Options API Demo</h2>
    <p>Xin chào, {{ name }}!</p>
    <input v-model="name" placeholder="Nhập tên của bạn" />

    <p>Giá trị bình phương của {{ number }} là: {{ squared }}</p>
    <input v-model.number="number" type="number" />

    <button @click="increase">Tăng số</button>
    <button @click="reset">Đặt lại</button>
    <p>Số lần bạn đã tăng: {{ count }}</p>
  </div>
</template>

<script>
export default {
  name: 'OptionsDemo',

  // 1. State (data)
  data() {
    return {
      name: 'Vue học viên',
      number: 2,
      count: 0
    };
  },

  // 2. Computed property
  computed: {
    squared() {
      return this.number * this.number;
    }
  },

  // 3. Methods
  methods: {
    increase() {
      this.count++;
    },
    reset() {
      this.count = 0;
    }
  },

  // 4. Watcher
  watch: {
    number(newVal, oldVal) {
      alert(`Giá trị number thay đổi từ ${oldVal} sang ${newVal}`);
    }
  },

  // 5. Lifecycle hooks
  created() {
    console.log('Component vừa được khởi tạo!');
  },
  mounted() {
    console.log('Component đã gắn vào DOM!');
  },
  updated() {
    console.log('Component vừa cập nhật lại!');
  },
  unmounted() {
    console.log('Component đã bị xóa khỏi DOM!');
  }
};
</script>
