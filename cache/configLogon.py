import json



def setField(key, value):
    """
    Change the value in the credentials file
    """
    with open('CTCollectionRobot\cache\credentials.json', 'r+') as f:
        data = json.load(f)
        data[key] = value # <--- add `id` value.
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part
