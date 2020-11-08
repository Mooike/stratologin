import twill.commands as twill
from selenium import webdriver
import time


#get username 
with open("creds.txt", "r") as text_file:
    data = text_file.readlines()

print("username: ", data[0])
print("password: ", data[1])

request = "https://www.strato.de/apps/CustomerService#/skl"
browser = webdriver.Chrome(executable_path=r"C:\Users\mikel\Downloads\chromedriver_win32 (1)\chromedriver.exe")
browser.get(request)
time.sleep(3)
username = browser.find_element_by_id("loginLP")
username.send_keys("test")

print("logged in!")