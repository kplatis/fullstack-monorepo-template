import { describe, it, expect } from 'vitest'
import { render, screen } from '@testing-library/react'
import { TextCard } from './TextCard'

const defaultProps = {
  id: 'test-id',
  content: 'Sample trip request content',
  language: 'English',
}

describe('TextCard', () => {
  it('renders the card with correct content and language', () => {
    render(<TextCard {...defaultProps} />)

    // Card test id
    expect(screen.getByTestId('text-card')).toBeInTheDocument()
    // Content in CardTitle
    expect(screen.getByText(defaultProps.content)).toBeInTheDocument()
    // Language label and value
    expect(screen.getByText(/Language/i)).toBeInTheDocument()
    expect(screen.getByText(defaultProps.language)).toBeInTheDocument()
  })

  it('uses the correct key prop', () => {
    // This test is mostly for coverage, as key is not visible in DOM
    // But we can render multiple cards and check they all exist
    const cards = [
      { ...defaultProps, id: 'id1', content: 'Content 1' },
      { ...defaultProps, id: 'id2', content: 'Content 2' },
    ]
    render(
      <>
        {cards.map((card) => (
          <TextCard key={card.id} {...card} />
        ))}
      </>,
    )
    expect(screen.getByText('Content 1')).toBeInTheDocument()
    expect(screen.getByText('Content 2')).toBeInTheDocument()
  })

  it('applies the correct class names', () => {
    render(<TextCard {...defaultProps} />)
    const card = screen.getByTestId('text-card')
    expect(card.className).toContain('hover:shadow-md')
    expect(card.className).toContain('transition-shadow')
    expect(card.className).toContain('cursor-pointer')
  })
})
