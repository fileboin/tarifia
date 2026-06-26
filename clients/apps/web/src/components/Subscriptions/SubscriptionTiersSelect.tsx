import { schemas } from '@tarifia-sh/client'
import {
  Select,
  SelectContent,
  SelectItem,
  SelectSeparator,
  SelectTrigger,
  SelectValue,
} from '@tarifia-sh/orbit'
import React from 'react'

interface SubscriptionTiersSelectProps {
  products: schemas['Product'][]
  value: string
  onChange: (value: string) => void
}

const SubscriptionTiersSelect: React.FC<SubscriptionTiersSelectProps> = ({
  products,
  value,
  onChange,
}) => {
  return (
    <Select value={value} onValueChange={onChange}>
      <SelectTrigger>
        <SelectValue placeholder="Select a product" />
      </SelectTrigger>
      <SelectContent>
        <SelectItem value="all">
          <span className="whitespace-nowrap">All products</span>
        </SelectItem>
        <SelectSeparator />
        {products.map((product) => (
          <SelectItem key={product.id} value={product.id}>
            {product.name}
          </SelectItem>
        ))}
      </SelectContent>
    </Select>
  )
}

export default SubscriptionTiersSelect
