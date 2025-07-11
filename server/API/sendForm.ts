// server/api/sendForm.ts
import { defineEventHandler } from 'h3'
import FormData from 'form-data'
import axios from 'axios'

export default defineEventHandler(async () => {
  const form = new FormData()
  form.append('email', 'a@a.com')
  form.append('password', '123')

  const res = await axios.post('https://reqres.in/api/login', form, {
    headers: form.getHeaders()
  })

  return res.data
})
