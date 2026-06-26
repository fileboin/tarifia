import { Footer, Intro, Text, WrapperTarifia } from '../components/foundation'
import type { schemas } from '../types'

export function TarifiaSelfSubscriptionCycled({
  email,
  product_name,
}: schemas['TarifiaSelfSubscriptionCycledProps']) {
  return (
    <WrapperTarifia preview={`Your ${product_name} subscription renewed`}>
      <Intro headline={`${product_name} renewed`}>
        Your{' '}
        <Text as="span" weight="medium">
          {product_name}
        </Text>{' '}
        subscription renewed for another cycle. The latest invoice is attached.
      </Intro>
      <Footer email={email} />
    </WrapperTarifia>
  )
}

TarifiaSelfSubscriptionCycled.PreviewProps = {
  email: 'john@example.com',
  product_name: 'Tarifia Pro',
} satisfies schemas['TarifiaSelfSubscriptionCycledProps']

export default TarifiaSelfSubscriptionCycled
