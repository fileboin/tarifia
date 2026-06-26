'use client'

import { TarifiaEmbedCheckout } from '@tarifia-sh/checkout/embed'
import type { schemas } from '@tarifia-sh/client'
import { useEffect } from 'react'

interface CheckoutEmbedLoadedProps {
  checkout: schemas['CheckoutPublic']
}

const CheckoutEmbedLoaded: React.FC<
  React.PropsWithChildren<CheckoutEmbedLoadedProps>
> = ({ checkout }) => {
  const embedOrigin = checkout.embed_origin
  useEffect(() => {
    if (!embedOrigin) {
      return
    }
    TarifiaEmbedCheckout.postMessage({ event: 'loaded' }, embedOrigin)
  }, [embedOrigin])

  return null
}

export default CheckoutEmbedLoaded
