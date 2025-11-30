import { textsApi } from '@/api'
import type { TextOut } from '@/api/backend'

export default async function getTextById(textId: string): Promise<TextOut> {
  try {
    const response = await textsApi.getTextById(textId)
    return response.data
  } catch (error) {
    console.error(error)
    throw new Error('Failed to fetch text data')
  }
}
