import os

from playwright.sync_api import Page, expect

BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:8000")


def test_home_page_is_ready(page: Page):
    page.goto(BASE_URL)
    expect(page).to_have_title("QA Automation Lab")
    expect(page.locator("h1")).to_have_text("QA Automation Lab")
    expect(page.locator("#status")).to_have_text("Application ready")


def test_successful_login_flow(page: Page):
    page.goto(BASE_URL)
    page.locator("#username").fill("tester")
    page.locator("#password").fill("qa1234")
    page.locator("#login-button").click()
    expect(page.locator("#result")).to_have_text("Login successful")


def test_invalid_login_flow(page: Page):
    page.goto(BASE_URL)
    page.locator("#username").fill("tester")
    page.locator("#password").fill("wrong")
    page.locator("#login-button").click()
    expect(page.locator("#result")).to_have_text("Login failed")
