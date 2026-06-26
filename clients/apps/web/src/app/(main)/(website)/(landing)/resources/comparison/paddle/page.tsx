import { TarifiaVsPaddlePage } from '@/components/Landing/comparison/TarifiaPaddlePage'
import { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Tarifia vs Paddle',
  description: 'Comparing Tarifia and Paddle',
  keywords:
    'tarifia vs paddle, paddle, tarifia, comparison, pricing, pricing for tarifia, pricing for tarifia, pricing for tarifia',
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
  return <TarifiaVsPaddlePage />
}
