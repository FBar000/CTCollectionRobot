'''
Search for an item, given its object identifier. 

For use in the CTCo website, as formatted 15 July 2022

Federico Barrera
15 July 2022
'''
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from InitializeCTCoSession import *

# Takes initialized driver (as in InitializeCTCoSession.py) and the object identifier, as a string
# Navigates to object_identifier page
def searchByObjectIdentifier(driver, object_identifier):
    """
    Navigate to object page by its object identifier

    Parameters:
        driver (webdriver) : a selenium driver object with an initialized CTCo session.
        object_identifier (string) : the object identifier of an object
    Returns:
        None
    """
    # search by object idenfitier
    searchbar = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH, "//input[@id='caQuickSearchFormText']"))
    searchbar.send_keys(object_identifier)
    searchbar.send_keys(Keys.ENTER)
    # Handle 'results screen' if necessary
    if driver.current_url.endswith('/index.php/find/QuickSearch/Index'):            # Fix this; Not working
        driver.find_element(By.XPATH, f"//li[contains(text(), '{object_identifier}')]//a").click()

if __name__ == '__main__':
    # Get a session
    username = 'Federico Barrera'
    password = '`ad/g3${6'
    ses = session(username, password)
    # Search for an item
    object_identifier = 'A2022.ClevelandFamily.015'
    searchByObjectIdentifier(ses, object_identifier)

