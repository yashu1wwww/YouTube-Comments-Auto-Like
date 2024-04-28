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

driver.get("https://www.youtube.com/shorts/USc22MHu9cU") #replace with your shorts url

time.sleep(5)

driver.find_element_by_css_selector('#comments-button > ytd-button-renderer > yt-button-shape > label > button > yt-touch-feedback-shape > div > div.yt-spec-touch-feedback-shape__fill').click() #click on youtube short cmt box

time.sleep(4)

like_buttons = driver.find_elements_by_xpath('//*[@id="like-button"]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]')

# Click on each like button
for button in like_buttons:
    button.click()

time.sleep(30)
