import {
  Button,
  Footer,
  Intro,
  Text,
  WrapperTarifia,
} from '../components/foundation'
import type { schemas } from '../types'

export function OrganizationInvite({
  email,
  organization_name,
  inviter_email,
  invite_url,
}: schemas['OrganizationInviteProps']) {
  return (
    <WrapperTarifia
      preview={`You've been added to ${organization_name} on Tarifia`}
    >
      <Intro>
        {inviter_email} has added you to{' '}
        <Text as="span" weight="bold">
          {organization_name}
        </Text>{' '}
        on Tarifia.
      </Intro>
      <Text>
        As a member of {organization_name} you're now able to manage{' '}
        {organization_name}'s products, customers, and subscriptions on Tarifia.
      </Text>
      <Button href={invite_url}>Go to the Tarifia dashboard</Button>
      <Footer email={email} />
    </WrapperTarifia>
  )
}

OrganizationInvite.PreviewProps = {
  email: 'john@example.com',
  organization_name: 'Acme Inc.',
  inviter_email: 'admin@acme.com',
  invite_url: 'https://tarifia.sh/dashboard/acme-inc',
}

export default OrganizationInvite
