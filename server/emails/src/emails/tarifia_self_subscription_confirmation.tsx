import { Footer, Intro, Text, WrapperTarifia } from '../components/foundation'
import type { schemas } from '../types'

export function TarifiaSelfSubscriptionConfirmation({
  email,
  product_name,
}: schemas['TarifiaSelfSubscriptionConfirmationProps']) {
  return (
    <WrapperTarifia preview="We're happy to have you selling on Tarifia!">
      <Intro headline="Thanks for choosing Tarifia!">
        You're now subscribed to{' '}
        <Text as="span" weight="medium">
          {product_name}
        </Text>
        . Your invoice is attached for your records.
      </Intro>
      <Footer email={email} />
    </WrapperTarifia>
  )
}

TarifiaSelfSubscriptionConfirmation.PreviewProps = {
  email: 'john@example.com',
  product_name: 'Tarifia Pro',
} satisfies schemas['TarifiaSelfSubscriptionConfirmationProps']

export default TarifiaSelfSubscriptionConfirmation
