from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys


def run():
    driver = webdriver.Chrome()
    driver.get('https://www.instagram.com/')
    email = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
    email.send_keys('its_the_alireza', Keys.RETURN)
    password = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
    password.send_keys('alireza_m2003', Keys.RETURN)

    sleep(25)


if __name__ == "__main__":
    run()
