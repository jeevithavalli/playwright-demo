import re
from playwright.sync_api import Page,expect
def test_have_title(page:Page):
    page.goto("https://www.flipkart.com/")
    expect(page).to_have_title(re.compile("Online Shopping"))

def test_have_price(page:Page):
    page.goto("https://www.flipkart.com/doubledicestore-back-cover-apple-iphone-17/p/itm66ec977123e01?pid=ACCHDG9FV2GZGG9R&lid=LSTACCHDG9FV2GZGG9RLIYXQH&hl_lid=&marketplace=FLIPKART&fm=eyJ3dHAiOiJyZWNvIiwicHJwdCI6ImhwIiwibWlkIjoicGVyc29uYWxpc2VkUmVjb21tZW5kYXRpb24vcDJwLXNhbWUifQ%3D%3D&pageUID=1781677371865")
    expect(page.locator(".v1zwn21m.v1zwn20._1psv1zeb9._1psv1ze0")).to_be_visible()