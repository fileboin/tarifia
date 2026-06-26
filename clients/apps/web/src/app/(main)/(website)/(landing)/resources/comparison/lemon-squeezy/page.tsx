import { TarifiaVsLemonSqueezyPage } from '@/components/Landing/comparison/TarifiaLemonSqueezyPage'
import { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Tarifia vs Lemon Squeezy',
  description: 'Comparing Tarifia and Lemon Squeezy',
  keywords:
    'tarifia vs lemon squeezy, lemon squeezy, tarifia, comparison, pricing, pricing for tarifia, pricing for tarifia, pricing for tarifia',
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
  return <TarifiaVsLemonSqueezyPage />
}
