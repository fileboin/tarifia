import { CostInsightsPage } from '@/components/Landing/features/CostInsightsPage'
import { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Cost Insights — Tarifia',
  description:
    'Track cost, profit, and customer LTV by annotating events with cost data.',
  keywords:
    'cost insights, profit tracking, LTV, customer lifetime value, cost events, llm cost tracking',
  openGraph: {
    siteName: 'Tarifia',
    type: 'website',
    images: [
      {
        url: 'https://tarifia.sh/assets/brand/tarifia_og.jpg',
        width: 1200,
        height: 630,
      },
    ],
  },
  twitter: {
    card: 'summary_large_image',
    images: [
      {
        url: 'https://tarifia.sh/assets/brand/tarifia_og.jpg',
        width: 1200,
        height: 630,
        alt: 'Tarifia',
      },
    ],
  },
}

export default function Page() {
  return <CostInsightsPage />
}
