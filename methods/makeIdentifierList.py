r'''
Used to specify lists of items to automate location and admin settings.

Usage:
> py makeIdentifierList.py

Feel free to feed previous as argument to automateLocAdm.py

'''
# Fill txt file + return address
import os


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


if __name__ == '__main__':
    txtFile()