"""
Program to automatically create a set of items.
"""
from methods import *
import json
import time
from selenium.webdriver.common.by import By
import os

def createSet(driver, object_identifiers):
    """
    Create a set of objects for manual batch editing.

    Uses batch editing in Collective Access.

    Parameters;
        driver: Selenium webDriver element
        object_identifiers (list[string]) : A list of the object identifiers for the objects to be accessioned
    Return:
        None
    """
    driver.implicitly_wait(5)
    if not driver.current_url.endswith('/index.php/manage/sets/SetEditor/Edit/set_id/0/type_id/12/table_num/57'):            # Fix this; Not working
        driver.get("/".join(driver.current_url.split('/')[:3])+'/index.php/manage/sets/SetEditor/Edit/set_id/0/type_id/12/table_num/57')
    box = driver.find_element(By.XPATH, "//div[contains(text(), 'Add')]/input")
    for ident in object_identifiers:
        try:
            box.send_keys(ident)
            driver.find_element(By.XPATH, f"//a[contains(text(), '{ident}')]").click()
            time.sleep(0.5)
            box.clear()
        except:
            box.clear()
            pass
    time.sleep(0.75)
    savePage(driver)



if __name__ == '__main__':

    # Use credentials
    local_path = os.path.dirname(os.path.abspath(__file__))
    credential_file = os.path.join(local_path+ '/cache/credentials.json')
    with open(credential_file, 'r') as jsonFile:
        credential = json.load(jsonFile)
    # Create set of objects
    objects = makeHandles()    
    # Navigate to sets
    dr = session()
    createSet(dr, objects)
    print("Done")
    dr.get(r"https://cdn.pixabay.com/photo/2020/04/10/13/28/success-5025797_1280.png")
