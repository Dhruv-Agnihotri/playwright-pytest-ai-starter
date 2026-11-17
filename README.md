# Playwright + PyTest Automation Starter (POM & Async Validation)

![CI Status](https://img.shields.io/badge/CI-GitHub_Actions-2088FF?logo=github-actions&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-PyTest-45ba4b?logo=playwright&logoColor=white)

A production-ready **Page Object Model (POM)** UI & API test automation starter built with **Python, Playwright, PyTest, and `asyncio`**. Designed for deterministic execution, automatic failure screenshots, concurrent URL health validation, and CI/CD integration.

## Architecture Overview

```text
playwright-pytest-ai-starter/
├── .github/workflows/ci.yml     # Automated GitHub Actions test runner
├── pages/                       # Page Object Model (UI locators & actions)
│   ├── base_page.py             # Shared navigation, wait, and screenshot helpers
│   └── login_page.py            # Encapsulated login flow & assertions
├── utils/
│   └── async_link_validator.py  # High-concurrency asyncio URL & status validator
├── tests/
│   ├── conftest.py              # PyTest fixtures (browser context, failure capture)
│   ├── test_login_pom.py        # End-to-end POM functional tests
│   └── test_async_links.py      # Concurrent link validation tests
├── pytest.ini                   # PyTest markers, CLI defaults, and HTML reporting
└── requirements.txt
```

## Key Engineering Patterns
- **Page Object Model (POM):** Isolates DOM selectors from test assertions so UI changes require updates in a single class rather than across test suites.
- **PyTest Fixture Lifecycle:** Function-scoped isolated browser contexts with automatic screenshot capture on test failure (`reports/screenshots/`).
- **Async I/O Concurrency:** Uses `asyncio` with semaphore-bounded concurrency to validate large URL batches without thread overhead or rate-limit spikes.

## Quickstart

```bash
# 1. Create virtual environment & install dependencies
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium

# 2. Run the full suite with HTML report generation
pytest
```
