import { queryClient, QueryClientProvider } from '@/utils/query'
import { useReactQueryDevTools } from '@dev-plugins/react-query'

export function TarifiaQueryClientProvider({
  children,
}: {
  children: React.ReactElement
}) {
  useReactQueryDevTools(queryClient)

  return (
    <QueryClientProvider client={queryClient}>{children}</QueryClientProvider>
  )
}
