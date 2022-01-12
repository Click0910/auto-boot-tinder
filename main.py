from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

EMAIL = "nicolas1009@live.com"
PASSWORD = "Nicoyclaudia4-3v3r"

URL = "https://tinder.com/"

chrome_driver_path = r"C:\Users\Nicolas\Desktop\Programacion\Development_tools\chromedriver.exe"


driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url=URL)

time.sleep(4)

logging = driver.find_element_by_css_selector(css_selector=".StyledButton")
logging.click()

time.sleep(1)

logging_with_facebook = driver.find_element_by_xpath(xpath='//*[@id="s-1005392171"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
logging_with_facebook.click()

time.sleep(3)

# Switch Window
first_window = driver.window_handles[0]
fb_window = driver.window_handles[1]
driver.switch_to_window(fb_window)

email = driver.find_element_by_xpath(xpath='//*[@id="email"]')
email.send_keys(EMAIL)
password = driver.find_element_by_name(name="pass")
password.send_keys(PASSWORD)
login_button = driver.find_element_by_name(name="login")
login_button.click()

driver.switch_to_window(first_window)

time.sleep(5)
allow_location = driver.find_element_by_xpath(xpath='//*[@id="s-1005392171"]/div/div/div/div/div[3]/button[1]')
allow_location.click()

time.sleep(5)
dismiss_notifications = driver.find_element_by_xpath(xpath='//*[@id="s-1005392171"]/div/div/div/div/div[3]/button[2]')
dismiss_notifications.click()

time.sleep(4)

cookies = driver.find_element_by_xpath(xpath='//*[@id="s722988905"]/div/div[2]/div/div/div[1]/button')
cookies.click()

time.sleep(5)

for n in range(100):

    #Add a 1 second delay between likes.
    time.sleep(1)

    try:
        print("called")
        like_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.XPATH,
        '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button'))

        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)
