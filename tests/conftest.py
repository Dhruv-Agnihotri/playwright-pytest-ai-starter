from pathlib import Path
import pytest


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


@pytest.fixture(autouse=True)
def capture_screenshot_on_failure(request):
    yield
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        page = request.node.funcargs.get("page")
        if page:
            out_dir = Path("reports/screenshots")
            out_dir.mkdir(parents=True, exist_ok=True)
            safe_name = request.node.name.replace("[", "_").replace("]", "_")
            page.screenshot(path=str(out_dir / f"FAIL_{safe_name}.png"), full_page=True)
