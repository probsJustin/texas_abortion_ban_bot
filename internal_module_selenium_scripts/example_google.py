from selenium import webdriver


def run(directory):
    browser = webdriver.Chrome(directory)
    for i in range(1):
        matched_elements = browser.get("https://www.google.com/")
    browser.close()
