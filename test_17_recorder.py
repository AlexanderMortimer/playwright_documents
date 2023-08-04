from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://google.com/")

    # ---------------------
    context.close()
    browser.close()


# with sync_playwright() as playwright:
#     run(playwright)
