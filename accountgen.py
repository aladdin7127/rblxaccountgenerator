from selenium import webdriver
from selenium.webdriver import common
from selenium.webdriver.support import ui
import random, string, os, time

chars = string.ascii_uppercase + string.ascii_lowercase + string.digits

def randomstr():
    return "".join(random.choice(chars) for _ in range(20))

driver = webdriver.Chrome()
driver.get("https://www.roblox.com/")

try:
    cookiebanner = driver.find_element(common.by.By.XPATH, "//*[@id=\"cookie-banner-wrapper\"]/div[1]/div[2]/div/div/button[2]")
    cookiebanner.click()
except:
    print("failed to click cookie banner")

day = driver.find_element(common.by.By.XPATH, "//*[@id=\"DayDropdown\"]")
month = driver.find_element(common.by.By.XPATH, "//*[@id=\"MonthDropdown\"]")
year = driver.find_element(common.by.By.XPATH, "//*[@id=\"YearDropdown\"]")

ui.Select(day).select_by_index(random.randint(1, 31))
ui.Select(month).select_by_index(random.randint(1, 12))
ui.Select(year).select_by_index(random.randint(24, 89))

username = driver.find_element(common.by.By.XPATH, "//*[@id=\"signup-username\"]")
password = driver.find_element(common.by.By.XPATH, "//*[@id=\"signup-password\"]")
inputvalid = driver.find_element(common.by.By.XPATH, "//*[@id=\"signup-usernameInputValidation\"]")

r_username = randomstr()
r_password = randomstr()

username.send_keys(r_username)
time.sleep(0.5)
while (inputvalid.text == "Username not appropriate for Roblox."):
    r_username = randomstr()
    username.send_keys(common.keys.Keys.CONTROL, "a")
    username.send_keys(r_username)
    time.sleep(1)

password.send_keys(r_password)
time.sleep(1)

signup = driver.find_element(common.by.By.XPATH, "//*[@id=\"signup-button\"]")
signup.click()

generated = os.path.join(os.getcwd(), "generated")
data = ""

if (not os.path.exist(generated + ".txt")):
    with open(generated, "w") as file:
        file.close()

# stupid method i know ¯\_(ツ)_/¯

with open(generated + ".txt", "r") as file:
    data = file.read()
    file.close()

with open(generated + ".txt", "w") as file:
    file.write(data + "\nusername: " + r_username + "\npassword: " + r_password + "\n\n")
    file.close()

    print(r_username + ":" + r_password)
    
driver.close()
