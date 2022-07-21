'''
Initialize driver object for use in madison CTCo

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# A single session of the CTCollections 
def session(username, password, url):
    """
    Initialize a selenium session in CTCo.

    Parameters:
        username (string) : username 
        password (string) : password
        url (string) : url of the CTCo page
    Return:
        driver (webdriver) : a selenium webdriver in a logged session
    """
    driver = webdriver.Chrome("C:\Drivers\SeleniumBrowsers\chromedriver.exe")
    driver.get(url)
    # sign in 
    user = WebDriverWait(driver, timeout=5).until(lambda u: u.find_element(By.XPATH,"//input[@name='username']"))
    user.send_keys(username)
    driver.find_element(By.XPATH,"//input[@name='password']").send_keys(password)
    driver.find_element(By.XPATH, "//a[@aria-label='Login']").click()
    return driver

