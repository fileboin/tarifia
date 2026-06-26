from tarifia.auth.models import AuthSubject
from tarifia.exceptions import TarifiaError, TarifiaRequestValidationError
from tarifia.kit.db.postgres import AsyncSession
from tarifia.models import Feedback, User
from tarifia.models.feedback import FeedbackType
from tarifia.user_organization.service import (
    user_organization as user_organization_service,
)
from tarifia.worker import enqueue_job

from .repository import FeedbackRepository
from .schemas import FeedbackCreate


class FeedbackError(TarifiaError): ...


class FeedbackService:
    async def submit(
        self,
        session: AsyncSession,
        auth_subject: AuthSubject[User],
        create_schema: FeedbackCreate,
    ) -> Feedback:
        user = auth_subject.subject

        membership = await user_organization_service.get_by_user_and_org(
            session, user.id, create_schema.organization_id
        )
        if membership is None:
            raise TarifiaRequestValidationError(
                [
                    {
                        "type": "value_error",
                        "loc": ("body", "organization_id"),
                        "msg": "User is not a member of this organization.",
                        "input": create_schema.organization_id,
                    }
                ]
            )

        repository = FeedbackRepository.from_session(session)
        feedback = await repository.create(
            Feedback(
                type=create_schema.type,
                message=create_schema.message,
                client_context=create_schema.client_context,
                user=membership.user,
                organization=membership.organization,
            ),
            flush=True,
        )

        # Questions automatically open a Plain support thread, impersonating the
        # customer with their message and attaching the conversation transcript.
        if feedback.type == FeedbackType.question:
            enqueue_job("feedback.reply_in_plain", feedback_id=feedback.id)

        return feedback


feedback = FeedbackService()
