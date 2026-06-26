import { refreshMiddleware } from '@/auth/refreshMiddleware'
import { Client, createClient } from '@tarifia-sh/client'
import Constants from 'expo-constants'
import * as Updates from 'expo-updates'
import {
  createContext,
  useContext,
  useMemo,
  type PropsWithChildren,
} from 'react'
import { useSession } from './SessionProvider'

// `version` is the human-readable marketing version, but it relies on a
// developer manually bumping it. `runtimeVersion` (the fingerprint) and
// `updateId` update automatically on every build/OTA, so they're the reliable
// signal for "which exact build is calling this endpoint". `updateId` is null
// on an embedded launch (fresh install before any OTA, or in dev).
const CLIENT_VERSION_HEADERS = {
  'X-Tarifia-Client-Version': `mobile/${Constants.expoConfig?.version ?? 'unknown'}`,
  'X-Tarifia-Client-Runtime': Updates.runtimeVersion ?? 'unknown',
  'X-Tarifia-Client-Update': Updates.updateId ?? 'embedded',
}

const TarifiaClientContext = createContext<{
  tarifia: Client
}>({
  tarifia: createClient(
    process.env.EXPO_PUBLIC_TARIFIA_SERVER_URL ?? 'https://api.tarifia.sh',
    undefined,
    CLIENT_VERSION_HEADERS,
  ),
})

export function useTarifiaClient() {
  const value = useContext(TarifiaClientContext)
  if (process.env.NODE_ENV !== 'production') {
    if (!value) {
      throw new Error(
        'useTarifiaClient must be wrapped in a <TarifiaClientProvider />',
      )
    }
  }
  return value
}

export function TarifiaClientProvider({ children }: PropsWithChildren) {
  const { session } = useSession()

  const tarifia = useMemo(() => {
    const client = createClient(
      process.env.EXPO_PUBLIC_TARIFIA_SERVER_URL ?? 'https://api.tarifia.sh',
      session ?? '',
      CLIENT_VERSION_HEADERS,
    )
    client.use(refreshMiddleware)
    return client
  }, [session])

  return (
    <TarifiaClientContext.Provider value={{ tarifia }}>
      {children}
    </TarifiaClientContext.Provider>
  )
}
