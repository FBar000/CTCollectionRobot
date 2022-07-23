''''
For use on madison.ctcollections.org. Takes a list of object identifiers and logs their location (LA/Lateral1/Draw3) and sets their admin status (accesioned, public).

For usage, specify login credentials

'''
import json
import pathlib
from posixpath import abspath
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import steps used in process
from methods import *
from configLogon import setField


# `objects` is a list with object identifier strings
def main(driver, objects):
    """Iterate over objects"""
    # loop over objects
    for object_identifier in objects:
        try:
            format_item(driver, object_identifier)
        except:
            print('passed '+str(object_identifier))


def getHandleElements():
    '''Get elements to construct object identifiers'''
    n = int(input('Sections in object identifiers: '))
    parts = []
    for i in range(n):
        n = input(f"Section {i+1}: Label or Index? (l/i) ")
        if n == 'l':
            parts.append([input('\tLabel: ')])
        else:
            l = int(input('\tLower bound: '))
            t = int(input('\tUpper bound: '))
            width = int(input('\tWidth: '))
            idx = [str(i).zfill(width) for i in range(l,t+1)]
            parts.append(idx)
    return parts

def format_item(driver, object_identifier):
    '''
    Set object location and admin status
    '''
    searchByObjectIdentifier(driver, object_identifier)
    # navigate to Location Editor
    url = driver.current_url
    tmp = url.split('Edit/')
    driver.get(tmp[0]+'Edit/Screen51/'+tmp[1])
    try:
        # set location: Root/LA/Lateral1/Draw3
        id1 = 'hierBrowser_P205ObjectEditorFormhierarchyBrowsernew_0_level_0_item_1_edit'
        id2 = 'hierBrowser_P205ObjectEditorFormhierarchyBrowsernew_0_level_1_item_75_edit'
        id3 = 'hierBrowser_P205ObjectEditorFormhierarchyBrowsernew_0_level_2_item_916_edit'
        id4 = 'hierBrowser_P205ObjectEditorFormhierarchyBrowsernew_0_level_3_item_934_edit'
        path = [id1, id2, id3, id4]
        for i in path:
            but = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, i))
            )
            but.click()

        # Save
        driver.find_element(By.XPATH, "//a[@aria-label='Save']").click()
        # navigate to Admin Status Editor
        driver.get(tmp[0]+'Edit/Screen52/'+tmp[1])
        # Set to accessioned
        driver.find_element(By.ID, 'P208ObjectEditorForm_attribute_162_162_new_0').click()
        # Allow public access
        driver.find_element(By.ID, 'P210ObjectEditorFormaccess').click()
        driver.find_element(By.XPATH, "//select[@id='P210ObjectEditorFormaccess']/option[@value='1']").click()
        driver.find_element(By.XPATH, "//select[@id='P209ObjectEditorFormstatus']/option[@value='0']").click()
        # Save
        driver.find_element(By.XPATH, "//a[@aria-label='Save']").click()
    except: pass


if __name__ == '__main__':
    '''
    Execute
    '''
    handle_elements = getHandleElements()

    # Generate object identifier
    objects = [i for i in handle_elements[0]]
    for i in range(1, len(handle_elements)):
        tmp = []
        for ob in objects:
            tmp += [".".join([ob, twig]) for twig in handle_elements[i]]
        objects=tmp
    # Check if credentials are cached
    local_path = os.path.dirname(os.path.abspath(__file__))
    credential_file = os.path.join(local_path+ '/cache/credentials.json')
    with open(credential_file, 'r') as jsonFile:
        credential = json.load(jsonFile)
    for key in credential:
        # Initilize if credentials are absent
        if credential[key] == "":
            tmp = input(f"{key}: ")
            setField(key, tmp)
    # Use credentials
    with open(credential_file, 'r') as jsonFile:
        credential = json.load(jsonFile)
    print(f"Using credentials: \n\t username: {credential['username']} \n\t password: {credential['password']} \n\t url: {credential['url']}\n")
    driver = session(credential['username'], credential['password'], credential['url'])
    main(driver, objects)
    driver.quit()
