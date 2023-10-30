from fastapi import APIRouter


from core.settings import get_settings
from schemas.health import HealthResponse

router = APIRouter()
settings = get_settings()


@router.get('/health', response_model=HealthResponse)
async def get_health() -> HealthResponse:
    return HealthResponse(
        status = 'ok',
        version = settings.app_version
    )