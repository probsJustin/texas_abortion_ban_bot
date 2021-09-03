from selenium import webdriver


def run():
    '''
    Generate a end point at webhook and check the request
    going to use https://webhook.site/
    1.) go to the site
    2.) copy link from site and paste it in the double quote of the browser.get() method
    '''

    browser = webdriver.Chrome('chromedriver')
    for i in range(1):
        matched_elements = browser.get("")