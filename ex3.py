import pytest
from playwright.sync_api import Page,expect
@pytest.fixture(scope="function",autouse=True)
def open_page(page:Page):
    print("before the test runs")
    page.goto("https://www.flipkart.com/")
    yield

    print("After the test runs")

def test_main(page: Page):
    expect(page).to_have_url("https://www.flipkart.com/")

