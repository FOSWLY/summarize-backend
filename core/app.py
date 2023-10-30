from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from core.settings import get_settings

settings = get_settings()
tags_meta = [
    {
        'name': 'Summarize',
        'description': 'Interaction with Yandex Summarize API without any authorization or restrictions'
    },
    {
        'name': 'Health',
        'description': 'Health of our servers'
    }
]

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=settings.app_name,
        version=settings.app_version,
        description=settings.app_desc,
        license_info = {
            "name": settings.app_license,
        },
        contact = {
            "name": "Developer",
            "url": settings.app_developer_url,
            "email": settings.app_developer_email
        },
        routes = app.routes,
        tags = tags_meta
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "/static/assets/logo.svg",
        "altText": "logo"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app = FastAPI(openapi_url = '/openapi.json', docs_url = '/docs', redoc_url = '/redoc')
app.mount('/static', StaticFiles(directory = 'static'), name = 'static')
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.openapi = custom_openapi