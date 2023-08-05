from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress","localhost:9222")

driver = webdriver.Chrome(options=option)

time.sleep(2)

driver.get("https://youtu.be/HUbrGucvxEA") #replace with your url

time.sleep(7)

driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button').click()

time.sleep(1)

driver.execute_script("window.scrollTo(0, 600);")

time.sleep(3)

like_button_xpath = '//*[@id="like-button"]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]'

like_buttons = driver.find_elements_by_xpath('//*[@id="like-button"]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]')

# Click on each like button
for button in like_buttons:
    button.click()

time.sleep(50)
