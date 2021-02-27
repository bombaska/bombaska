from selenium import webdriver
import time
browser = webdriver.Chrome('chromedriver.exe')
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
        time.sleep(3)
        submit = browser.find_element_by_xpath('//*[@id="initiate_interstitial"]/div[3]/div/div[1]/button')
        submit.click()
        time.sleep(5)
def privat(num):
        browser.get("https://www.privat24.ua/")
        time.sleep(10)
        nextTo = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/form/div[2]/div/div/div[2]/div[3]/div[1]/input')
        #did_submit = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/form/div[3]/div/button/div')
        nextTo.send_keys(str(num))
        #did_submit.click()
        time.sleep(3)
        forget = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[3]/div[2]/a')
        submit.click()
        time.sleep(5)
        another = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[5]/a')
        another.click()
        time.sleep(30)
        anotherCall = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[5]/a')
        time.sleep()
def tinder(num):
    browser.get("https://tinder.com/")
    time.sleep(1)
    register = browser.find_element_by_xpath('//*[@id="t-1801132545"]/div/div[1]/div/main/div[1]/div/div/div/div/div[3]/div/div[2]/button')
    register.click()
    time.sleep(1)
    another = browser.find_element_by_xpath('//*[@id="t--239073259"]/div/div/div[1]/div/div[3]/span/button')
    another.click()
    time.sleep(1)
    usingNumber = browser.find_element_by_xpath('//*[@id="t--239073259"]/div/div/div[1]/div/div[3]/span/div[3]/button')
    usingNumber.click()
    time.sleep(1)
    inputNum = browser.find_element_by_xpath('//*[@id="t--239073259"]/div/div/div[1]/div[2]/div/input')
    inputNum.send_keys(str(num))
    nextTo = browser.find_element_by_xpath('//*[@id="t--239073259"]/div/div/div[1]/button')
    nextTo.click()
    time.sleep(2)
    newTry = browser.find_element_by_xpath('//*[@id="t--239073259"]/div/div/div[1]/div[3]/button')
    newTry.click()
    time.sleep(1)
def sweet_tv (num):
    browser.get("https://sweet.tv/ru")
    time.sleep(1)
    logIn = browser.find_element_by_xpath('//*[@id="tabs"]/div/div/div[2]/div/div[3]')
    logIn.click()
    time.sleep(1)
    input = browser.find_element_by_xpath('//*[@id="m--login"]/div/div/div[2]/div[1]/div[1]/form/div[1]/input')
    input.click()
    input.send_keys(str(num))
    time.sleep(1)
    sendSMS = browser.find_element_by_xpath('//*[@id="m--login"]/div/div/div[2]/div[1]/div[1]/form/button')
    sendSMS.click()
    time.sleep(1)
    againSend = browser.find_element_by_xpath('//*[@id="inputSMS"]/div[2]/button')
    againSend.click()
sweet_tv(phoneNumber)
#facebook(fullnumber)
#privat()
#tinder(phoneNumber)
#browser.find_element_by_xpath
#browser.find_element_by_xpath
#browser.find_element_by_xpath
#browser.find_element_by_xpath
#browser.find_element_by_xpath
#browser.find_element_by_xpath
#browser.find_element_by_xpath
#browser.find_element_by_xpath
#browser.find_element_by_xpath
#browser.find_element_by_xpath
#
#