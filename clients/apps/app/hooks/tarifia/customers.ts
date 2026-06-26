import { useTarifiaClient } from '@/providers/TarifiaClientProvider'
import { operations, unwrap } from '@tarifia-sh/client'
import { useInfiniteQuery, useQuery } from '@tanstack/react-query'

export const useCustomer = (organizationId: string | undefined, id: string) => {
  const { tarifia } = useTarifiaClient()

  return useQuery({
    queryKey: ['customers', organizationId, { id }],
    queryFn: () =>
      unwrap(
        tarifia.GET('/v1/customers/{id}', {
          params: {
            path: { id },
          },
        }),
      ),
    enabled: !!organizationId,
  })
}

export const useCustomers = (
  organizationId: string | undefined,
  parameters?: Omit<
    operations['customers:list']['parameters']['query'],
    'organization_id'
  >,
) => {
  const { tarifia } = useTarifiaClient()

  return useInfiniteQuery({
    queryKey: ['customers', { organizationId, ...(parameters || {}) }],
    queryFn: ({ pageParam = 1 }) =>
      unwrap(
        tarifia.GET('/v1/customers/', {
          params: {
            query: {
              organization_id: organizationId,
              ...(parameters || {}),
              page: pageParam,
            },
          },
        }),
      ),
    enabled: !!organizationId,
    initialPageParam: 1,
    getNextPageParam: (lastPage, pages) => {
      if (lastPage.items.length === 0) return undefined
      return pages.length + 1
    },
  })
}
