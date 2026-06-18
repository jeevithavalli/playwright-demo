from playwright.sync_api import sync_playwright
import time

with (sync_playwright() as pw):
    browser=pw.chromium.launch()
    page=browser.new_page()
    page.goto("https://www.flipkart.com/")
    print(page.get_by_role("link").all_inner_texts())
    print(page.get_by_role("button").all_text_contents())
    browser.close()
