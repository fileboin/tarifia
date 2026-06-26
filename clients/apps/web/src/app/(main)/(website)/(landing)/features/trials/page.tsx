import { TrialsPage } from '@/components/Landing/features/TrialsPage'
import { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Trials — Tarifia',
  description:
    'Free or paid trials with automatic conversion, conversion reminders, and abuse protection — built into your subscriptions.',
  keywords:
    'free trial, trial period, trial conversion, trial abuse prevention, saas trial',
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
  return <TrialsPage />
}
