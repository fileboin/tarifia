import { useTarifiaClient } from '@/providers/TarifiaClientProvider'
import { queryClient } from '@/utils/query'
import { operations, schemas, unwrap } from '@tarifia-sh/client'
import { useInfiniteQuery, useMutation, useQuery } from '@tanstack/react-query'

export const useCheckoutLink = (
  organizationId: string | undefined,
  id: string | undefined,
) => {
  const { tarifia } = useTarifiaClient()

  return useQuery({
    queryKey: ['checkout_link', organizationId, { id }],
    queryFn: () =>
      unwrap(
        tarifia.GET('/v1/checkout-links/{id}', {
          params: { path: { id: id ?? '' } },
        }),
      ),
    enabled: !!organizationId && !!id,
  })
}

export const useInfiniteCheckoutLinks = (
  organizationId: string | undefined,
  params?: Omit<
    operations['checkout-links:list']['parameters']['query'],
    'organization_id'
  >,
) => {
  const { tarifia } = useTarifiaClient()

  return useInfiniteQuery({
    queryKey: ['infinite', 'checkout_links', organizationId, { ...params }],
    queryFn: ({ pageParam = 1 }) =>
      unwrap(
        tarifia.GET('/v1/checkout-links/', {
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

export const useCheckoutLinkCreate = (organizationId: string | undefined) => {
  const { tarifia } = useTarifiaClient()

  return useMutation({
    mutationFn: (data: schemas['CheckoutLinkCreateProducts']) =>
      unwrap(
        tarifia.POST('/v1/checkout-links/', {
          body: data,
        }),
      ),
    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: ['checkout_links', organizationId],
      })

      queryClient.invalidateQueries({
        queryKey: ['infinite', 'checkout_links', organizationId],
      })
    },
  })
}

export const useCheckoutLinkUpdate = (
  organizationId: string | undefined,
  id: string,
) => {
  const { tarifia } = useTarifiaClient()

  return useMutation({
    mutationFn: (data: schemas['CheckoutLinkUpdate']) =>
      unwrap(
        tarifia.PATCH('/v1/checkout-links/{id}', {
          params: { path: { id } },
          body: data,
        }),
      ),
    onSuccess: (data) => {
      queryClient.setQueryData(['checkout_link', organizationId, { id }], data)

      queryClient.invalidateQueries({
        queryKey: ['checkout_links', organizationId],
      })

      queryClient.invalidateQueries({
        queryKey: ['infinite', 'checkout_links', organizationId],
      })
    },
  })
}
