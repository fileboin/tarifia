from __future__ import annotations

from tarifia.base import TarifiaClientError
from tarifia.outputs import (
    AlreadyCanceledSubscription as AlreadyCanceledSubscriptionModel,
)
from tarifia.outputs import (
    CheckoutForbiddenError as CheckoutForbiddenErrorModel,
)
from tarifia.outputs import (
    CustomerNotReady as CustomerNotReadyModel,
)
from tarifia.outputs import (
    ExpiredCheckoutError as ExpiredCheckoutErrorModel,
)
from tarifia.outputs import (
    HTTPValidationError as HTTPValidationErrorModel,
)
from tarifia.outputs import (
    ManualRetryLimitExceeded as ManualRetryLimitExceededModel,
)
from tarifia.outputs import (
    MissingInvoiceBillingDetails as MissingInvoiceBillingDetailsModel,
)
from tarifia.outputs import (
    NotPermitted as NotPermittedModel,
)
from tarifia.outputs import (
    OffSessionChargesNotEnabled as OffSessionChargesNotEnabledModel,
)
from tarifia.outputs import (
    OrderNotDraft as OrderNotDraftModel,
)
from tarifia.outputs import (
    OrderNotEligibleForRetry as OrderNotEligibleForRetryModel,
)
from tarifia.outputs import (
    OrganizationNotReadyForPayments as OrganizationNotReadyForPaymentsModel,
)
from tarifia.outputs import (
    PaymentActionRequired as PaymentActionRequiredModel,
)
from tarifia.outputs import (
    PaymentAlreadyInProgress as PaymentAlreadyInProgressModel,
)
from tarifia.outputs import (
    PaymentError as PaymentErrorModel,
)
from tarifia.outputs import (
    PaymentFailed as PaymentFailedModel,
)
from tarifia.outputs import (
    PaymentMethodInUseByActiveSubscription as PaymentMethodInUseByActiveSubscriptionModel,
)
from tarifia.outputs import (
    PaymentMethodSetupFailed as PaymentMethodSetupFailedModel,
)
from tarifia.outputs import (
    RefundedAlready as RefundedAlreadyModel,
)
from tarifia.outputs import (
    ResourceNotFound as ResourceNotFoundModel,
)
from tarifia.outputs import (
    SubscriptionLocked as SubscriptionLockedModel,
)
from tarifia.outputs import (
    Unauthorized as UnauthorizedModel,
)


class HTTPValidationError(TarifiaClientError):
    error_type = HTTPValidationErrorModel
    error: HTTPValidationErrorModel

    def __init__(self, status_code: int, error: HTTPValidationErrorModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class ResourceNotFound(TarifiaClientError):
    error_type = ResourceNotFoundModel
    error: ResourceNotFoundModel

    def __init__(self, status_code: int, error: ResourceNotFoundModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class NotPermitted(TarifiaClientError):
    error_type = NotPermittedModel
    error: NotPermittedModel

    def __init__(self, status_code: int, error: NotPermittedModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class AlreadyCanceledSubscription(TarifiaClientError):
    error_type = AlreadyCanceledSubscriptionModel
    error: AlreadyCanceledSubscriptionModel

    def __init__(
        self, status_code: int, error: AlreadyCanceledSubscriptionModel
    ) -> None:
        self.error = error
        super().__init__(status_code, error)


class SubscriptionLocked(TarifiaClientError):
    error_type = SubscriptionLockedModel
    error: SubscriptionLockedModel

    def __init__(self, status_code: int, error: SubscriptionLockedModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class PaymentFailed(TarifiaClientError):
    error_type = PaymentFailedModel
    error: PaymentFailedModel

    def __init__(self, status_code: int, error: PaymentFailedModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class Finalize402Error(TarifiaClientError):
    error_type = PaymentFailedModel | PaymentActionRequiredModel
    error: PaymentFailedModel | PaymentActionRequiredModel

    def __init__(
        self, status_code: int, error: PaymentFailedModel | PaymentActionRequiredModel
    ) -> None:
        self.error = error
        super().__init__(status_code, error)


class Finalize403Error(TarifiaClientError):
    error_type = OffSessionChargesNotEnabledModel | OrganizationNotReadyForPaymentsModel
    error: OffSessionChargesNotEnabledModel | OrganizationNotReadyForPaymentsModel

    def __init__(
        self,
        status_code: int,
        error: OffSessionChargesNotEnabledModel | OrganizationNotReadyForPaymentsModel,
    ) -> None:
        self.error = error
        super().__init__(status_code, error)


class OrderNotDraft(TarifiaClientError):
    error_type = OrderNotDraftModel
    error: OrderNotDraftModel

    def __init__(self, status_code: int, error: OrderNotDraftModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class MissingInvoiceBillingDetails(TarifiaClientError):
    error_type = MissingInvoiceBillingDetailsModel
    error: MissingInvoiceBillingDetailsModel

    def __init__(
        self, status_code: int, error: MissingInvoiceBillingDetailsModel
    ) -> None:
        self.error = error
        super().__init__(status_code, error)


class RefundedAlready(TarifiaClientError):
    error_type = RefundedAlreadyModel
    error: RefundedAlreadyModel

    def __init__(self, status_code: int, error: RefundedAlreadyModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class Update403Error(TarifiaClientError):
    error_type = CheckoutForbiddenErrorModel
    error: CheckoutForbiddenErrorModel

    def __init__(self, status_code: int, error: CheckoutForbiddenErrorModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class ExpiredCheckoutError(TarifiaClientError):
    error_type = ExpiredCheckoutErrorModel
    error: ExpiredCheckoutErrorModel

    def __init__(self, status_code: int, error: ExpiredCheckoutErrorModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class ClientUpdate403Error(TarifiaClientError):
    error_type = CheckoutForbiddenErrorModel
    error: CheckoutForbiddenErrorModel

    def __init__(self, status_code: int, error: CheckoutForbiddenErrorModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class PaymentError(TarifiaClientError):
    error_type = PaymentErrorModel
    error: PaymentErrorModel

    def __init__(self, status_code: int, error: PaymentErrorModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class ClientConfirm403Error(TarifiaClientError):
    error_type = CheckoutForbiddenErrorModel
    error: CheckoutForbiddenErrorModel

    def __init__(self, status_code: int, error: CheckoutForbiddenErrorModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class Unauthorized(TarifiaClientError):
    error_type = UnauthorizedModel
    error: UnauthorizedModel

    def __init__(self, status_code: int, error: UnauthorizedModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class CreateMember403Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class PaymentMethodSetupFailed(TarifiaClientError):
    error_type = PaymentMethodSetupFailedModel
    error: PaymentMethodSetupFailedModel

    def __init__(self, status_code: int, error: PaymentMethodSetupFailedModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerNotReady(TarifiaClientError):
    error_type = CustomerNotReadyModel
    error: CustomerNotReadyModel

    def __init__(self, status_code: int, error: CustomerNotReadyModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class PaymentMethodInUseByActiveSubscription(TarifiaClientError):
    error_type = PaymentMethodInUseByActiveSubscriptionModel
    error: PaymentMethodInUseByActiveSubscriptionModel

    def __init__(
        self, status_code: int, error: PaymentMethodInUseByActiveSubscriptionModel
    ) -> None:
        self.error = error
        super().__init__(status_code, error)


class CheckEmailUpdate401Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class VerifyEmailUpdate401Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class VerifyEmailUpdate422Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class ListSeats401Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class ListSeats403Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class ListSeats404Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class AssignSeat400Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class AssignSeat401Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class AssignSeat403Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class AssignSeat404Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class RevokeSeat401Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class RevokeSeat403Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class RevokeSeat404Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class ResendInvitation400Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class ResendInvitation401Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class ResendInvitation403Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class ResendInvitation404Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class ListClaimedSubscriptions401Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class ListMembers401Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class ListMembers403Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class AddMember400Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class AddMember401Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class AddMember403Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class RemoveMember400Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class RemoveMember401Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class RemoveMember403Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class RemoveMember404Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class UpdateMember400Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class UpdateMember401Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class UpdateMember403Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class UpdateMember404Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class PaymentAlreadyInProgress(TarifiaClientError):
    error_type = PaymentAlreadyInProgressModel
    error: PaymentAlreadyInProgressModel

    def __init__(self, status_code: int, error: PaymentAlreadyInProgressModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class OrderNotEligibleForRetry(TarifiaClientError):
    error_type = OrderNotEligibleForRetryModel
    error: OrderNotEligibleForRetryModel

    def __init__(self, status_code: int, error: OrderNotEligibleForRetryModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class ManualRetryLimitExceeded(TarifiaClientError):
    error_type = ManualRetryLimitExceededModel
    error: ManualRetryLimitExceededModel

    def __init__(self, status_code: int, error: ManualRetryLimitExceededModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class GetClaimInfo400Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class GetClaimInfo403Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class GetClaimInfo404Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class ClaimSeat400Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class ClaimSeat403Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class Update404Error(TarifiaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)
