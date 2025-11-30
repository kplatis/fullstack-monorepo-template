import { textsApi } from '@/api'
import type { PaginatedResponseTextOut } from '@/api/backend'

export default async function getTexts(
  page: number = 1,
  pageSize: number = 10,
): Promise<PaginatedResponseTextOut> {
  try {
    const response = await textsApi.getTexts(page, pageSize)
    return response.data
  } catch (error) {
    console.error(error)
    throw new Error('Failed to fetch text data')
  }
}
