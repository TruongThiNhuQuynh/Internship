// server/api/login.ts
import { defineEventHandler } from 'h3'
import FormData from 'form-data'
import axios from 'axios'

export default defineEventHandler(async () => {
  const form = new FormData()
  form.append('email', 'eve.holt@reqres.in')
  form.append('password', 'cityslicka')

  const res = await axios.post('https://reqres.in/api/login', form, {
    headers: form.getHeaders()
  })

  return res.data
})
