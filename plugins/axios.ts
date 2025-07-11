import axios from 'axios'
import FormData from 'form-data'

export default defineNuxtPlugin(() => {
  const instance = axios.create({
    baseURL: 'https://reqres.in/api',
  })

  return {
    provide: {
      axios: instance
    }
  }
})
