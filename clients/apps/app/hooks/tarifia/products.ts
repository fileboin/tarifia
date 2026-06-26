import { useTarifiaClient } from '@/providers/TarifiaClientProvider'
import { operations, unwrap } from '@tarifia-sh/client'
import { useInfiniteQuery, useQuery } from '@tanstack/react-query'

export const useProduct = (
  organizationId: string | undefined,
  id: string | undefined,
) => {
  const { tarifia } = useTarifiaClient()

  return useQuery({
    queryKey: ['product', organizationId, { id }],
    queryFn: () =>
      unwrap(
        tarifia.GET('/v1/products/{id}', { params: { path: { id: id ?? '' } } }),
      ),
    enabled: !!organizationId && !!id,
  })
}

export const useProducts = (
  organizationId: string | undefined,
  options: Omit<
    operations['products:list']['parameters']['query'],
    'organization_id'
  >,
) => {
  const { tarifia } = useTarifiaClient()

  return useQuery({
    queryKey: ['products', organizationId, { ...options }],
    queryFn: () =>
      unwrap(
        tarifia.GET('/v1/products/', {
          params: { query: { organization_id: organizationId, ...options } },
        }),
      ),
  })
}

export const useInfiniteProducts = (
  organizationId: string | undefined,
  options?: Omit<
    operations['products:list']['parameters']['query'],
    'organization_id'
  >,
) => {
  const { tarifia } = useTarifiaClient()

  return useInfiniteQuery({
    queryKey: ['infinite', 'products', organizationId, { ...options }],
    queryFn: ({ pageParam = 1 }) =>
      unwrap(
        tarifia.GET('/v1/products/', {
          params: {
            query: {
              organization_id: organizationId,
              ...options,
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
