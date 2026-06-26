import { useTarifiaClient } from '@/providers/TarifiaClientProvider'
import { operations, unwrap } from '@tarifia-sh/client'
import { useQuery } from '@tanstack/react-query'

export const useCustomFields = (
  organizationId: string | undefined,
  parameters?: Omit<
    NonNullable<operations['custom-fields:list']['parameters']['query']>,
    'organization_id'
  >,
) => {
  const { tarifia } = useTarifiaClient()

  return useQuery({
    queryKey: ['custom_fields', { organizationId, ...(parameters || {}) }],
    queryFn: () =>
      unwrap(
        tarifia.GET('/v1/custom-fields/', {
          params: {
            query: {
              organization_id: organizationId,
              ...(parameters || {}),
            },
          },
        }),
      ),
    enabled: !!organizationId,
  })
}
