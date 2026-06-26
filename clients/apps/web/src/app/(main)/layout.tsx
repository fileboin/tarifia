import { CookieConsent } from '@/components/Privacy/CookieConsent'
import { CONFIG } from '@/utils/config'
import { headers } from 'next/headers'
import { Metadata } from 'next/types'
import { TarifiaThemeProvider } from '../providers'

export async function generateMetadata(): Promise<Metadata> {
  const baseMetadata: Metadata = {
    title: {
      template: '%s | Tarifia',
      default: 'Tarifia',
    },
    description: 'A billing platform for the intelligence era',
    openGraph: {
      images: 'https://tarifia.sh/assets/brand/tarifia_og.jpg',
      type: 'website',
      siteName: 'Tarifia',
      title: 'Tarifia | A billing platform for the intelligence era',
      description:
        'Create digital products and SaaS billing with flexible pricing models and seamless payment processing.',
      locale: 'en_US',
    },
    twitter: {
      images: 'https://tarifia.sh/assets/brand/tarifia_og.jpg',
      card: 'summary_large_image',
      title: 'Tarifia | A billing platform for the intelligence era',
      description:
        'Create digital products and SaaS billing with flexible pricing models and seamless payment processing.',
    },
    metadataBase: new URL('https://tarifia.sh/'),
    alternates: {
      canonical: 'https://tarifia.sh/',
    },
  }

  if (CONFIG.IS_SANDBOX) {
    return {
      ...baseMetadata,
      robots: {
        index: false,
        follow: false,
        googleBot: {
          index: false,
          follow: false,
        },
      },
    }
  }

  return {
    ...baseMetadata,
    robots: {
      index: true,
      follow: true,
      googleBot: {
        index: true,
        follow: true,
        'max-video-preview': -1,
        'max-image-preview': 'large',
        'max-snippet': -1,
      },
    },
  }
}

export default async function MainLayout({
  children,
}: {
  children: React.ReactNode
}) {
  const headersList = await headers()
  const countryCode = headersList.get('x-vercel-ip-country')

  return (
    <TarifiaThemeProvider>
      <link
        rel="preload"
        href="/fonts/Inter-Light.woff2"
        as="font"
        type="font/woff2"
        crossOrigin=""
      />
      <link
        rel="preload"
        href="/fonts/Inter-Regular.woff2"
        as="font"
        type="font/woff2"
        crossOrigin=""
      />
      <link
        rel="preload"
        href="/fonts/Inter-Medium.woff2"
        as="font"
        type="font/woff2"
        crossOrigin=""
      />
      <link
        rel="preload"
        href="/fonts/Inter-SemiBold.woff2"
        as="font"
        type="font/woff2"
        crossOrigin=""
      />
      <link
        rel="preload"
        href="/fonts/InterDisplay-Light.woff2"
        as="font"
        type="font/woff2"
        crossOrigin=""
      />
      <link
        rel="preload"
        href="/fonts/InterDisplay-Regular.woff2"
        as="font"
        type="font/woff2"
        crossOrigin=""
      />
      <link
        rel="preload"
        href="/fonts/InterDisplay-Medium.woff2"
        as="font"
        type="font/woff2"
        crossOrigin=""
      />
      <link
        rel="preload"
        href="/fonts/InterDisplay-SemiBold.woff2"
        as="font"
        type="font/woff2"
        crossOrigin=""
      />
      <link
        rel="preload"
        href="/fonts/Louize-Italic-205TF.otf"
        as="font"
        type="font/otf"
        crossOrigin=""
      />
      <link
        rel="preload"
        href="/fonts/GeistMono-Variable.woff2"
        as="font"
        type="font/woff2"
        crossOrigin=""
      />
      <div className="dark:bg-tarifia-950 h-full bg-white dark:text-white">
        {children}
        <CookieConsent countryCode={countryCode} />
      </div>
    </TarifiaThemeProvider>
  )
}
