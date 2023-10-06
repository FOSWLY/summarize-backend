from fastapi import APIRouter

from routes.endpoints import health, summarize

api_router = APIRouter()
api_router.include_router(summarize.router, tags = ['Summarize'])
api_router.include_router(health.router, tags = ['Health'])