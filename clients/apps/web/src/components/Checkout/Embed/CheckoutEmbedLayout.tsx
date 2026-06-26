import type { schemas } from '@tarifia-sh/client'
import CheckoutEmbedClose from './CheckoutEmbedClose'
import CheckoutEmbedLoaded from './CheckoutEmbedLoaded'

const CheckoutEmbedLayout = ({
  children,
  checkout,
  theme,
}: React.PropsWithChildren<{
  checkout: schemas['CheckoutPublic']
  theme?: 'light' | 'dark'
}>) => {
  return (
    <div
      className={theme === 'dark' ? 'dark' : 'light'}
      id="tarifia-embed-layout"
    >
      <div className="flex h-full w-full items-center justify-center p-0 md:p-12 dark:text-white">
        <div className="h-full w-full max-w-2xl" id="tarifia-embed-content">
          {children}
        </div>
      </div>
      <CheckoutEmbedClose checkout={checkout} />
      <CheckoutEmbedLoaded checkout={checkout} />
    </div>
  )
}

export default CheckoutEmbedLayout
