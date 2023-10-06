import logging
from fastapi import APIRouter, HTTPException, status


from api.summarize import YandexSummarize
from schemas.summarize_requests import GenerationRequest, GetSummarizeURLRequest, GetSummarizeDataRequest
from schemas.summarize_responses import GetSummarizeURLResponse, GetSummarizeDataResponse, GenerationResponse

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post('/sharing-url', response_model=GetSummarizeURLResponse, response_model_exclude_none=True)
async def get_sharing_url(body: GetSummarizeURLRequest) -> GetSummarizeURLResponse:
    return await YandexSummarize().get_sharing_url(body.model_dump())


@router.post('/sharing', response_model=GetSummarizeDataResponse, response_model_exclude_none=True)
async def get_sharing_data(body: GetSummarizeDataRequest) -> GetSummarizeDataResponse:
    return await YandexSummarize().get_sharing_data(body.model_dump())


@router.post('/generation', response_model=GenerationResponse, response_model_exclude_none=True)
async def generation(body: GenerationRequest) -> GenerationResponse:
    generation_params = body.model_dump(exclude_none=True)
    if generation_params == {}:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail='At least one parameter for generation should be provided',
        )
    elif 'video_url' in generation_params and 'article_url' in generation_params:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail='You can select only 1 parameter: article_url or video_url',
        )
    test = await YandexSummarize().generation(generation_params)
    logger.info(test)
    return test