import { TarifiaThemeProvider } from '@/app/providers'
import type { schemas } from '@tarifia-sh/client'
import CheckoutEmbedLayout from './Embed/CheckoutEmbedLayout'

const CheckoutLayout = ({
  children,
  checkout,
  embed,
  theme,
}: React.PropsWithChildren<{
  checkout: schemas['CheckoutPublic']
  embed: boolean
  theme?: 'light' | 'dark'
}>) => {
  if (embed) {
    return (
      <CheckoutEmbedLayout checkout={checkout} theme={theme}>
        {children}
      </CheckoutEmbedLayout>
    )
  }

  return (
    <TarifiaThemeProvider>
      <div className="md:dark:bg-tarifia-950 dark:bg-tarifia-900 h-full min-h-screen bg-white md:bg-gray-50 dark:text-white">
        {children}
      </div>
    </TarifiaThemeProvider>
  )
}

export default CheckoutLayout
