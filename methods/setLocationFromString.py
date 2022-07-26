'''
Set an object's location from a string of form

    Storage Locations / Path / To / Object

'''
import time
from selenium.webdriver.common.by import By

# # In Progress
# def bulkLocationSet(driver, object_identifiers, location_string):
#     """
#     Create a set of objects for manual batch editing.

#     Uses batch editing in Collective Access.

#     Parameters;
#         driver : Selenium webDriver element
#         object_identifiers (list[string]) : A list of the object identifiers for the objects to be accessioned
#     Return:
#         None
#     """
#     # Create Set
#     driver.implicitly_wait(5)
#     if not driver.current_url.endswith('/index.php/manage/sets/SetEditor/Edit/set_id/0/type_id/12/table_num/57'):            # Fix this; Not working
#         driver.get("/".join(driver.current_url.split('/')[:3])+'/index.php/manage/sets/SetEditor/Edit/set_id/0/type_id/12/table_num/57')
#     box = driver.find_element(By.XPATH, "//div[contains(text(), 'Add')]/input")
#     for ident in object_identifiers:
#         box.send_keys(ident)
#         driver.find_element(By.XPATH, f"//a[contains(text(), '{ident}')]").click()
#     # Save
#     time.sleep(0.75)
#     driver.find_element(By.XPATH, "//a/*[contains(text(), 'Save')]").click()


# PC: driver on main object page
def setLocation(driver, location_string):
    """
    Set the location for an object from a string of the form.

    Assumes that driver is on object page.

    Storage Locations / Path / To / Object
    
    Parameters:
        driver (webdriver) : a selenium driver object with an initialized CTCo session.
        location_string (string) : the location for an object
    Returns:
        None
    """
    driver.implicitly_wait(3)
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
