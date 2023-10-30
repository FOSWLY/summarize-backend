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

    text: str = Field(
        min_length=300,
        max_length=30000,
        description="Text to summarize",
        examples=[
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
        ],
        default=None
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