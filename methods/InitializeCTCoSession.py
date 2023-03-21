'''
Initialize driver object for use in madison CTCo

'''
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# A single session of the CTCollections 
def session():
    """
    Initialize a selenium session in CTCo using cached credentials

    Return:
        driver (webdriver) : a selenium webdriver in a logged session
    """
    credentials = getCredentials()
    driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chrome.exe")
    driver.get(credentials["url"])
    # sign in 
    user = WebDriverWait(driver, timeout=5).until(lambda u: u.find_element(By.XPATH,"//input[@name='username']"))
    user.send_keys(credentials["username"])
    driver.find_element(By.XPATH,"//input[@name='password']").send_keys(credentials["password"])
    driver.find_element(By.XPATH, "//a[@aria-label='Login']").click()
    return driver

def getCredentials():
    """
    Either get credentials or initialize them

    Arguments:
        None
    Return:
        credentials (dict(strings)): a dictionary form of the json

    """
    local_path = "\\".join(os.path.dirname(os.path.abspath(__file__)).split('\\')[:-1])   
    credential_file = os.path.join(local_path+ '/cache/credentials.json')
    # Check if credentials are cached
    with open(credential_file, 'r') as jsonFile:
        credential = json.load(jsonFile)
    for key in credential:
        # Initilize if credentials are absent
        if credential[key] == "":
            tmp = input(f"{key}: ")
            setField(key, tmp)
    # Credentials into dict
    with open(credential_file, 'r') as jsonFile:
        credentials = json.load(jsonFile)
    return credentials

if __name__ == 'main':
    session()