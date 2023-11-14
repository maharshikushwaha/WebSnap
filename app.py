import argparse
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from PIL import Image

def capture_screenshot(url, output_path, width=None, height=None):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities['goog:loggingPrefs'] = {'browser': 'ALL'}

    driver = webdriver.Chrome(options=options, desired_capabilities=capabilities)

    try:
        driver.get(url)
        driver.maximize_window()

        if width and height:
            driver.set_window_size(width, height)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)

        screenshot_path = output_path if output_path.endswith(('.png', '.jpg', '.jpeg')) else output_path + '.png'
        driver.save_screenshot(screenshot_path)

        print(f"Screenshot saved to: {screenshot_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()

def main():
    parser = argparse.ArgumentParser(description='Webpage Screenshot Generator')
    parser.add_argument('--url', required=True, help='URL of the webpage to capture')
    parser.add_argument('--output', required=True, help='Output path for the screenshot')
    parser.add_argument('--width', type=int, help='Width of the screenshot')
    parser.add_argument('--height', type=int, help='Height of the screenshot')

    args = parser.parse_args()

    capture_screenshot(args.url, args.output, args.width, args.height)

if __name__ == "__main__":
    main()
