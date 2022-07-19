# CTCollectionRobot


## Description

These scripts automate parts of the accessioning process on the Madison [Collective Access](https://collectiveaccess.org/) database, and possibly the Collective Access database interface more broadly. The scripts use python's selenium library to navigate the database website as any user would and therby automate certain tasks. This is a temporary solution and should not be relied upon; the scripts rely on a version of the website which is not guaranteed to remain the same. 

<br>

## Installation

Initalize a virtual environment for this project. Download the python library `selenium` as detailed inthe [selenium with python setup procedures](https://selenium-python.readthedocs.io/). When doing this, download  `chromedriver.exe` into 

>`C:\Drivers\SeleniumBrowsers\chromedriver.exe`

After this procedure, verify that the installation worked via

> `$ pip show selenium`

Now, clone this repository into your directory.

> `$ git clone https://github.com/FBar000/CTCollectionRobot.git`

Done. 

<br>

## Usage

This is a sloppy stub. Clearer and more extensive documentation will come in a later version.

Use `automateLocAdm.py` to automate setting locations and admin status. The admin status will be "publicly accessible" and "accessioned" by default. Specifying the location will require configuration; the location I require is hardcoded as follows:

```
...
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
...
```

For different locations, use the id's of the web elements that you must click to specify a location instead.

To use `automateLocAdm.py`, run

>  `py automateLocAdm.py`

Input the data requested. The script will start a session on CTCo, and iterate over the objects specified by the object identifiers generated from your input. Any errors during while on a given object will skip to the next object and print `passed #`, where `#` is the skipped object's identifier. 

<br>

## TODO

As mentioned, this project is temporary. I am learning how to make these same changes using the [database's API](https://manual.collectiveaccess.org/providence/developer/index.html) to develop more sustainable tools. In any case, here's the to-do list for this project

- Fix navigation: Immediately fails when multiple objects appear on search results for a given object_identifier
- Soften location: Add a tool to set location path to custom locations
