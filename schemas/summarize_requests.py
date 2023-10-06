from pydantic import BaseModel, Field

URL_PATTERN= r'(http|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])'


class GetSummarizeURLRequest(BaseModel):
    article_url: str = Field(
        pattern = URL_PATTERN,
        description = "Link to article"
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "article_url": "https://toil.cc",
                },
                {
                    "article_url": "https://bad.toil.cc",
                },
            ]
        }
    }


class GetSummarizeDataRequest(BaseModel):
    token: str = Field(description="Token from yandex url")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "token": "hQwoyXuM",
                },
                {
                    "token": "1",
                },
            ]
        }
    }


class GenerationRequest(BaseModel):
    article_url: str = Field(
        pattern = URL_PATTERN,
        description="Link to article",
        examples=[
            "https://toil.cc",
        ],
        default=None
    )

    video_url: str = Field(
        pattern = URL_PATTERN,
        description = "Link to video",
        examples=[
            "https://www.youtube.com/watch?v=1Nl5APO95Hc",
        ],
        default = None
    )

    session_id: str = Field(
        description="Session id of the generation",
        examples=[
            "77053a47-731434ec-bc52547c-dedf879a",
        ],
        default=None
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "article_url": "https://toil.cc",
                },
                {
                    "video_url": "https://www.youtube.com/watch?v=1Nl5APO95Hc",
                },
                {
                    "session_id": "77053a47-731434ec-bc52547c-dedf879a",
                },
            ]
        }
    }