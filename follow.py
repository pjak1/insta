from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import random

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


def Login():
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


def Search():
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


def FollowUnfollow(mode):
    try:
        followers = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")))
        followers_count = followers.text.strip("Sledující")
        followers_count = followers_count.split("(")[1]
        followers_count = followers_count.split(")")[0]
        followers_count = int(followers_count)
        print("Počet followeru: ", followers_count)
        followers.click()
        followers_div = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div/div/div[2]")))
        print("\n")
        for i in range(followers_count // 8):
            driver.execute_script('''
        var fDialog = document.querySelector('div[role="dialog"] .isgrP');
        fDialog.scrollTop = fDialog.scrollHeight''')
            b = "Počet scrollu:{}/{}".format(i, followers_count // 8)
            print(b, end="\r")
            sleep(2)
        for i in range(1, followers_count):
            follow_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div/div/div[2]/ul/div/li[{}]/div/div[2]/button".format(i))))
            if follow_button.text == "Sledování" and mode == "1":
                follow_button.click()
                sleep(2)
                print("Follow")
                if random.randint(1, 100) < 25:
                    sleep(4)
            elif follow_button.text == "Sleduji" and mode == "2" or follow_button.text == "Vyžádáno" and mode == "2":
                follow_button.click()
                unfollow_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[7]/div/div/div/div[3]/button[1]")))
                unfollow_button.click()
                sleep(2)
                print("Unfollow")
                if random.randint(1, 100) < 25:
                    sleep(4)
    except:
        pass


mode = input("Zadej 1 pro follow nebo 2 pro unfollow: ")
Login()
Search()
FollowUnfollow(mode)
input("Hotovo! Stiskni enter pro ukončení")
driver.quit()
