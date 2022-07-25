'''
Use to navigate an object's page.


'''

def getURL(driver, new_screen):
    # navigate to Location Editor
    url = driver.current_url
    tmp = url[33:].split('/')
    new_url = url[:33] + '/'.join(tmp[:6]) +f"/{new_screen}/object_id/{tmp[-1]}"
    driver.get(new_url)