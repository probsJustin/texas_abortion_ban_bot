from selenium import webdriver


browser = webdriver.Chrome('chromedriver')
for i in range(1):
    matched_elements = browser.get("https://www.google.com/")