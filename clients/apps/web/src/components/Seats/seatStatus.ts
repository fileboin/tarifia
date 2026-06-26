import { schemas } from '@tarifia-sh/client'
import { type StatusColor } from '@tarifia-sh/orbit'

export const seatStatusDisplayConfig: Record<
  schemas['SeatStatus'],
  [string, StatusColor]
> = {
  pending: ['Pending', 'yellow'],
  claimed: ['Claimed', 'green'],
  revoked: ['Revoked', 'gray'],
}
