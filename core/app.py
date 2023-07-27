from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from config.load import load_cfg

settings = load_cfg()['server']


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=settings['site_name'],
        version="1.0.0",
        description=f"{settings['site_name']} is Free Yandex Summarize API without any authorization or restrictions.",
        license_info = {
            "name": "MIT",
        },
        servers=[
            {
                "name": "production",
                "url": settings['site_url']
            }
        ],
        contact = {
            "name": "Developer",
            "url": "https://github.com/FOSWLY/summarize-articles-backend",
            "email": "toil.contact@yandex.com"
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

tags_meta = [
    {
        'name': 'Summarize',
        'description': 'Interaction with Yandex Summarize API without any authorization or restrictions'
    }
]


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