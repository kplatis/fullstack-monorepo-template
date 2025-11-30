import { QueryKey } from '@/types'
import { queryOptions, useQuery } from '@tanstack/react-query'
import getTexts from '../api/getTexts'

interface PaginationParams {
  page?: number
  pageSize?: number
}

export const textsQueryOptions = ({
  page = 1,
  pageSize = 5,
}: PaginationParams = {}) =>
  queryOptions({
    queryKey: [QueryKey.TEXTS, { page, pageSize }],
    queryFn: () => getTexts(page, pageSize),
    staleTime: 5 * 60 * 1000, // cache for 5 minutes
    refetchOnWindowFocus: false,
  })

export default function useTexts(params: PaginationParams = {}) {
  const { isLoading, error, data: texts } = useQuery(textsQueryOptions(params))

  return { isLoading, error, texts }
}
