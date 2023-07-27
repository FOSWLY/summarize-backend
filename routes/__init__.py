from fastapi import APIRouter

from routes.endpoints import summarize

api_router = APIRouter()
api_router.include_router(summarize.router, tags = ['Summarize'])