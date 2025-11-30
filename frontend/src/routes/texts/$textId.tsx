import useText, { textQueryOptions } from '@/features/texts/hooks/useText'
import type { QueryClient } from '@tanstack/react-query'
import { createFileRoute } from '@tanstack/react-router'
import { Loader } from 'lucide-react'

export const Route = createFileRoute('/texts/$textId')({
  loader: async (ctx) => {
    const { queryClient } = ctx.context as { queryClient: QueryClient }
    const { textId } = ctx.params as { textId: string }
    await queryClient.ensureQueryData(textQueryOptions(textId))
  },
  component: TextPage,
})

function TextPage() {
  const textId = Route.useParams().textId

  const { isLoading, error, text } = useText(textId)

  if (isLoading) return <Loader />
  if (error) return <div>Error loading text.</div>
  if (!text) return <div>No text found.</div>
  return <div>{text.content}</div>
}
