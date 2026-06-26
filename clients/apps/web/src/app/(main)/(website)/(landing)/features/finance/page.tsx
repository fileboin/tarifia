import { FinancePage } from '@/components/Landing/features/FinancePage'
import { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Finance — Tarifia',
  description:
    'Live balance, transactions ledger, transparent fees, and manual payouts. All visible.',
  keywords:
    'finance, payouts, transactions, ledger, balance, fees, stripe connect, multi-currency',
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
  return <FinancePage />
}
