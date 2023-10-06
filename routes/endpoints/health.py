import logging
from fastapi import APIRouter


from schemas.health import HealthResponse

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get('/health', response_model=HealthResponse)
async def get_health() -> HealthResponse:
    return HealthResponse(status = 'ok')