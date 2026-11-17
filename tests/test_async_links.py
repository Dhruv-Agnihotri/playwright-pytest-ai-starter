import asyncio
import pytest
from utils.async_link_validator import AsyncLinkValidator


@pytest.mark.regression
def test_concurrent_url_validation():
    urls = [
        "https://www.saucedemo.com",
        "https://example.com",
        "https://httpbin.org/status/200",
        "https://httpbin.org/status/404",
    ]
    validator = AsyncLinkValidator(max_concurrency=4, timeout_sec=10.0)
    results = asyncio.run(validator.validate_urls(urls))

    by_url = {r.url: r for r in results}
    assert by_url["https://example.com"].ok is True
    assert by_url["https://httpbin.org/status/404"].status == 404
    assert by_url["https://httpbin.org/status/404"].ok is False
