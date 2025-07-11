// plugins/form.ts
import FormData from 'form-data'

export default defineNuxtPlugin(() => {
  const createForm = (data: Record<string, string>) => {
    const form = new FormData()
    Object.entries(data).forEach(([key, value]) => {
      form.append(key, value)
    })
    return form
  }

  return {
    provide: {
      createForm
    }
  }
})
