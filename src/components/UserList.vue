<template>
  <div>
    <h2>Team Members</h2>
    <div class="list">
      <UserCard
        v-for="user in users"
        :key="user.name"
        :name="user.name"
        :description="user.description"
        :avatar="user.avatar"
      />
    </div>
  </div>
</template>

<script setup>
import UserCard from './UserCard.vue'

const users = [
  {
    name: 'Alice',
    description: 'Frontend Developer',
    avatar: 'https://i.pravatar.cc/100?img=1'
  },
  {
    name: 'Bob',
    description: 'Backend Developer',
    avatar: 'https://i.pravatar.cc/100?img=2'
  }
]
</script>

<style scoped>
.list {
  display: flex;
  gap: 20px;
}
</style>
