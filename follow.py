from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "E:\Python\Insta\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://instagram.com")


# cookie button
cookie_accept = driver.find_element_by_xpath("/html/body/div[4]/div/div/button[1]")
cookie_accept.click()


input()
driver.quit()
# cookie button "aOOlW  bIiDR  "
