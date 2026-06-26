import { operations } from '@tarifia-sh/client'

export type AuthorizeResponse =
  operations['oauth2:authorize']['responses']['200']['content']['application/json']
