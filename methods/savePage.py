from selenium.webdriver.common.by import By

def savePage(driver):
    """
    Save an object's page after changes were made.

    Arguments:
        driver (WebDriver): A Selenium WebDriver object in a CTCo session on an object's page 
    Return:
        None
    """
    element = driver.find_element(By.XPATH, "//a[@aria-label='Save']")
    driver.execute_script("arguments[0].click();", element)
    