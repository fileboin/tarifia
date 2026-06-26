import { api } from '@/utils/client'
import { unwrap } from '@tarifia-sh/client'
import { useQuery } from '@tanstack/react-query'
import { defaultRetry } from './retry'

export const useListNotificationRecipients = () => {
  return useQuery({
    queryKey: ['notification_recipients'],
    queryFn: () => unwrap(api.GET('/v1/notifications/recipients')),
    retry: defaultRetry,
  })
}
