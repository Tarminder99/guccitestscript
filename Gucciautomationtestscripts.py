from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback

# Initialize the Chrome driver
driver = webdriver.Chrome()

try:
    # Open the Gucci homepage
    driver.get('https://www.gucci.com/ca/en/')

    # Wait for the cookies consent prompt and handle it using the specific ID
    try:
        accept_cookies_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))
        )
        accept_cookies_button.click()
        print("Cookies consent accepted.")
    except Exception as e:
        print("No cookies consent prompt found or handled:", e)

    # Handle the additional popup button
    try:
        close_popup_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'bx-close-inside-1753406'))
        )
        close_popup_button.click()
        print("Popup closed successfully.")
    except Exception as e:
        print("No additional popup found or handled:", e)

    # Verify the homepage is loaded completely
    homepage_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, 'body'))
    )
    print("Gucci homepage loaded successfully.")

    # Print the page source to check for search button locator
    page_source = driver.page_source
    if 'data-testid="search-spa-driven-search"' in page_source:
        print("Search button found in the page source.")
    else:
        print("Search button not found in the page source.")

    # Use JavaScript as a fallback to click the search button
    try:
        search_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="search-spa-driven-search"]'))
        )
        driver.execute_script("arguments[0].click();", search_button)
        print("Search button clicked using JavaScript.")
    except Exception as e:
        print("Search button not found or clickable:", e)

    # Wait for the search bar to appear and enter a product name
    try:
        search_bar = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, 'search-input'))
        )
        search_bar.send_keys('bag')
        search_bar.send_keys(Keys.RETURN)
        print("Product name 'bag' entered in the search bar.")
    except Exception as e:
        print("Search bar not found or not interactable:", e)

    # Validate the search results page and wait for products to display
    try:
        products_container = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.product-tiles, div.product-grid'))
        )
        print("Product search completed successfully and products are displayed.")
    except Exception as e:
        print("Search results page validation failed or products not displayed:", e)
        # Log the page source for debugging
        with open("page_source.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        traceback.print_exc()

    # Open the Gucci access view page
    driver.get("https://www.gucci.com/ca/en/access/view?stateToken=C05C1082E05C16D87CAC7597B3162D38&nonce=BAB45876544B1071B0F78890D6DDF6E1&cart=471408ab-36fc-41b1-a0c2-5c13b1e66fce&returnURI=%2F&pkceConfig=eyJkaXNwbGF5IjoiZW1iZWRkZWQiLCJyZW1lbWJlck1lRW5hYmxlZCI6dHJ1ZSwiY2xpZW50SWQiOiIwb2EydHh2c29ySlZDS0ZBcTQxNyIsImNvZGVDaGFsbGVuZ2UiOiJCZlFxTFhSVk9ZSVBfbVFyd1FXTlJka0pMVlVQY3lZTmtHd2lyNFE1aGpZIiwicmVkaXJlY3RVcmkiOiJodHRwczovL3d3dy5ndWNjaS5jb20vYWNjZXNzL2F1dGhvcml6YXRpb24ifQ%3D%3D")

    # Wait for the cookies consent prompt and handle it using the specific ID
    try:
        accept_cookies_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))
        )
        accept_cookies_button.click()
        print("Cookies consent accepted.")
    except Exception as e:
        print("No cookies consent prompt found or handled:", e)

    # Wait for the email input field to appear and enter the email
    email_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "email-input"))
    )
    email_input.send_keys("tarminder4999@gmail.com")
    print("Email entered successfully.")

    # Wait for the confirm button to be clickable and click it
    confirm_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "confirm-button"))
    )
    confirm_button.click()
    print("Confirm button clicked successfully.")

    # Wait for some time after clicking the confirm button to ensure next steps can be performed
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'body'))
    )
    print("Waited for the page to load after clicking the confirm button.")

except Exception as e:
    print(f"An error occurred: {e}")
    traceback.print_exc()

finally:
    # Close the driver
    driver.quit()
