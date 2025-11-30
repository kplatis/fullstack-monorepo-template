import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { useNavigate } from '@tanstack/react-router'

type TextCardProps = {
  id: string
  content: string
  language: string
}

export const TextCard = ({ id, content, language }: TextCardProps) => {
  const navigate = useNavigate({ from: '/texts/$textId' })
  return (
    <Card
      key={id}
      data-testid={'text-card'}
      onClick={() => navigate({ to: `/texts/$textId`, params: { textId: id } })}
      className="hover:shadow-md transition-shadow cursor-pointer"
    >
      <CardHeader>
        <div className="flex items-start justify-between">
          <div className="flex-1">
            <CardTitle className="text-xl mb-2">{content}</CardTitle>
          </div>
        </div>
      </CardHeader>
      <CardContent>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          <div className="text-sm">
            <p className="text-muted-foreground text-xs mb-1">Language</p>
            <p className="font-medium">{language}</p>
          </div>
        </div>
      </CardContent>
    </Card>
  )
}
