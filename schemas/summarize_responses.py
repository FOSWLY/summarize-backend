from typing import Dict, List
from pydantic import Field
from schemas.base import YandexPublicResponse, YandexPublicStatus, YandexPrivateResponse, YandexPrivateStatus, YandexPrivateErrorStatus

URL_PATTERN= r'(http|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])'


class GetSummarizeURLResponse(YandexPublicResponse):
    sharing_url: str = Field(
        pattern=URL_PATTERN,
        description="Link to summarized article",
        default=None,
    )
    message: str = Field(
        description="Error message descriptions",
        default=None,
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "status": YandexPublicStatus.SUCCESS,
                    "sharing_url": "https://300.ya.ru/hQwoyXuM",
                },
                {
                    "status": YandexPublicStatus.ERROR,
                    "message": "not found",
                }
            ]
        }
    }


# universal
class GetSummaryDataResponse(YandexPrivateResponse):
    thesis: List[Dict[str, int|str]] = Field(
        description="Retelling of the article",
        default=None
    )
    normalized_url: str = Field(
        pattern=URL_PATTERN,
        description="Link to the original article",
        default=None,
    )
    sharing_url: str = Field(
        pattern=URL_PATTERN,
        description="Link to summarized article",
        default=None,
    )
    title: str = Field(
        description="The title of the original site",
        default=None
    )

class GetSummarizeDataResponse(GetSummaryDataResponse):
    article_age_seconds: int = Field(
        ge=0,
        description="How long ago the article was retold (seconds)",
        default=None
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "thesis": [
                        {
                            "id": 0,
                            "content": "На сайте можно найти информацию о проектах и донаты."
                        },
                        {
                            "id": 1,
                            "content": "FeimisioDonate - система донатов для CS:GO серверов на Python, NuxtJS и FastAPI."
                        },
                        {
                            "id": 2,
                            "content": "Toiloff Website - личный сайт с информацией о себе и проектах."
                        },
                        {
                            "id": 3,
                            "content": "LZT Upgrade - реализация полезных скриптов для форума Lolzteam на JavaScript, JQuery и Webpack."
                        },
                        {
                            "id": 4,
                            "content": "Simple MySQL Backuper - утилита для резервного копирования баз данных MySQL на Python."
                        },
                        {
                            "id": 5,
                            "content": "Voice Over Translation - расширение для закадрового перевода видео в других браузерах."
                        },
                        {
                            "id": 6,
                            "content": "SB-MaterialAdmin/New Server - плагин для администраторов CS:GO серверов на SourcePawn, CS:GO и MySQL."
                        }
                    ],
                    "status_code": YandexPrivateStatus.SUCCESS,
                    "normalized_url": "https://toiloff.ru",
                    "sharing_url": "https://300.ya.ru/hQwoyXuM",
                    "article_age_seconds": 5169,
                    "title": "Главная - Toiloff"
                },
                {
                    "status_code": YandexPrivateStatus.NOT_FOUND_IN_CACHE
                }
            ]
        }
    }


class GenerationResponse(GetSummaryDataResponse):
    session_id: str = Field(
        description="Session id of the generation",
        examples=[
            "77053a47-731434ec-bc52547c-dedf879a",
        ],
        default=None
    )
    poll_interval_ms: int = Field(
        description="The interval with which requests should be sent (in milliseconds)",
        default=None
    )
    error_code: int = Field(
        description="Error code ID (see the repository documentation)",
        default=None,
        examples=[
            YandexPrivateErrorStatus.PAGE_NOT_FOUND,
            YandexPrivateErrorStatus.AI_COULDNT_EXTRACT_TEXT,
            YandexPrivateErrorStatus.ARTICLE_IS_TOO_LONG,
            YandexPrivateErrorStatus.UNKNOWN_ERROR,
            YandexPrivateErrorStatus.AI_COULDNT_RETELL_ARTICLE,
            YandexPrivateErrorStatus.BROWSER_OUTDATED
        ]
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "thesis": [
                        {
                            "id": 0,
                            "content": "На сайте можно найти информацию о проектах и донаты."
                        },
                        {
                            "id": 1,
                            "content": "FeimisioDonate - система донатов для CS:GO серверов на Python, NuxtJS и FastAPI."
                        },
                        {
                            "id": 2,
                            "content": "Toiloff Website - личный сайт с информацией о себе и проектах."
                        },
                        {
                            "id": 3,
                            "content": "LZT Upgrade - реализация полезных скриптов для форума Lolzteam на JavaScript, JQuery и Webpack."
                        },
                        {
                            "id": 4,
                            "content": "Simple MySQL Backuper - утилита для резервного копирования баз данных MySQL на Python."
                        },
                        {
                            "id": 5,
                            "content": "Voice Over Translation - расширение для закадрового перевода видео в других браузерах."
                        },
                        {
                            "id": 6,
                            "content": "SB-MaterialAdmin/New Server - плагин для администраторов CS:GO серверов на SourcePawn, CS:GO и MySQL."
                        }
                    ],
                    "status_code": YandexPrivateStatus.SUCCESS,
                    "session_id": "77053a47-731434ec-bc52547c-dedf879a",
                    "normalized_url": "https://toiloff.ru",
                    "sharing_url": "https://300.ya.ru/hQwoyXuM",
                    "poll_interval_ms": 500,
                    "title": "Главная - Toiloff"
                },
                {
                    "status_code": YandexPrivateStatus.IN_PROGRESS,
                    "session_id": "77053a47-731434ec-bc52547c-dedf879a",
                    "poll_interval_ms": 500,
                    "normalized_url": "https://toiloff.ru/",
                    "title": "Главная - Toiloff",
                },
                {
                    "status_code": YandexPrivateStatus.ERROR,
                    "error_code": YandexPrivateErrorStatus.PAGE_NOT_FOUND
                }
            ]
        }
    }