from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page(no_viewport=True)
    page.goto("https://devexpress.github.io/testcafe/example/")
    expect(page).to_have_url("https://devexpress.github.io/testcafe/example/", timeout=20000)
    your_name ="Lilac Utz"
    fill_name = page.get_by_test_id('name-input')
    fill_name.highlight()
    fill_name.press_sequentially(your_name, delay=500)

    remote_check = page.get_by_test_id('remote-testing-checkbox')
    remote_check.check()

    choose_os = page.get_by_test_id('windows-radio')
    choose_os.click()

    cafe_check = page.get_by_test_id('tried-testcafe-checkbox')
    cafe_check.highlight()
    cafe_check.check()

    comment_area = page.get_by_test_id('comments-area')
    comment_area.fill("hello you")
    page.screenshot(path="../../full_screenshot.jpg", full_page=True)
    submit_button = page.get_by_test_id('submit-button')
    submit_button.click()

    thank_header = page.get_by_test_id('thank-you-header')
    expect(thank_header).to_contain_text(your_name)
    page.screenshot(path="../../full_screenshot.jpg", full_page=True)


    browser.close()


