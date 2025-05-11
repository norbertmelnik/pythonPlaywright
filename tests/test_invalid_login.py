from playwright.sync_api import sync_playwright, expect
from fixtures.browser_context import browser_context
from pages import inventory_page
from pages.login_page import loginPage
import pytest

@pytest.mark.parametrize("username, password, message", [
    ("", "", "Username is required"),
    ("standard_user", "", "Password is required"),
    ("standard_user", "wrong_password", "Username and password do not match any user in this service")
])

def test_invalid_login(browser_context, username, password, message):
    login_page = loginPage(browser_context)
    login_page.load()
    login_page.login(username, password)
    login_page.assert_error_message(f"Epic sadface: {message}")
    login_page.assert_url_for_page()
