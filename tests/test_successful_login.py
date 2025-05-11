from playwright.sync_api import sync_playwright, expect
from fixtures.browser_context import browser_context
from pages.inventory_page import inventoryPage
from pages.login_page import loginPage


def test_successful_login(browser_context):
    login_page = loginPage(browser_context)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    inventory_page = inventoryPage(browser_context)
    inventory_page.assert_url_for_page()
