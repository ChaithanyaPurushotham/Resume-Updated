from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
user = "chaithanyapl57@gmail.com"
pwd = "Iloveu5@amma"
driver = webdriver.Chrome(executable_path=r"D:\\New folder\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.naukri.com/")

print("Page title =",driver.title)

elem = driver.find_element_by_id("login_Layer")
elem.click()
elem = driver.find_element_by_xpath("//*[@id='eRowNew']/div/input")
elem.send_keys(user)
elem = driver.find_element_by_id("pLogin")
elem.send_keys(pwd)
elem = driver.find_element_by_xpath("//*[@value='Login']")
elem.click()
'''elem = driver.find_element_by_id("usernameField")
elem.send_keys(user)
elem = driver.find_element_by_id("passwordField")
elem.send_keys(pwd)
elem = driver.find_element_by_xpath("//*[@class='g-recaptcha']/following-sibling::button")
elem.click()'''
elem = driver.find_element_by_xpath("//*[@class='mb10']/a")
elem.click()
filepath = "C://Users//ganesh//Documents//chaithu2019_17-Mar-19_21_08_16.doc"
driver.find_element_by_xpath("//*[@class='uploadContainer']/input").send_keys(filepath)
driver.find_element_by_xpath('//html/body/button').click()