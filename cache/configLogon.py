import json
import os


def setField(key, value):
    """
    Change the value in the credentials file
    """
    # Find address
    dr = os.path.dirname(__file__)
    a = os.path.join(dr, 'credentials.json')
    with open(a, 'r+') as f:
        data = json.load(f)
        data[key] = value # <--- add `id` value.
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part