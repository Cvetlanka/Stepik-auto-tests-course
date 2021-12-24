import time
import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get(" http://suninjuly.github.io/explicit_wait2.html")

 #   browser.implicitly_wait(5)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.XPATH, ("//*[@id='price']")), "$100"))

    browser.find_element_by_xpath("//*[@id='book']").click()

    x = int(browser.find_element_by_xpath("//*[@id='input_value']").text)
    func = math.log(math.fabs((12 * math.sin(x))), math.e)

    btn = browser.find_element_by_xpath("//*[@id='solve']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", btn)

    browser.find_element_by_xpath("//*[@id='answer']").send_keys(str(func))
    btn.click()

    alert_text = browser.switch_to.alert.text
    pyperclip.copy(alert_text.split(': ')[-1])

finally:
    time.sleep(10)
    browser.quit()