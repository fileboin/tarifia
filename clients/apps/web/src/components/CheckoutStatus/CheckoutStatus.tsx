import {
  CheckoutStatusDisplayColor,
  CheckoutStatusDisplayTitle,
} from '@/utils/checkout'
import { schemas } from '@tarifia-sh/client'
import { Status } from '@tarifia-sh/orbit'

const CheckoutStatus = ({
  checkout: { status },
}: {
  checkout: schemas['Checkout']
}) => {
  return (
    <Status
      color={CheckoutStatusDisplayColor[status]}
      status={CheckoutStatusDisplayTitle[status]}
    />
  )
}

export default CheckoutStatus
