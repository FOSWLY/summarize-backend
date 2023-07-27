from enum import Enum
from pydantic import BaseModel, Field


class YandexPublicStatus(str, Enum):
    SUCCESS = 'success'
    ERROR = 'error'


class YandexPublicResponse(BaseModel):
    status: str = Field(examples=[
        YandexPublicStatus.SUCCESS,
        YandexPublicStatus.ERROR,
    ])


class YandexPrivateErrorStatus(str, Enum):
    PAGE_NOT_FOUND = 1 # error_code is 1 or 4
    AI_COULDNT_EXTRACT_TEXT = 2
    ARTICLE_IS_TOO_LONG = 3
    UNKNOWN_ERROR = 5 # error_code is 5 or 7 or 9
    AI_COULDNT_RETELL_ARTICLE = 6 # error_code is 6 or 8 or 11 or 12
    BROWSER_OUTDATED = 10


class YandexPrivateStatus(str, Enum):
    IN_PROGRESS = 1
    SUCCESS = 2
    ERROR = 3
    NOT_FOUND_IN_CACHE = 4


class YandexPrivateResponse(BaseModel):
    status_code: int = Field(examples=[
        YandexPrivateStatus.IN_PROGRESS,
        YandexPrivateStatus.SUCCESS,
        YandexPrivateStatus.ERROR,
        YandexPrivateStatus.NOT_FOUND_IN_CACHE
    ]) # 4 - couldn't be found in the cache