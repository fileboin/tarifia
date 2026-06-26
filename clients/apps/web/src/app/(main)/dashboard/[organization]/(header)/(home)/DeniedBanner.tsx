import { schemas } from '@tarifia-sh/client'
import { Text } from '@tarifia-sh/orbit'
import { Box } from '@tarifia-sh/orbit/Box'
import { Button } from '@tarifia-sh/orbit'
import { AlertCircleIcon } from 'lucide-react'
import Link from 'next/link'

interface DeniedBannerProps {
  organization: schemas['Organization']
}

export const DeniedBanner = ({ organization }: DeniedBannerProps) => {
  return (
    <Box
      flexDirection={{ base: 'column', md: 'row' }}
      justifyContent="between"
      gap="l"
      borderRadius="l"
      backgroundColor="background-card"
      padding={{ base: 'l', md: 'xl' }}
    >
      <Box flexDirection="column" rowGap="s">
        <Box alignItems="center" columnGap="s">
          <AlertCircleIcon className="h-4 w-4 shrink-0" />
          <Text as="strong">
            Payments are unavailable for your organization
          </Text>
        </Box>
        <Box maxWidth={720}>
          <Text color="muted">
            Your organization has been denied access to payments.
          </Text>
        </Box>
      </Box>
      <Link href={`/dashboard/${organization.slug}/finance/account`}>
        <Button>Learn More</Button>
      </Link>
    </Box>
  )
}
