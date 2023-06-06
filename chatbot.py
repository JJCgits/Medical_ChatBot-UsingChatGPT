
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time 

LoginButton = '//*[@id="__next"]/div[1]/div[1]/div[4]/button[1]'
googleLoginButton = '/html/body/div/main/section/div/div/div/div[3]/form[2]/button'
googleEmail = '//*[@id="identifierId"]'
googlePassword = '//*[@id="password"]/div[1]/div/div[1]/input'
nextButton = '//*[@id="identifierNext"]/div/button'
pNextButton = '//*[@id="passwordNext"]/div/button'
myEmail = ""
password = ""

next = '//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button/div'
chatNextButton = '//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button'
chatNextButton2 = '//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button[2]'

chatGPT = '//*[@id="__next"]/div[2]/div[2]/main/div[2]/form/div/div[2]/textarea'
sendButton = '//*[@id="__next"]/div[2]/div[2]/main/div[2]/form/div/div[2]/button'

# Setting up the chromedriver
driver = uc.Chrome()
driver.get("https://chat.openai.com/auth/login")

#Opening up chatGPT using Chrome and chromedriver

def readyUP():

    time.sleep(5)

    LButton = driver.find_element(By.XPATH, LoginButton)
    LButton.click()

    time.sleep(3)

    GButton = driver.find_element(By.XPATH, googleLoginButton)
    GButton.click()

    time.sleep(5)

    gmail = driver.find_element(By.XPATH, googleEmail)
    gmail.send_keys(myEmail)

    time.sleep(1)

    nButton = driver.find_element(By.XPATH, nextButton)
    nButton.click()

    time.sleep(4)

    gpassword = driver.find_element(By.XPATH, googlePassword)
    gpassword.send_keys(password)

    time.sleep(1)

    pnButton = driver.find_element(By.XPATH, pNextButton)
    pnButton.click()


    time.sleep(1)

    chatNext = driver.find_element(By.XPATH, chatNextButton)
    chatNext.click()

    time.sleep(1)

    chatNext = driver.find_element(By.XPATH, chatNextButton2)
    chatNext.click()


    time.sleep(1)

    chatNext = driver.find_element(By.XPATH, chatNextButton2)
    chatNext.click()


    time.sleep(2)

    gpt = driver.find_element(By.XPATH, chatGPT)
    gpt.send_keys("Hello, all the questions I'm going to ask you are ging to be medically related, if they are not, answer with This is not a medical question")

    sendButtonR = driver.find_element(By.XPATH, sendButton)
    sendButtonR.click()

def chatBot():
    chat = input("What medical questions do you have?\n")

    gpt = driver.find_element(By.XPATH, chatGPT)
    gpt.send_keys(chat)

    sendButtonR = driver.find_element(By.XPATH, sendButton)
    sendButtonR.click()

if __name__ == '__main__':
    readyUP()
