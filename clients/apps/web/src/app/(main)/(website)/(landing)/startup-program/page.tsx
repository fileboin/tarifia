import { StartupProgramPage } from '@/components/Landing/startup-program/StartupProgramPage'
import { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Tarifia Startup Program',
  description:
    'Scale-tier pricing for a full year, free. For AI and SaaS startups building on Tarifia.',
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
  return <StartupProgramPage />
}
