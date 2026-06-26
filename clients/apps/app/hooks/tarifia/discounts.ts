import { useTarifiaClient } from '@/providers/TarifiaClientProvider'
import { operations, unwrap } from '@tarifia-sh/client'
import { useInfiniteQuery } from '@tanstack/react-query'

export const useInfiniteDiscounts = (
  organizationId: string | undefined,
  params?: Omit<
    operations['discounts:list']['parameters']['query'],
    'organization_id'
  >,
) => {
  const { tarifia } = useTarifiaClient()

  return useInfiniteQuery({
    queryKey: ['infinite', 'discounts', organizationId, { ...params }],
    queryFn: ({ pageParam = 1 }) =>
      unwrap(
        tarifia.GET('/v1/discounts/', {
          params: {
            query: {
              organization_id: organizationId,
              ...params,
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
