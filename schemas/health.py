from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: str = Field(description='Returns ok if FOSWLY API is available')
    version: str = Field(description='Returns version of FOSWLY API')