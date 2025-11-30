import { QueryKey } from '@/types'
import { queryOptions, useQuery } from '@tanstack/react-query'
import getTextById from '../api/getText'

export const textQueryOptions = (textId: string) =>
  queryOptions({
    queryKey: [QueryKey.TEXT, { textId }],
    queryFn: () => getTextById(textId),
    staleTime: 5 * 60 * 1000, // cache for 5 minutes
    refetchOnWindowFocus: false,
  })

export default function useText(textId: string) {
  const { isLoading, error, data: text } = useQuery(textQueryOptions(textId))

  return { isLoading, error, text }
}
