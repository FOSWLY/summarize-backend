import logging
import httpx

from typing import Dict
from settings import API_KEY, YANDEX_COOKIE


class YandexSummarize:
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        self.domain: str = '300.ya.ru'
        self.headers: Dict = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.0.2526 Yowser/2.5 Safari/537.36",
            "Referer": f'https://{self.domain}/summary',
            "Origin": f'https://{self.domain}',
            "pragma": "no-cache",
            "cache-control": "no-cache"
        }

    async def request(self, endpoint: str, body: Dict, headers: Dict):
        async with httpx.AsyncClient(http2=True) as client:
            r = await client.post(
                f'https://{self.domain}/api/{endpoint}',
                json = body,
                headers = headers
            )
            self.logger.debug(f'POST /api/{endpoint}: {r.status_code}')
            return r.json()

    async def get_sharing_url(self, data: dict):
        headers = self.headers.copy()
        headers['Authorization'] = f'OAuth {API_KEY}'
        return await self.request('sharing-url', data, headers)

    async def get_sharing_data(self, data: dict):
        headers = self.headers.copy()
        headers['Cookie'] = YANDEX_COOKIE
        return await self.request('sharing', data, headers)

    async def generation(self, data: dict):
        headers = self.headers.copy()
        headers['Cookie'] = YANDEX_COOKIE
        return await self.request('generation', data, headers)