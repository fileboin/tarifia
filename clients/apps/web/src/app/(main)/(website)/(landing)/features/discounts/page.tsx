import { DiscountsPage } from '@/components/Landing/features/DiscountsPage'
import { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Discounts — Tarifia',
  description:
    'Coupons, promo codes, and recurring discounts. Apply automatically at checkout, prefill via URL, or via the API.',
  keywords:
    'discounts, coupons, promo codes, percentage discount, fixed amount discount, recurring discount',
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
  return <DiscountsPage />
}
