import { WhyTarifiaPage } from '@/components/Landing/resources/WhyTarifiaPage'
import { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Why Tarifia is the best way to monetize your software',
  description: 'Learn why Tarifia is the best way to monetize your software',
  keywords:
    'monetize, monetization, switch, migration, payment infrastructure, saas, monetization, developer tools',
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
  return <WhyTarifiaPage />
}
