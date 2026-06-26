import { TarifiaLogotype } from '../Layout/Public/TarifiaLogotype'

export function EndSection() {
  return (
    <div className="flex h-full w-full flex-col items-center justify-center gap-6 p-12 md:p-64">
      <TarifiaLogotype logoVariant="icon" size={80} />
    </div>
  )
}
