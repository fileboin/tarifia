from fastapi import Depends

from tarifia.authz.dependencies import AuthorizeWebUserWrite
from tarifia.kit.db.postgres import AsyncSession
from tarifia.models import Feedback as FeedbackModel
from tarifia.openapi import APITag
from tarifia.postgres import get_db_session
from tarifia.routing import APIRouter

from .schemas import Feedback, FeedbackCreate
from .service import feedback as feedback_service

router = APIRouter(prefix="/feedbacks", tags=["feedbacks", APITag.private])


@router.post("/", response_model=Feedback, status_code=201)
async def submit(
    create_schema: FeedbackCreate,
    auth_subject: AuthorizeWebUserWrite,
    session: AsyncSession = Depends(get_db_session),
) -> FeedbackModel:
    return await feedback_service.submit(session, auth_subject, create_schema)
