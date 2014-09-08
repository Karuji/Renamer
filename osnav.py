import os

def dir():
    """An attempted to replicate the command line dir function for navigation."""
    print(os.getcwd())
    print()
    dirList = os.listdir(os.getcwd())
    for i in dirList:
        print(i)

def cd(string):
    """An attempted to replicate the command line cd function for navigation."""
    if string[:3] == 'cd ':
        string = string[3:]
    if string[-1] != os.sep:
        string += os.sep

    if string == '..' + os.sep:
        newPath = os.path.dirname(os.getcwd())
    else:
        newPath = os.path.join(os.getcwd(), os.sep, string)
    if os.path.isdir(newPath):
        os.chdir(newPath)
        print(os.getcwd())
    else:
        newPath = string
        if os.path.isdir(newPath):
            os.chdir(newPath)
            print(os.getcwd())
        else:
            print(newPath + " is not a correct directory: err#4")