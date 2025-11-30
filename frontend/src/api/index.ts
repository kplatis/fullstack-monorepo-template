import axios from 'axios'
import { TextsApi } from './backend'

const axiosInstance = axios.create({})

export const textsApi = new TextsApi(
  undefined,
  import.meta.env.VITE_API_BASE_URL,
  axiosInstance,
)
