r'''
Used to specify lists of items to automate location and admin settings.

Usage:
> py makeIdentifierList.py

Input data.
View result at: r"C:\Users\Federico\Desktop\SimplePrograms\MHSAutomation\automateLogs\partials"

Feel free to feed previous as argument to automateLocAdm.py

'''

# Fill txt file + return address
def main():
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
    with open(r"C:\Users\Federico\Desktop\SimplePrograms\MHSAutomation\automateLogs\data\objs.txt", "w") as f:
        for i in tags:
            f.write(f'{i}\n')
    return r"C:\Users\Federico\Desktop\SimplePrograms\MHSAutomation\automateLogs\data\objs.txt"

if __name__ == '__main__':
    main()