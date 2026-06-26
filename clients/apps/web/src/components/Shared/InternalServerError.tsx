'use client'

import Link from 'next/link'
import LogoType from '../Brand/logos/LogoType'

export default function InternalServerError({ digest }: { digest?: string }) {
  return (
    <div className="dark:bg-tarifia-950 flex h-screen w-full flex-col items-center justify-center gap-y-12 bg-gray-50 px-12 text-center">
      <div className="flex flex-col items-center justify-center gap-y-1">
        <h1 className="text-2xl font-medium text-black dark:text-white">
          Something went wrong
        </h1>
        <p className="dark:text-tarifia-400 -mb-1 max-w-md text-center text-base text-balance text-gray-600">
          Sorry, we&rsquo;re having an issue on our end. Please try again later
          or reach out to support if the issue persists.
        </p>
      </div>
      <ul className="dark:text-tarifia-400 dark:bg-tarifia-800 flex max-w-md items-center gap-x-2 rounded-lg bg-white p-1.5 px-3 text-center text-sm leading-normal text-balance text-gray-600">
        <li>
          <Link
            href="/"
            className="dark:hover:text-tarifia-300 block p-1 hover:text-gray-700 hover:underline"
            prefetch={false}
          >
            Homepage
          </Link>
        </li>
        <li className="dark:text-tarifia-500 user-select-none text-gray-400">
          ·
        </li>
        <li>
          <a
            href="https://tarifia.sh/docs"
            className="dark:hover:text-tarifia-300 block p-1 hover:text-gray-700 hover:underline"
          >
            Documentation
          </a>
        </li>
        <li className="dark:text-tarifia-500 user-select-none text-gray-400">
          ·
        </li>
        <li>
          <a
            href="mailto:support@tarifia.sh"
            className="dark:hover:text-tarifia-300 block p-1 hover:text-gray-700 hover:underline"
          >
            Support
          </a>
        </li>
      </ul>
      <LogoType className="h-5 text-black dark:text-white" />
      {digest && (
        <pre className="dark:text-tarifia-600 font-mono text-xs whitespace-break-spaces text-gray-400">
          Debugging information: {digest}
        </pre>
      )}
    </div>
  )
}
