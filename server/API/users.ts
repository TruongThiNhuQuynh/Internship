// server/api/users.ts

export default defineEventHandler(() => {
  return [
    { id: 1, name: 'John Doe', email: 'john@example.com' },
    { id: 2, name: 'Jane Smith', email: 'jane@example.com' },
    { id: 3, name: 'Alice Tran', email: 'alice@example.com' }
  ]
})
