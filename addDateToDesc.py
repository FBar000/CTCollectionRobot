from methods import *


def addDateToDesc(driver, object_identifier):
    """
    Add information from date field to the top of the description field.

    Arguments:
        driver (WebDriver): Selenium WebDriver in a CTCO session
        object_identifier (string): The object identifier of a document
    Return:
        None
    """
    # Go to object page
    try:
        searchByObjectIdentifier(driver, object_identifier)
    except:
        print(f"passed {object_identifier}")
        return
    # Get Date
    date_data = driver.find_element(By.XPATH, "(//*[contains(text(), 'Date')])[3]/../input").get_attribute("value")
    if date_data != "":
        # Add to Description
        try:
            iframe = driver.find_element(By.XPATH, "(//iframe)[1]")
            driver.switch_to.frame(iframe)
            driver.find_element(By.XPATH, "//body").send_keys(date_data+"\n\n")
            driver.switch_to.default_content()
            savePage(driver)
        except:
            print(f"passed {object_identifier}")
    else:
        date_data = "NO DATA"
    print(f"{object_identifier}: {date_data}")
    

if __name__ == '__main__':

    # Get a list of objects to act on
    object_identifiers = makeHandles()
    
    driver = session()
    for o_identifier in object_identifiers:
        addDateToDesc(driver, o_identifier)
    print("Done")
    driver.close()

        
