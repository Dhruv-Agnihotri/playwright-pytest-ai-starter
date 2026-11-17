import asyncio
import time
from dataclasses import dataclass
from typing import Sequence
import aiohttp


@dataclass
class LinkCheckResult:
    url: str
    status: int | None
    ok: bool
    latency_ms: float
    error: str | None = None


class AsyncLinkValidator:
    """Concurrent URL validator using semaphore-bounded asyncio requests."""

    def __init__(self, max_concurrency: int = 10, timeout_sec: float = 10.0):
        self.semaphore = asyncio.Semaphore(max_concurrency)
        self.timeout = aiohttp.ClientTimeout(total=timeout_sec)

    async def _check_one(self, session: aiohttp.ClientSession, url: str) -> LinkCheckResult:
        async with self.semaphore:
            start = time.perf_counter()
            try:
                async with session.get(url, allow_redirects=True) as resp:
                    elapsed = round((time.perf_counter() - start) * 1000, 2)
                    return LinkCheckResult(
                        url=url,
                        status=resp.status,
                        ok=200 <= resp.status < 400,
                        latency_ms=elapsed,
                    )
            except Exception as exc:
                elapsed = round((time.perf_counter() - start) * 1000, 2)
                return LinkCheckResult(
                    url=url,
                    status=None,
                    ok=False,
                    latency_ms=elapsed,
                    error=str(exc),
                )

    async def validate_urls(self, urls: Sequence[str]) -> list[LinkCheckResult]:
        async with aiohttp.ClientSession(timeout=self.timeout) as session:
            tasks = [self._check_one(session, u) for u in urls]
            return await asyncio.gather(*tasks)
