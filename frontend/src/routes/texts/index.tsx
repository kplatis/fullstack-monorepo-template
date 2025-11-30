import { useState } from 'react'
import type { QueryClient } from '@tanstack/react-query'
import { createFileRoute } from '@tanstack/react-router'

import { TextCard } from '@/features/texts/components/TextCard/TextCard'
import useTexts, { textsQueryOptions } from '@/features/texts/hooks/useTexts'
import { CustomPagination } from '@/components/CustomPagination'
import { Spinner } from '@/components/ui/spinner'

export const Route = createFileRoute('/texts/')({
  loader: async (ctx) => {
    const { queryClient } = ctx.context as { queryClient: QueryClient }
    await queryClient.ensureQueryData(textsQueryOptions())
  },
  component: TextsPage,
})

function TextsPage() {
  const [page, setPage] = useState(1)
  const [pageSize, setPageSize] = useState(5)

  const { isLoading, error, texts } = useTexts({ page, pageSize })

  return (
    <div className="min-h-screen bg-gradient-to-b from-muted/30 to-background">
      <div className="container mx-auto px-4 py-12 max-w-4xl">
        <div className="flex items-center justify-between mb-8">
          <div>
            <h1 className="text-3xl font-bold tracking-tight mb-2">Texts</h1>
            <p className="text-muted-foreground">View all your past texts</p>
          </div>
        </div>
        {isLoading && <Spinner />}
        {error && <div>Error loading texts</div>}
        {texts && texts.items.length === 0 && <div>No texts found</div>}
        {texts && texts.items.length > 0 && (
          <div className="flex flex-col gap-4">
            <div className="space-y-4">
              {texts?.items.map((request) => (
                <TextCard
                  key={request.id}
                  id={request.id}
                  content={request.content}
                  language={request.language}
                />
              ))}
            </div>
            <CustomPagination
              currentPage={page}
              currentPageSize={pageSize}
              totalPages={texts.pagination.total_pages}
              onChangePage={setPage}
              onChangePageSize={setPageSize}
            />
          </div>
        )}
      </div>
    </div>
  )
}
