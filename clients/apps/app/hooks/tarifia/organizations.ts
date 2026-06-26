import { useTarifiaClient } from '@/providers/TarifiaClientProvider'
import { queryClient } from '@/utils/query'
import { schemas, unwrap } from '@tarifia-sh/client'
import * as Sentry from '@sentry/react-native'
import { useMutation, useQuery } from '@tanstack/react-query'

export const useOrganizations = (
  {
    enabled = true,
  }: {
    enabled?: boolean
  } = { enabled: true },
) => {
  const { tarifia } = useTarifiaClient()

  return useQuery({
    queryKey: ['organizations'],
    queryFn: async () => {
      try {
        return await unwrap(
          tarifia.GET('/v1/organizations/', {
            params: {
              query: {
                limit: 100,
              },
            },
          }),
        )
      } catch (error) {
        Sentry.captureException(error, {
          tags: { context: 'useOrganizations' },
        })
        throw error
      }
    },
    enabled,
  })
}

export const useCreateOrganization = () => {
  const { tarifia } = useTarifiaClient()

  return useMutation({
    mutationFn: (organization: schemas['OrganizationCreate']) =>
      unwrap(
        tarifia.POST('/v1/organizations/', {
          body: organization,
        }),
      ),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['organizations'] })
    },
  })
}

export const useDeleteOrganization = () => {
  const { tarifia } = useTarifiaClient()

  return useMutation({
    mutationFn: async (organizationId: string) => {
      const { data, error } = await tarifia.DELETE('/v1/organizations/{id}', {
        params: { path: { id: organizationId } },
      })
      return { data, error }
    },
  })
}
