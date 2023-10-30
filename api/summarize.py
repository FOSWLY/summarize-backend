import logging
import httpx

from fastapi import HTTPException, status

from core.settings import get_settings

settings = get_settings()


class YandexSummarize:
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        self.domain: str = '300.ya.ru'
        self.headers: dict = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.967 YaBrowser/23.9.1.967 Yowser/2.5 Safari/537.36",
            "Referer": f'https://{self.domain}/summary',
            "Origin": f'https://{self.domain}',
            "pragma": "no-cache",
            "cache-control": "no-cache"
        }

    async def request(self, endpoint: str, body: dict, headers: dict):
        async with httpx.AsyncClient(http2=True) as client:
            r = await client.post(
                f'https://{self.domain}/api/{endpoint}',
                json = body,
                headers = headers
            )
            self.logger.debug(f'POST /api/{endpoint}: {r.status_code}')
            if r.status_code != status.HTTP_200_OK:
                self.logger.error(f'API answer: {r.read()}')
                raise HTTPException(
                    status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                    detail='Unable to access Yandex API',
                )
            return r.json()

    async def get_sharing_url(self, data: dict):
        headers = self.headers.copy()
        headers['Authorization'] = f'OAuth {settings.api_key}'
        return await self.request('sharing-url', data, headers)

    async def get_sharing_data(self, data: dict):
        headers = self.headers.copy()
        headers['Cookie'] = settings.yandex_cookie
        return await self.request('sharing', data, headers)

    async def generation(self, data: dict):
        headers = self.headers.copy()
        headers['Cookie'] = settings.yandex_cookie
        return await self.request('generation', data, headers)