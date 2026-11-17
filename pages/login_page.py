from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page Object encapsulating authentication UI interactions."""

    def __init__(self, page: Page):
        super().__init__(page, base_url="https://www.saucedemo.com")
        self.username_input = page.locator("[data-test='username']")
        self.password_input = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
        self.error_banner = page.locator("[data-test='error']")

    def login(self, username: str, password: str) -> None:
        self.navigate()
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def assert_error_contains(self, expected_text: str) -> None:
        expect(self.error_banner).to_be_visible()
        expect(self.error_banner).to_contain_text(expected_text)
