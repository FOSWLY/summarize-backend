from typing import Dict, List
from pydantic import Field, BaseModel
from schemas.base import YandexPublicResponse, YandexPublicStatus, YandexPrivateResponse, YandexPrivateStatus, YandexPrivateErrorStatus, YandexType

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
class ThesisItem(BaseModel):
    id: int = Field(
        description="Id of the Item",
        default=None
    )
    content: str = Field(
        description="Content of the Item",
        default=None
    )


class ArticleThesisItem(ThesisItem):
    link: str = Field(
        description="Link to item",
        default=None
    )


class VideoSummaryKeyPoints(BaseModel):
    id: int = Field(
        description="Id of the Item",
        default=None
    )
    content: str = Field(
        description="Content of the Item",
        default=None
    )
    start_time: int = Field(
        description="Time of Item in seconds",
        default=None
    )
    theses: List[ThesisItem] = Field(
        description="Retelling of the segment",
        default=None
    )


class GetSummaryDataResponse(YandexPrivateResponse):
    # Universal
    sharing_url: str = Field(
        pattern=URL_PATTERN,
        description="Link to summarized article",
        default=None,
    )
    poll_interval_ms: int = Field(
        description="The interval with which requests should be sent (in milliseconds)",
        default=None
    )
    normalized_url: str = Field(
        pattern=URL_PATTERN,
        description="Link to the original article",
        default=None,
    )

    # Only for articles
    thesis: List[ArticleThesisItem] = Field(
        description="Retelling of the article",
        default=None
    )
    title: str = Field(
        description="The title of the original site",
        default=None
    )
    total_parts: int = Field(
        description="Count of summarized parts of article",
        default=None
    )

    # Only for video
    keypoints: List[VideoSummaryKeyPoints] = Field(
        description="List of Thesis with times and titles",
        default=None
    )
    video_title: str = Field(
        description="The title of the original video",
        default=None
    )
    type: str = Field(
        # article / video
        description="Type of summarize",
        default=None
    )


class GetSummarizeDataResponse(GetSummaryDataResponse):
    # for article
    article_age_seconds: int = Field(
        ge=0,
        description="How long ago the article was retold (seconds)",
        default=None
    )
    # for video
    summary_age_seconds: int = Field(
        ge=0,
        description="How long ago the video was retold (seconds)",
        default=None
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                # article example
                {
                    "thesis": [
                        {
                            "id": 0,
                            "content": "На сайте можно найти информацию о проектах и узнать о создателе.",
                            "link": "https://toil.cc/#:~:text=..."
                        },
                        {
                            "id": 1,
                            "content": "Проекты включают: VOT-CLI, FeimisioDonate, Toiloff Website, LZT Upgrade, Voice Over Translation, SB-MaterialAdmin/NewServer.",
                            "link": "https://toil.cc/#:~:text=..."
                        },
                        {
                            "id": 2,
                            "content": "VOT-CLI - CLI для перевода видео с закадровым озвучиванием.",
                            "link": "https://toil.cc/#:~:text=..."
                        },
                        {
                            "id": 3,
                            "content": "FeimisioDonate - система донатов для CS:GO серверов на Python, NodeJS, NuxtJS, FastAPI, MySQL.",
                            "link": "https://toil.cc/#:~:text=..."
                        },
                        {
                            "id": 4,
                            "content": "Toiloff Website - личный сайт с информацией о создателе и его проектах.",
                            "link": "https://toil.cc/#:~:text=..."
                        },
                        {
                            "id": 5,
                            "content": "LZT Upgrade - реализация полезных скриптов для форума Lolzteam на JavaScript, JQuery, Extensions.",
                            "link": "https://toil.cc/#:~:text=..."
                        },
                        {
                            "id": 6,
                            "content": "Voice Over Translation - расширение для Yandex Browser, добавляющее закадровый перевод видео в другие браузеры.",
                            "link": "https://toil.cc/#:~:text=..."
                        },
                        {
                            "id": 7,
                            "content": "SB-MaterialAdmin/NewServer - плагин для администраторов CS:GO серверов на SourcePawn, MySQL.",
                            "link": "https://toil.cc/#:~:text=..."
                        }
                    ],
                    "status_code": YandexPrivateStatus.SUCCESS,
                    "normalized_url": "https://toil.cc",
                    "sharing_url": "https://300.ya.ru/hQwoyXuM",
                    "article_age_seconds": 51,
                    "title": "Главная - Toiloff",
                    "total_parts": 1,
                    "type": "article"
                },
                # video example
                {
                    "keypoints": [
                        {
                            "id": 1,
                            "content": "Влюбленность и ревность",
                            "start_time": 17,
                            "theses": [
                                {
                                    "id": 1,
                                    "content": "В видео автор выражает свои чувства к другому человеку, признаваясь в любви и ревности."
                                },
                                {
                                    "id": 2,
                                    "content": "Он задается вопросом, в чем его вина и почему он продолжает влюбляться в этого человека."
                                }
                            ]
                        },
                        {
                            "id": 2,
                            "content": "Размышления о любви",
                            "start_time": 98,
                            "theses": [
                                {
                                    "id": 1,
                                    "content": "Автор размышляет о том, что любовь может быть сложной и причинять боль, но он все равно продолжает влюбляться в этого человека."
                                },
                                {
                                    "id": 2,
                                    "content": "Он предлагает забыть о любви и просто наслаждаться моментом, но в то же время понимает, что это невозможно."
                                }
                            ]
                        },
                        {
                            "id": 3,
                            "content": "Признание в любви",
                            "start_time": 150,
                            "theses": [
                                {
                                    "id": 1,
                                    "content": "В конце видео автор признается в любви к этому человеку, несмотря на все сложности и боль, которые они испытывают."
                                },
                                {
                                    "id": 2,
                                    "content": "Он просит этого человека держаться и раздеваться, если он пришел."
                                }
                            ]
                        }
                    ],
                    "status_code": YandexPrivateStatus.SUCCESS_VIDEO,
                    "poll_interval": 500,
                    "normalized_url": "https://youtu.be/nr1tV3HLQhQ",
                    "sharing_url": "https://300.ya.ru/v_3d6661EN",
                    "summary_age_seconds": 148,
                    "video_title": "к черту любовь - speed up",
                    "type": "video"
                },
                {
                    "status_code": YandexPrivateStatus.NOT_FOUND_IN_CACHE
                }
            ]
        }
    }


class GenerationResponse(GetSummaryDataResponse):
    # status_code only for articles
    status_code: int = Field(examples=[
        YandexPrivateStatus.IN_PROGRESS,
        YandexPrivateStatus.SUCCESS,
        YandexPrivateStatus.ERROR,
        YandexPrivateStatus.NOT_FOUND_IN_CACHE
    ], default=None)

    session_id: str = Field(
        description="Session id of the generation",
        examples=[
            "77053a47-731434ec-bc52547c-dedf879a",
        ],
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

    message: str = Field(
        description="Error message descriptions (only for video)",
        default=None,
    )

    type: str = Field(
        # video or article
        description="Type of content (video or article)",
        default=None,
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                # article example
                {
                    "thesis": [
                        {
                            "id": 0,
                            "content": "На сайте можно найти информацию о проектах и узнать о создателе.",
                            "link": "https://toil.cc/#:~:text=..."
                        },
                        {
                            "id": 1,
                            "content": "Проекты включают: VOT-CLI, FeimisioDonate, Toiloff Website, LZT Upgrade, Voice Over Translation, SB-MaterialAdmin/NewServer.",
                            "link": "https://toil.cc/#:~:text=..."
                        },
                        {
                            "id": 2,
                            "content": "VOT-CLI - CLI для перевода видео с закадровым озвучиванием.",
                            "link": "https://toil.cc/#:~:text=..."
                        },
                        {
                            "id": 3,
                            "content": "FeimisioDonate - система донатов для CS:GO серверов на Python, NodeJS, NuxtJS, FastAPI, MySQL.",
                            "link": "https://toil.cc/#:~:text=..."
                        },
                        {
                            "id": 4,
                            "content": "Toiloff Website - личный сайт с информацией о создателе и его проектах.",
                            "link": "https://toil.cc/#:~:text=..."
                        },
                        {
                            "id": 5,
                            "content": "LZT Upgrade - реализация полезных скриптов для форума Lolzteam на JavaScript, JQuery, Extensions.",
                            "link": "https://toil.cc/#:~:text=..."
                        },
                        {
                            "id": 6,
                            "content": "Voice Over Translation - расширение для Yandex Browser, добавляющее закадровый перевод видео в другие браузеры.",
                            "link": "https://toil.cc/#:~:text=..."
                        },
                        {
                            "id": 7,
                            "content": "SB-MaterialAdmin/NewServer - плагин для администраторов CS:GO серверов на SourcePawn, MySQL.",
                            "link": "https://toil.cc/#:~:text=..."
                        }
                    ],
                    "status_code": YandexPrivateStatus.SUCCESS,
                    "session_id": "77053a47-731434ec-bc52547c-dedf879a",
                    "normalized_url": "https://toil.cc",
                    "sharing_url": "https://300.ya.ru/hQwoyXuM",
                    "poll_interval_ms": 500,
                    "type": YandexType.ARTICLE,
                    "title": "Главная - Toiloff",
                    "total_parts": 1
                },
                # video example
                {
                    "keypoints": [
                        {
                            "id": 1,
                            "content": "Перчатки с резинкой",
                            "start_time": 22,
                            "theses": [
                                {
                                    "id": 1,
                                    "content": "Автор рассказывает о своем лайфхаке с пришитыми резинками на перчатках, чтобы они не терялись."
                                }
                            ]
                        },
                        {
                            "id": 2,
                            "content": "Исторический момент",
                            "start_time": 45,
                            "theses": [
                                {
                                    "id": 1,
                                    "content": "Автор говорит о том, что он откроет крепость и расскажет об этом своим знакомым."
                                }
                            ]
                        },
                        {
                            "id": 3,
                            "content": "Вавилон",
                            "start_time": 69,
                            "theses": [
                                {
                                    "id": 1,
                                    "content": "Автор говорит, что он не сдастся и не успокоится, пока не построит свою крепость."
                                }
                            ]
                        },
                        {
                            "id": 4,
                            "content": "Финальная точка",
                            "start_time": 69,
                            "theses": [
                                {
                                    "id": 1,
                                    "content": "Автор говорит, что его крепость будет построена и он будет жить в ней, не обращая внимания на окружающих."
                                }
                            ]
                        }
                    ],
                    "status_code": YandexPrivateStatus.SUCCESS_VIDEO,
                    "session_id": "0abd5e93-d639-400a-a7cb-fd8227ca5b78",
                    "sharing_url": "https://300.ya.ru/v_HlUtZy1Q",
                    "poll_interval_ms": 500,
                    "video_title": "Дайте танк(!) - Крепость [speed up]",
                    "type": YandexType.VIDEO,
                },
                # article in progress
                {
                    "status_code": YandexPrivateStatus.IN_PROGRESS,
                    "session_id": "77053a47-731434ec-bc52547c-dedf879a",
                    "poll_interval_ms": 500,
                    "normalized_url": "https://toil.cc/",
                    "title": "Главная - Toiloff",
                    "type": YandexType.ARTICLE,
                },
                # article error
                {
                    "status_code": YandexPrivateStatus.ERROR,
                    "type": YandexType.ARTICLE,
                    "error_code": YandexPrivateErrorStatus.PAGE_NOT_FOUND
                },
                # video error
                {
                    "type": YandexType.VIDEO,
                    "message": "Not Found"
                }
            ]
        }
    }