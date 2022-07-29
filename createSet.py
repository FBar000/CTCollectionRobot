"""
Program to automatically create a set of items.


"""
from methods import *
import json

if __name__ == '__main__':

    # Use credentials
    local_path = os.path.dirname(os.path.abspath(__file__))
    credential_file = os.path.join(local_path+ '/cache/credentials.json')
    with open(credential_file, 'r') as jsonFile:
        credential = json.load(jsonFile)

    # Navigate to sets
    dr = session(credential['username'], credential['password'], credential['url'])
    bulkLocationSet(dr, ['A2022.DowdCharles.017'], 'Storage locations / Lee Academy / Lateral File 1 / Draw 3')
    dr.quit()
