import pytest
from playwright.sync_api import Page

@pytest.fixture
def navigate_to_url(page: Page):
    print('Navigating to the login page')
    url = 'https://sso.teachable.com/secure/9521/identity/login/otp'
    page.goto(url)

    yield

    print('closing browser session')
    page.close()




def test_chromium_engine_m1(playwright):
    # we can use the `playwright` global fixture to access the Playwright API(pkg: pytest-playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = browser.new_page()
    page.goto("https://www.amazon.com/")


def test_chromium_engine_m2(page: Page):
    # using page fixture from Page class
    page.goto("https://www.amazon.com/")


def test_login(navigate_to_url, page: Page, ):
    url = 'https://sso.teachable.com/secure/9521/identity/login/otp'
    username = 'akash'
    password = 'akash123@#'

    print('clicking on the password reset link')
    passw_reset_link = page.locator("xpath=//a[@id='login-with-password-link']")
    passw_reset_link.click()

    print(f'Entering username: {username}')
    username_input = page.get_by_label('Email').fill(username)

    print(f'Entering password: {password}')
    password_input = page.get_by_label('Password').fill(password)
