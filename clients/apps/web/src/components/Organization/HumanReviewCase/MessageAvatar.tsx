import LogoIcon from '@/components/Brand/logos/LogoIcon'
import { schemas } from '@tarifia-sh/client'
import { Avatar } from '@tarifia-sh/orbit'
import React from 'react'

interface Props {
  organization: schemas['Organization']
  fromMerchant: boolean
}

export const MessageAvatar = ({ organization, fromMerchant }: Props) => {
  if (fromMerchant) {
    return (
      <Avatar
        name={organization.name}
        avatar_url={organization.avatar_url}
        className="h-7 w-7 text-[11px]"
      />
    )
  }

  return (
    <div className="dark:bg-tarifia-50 dark:text-tarifia-900 flex h-7 w-7 shrink-0 items-center justify-center rounded-full bg-gray-900 text-white">
      <LogoIcon className="h-6 w-6" />
    </div>
  )
}
