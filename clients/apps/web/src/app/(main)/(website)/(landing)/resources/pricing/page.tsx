import { PricingPage } from '@/components/Landing/resources/PricingPage'
import { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Pricing',
  description: 'Transparent pricing for every stage of growth',
  keywords:
    'pricing, price, usage billing, tarifia, pricing, pricing for tarifia, pricing for tarifia, pricing for tarifia',
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
  return <PricingPage />
}
