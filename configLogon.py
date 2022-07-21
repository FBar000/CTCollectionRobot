'''
Scripts for configuring logon data.


'''
import json
import sys

def main():
    if sys.argv[1] == '-h':
        print('\nCredential names: \n\t --username \n\t --password \n\t --url\n')
        return 0
    modes = ['username', 'password', 'url']
    if sys.argv[1] not in ['--'+i for i in modes]:
        print(f"\nInvalid credential name: {sys.argv[1]}")
        print('Usage: \n $ python configLogon.py [CREDENTIAL NAME] [NEW VALUE]\n\n Execute \n $ py configLogon.py -h \n for a list of valid credential names.\n')
        return 1
    args = sys.argv[1:]
    if len(args) != 2:
        print("\nExpected 2 args. Use command as follows: \n$ python configLogon.py -[CREDENTIAL NAME] [NEW VALUE]\n")
        return 2
    m = args[0]
    modes = ['username', 'password', 'url']
    for mode in modes:
        if m == '--'+mode:
            with open('credentials.json', 'r') as jsonFile:
                txt = json.load(jsonFile)
            print(f'Old {mode}: '+txt[mode])
            setField(mode, args[1])
            with open('credentials.json', 'r') as jsonFile:
                txt = json.load(jsonFile)
            print(f'New {mode}: '+txt[mode])
            return -1

def setField(field_key, new_value):
    with open('credentials.json', 'r') as jsonFile:
        data = json.load(jsonFile)
    try:
        data[field_key] = new_value
    except KeyError:
        print("Key Error. Must be 'username', 'password', or 'url'")
        return 1    
    with open('credentials.json', 'w') as jsonFile:
        json.dump(data, jsonFile)

if __name__ == '__main__':
    main()