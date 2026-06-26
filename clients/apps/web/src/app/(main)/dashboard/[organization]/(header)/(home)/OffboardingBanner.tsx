import { schemas } from '@tarifia-sh/client'
import { Text } from '@tarifia-sh/orbit'
import { Box } from '@tarifia-sh/orbit/Box'
import { Button } from '@tarifia-sh/orbit'
import { AlertTriangleIcon } from 'lucide-react'
import Link from 'next/link'

interface OffboardingBannerProps {
  organization: schemas['Organization']
}

export const OffboardingBanner = ({ organization }: OffboardingBannerProps) => {
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
          <AlertTriangleIcon className="h-4 w-4 shrink-0" />
          <Text as="strong">Your organization is being offboarded</Text>
        </Box>
        <Box maxWidth="45rem">
          <Text color="muted">
            Your organization is in the process of being offboarded from Tarifia.
            Some features may be limited. Reach out if you have any questions.
          </Text>
        </Box>
      </Box>
      <Link href={`/dashboard/${organization.slug}/finance/account`}>
        <Button variant="secondary">Learn More</Button>
      </Link>
    </Box>
  )
}
