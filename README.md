# CTCollectionRobot


## Description

These scripts automate parts of the accessioning process on the Madison [Collective Access](https://collectiveaccess.org/) database, and possibly the Collective Access database interface more broadly. The scripts use python's selenium library to navigate the database website as any user would and thereby automate certain tasks. This is a temporary solution and should not be relied upon; the scripts rely on a version of the website which is not guaranteed to remain the same. 

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

## Set Location and Admin Status

Use `automateLocAdm.py` to automate setting locations and admin status. The admin status will be "publicly accessible" and "accessioned" by default. Specifying the location will require configuration; the location I require is hardcoded as follows:

To use `automateLocAdm.py`, run

>  `py automateLocAdm.py`

Input the data requested. The script will start a session on CTCo, and iterate over the objects specified by the object identifiers generated from your input. 

When prompted for a location (`location: `), input a path to a location as `Storage locations / PATH / TO / LOCATION`.

Any errors during while on a given object will skip to the next object and print `passed #`, where `#` is the skipped object's identifier. 

## Logon 

You will be prompted for your personal credentials when you run this program for the first time. The credentials are the url of your database, your username, and your password. If you want to change the site you're on, or if you changed your password, use the following commands to change your credentials:

Change username
> `$ py configLogon.py -username [NEW USERNAME]`

Change password

> `py configLogon.py -password [NEW PASSWORD]`

Change url

> `py configLogon.py -url [NEW URL]`


Here's an example:
```
$ py configLogon.py -username my_newUSER
Old username: my_oldUSER
New username: my_newUSER
$ 
```

### Possible Error

If after running this you get the error:

> `json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)`

Manually set `credentials.json` to:
```
{
    "username": "",
    "password": "",
    "url": ""
}
```

