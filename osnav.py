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

    if '..' in string:
        container = string.split(os.sep)
        # Remove blanks so that we don't change to the root.
        for item in container:
            if item == '':
                container.pop(container.index(item))
        _cdParts(container, os.getcwd())
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

def _cdParts(container, orig):
    if container[0] == '..':
        container.pop(0)
        os.chdir(os.path.dirname(os.getcwd()))
        check = True
    else:
        target = container.pop(0)
        #newPath = os.path.join(os.getcwd(), os.sep, target)
        newPath = os.getcwd() + os.sep + target
        print(newPath)
        if os.path.isdir(newPath):
            os.chdir(newPath)
            check = False
        else:
            os.chdir(orig)
            print('Invalid directory\n')
            return None
    if len(container) > 0:
        _cdParts(container, orig)
    else:
        if check:
            print(os.getcwd())
