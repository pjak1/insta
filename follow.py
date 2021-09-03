from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

PATH = "E:\Python\Insta\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://instagram.com")
accounts_info = []
# cookie button
try:
    cookie_accept = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/button[1]")))
    cookie_accept.click()
except:
    print("Došlo k chybě")
    driver.quit()

# Prihlaseni
sleep(3)
username = input("Zadej uživatelské jméno tvého účtu: ")
passwd = input("Zadej heslo ke tvému účtu: ")
try:
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")))
except:
    print("Došlo k chybě")
    driver.quit()
try:
    passwd_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")))
except:
    print("Došlo k chybě")
    driver.quit()

username_input.send_keys(username)
passwd_input.send_keys(passwd)

try:
    login = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='loginForm']/div/div[3]/button")))
    login.click()
except:
    print("Došlo k chybě")
    driver.quit()

# ulozit login info button
try:
    save_info = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='react-root']/section/main/div/div/div/section/div/button")))
    save_info.click()
except:
    print("Došlo k chybě")
    driver.quit()

# ted nezobrazovat upozorneni button
try:
    notifications = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div/div[3]/button[2]")))
    notifications.click()
except:
    print("Došlo k chybě")
    driver.quit()

target = input("Zadej cílový účet: ")

# vyhledat cílový účet
try:
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")))
    search.send_keys(target)
    sleep(1)
    search.send_keys(Keys.RETURN)
    sleep(1)
    search.send_keys(Keys.RETURN)
except:
    print("Došlo k chybě")
    driver.quit()

# zobrazit seznam účtů, které sledují cílový účet
followers = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")))
followers_count = followers.text.strip("Sledující")
followers_count = followers_count.split("(")[1]
followers_count = followers_count.split(")")[0]
followers_count = int(followers_count)
print(followers_count)
followers.click()
followers_div = WebDriverWait(driver, 100).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div/div/div[2]")))
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_div)
accounts = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, "/html/body/div[6]/div/div/div[2]/ul/div/li[1]/div/div[1]/div[2]/div[1]/span/a")))
for account in accounts:
    print(account.text)


input()
driver.quit()
