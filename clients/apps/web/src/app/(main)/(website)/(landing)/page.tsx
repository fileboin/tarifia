import { Metadata } from 'next'
import LandingPage from '../../../../components/Landing/LandingPage'
export const metadata: Metadata = {
  title: 'Tarifia — A billing platform for the intelligence era',
  description: 'A billing platform for the intelligence era',
  keywords:
    'monetization, merchant of record, saas, digital products, platform, developer, open source, funding, open source, economy',
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
  return <LandingPage />
}
