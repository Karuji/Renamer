import os

class FileName(object):
    string    = "" #not to be changed
    file      = ""
    extention = ""
    newName   = ""

    def __init__(self, string):
        self.string = string
        pos = 0
        for i in range(1, len(self.string)):
            if self.string[-i] == ".":
                pos = i
                break
        self.file = self.string[:len(self.string)-pos]
        self.extention = self.string[-pos:]

    def setName(self, name):
        self.file = name

    def getName(self):
        return self.string

    def getFile(self):
        return self.file

    def getExt(self):
        return self.extention

    def rename(self):
        self.newName = self.file + self.extention
        os.rename(self.string, self.newName)
        print(self.string + "-->" + self.newName)
            

class Renamer(object):
    mainList     = []
    subList      = []
    fill         = 0
    toName       = ""
    string       = ""
    sel          = False
    term1, term2 = 0, 0

    def printList(self):
        i = 1
        for item in self.mainList:
            print(str(i).zfill(self.fill) + ": " + item.getName())
            i += 1

    def printSubList(self):
        for item in self.subList:
            print(item.getName())

    def inString(self, string):
        self.string = string

    def list(self):
        printList()
            
    def swap(self, cmd):
        term1, term2 = eval(cmd[1])-1, eval(cmd[2])-1
        self.mainList[term1], self.mainList[term2] = self.mainList[term2], self.mainList[term1]
        self.sel = False
        self.printList()

    def select(self, cmd):
        self.term1, self.term2 = eval(cmd[1]), eval(cmd[2])
        self.term1 -= 1
        self.subList = self.mainList[self.term1 : self.term2]
        self.sel = True
        self.printSubList()

    def restart(self):
        self.mainList = []
        self.subList = []
        self.sel = False
        self.term1, self.term2 = 0, 0
        for i in range(10):
            self.mainList.append(i+1)
        self.printList()

    def insert(self, cmd):
        if self.sel == True:
            iIn = eval(cmd[1])
            if iIn > self.term1 and iIn <= self.term2:
                print("Cannot insert the selected list into itself")
            elif iIn <= self.term1:
                self.mainList[self.term1 : self.term2] = []
                for j in range(len(self.subList)):
                    self.mainList.insert(iIn-1+j, self.subList[j])
                self.printList()
            elif iIn > self.term2:
                self.mainList[self.term1 : self.term2] = []
                for j in range(len(self.subList)):
                    self.mainList.insert(iIn-len(self.subList)+j+1, self.subList[j])
                self.printList()
                self.sel = False
                
        else:
            print("Nothing is selects to insert")

    def showList(self):
        self.printList()

    def set(self, cmd):
        if cmd[1] == "name":
            self.toName = self.string[len(cmd[0]) + len(cmd[1]) + 2:]
            self.printList()

    def show(self, cmd):
        if cmd[1] == "ext":
            i = 1
            for item in self.mainList:
                print(str(i).zfill(self.fill) + ": " + item.getExt())
                i += 1
        if cmd[1] == "file":
            i = 1
            for item in self.mainList:
                print(str(i).zfill(self.fill) + ": " + item.getFile())
                i +=1

    def dir(self):
        print(os.getcwd())
        print()
        dirList = os.listdir(os.getcwd())
        for i in dirList:
            print(i)

    def cd(self, cmd):
        inDir = False
        dirList = os.listdir(os.getcwd())
        for i in dirList:
            if i == cmd[1]:
                inDir = True
        if inDir:
            newPath = os.path.join(os.getcwd(), os.sep, cmd[1])
            if os.path.isdir(newPath):
                os.chdir(newPath)
                print(os.getcwd())
            else:
                print(newPath + " is not a correct directory: err#3")
        else:
            newPath = self.string[(len(cmd[0]))+1:]
            if os.path.isdir(newPath):
                os.chdir(newPath)
                print(os.getcwd())
            else:
                print(newPath + " is not a correct directory: err#4")

    def sort(self):
        dirList = os.listdir(os.getcwd())
        for i in dirList:
            if os.path.isfile(i):
                fileName = FileName(i)
                self.mainList.append(fileName)
        
        self.fill = len(str(len(self.mainList)))
        i = 1
        for item in self.mainList:
            print(str(i).zfill(self.fill) + ": " + item.getName())
            i += 1

    def remove(self, cmd):
        self.mainList.pop(eval(cmd[1])-1)
        self.printList()

    def rename(self):
        i = 1
        for item in self.mainList:
            item.setName(self.toName + str(i).zfill(self.fill))
            item.rename()
            i += 1
        self.printList()

    def help(self, cmd):
        if len(cmd) == 1:
            print("This is the help function")
            print("For help on a specific function please type help follow by the function")
            print("Example help swp")
            print("For a list of functions type help functions")
            print()
        else:
            if cmd[1] == "functions":
                print("Renamer functions: swp, sel, ins, lst, set, dir, cd, srt, rm, rename, exit")
                print("Type help followed by the command")
                print("example help swp")
                print()
            elif cmd[1] == "swt" or cmd[1] == "swp":
                print("swp, or swt, or swap")
                print("Swaps two items on the list by their indecies")
                print("Example: swp 1 5")
                print("Will swap the first and fifth items on the list")
                print()
            elif cmd[1] == "sel" or cmd[1] == "select":
                print("sel or select")
                print("Selects a sub-list from the main list")
                print("This sub-list is the inserted into the main list with the ins commd")
                print("Example: sel 4 7")
                print("Will select the fourth through sevent elements")
                print()
            elif cmd[1] == "ins" or cmd[1] == "insert":
                print("ins or insert")
                print("Inserts a selected sublist into a given position")
                print("The sublist cannot be inserted into itself")
                print("So sel 1 4, ins 3 will not work")
                print("If the insert position is higher than the selected position:")
                print("    Then the sublist first element will align with the insert position")
                print("    Example sel 4 6, ins 1")
                print("    The item in position 4 will be in position 1")
                print("If the insert position is lower than the select position:")
                print("    Then the sublist last element will align with the insert position")
                print("    Example sel 1 4, ins 8")
                print("    The item in position 4 will be in position 8")
                print()
            elif cmd[1] == "lst" or cmd[1] == "list":
                print("Prints the list to the command line")
                print()
            elif cmd[1] == "set":
                print("set name")
                print("Sets the name of the listed output there are no automatic spaces")
                print("It can be left blank if you want the list to simply be numbers")
                print()
            elif cmd[1] == "dir" or cmd[1] == "ls":
                print("dir or ls")
                print("Functions similar to the operating system function in that it will list the contents of the current directory")
                print()
            elif cmd[1] == "cd":
                print("cd")
                print("Functions like the os cd in that it can take an absolute or relative directory change")
                print("The directory must exist in order for it to change to that directoy")
                print()
            elif cmd[1] == "srt" or cmd[1] == "sort":
                print("srt or sort")
                print("Signifies to the program that this is the directory in which you want to sort the files to be renamed")
                print("It is normally used after using cd and dir to find the correct directory")
                print()
            elif cmd[1] == "rm" or cmd[1] == "remove":
                print("rm or remove")
                print("Removes a file from the list so that it will not be renamed")
            elif cmd[1] == "rename":
                print("The final command telling the program that the list is sorted in order, and the name has been set")
                print("Will rename the files, this cannot be undone")
                print()
            elif cmd[1] == "exit":
                print("exit")
                print("Exit the program")
                print()
            else:
                print("Help request not recognized")
                print("type help functions")
                print("For a list of functions that help has info on")
                print()


    def processInput(self, cmd): 
        if cmd[0]   == "swt" or cmd[0] == "swp" or cmd[0] == "swap":
            self.swap(cmd)
        elif cmd[0] == "sel" or cmd[0] == "select":
            self.select(cmd)
        elif cmd[0] == "ins" or cmd[0] == "insert":
            self.insert(cmd)
        elif cmd[0] == "lst" or cmd[0] == "list":
            self.showList()
        elif cmd[0] == "rst":
            self.restart()
        elif cmd[0] == "set":
            self.set(cmd)
        elif cmd[0] == "dir" or cmd[0] == "ls":
            self.dir()
        elif cmd[0] == "cd":
            self.cd(cmd)
        elif cmd[0] == "srt" or cmd[0] == "sort":
            self.sort()
        elif cmd[0] == "rm" or cmd[0] == "remove":
            self.remove(cmd)
        elif cmd[0] == "shw" or cmd[0] == "show":
            self.show(cmd)
        elif cmd[0] == "help":
            self.help(cmd)
        elif cmd[0] == "rename":
            self.rename()
        
def main():
    renamer = Renamer()
    print("Type help functions for a list of commands")
    while True:
            var = input("Enter a Command: ")
            if var == "exit":
                    break
            renamer.inString( var)
            var = var.split(" ")
            renamer.processInput( var)
            
if __name__ == '__main__':
    main()
