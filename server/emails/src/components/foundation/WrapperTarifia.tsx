import { Container, Preview } from 'react-email'
import TarifiaHeader from '../TarifiaHeader'
import WrapperBase from '../WrapperBase'

interface WrapperTarifiaProps {
  children: React.ReactNode
  preview?: string
}

const WrapperTarifia = ({ children, preview }: WrapperTarifiaProps) => {
  return (
    <WrapperBase>
      {preview ? <Preview>{preview}</Preview> : null}
      <Container className="px-[12px] pt-[20px] pb-[10px]">
        <TarifiaHeader />
      </Container>
      <Container className="px-[20px] pt-[10px] pb-[20px]">
        {children}
      </Container>
    </WrapperBase>
  )
}

export default WrapperTarifia
