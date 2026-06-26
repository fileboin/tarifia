import { UsageBillingPage } from '@/components/Landing/features/UsageBillingPage'
import { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Usage Billing — Tarifia',
  description:
    'Bill what your customers actually use. Ingest events, aggregate them into meters, and charge with precision — built for tokens, API calls, and compute.',
  keywords:
    'usage billing, metered billing, consumption billing, pay-as-you-go, event ingestion, saas billing',
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
  return <UsageBillingPage />
}
