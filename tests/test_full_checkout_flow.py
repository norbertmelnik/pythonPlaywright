from playwright.sync_api import sync_playwright, expect
from fixtures.browser_context import browser_context
from pages.cart_page import CartPage
from pages.inventory_page import inventoryPage
from pages.checkout_step_one import CheckoutStepOnePage
from pages.login_page import loginPage
from pages.checkout_step_two import CheckoutStepTwoPage
from pages.checkout_complete import CheckoutCompletePage
import pytest

def test_e2e_checkout_flow(browser_context):
    login_page = loginPage(browser_context)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    #dodajemy elementy do koszyka
    inventory_page = inventoryPage(browser_context)
    inventory_page.assert_url_for_page()
    inventory_page.add_product_by_name("Sauce Labs Backpack")
    inventory_page.add_product_by_name("Sauce Labs Onesie")
    inventory_page.open_shopping_cart()

    #sprawdzamy dwa elementy w koszyku
    cart_page = CartPage(browser_context)
    cart_page.assert_url_for_page()
    cart_page.assert_cart_items_count(2)
    cart_page.click_checkout_button()

    # checkout step one - wypelniamy dane
    checkout_step_one_page = CheckoutStepOnePage(browser_context)
    checkout_step_one_page.assert_url_for_page()
    checkout_step_one_page.fill_your_information(
        "Norbert",
        "Melnik",
        "99999"
    )
    checkout_step_one_page.click_continute_button()

    # checkout step two - sprawdz strone i liczbe produktow
    checkout_step_two_page = CheckoutStepTwoPage(browser_context)
    checkout_step_two_page.assert_url_for_page()
    checkout_step_two_page.assert_cart_items_count(2)
    checkout_step_two_page.click_finish_button()

    #checkout complete page = sprawdz strone i tytul
    checkout_complete_page = CheckoutCompletePage(browser_context)
    checkout_complete_page.assert_url_for_page()
    checkout_complete_page.assert_complete_header_text("THANK YOU FOR YOUR ORDER")
