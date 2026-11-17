from pathlib import Path
from playwright.sync_api import Page


class BasePage:
    """Base Page Object providing common navigation, waiting, and evidence capture."""

    def __init__(self, page: Page, base_url: str = ""):
        self.page = page
        self.base_url = base_url.rstrip("/")

    def navigate(self, path: str = "") -> None:
        target = f"{self.base_url}/{path.lstrip('/')}" if path else self.base_url
        self.page.goto(target, wait_until="domcontentloaded")

    def get_title(self) -> str:
        return self.page.title()

    def capture_evidence(self, filename: str) -> Path:
        out_dir = Path("reports/screenshots")
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / filename
        self.page.screenshot(path=str(out_path), full_page=True)
        return out_path
