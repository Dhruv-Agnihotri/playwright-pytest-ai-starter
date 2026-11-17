import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


@pytest.mark.smoke
def test_valid_user_login(page: Page):
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


@pytest.mark.regression
def test_locked_out_user_shows_error(page: Page):
    login_page = LoginPage(page)
    login_page.login("locked_out_user", "secret_sauce")
    login_page.assert_error_contains("Sorry, this user has been locked out")
