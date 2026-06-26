import { MerchantOfRecordPage } from '@/components/Landing/features/MerchantOfRecordPage'
import { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Merchant of Record — Tarifia',
  description:
    'Tarifia is your reseller. We handle international sales taxes globally so you can focus on the product.',
  keywords:
    'merchant of record, MoR, sales tax, VAT, GST, international taxes, reseller, EU OSS, tax compliance',
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
  return <MerchantOfRecordPage />
}
