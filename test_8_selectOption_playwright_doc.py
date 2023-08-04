import re
from playwright.sync_api import Playwright, expect

def test_checkbox(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False,slow_mo=1000)
    context = browser.new_context()
    

    page = context.new_page()

    page.goto("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select",wait_until='domcontentloaded')
    # page.get_by_role("button", name="Run ❯").click()
    scale_chckBox = page.frame_locator("iframe[name=\"iframeResult\"]").get_by_label("Choose a car:")
    scale_chckBox.select_option('Saab')

    








