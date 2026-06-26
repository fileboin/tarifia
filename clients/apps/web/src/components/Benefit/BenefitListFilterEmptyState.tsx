import { Box } from '@tarifia-sh/orbit/Box'
import { Button, Text } from '@tarifia-sh/orbit'

export const BenefitListFilterEmptyState = ({
  onClearFilters,
}: {
  onClearFilters: () => void
}) => {
  return (
    <Box
      flexDirection="column"
      alignItems="center"
      justifyContent="center"
      gap="m"
      paddingVertical="2xl"
      paddingHorizontal="xl"
      textAlign="center"
    >
      <Box flexDirection="column" gap="xs">
        <Text variant="default">No benefits found</Text>
        <Text variant="caption" color="muted">
          No benefits match your search or filter.
        </Text>
      </Box>
      <Button variant="secondary" size="sm" onClick={onClearFilters}>
        Clear filters
      </Button>
    </Box>
  )
}
