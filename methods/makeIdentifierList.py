r'''
Used to specify lists of items to automate location and admin settings.

Usage:
> py makeIdentifierList.py

Feel free to feed previous as argument to automateLocAdm.py

'''
# Fill txt file + return address
import os


def main():
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
    main()