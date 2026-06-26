import { useTarifiaClient } from '@/providers/TarifiaClientProvider'
import { queryClient } from '@/utils/query'
import { operations, schemas, unwrap } from '@tarifia-sh/client'
import { useInfiniteQuery, useMutation, useQuery } from '@tanstack/react-query'

export const useSubscription = (id: string) => {
  const { tarifia } = useTarifiaClient()

  return useQuery({
    queryKey: ['subscription', id],
    queryFn: () =>
      unwrap(tarifia.GET('/v1/subscriptions/{id}', { params: { path: { id } } })),
  })
}

export const useSubscriptions = (
  organizationId?: string,
  parameters?: Omit<
    operations['subscriptions:list']['parameters']['query'],
    'organization_id'
  >,
) => {
  const { tarifia } = useTarifiaClient()

  return useInfiniteQuery({
    queryKey: ['subscriptions', { organizationId, ...(parameters || {}) }],
    queryFn: async ({ pageParam = 1 }) =>
      unwrap(
        tarifia.GET('/v1/subscriptions/', {
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

export const useUpdateSubscription = (id: string) => {
  const { tarifia } = useTarifiaClient()

  return useMutation({
    mutationFn: (body: schemas['SubscriptionUpdate']) =>
      tarifia.PATCH('/v1/subscriptions/{id}', {
        params: { path: { id } },
        body,
      }),
    onSuccess: (data, variables) => {
      queryClient.setQueryData(['subscription', id], data.data)

      queryClient.invalidateQueries({
        queryKey: ['subscriptions'],
      })
    },
  })
}
