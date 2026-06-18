from playwright.sync_api import sync_playwright
import time

with (sync_playwright() as pw):
    browser=pw.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://www.amazon.in/")
    page.get_by_placeholder("Search Amazon.in").click()
    time.sleep(3)
    page.get_by_placeholder("Search Amazon.in").fill("Mobile")
    time.sleep(3)
    page.locator("#nav-search-submit-button").click()
    time.sleep(3)
