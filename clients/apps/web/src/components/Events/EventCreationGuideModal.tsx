import { Button } from '@tarifia-sh/orbit'
import { Well } from '../Shared/Well'
import {
  SyntaxHighlighterClient,
  SyntaxHighlighterProvider,
} from '../SyntaxHighlighterShiki/SyntaxHighlighterClient'

export interface EventCreationGuideModalProps {
  hide: () => void
}

export const EventCreationGuideModal = ({
  hide,
}: EventCreationGuideModalProps) => {
  return (
    <SyntaxHighlighterProvider>
      <div className="flex flex-col gap-4 p-8">
        <h1 className="text-2xl">Event Ingestion</h1>
        <p>Events can only be created through the Tarifia Ingestion API.</p>
        <Well className="dark:bg-tarifia-900 rounded-lg bg-gray-100 p-4 text-sm">
          <SyntaxHighlighterClient
            lang="typescript"
            code={`import { Tarifia } from "@tarifia-sh/sdk";

const tarifia = new Tarifia({
  accessToken: process.env["TARIFIA_ACCESS_TOKEN"] ?? "",
});

const result = await tarifia.events.ingest({
  events: [
    {
      name: "<value>",
      customerId: "<value>",
      metadata: {
        myCustomProperty: "value",
      },
    },
  ],
});`}
          />
        </Well>
        <Button className="self-start" onClick={hide} variant="secondary">
          Close
        </Button>
      </div>
    </SyntaxHighlighterProvider>
  )
}
