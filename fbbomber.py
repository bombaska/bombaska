from selenium import webdriver
from time import sleep
import pyautogui as pg
browser = webdriver.Chrome("chromedriver.exe")
phoneNumber = "687962598"
#number = str(number)
countryCode = "+380"
#countryCode = str(countryCode)
fullnumber = str(countryCode) + str(phoneNumber)
def facebook(fullNumber):
    browser.get("https://www.facebook.com/login/identify/?str=recover")
    number = browser.find_element_by_xpath('//*[@id="identify_email"]')
    did_submit = browser.find_element_by_name('did_submit')
    #fullNumber =str(countryCode) + str(number)
    #fullNumber = str(fullNumber)
    number.send_keys(fullNumber)
    did_submit.click()
    sleep(3)
    submit = browser.find_element_by_xpath('//*[@id="initiate_interstitial"]/div[3]/div/div[1]/button')
    submit.click()
    sleep(5)
def privat(num):
    browser.get("https://www.privat24.ua/")
    sleep(10)
    nextTo = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/form/div[2]/div/div/div[2]/div[3]/div[1]/input')
    #did_submit = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/form/div[3]/div/button/div')
    nextTo.send_keys(str(num))
    #did_submit.click()
    sleep(3)
    forget = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[3]/div[2]/a')
    forget.click()
    sleep(5)
    another = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[5]/a')
    another.click()
    sleep(30)
    # anotherCall = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[5]/a')
    # sleep()
def tinder(num):
    browser.get("https://tinder.com/")
    sleep(1)
    register = browser.find_element_by_xpath('//*[@id="t-1801132545"]/div/div[1]/div/main/div[1]/div/div/div/div/div[3]/div/div[2]/button')
    register.click()
    sleep(1)
    try:
        another = browser.find_element_by_xpath('//*[@id="t--239073259"]/div/div/div[1]/div/div[3]/span/button')
        another.click()
        sleep(1)
    except:
        usingNumber = browser.find_element_by_xpath('//*[@id="t--239073259"]/div/div/div[1]/div/div[3]/span/div[3]/button')
        usingNumber.click()
        sleep(1)
        inputNum = browser.find_element_by_xpath('//*[@id="t--239073259"]/div/div/div[1]/div[2]/div/input')
        inputNum.send_keys(str(num))
        nextTo = browser.find_element_by_xpath('//*[@id="t--239073259"]/div/div/div[1]/button')
        nextTo.click()
        sleep(2)
        newTry = browser.find_element_by_xpath('//*[@id="t--239073259"]/div/div/div[1]/div[3]/button')
        newTry.click()
        sleep(1)
def sweet_tv (num):
    browser.get("https://sweet.tv/ru")
    sleep(1)
    logIn = browser.find_element_by_xpath('//*[@id="tabs"]/div/div/div[2]/div/div[3]')
    logIn.click()
    sleep(1)
    input = browser.find_element_by_xpath('//*[@id="m--login"]/div/div/div[2]/div[1]/div[1]/form/div[1]/input')
    input.click()
    input.send_keys(str(num))
    sleep(1)
    sendSMS = browser.find_element_by_xpath('//*[@id="m--login"]/div/div/div[2]/div[1]/div[1]/form/button')
    sendSMS.click()
    sleep(1)
    againSend = browser.find_element_by_xpath('//*[@id="inputSMS"]/div[2]/button')
    againSend.click()
def oll_tv(num):
    browser.get("https://oll.tv/ru/")
    sleep(0.5)
    log_in = browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div')
    log_in.click()
    sleep(0.1)
    reg_button = browser.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div[2]')
    reg_button.click()
    num_input = browser.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div[3]/input')
    num_input.click()
    num_input.send_keys(str(num))
    email_input = browser.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div[4]/input')
    email_input.click()
    email = 'cloud.mad74060@gmail.com'
    email_input.send_keys(str(email))
    continue_button = browser.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div[7]/div[1]')
    continue_button.click()
def cookie_clear():
    browser.get("chrome://settings/clearBrowserData")
    sleep(1)
    pg.moveTo(684,671,0.5)
    sleep(0.5)
    pg.click()
    # print(pg.position())
def twitch(num):
    browser.get("https://www.twitch.tv/user/account-recovery")
    number_input = browser.find_element_by_xpath('//*[@id="account-recovery-label"]')
    number_input.send_keys(str(num))
    button = browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div[3]/button')
    button.click()
    comfirm_button = browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/div[3]/div[1]/button')
    comfirm_button.click()
def uklon(num):
    browser.get("https://uklon.com.ua/ru/online-order-ru")
    sleep(3)
    pg.scroll(-400)
    start_point = browser.find_element_by_xpath('/html/body/ukl-application/div/ukl-home-page/div/section[2]/div[1]')
    start_point.click()
def kyivstar(num):
    browser.get("https://account.kyivstar.ua/cas/login")
    # input_number = browser.find_element_by_xpath('//*[@id="section-left"]/section[2]/div/div/div[2]/input')
    # input_number.click()
    # input_number.send_keys(str(num))
    # send_button = browser.find_element_by_xpath('//*[@id="section-left"]/section[2]/div/div/div[4]/div/div/button')
    # send_button.click()
    sleep(1)
    pg.typewrite(num)
    sleep(0.3)
    pg.press('enter')

# kyivstar(phoneNumber)
# cookie_clear()
# uklon(phoneNumber) ---
# twitch(fullnumber) # fullnumber or phoneNumber (more tests)
# sweet_tv(phoneNumber)
# oll_tv(fullnumber) # check more (cookies clear didn't help)
# facebook(fullnumber)
tinder(phoneNumber)
# privat()

sleep(0.5)

#browser.find_element_by_xpath
#browser.find_element_by_xpath
#browser.find_element_by_xpath
#browser.find_element_by_xpath
#browser.find_element_by_xpath
#browser.find_element_by_xpath
#browser.find_element_by_xpath
#browser.find_element_by_xpath