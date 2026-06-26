import { Box, type BoxProps } from '@tarifia-sh/orbit/Box'

export const LoadingBox = (props: BoxProps) => (
  <Box
    display="block"
    {...props}
    // eslint-disable-next-line tarifia/no-classname-box
    className="dark:bg-tarifia-700 animate-pulse bg-gray-100"
  />
)
