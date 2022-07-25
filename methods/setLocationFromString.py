'''
Set an object's location from a string of form

    Storage Locations / Path / To / Object

'''
from selenium.webdriver.common.by import By

# PC: driver on main object page
def setLocation(driver, location_string):
    """
    Set the location for an object from a string of the form 

    Storage Locations / Path / To / Object
    
    Parameters:
        driver (webdriver) : a selenium driver object with an initialized CTCo session.
        location_string (string) : the location for an object
    Returns:
        None
    """
    driver.implicitly_wait(3)
    getURL(driver, 'Screen51')
    # Split location
    path = [i.strip() for i in location_string.split('/')]
    # Validate
    if path[0] != 'Storage locations':
        print("Location String incorrectly formatted")
        return -1
    # Select
    driver.find_element(By.XPATH, f"(//a[contains(text(), 'Storage locations')])[2]/../div").click()
    for loc in path[1:]:
        driver.find_element(By.XPATH, f"//a[contains(text(), '{loc}')]/../div").click()
    driver.find_element(By.XPATH, "//a[@aria-label='Save']").click()
    getURL(driver, 'Screen40')


def getURL(driver, new_screen):
    # navigate to Location Editor
    url = driver.current_url
    tmp = url[33:].split('/')
    new_url = url[:33] + '/'.join(tmp[:6]) +f"/{new_screen}/object_id/{tmp[-1]}"
    driver.get(new_url)