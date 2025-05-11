from playwright.sync_api import sync_playwright, expect
from fixtures.browser_context import browser_context
from pages.inventory_page import inventoryPage
from pages.login_page import loginPage
import pytest

def test_inventory_item_count(browser_context):
    login_page = loginPage(browser_context)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")


    inventory_page = inventoryPage(browser_context)
    inventory_page.assert_url_for_page()
    inventory_page.assert_inventory_items_count(6)

def test_inventory_sorting(browser_context):
    #login
    login_page = loginPage(browser_context)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    #check if page displayed
    inventory_page = inventoryPage(browser_context)
    inventory_page.assert_url_for_page()

    #sort inventory z-a
    inventory_page.sort_by("za")
    inventory_page.assert_sorted_z_to_a()
    inventory_page.sort_by("az")
    inventory_page.assert_sorted_a_to_z()
    # check if sorted
    #sort a-z
    # check if sorted
