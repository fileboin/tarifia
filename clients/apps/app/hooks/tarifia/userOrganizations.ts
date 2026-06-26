import { useTarifiaClient } from '@/providers/TarifiaClientProvider'
import { schemas, unwrap } from '@tarifia-sh/client'
import {
  skipToken,
  useMutation,
  useQuery,
  useQueryClient,
} from '@tanstack/react-query'

export const useUserOrganizationNotificationSettings = (
  organizationId?: string,
) => {
  const { tarifia } = useTarifiaClient()

  return useQuery({
    queryKey: ['user', 'notificationSettings', organizationId],
    queryFn: organizationId
      ? () =>
          unwrap(
            tarifia.GET(
              '/v1/users/me/organizations/{organization_id}/notification-settings',
              {
                params: { path: { organization_id: organizationId } },
              },
            ),
          )
      : skipToken,
  })
}

export const useUpdateUserOrganizationNotificationSettings = () => {
  const { tarifia } = useTarifiaClient()
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: ({
      organizationId,
      notification_settings,
    }: {
      organizationId: string
      notification_settings: schemas['OrganizationNotificationSettings']
    }) =>
      unwrap(
        tarifia.PATCH(
          '/v1/users/me/organizations/{organization_id}/notification-settings',
          {
            params: { path: { organization_id: organizationId } },
            body: { notification_settings },
          },
        ),
      ),
    onSettled: (_data, _error, variables) => {
      queryClient.invalidateQueries({
        queryKey: ['user', 'notificationSettings', variables.organizationId],
      })
    },
  })
}
