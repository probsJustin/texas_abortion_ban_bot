from selenium import webdriver


def run(directory):
    '''
    Generate a end point at webhook and check the request
    going to use https://webhook.site/
    1.) go to the site
    2.) copy link from site and paste it in the double quote of the browser.get() method
    '''

    browser = webdriver.Chrome(directory)
    for i in range(1):
        matched_elements = browser.get("https://webhook.site/c8ffab5a-e125-4d44-b4b3-271dad8307bb")
    browser.close()