from pydantic import Field

from tarifia.customer_meter.schemas import CustomerMeterBase
from tarifia.kit.schemas import IDSchema, TimestampedSchema
from tarifia.meter.schemas import NAME_DESCRIPTION as METER_NAME_DESCRIPTION


class CustomerCustomerMeterMeter(IDSchema, TimestampedSchema):
    name: str = Field(description=METER_NAME_DESCRIPTION)


class CustomerCustomerMeter(CustomerMeterBase):
    meter: CustomerCustomerMeterMeter
