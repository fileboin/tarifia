import types
import typing

from tarifia.base import AsyncClientBase, SyncClientBase
from tarifia.benefit_grants import BenefitGrantsAsync, BenefitGrantsSync
from tarifia.benefits import BenefitsAsync, BenefitsSync
from tarifia.checkout_links import CheckoutLinksAsync, CheckoutLinksSync
from tarifia.checkouts import CheckoutsAsync, CheckoutsSync
from tarifia.custom_fields import CustomFieldsAsync, CustomFieldsSync
from tarifia.customer_meters import CustomerMetersAsync, CustomerMetersSync
from tarifia.customer_portal import CustomerPortalAsync, CustomerPortalSync
from tarifia.customer_seats import CustomerSeatsAsync, CustomerSeatsSync
from tarifia.customer_sessions import CustomerSessionsAsync, CustomerSessionsSync
from tarifia.customers import CustomersAsync, CustomersSync
from tarifia.discounts import DiscountsAsync, DiscountsSync
from tarifia.disputes import DisputesAsync, DisputesSync
from tarifia.event_types import EventTypesAsync, EventTypesSync
from tarifia.events import EventsAsync, EventsSync
from tarifia.files import FilesAsync, FilesSync
from tarifia.license_keys import LicenseKeysAsync, LicenseKeysSync
from tarifia.members import MembersAsync, MembersSync
from tarifia.meters import MetersAsync, MetersSync
from tarifia.metrics import MetricsAsync, MetricsSync
from tarifia.oauth2 import Oauth2Async, Oauth2Sync
from tarifia.orders import OrdersAsync, OrdersSync
from tarifia.organizations import OrganizationsAsync, OrganizationsSync
from tarifia.payments import PaymentsAsync, PaymentsSync
from tarifia.products import ProductsAsync, ProductsSync
from tarifia.refunds import RefundsAsync, RefundsSync
from tarifia.subscriptions import SubscriptionsAsync, SubscriptionsSync
from tarifia.webhooks import WebhooksAsync, WebhooksSync


class Tarifia:
    def __init__(self, base_url: str, version: str, access_token: str) -> None:
        self._client = SyncClientBase(base_url, version, access_token)
        self.organizations = OrganizationsSync(self._client)
        self.subscriptions = SubscriptionsSync(self._client)
        self.oauth2 = Oauth2Sync(self._client)
        self.benefits = BenefitsSync(self._client)
        self.benefit_grants = BenefitGrantsSync(self._client)
        self.webhooks = WebhooksSync(self._client)
        self.products = ProductsSync(self._client)
        self.orders = OrdersSync(self._client)
        self.refunds = RefundsSync(self._client)
        self.disputes = DisputesSync(self._client)
        self.checkouts = CheckoutsSync(self._client)
        self.files = FilesSync(self._client)
        self.metrics = MetricsSync(self._client)
        self.license_keys = LicenseKeysSync(self._client)
        self.checkout_links = CheckoutLinksSync(self._client)
        self.custom_fields = CustomFieldsSync(self._client)
        self.discounts = DiscountsSync(self._client)
        self.customers = CustomersSync(self._client)
        self.members = MembersSync(self._client)
        self.customer_portal = CustomerPortalSync(self._client)
        self.customer_seats = CustomerSeatsSync(self._client)
        self.customer_sessions = CustomerSessionsSync(self._client)
        self.events = EventsSync(self._client)
        self.event_types = EventTypesSync(self._client)
        self.meters = MetersSync(self._client)
        self.customer_meters = CustomerMetersSync(self._client)
        self.payments = PaymentsSync(self._client)

    def __enter__(self) -> typing.Self:
        self._client.__enter__()
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None = None,
        exc_val: BaseException | None = None,
        exc_tb: types.TracebackType | None = None,
    ) -> None:
        self._client.__exit__(exc_type, exc_val, exc_tb)


class TarifiaAsync:
    def __init__(self, base_url: str, version: str, access_token: str) -> None:
        self._client = AsyncClientBase(base_url, version, access_token)
        self.organizations = OrganizationsAsync(self._client)
        self.subscriptions = SubscriptionsAsync(self._client)
        self.oauth2 = Oauth2Async(self._client)
        self.benefits = BenefitsAsync(self._client)
        self.benefit_grants = BenefitGrantsAsync(self._client)
        self.webhooks = WebhooksAsync(self._client)
        self.products = ProductsAsync(self._client)
        self.orders = OrdersAsync(self._client)
        self.refunds = RefundsAsync(self._client)
        self.disputes = DisputesAsync(self._client)
        self.checkouts = CheckoutsAsync(self._client)
        self.files = FilesAsync(self._client)
        self.metrics = MetricsAsync(self._client)
        self.license_keys = LicenseKeysAsync(self._client)
        self.checkout_links = CheckoutLinksAsync(self._client)
        self.custom_fields = CustomFieldsAsync(self._client)
        self.discounts = DiscountsAsync(self._client)
        self.customers = CustomersAsync(self._client)
        self.members = MembersAsync(self._client)
        self.customer_portal = CustomerPortalAsync(self._client)
        self.customer_seats = CustomerSeatsAsync(self._client)
        self.customer_sessions = CustomerSessionsAsync(self._client)
        self.events = EventsAsync(self._client)
        self.event_types = EventTypesAsync(self._client)
        self.meters = MetersAsync(self._client)
        self.customer_meters = CustomerMetersAsync(self._client)
        self.payments = PaymentsAsync(self._client)

    async def __aenter__(self) -> typing.Self:
        await self._client.__aenter__()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None = None,
        exc_val: BaseException | None = None,
        exc_tb: types.TracebackType | None = None,
    ) -> None:
        await self._client.__aexit__(exc_type, exc_val, exc_tb)


__all__ = ["Tarifia", "TarifiaAsync"]
