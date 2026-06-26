import { MORPage } from '@/components/Landing/resources/MORPage'
import { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Merchant of Record',
  description: 'A deep dive into Merchant of Records & what they mean for you',
  keywords:
    'mor, merchant of record, lemon squeezy, paddle, taxes, compliance, monetization',
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
  return <MORPage />
}
