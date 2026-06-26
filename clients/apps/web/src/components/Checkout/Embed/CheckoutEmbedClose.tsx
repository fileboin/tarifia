'use client'

import { TarifiaEmbedCheckout } from '@tarifia-sh/checkout/embed'
import type { schemas } from '@tarifia-sh/client'
import { X } from 'lucide-react'
import { useCallback, useEffect } from 'react'

interface CheckoutEmbedCloseProps {
  checkout: schemas['CheckoutPublic']
}

const CheckoutEmbedClose: React.FC<
  React.PropsWithChildren<CheckoutEmbedCloseProps>
> = ({ checkout }) => {
  const onClose = useCallback(() => {
    if (!checkout.embed_origin) {
      return
    }
    TarifiaEmbedCheckout.postMessage({ event: 'close' }, checkout.embed_origin)
  }, [checkout])

  useEffect(() => {
    const outsideClickListener = (event: MouseEvent) => {
      const contentElement = document.getElementById('tarifia-embed-content')
      if (contentElement && !contentElement.contains(event.target as Node)) {
        onClose()
      }
    }
    document
      .getElementById('tarifia-embed-layout')
      ?.addEventListener('click', outsideClickListener)

    return () => {
      document
        .getElementById('tarifia-embed-layout')
        ?.removeEventListener('click', outsideClickListener)
    }
  }, [onClose])

  return (
    <button
      type="button"
      className="dark:bg-tarifia-950 fixed top-2 right-2 cursor-pointer rounded-full bg-transparent bg-white p-2 shadow-xl md:top-4 md:right-4 dark:text-white"
      onClick={onClose}
    >
      <X className="h-4 w-4 md:h-6 md:w-6" />
    </button>
  )
}

export default CheckoutEmbedClose
