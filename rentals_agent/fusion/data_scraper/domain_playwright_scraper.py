from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/114.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 800},
            locale="en-US",
            java_script_enabled=True,
            device_scale_factor=1,
            is_mobile=False,
            has_touch=False,
        )
        page = context.new_page()
        url = "https://www.domain.com.au/rent/nsw/rosebery/"
        page.goto(url, wait_until="networkidle", timeout=90000)

        time.sleep(5)  # 等待手动操作弹窗

        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(5)

        content = page.content()
        with open("page_content.html", "w", encoding="utf-8") as f:
            f.write(content)

        print("已保存 page_content.html，你可以打开查看页面结构")

        browser.close()

if __name__ == "__main__":
    run()