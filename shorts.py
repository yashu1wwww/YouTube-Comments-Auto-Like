from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress", "localhost:9222")

driver = webdriver.Chrome(options=option)

time.sleep(2)

driver.get("https://www.youtube.com/shorts/USc22MHu9cU")  # Replace with your Shorts URL

time.sleep(5)

# Click on the "Comments" button
try:
    comment_button = driver.find_element(By.CSS_SELECTOR, '#comments-button ytd-button-renderer yt-button-shape button')
    comment_button.click()
    print("Opened comments section.")
except Exception as e:
    print(f"Error opening comments: {e}")

time.sleep(4)

liked_count = 0

while True:  # Runs indefinitely until manually stopped
    like_buttons = driver.find_elements(By.XPATH, '//*[@id="like-button"]/yt-button-shape/button')

    for button in like_buttons:
        try:
            button.click()
            liked_count += 1
            print(f"Liked comment {liked_count}")
            time.sleep(random.randint(1, 3))  # Random delay
        except Exception as e:
            print(f"Error: {e}")

    # Scroll down to load more comments
    driver.execute_script("window.scrollBy(0, 500);")

    time.sleep(2)
