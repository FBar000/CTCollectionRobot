r'''
Used to specify lists of items to automate location and admin settings.

Usage:
> py makeIdentifierList.py

Feel free to feed previous as argument to automateLocAdm.py

'''
# Fill txt file + return address
import os


def makeHandles():
    '''
    Makes a list of object identifier strings
    
    Arguments: 
        In Terminal, requests # of sections in identifier, type (label/index), and either the string (if label) or the lower bound, upper bound, and width (if id)
    Return:
        objects [list(string)]: A list with the object identifier strings
    '''
    handle_elements = getHandleElements()
    objects = makeHandlesfromElements(handle_elements)
    return objects


def getHandleElements():
    '''
    Get elements to construct object identifiers

    Arguments:
        In Terminal, requests # of sections in identifier, type (label/index), and either the string (if label) or the lower bound, upper bound, and width (if id)
    Return:
        handle_elements [list(str)]: A list with the sections of the object identifier 
    '''
    n = int(input('Sections in object identifiers: '))
    handle_elements = []
    for i in range(n):
        n = input(f"Section {i+1}: Label or Index? (l/i) ")
        if n == 'l':
            handle_elements.append([input('\tLabel: ')])
        else:
            l = int(input('\tLower bound: '))
            t = int(input('\tUpper bound: '))
            width = int(input('\tWidth: '))
            idx = [str(i).zfill(width) for i in range(l,t+1)]
            handle_elements.append(idx)
    return handle_elements

def makeHandlesfromElements(handle_elements):
    '''
    Generate list of object identifier strings from handle_elements
    
    Parameters:
        handle_elements [list(string)] : A list of the elements to the handle elements
    Returns: 
        objects [list(string)] : A list of the object identifiers
    '''
    # Generate object identifier
    objects = [i for i in handle_elements[0]]
    for i in range(1, len(handle_elements)):
        tmp = []
        for ob in objects:
            tmp += [".".join([ob, twig]) for twig in handle_elements[i]]
        objects=tmp
    return objects


def txtFile():
    """Creates a txt file with object identifiers in ~/data"""
    # Gather handle dataa
    print("="*50)
    print("TAG".center(50, "-"))
    print("+"*50)
    try:
        handle = str(input('Handle: '))
    except ValueError:
        print("Expected strings...")
    # Gather index data
    print("x"*50)
    print("INDICES".center(50, "-"))
    print("+"*50)
    try:
        bottom = int(input('Start: '))
        top = int(input('End: '))
        width = int(input("Width: "))
    except ValueError:
        print("Expected integers...")
    print("="*50)
    # Generate index strings
    endings = []
    for i in range(bottom, top+1):
        endings.append(str(i).zfill(width))
    # Create object identifier strings
    tags = []
    for i in endings:
        tags.append('.'.join([handle, i]))
    # Write into a text file
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, 'objIdentifiers')
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)
    path = os.path.join(final_directory,  "objs.txt")
    with open(path, 'w') as f:
        for i in tags:
            f.write(f'{i}\n')
    return path

if __name__ == '__main__':
    txtFile()