// composables/useLogin.ts
import FormData from 'form-data'
import axios from 'axios'

export const useLogin = async () => {
  const form = new FormData()
  form.append('email', 'a@a.com')
  form.append('password', '123')

  const res = await axios.post('https://reqres.in/api/login', form, {
    headers: form.getHeaders()
  })

  return res.data
}
