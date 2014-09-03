#!/usr/bin/env python3
"""Program for the bulk renaming of files in an ordered manner."""

import os
from FileName import *
import RenamerHelp

class RenamerFile(FileName):

    def __init__(self, string, renamer):
        super().__init__(string)
        self.tempName = ""
        self.oldName  = string
        self.renamer = renamer

    def rename(self):
        """Renames the file from the current name (string) to the new one (file)."""
        self.newName = self.file + self.extention
        os.rename(self.string, self.newName)
        #print(self.string + "-->" + self.newName)

    def renamePrint(self):
        """Functions like rename but prints the change from original filename to new."""
        self.newName = self.file + self.extention
        try:
            os.rename(self.string, self.newName)
            print(self.oldName + " --> " + self.newName)
        except FileExistsError:
            raise

class SplitString(object):
    """Class to place numbers at an arbitrary place in an arbitrary string."""
    initialString = ""
    numberPos     = -1 
        
            
class Renamer(object):
    """Takes a directory and renams the files in that directory in an ordered manner."""
    mainList     = []
    subList      = []
    fill         = 0
    startNum     = 1
    toName       = ""
    string       = ""
    sel          = False
    term1, term2 = 0, 0
    canRename    = False
    prefixMode   = False #Need to change rename modes to a class

    def printList(self):
        """Prints the names of the current files in the directoy."""
        i = 1
        for item in self.mainList:
            print(str(i).zfill(self.fill) + ": " + item.getName())
            i += 1
        print()

    def printSubList(self):
        """Prints the list of items selected by the select function."""
        for item in self.subList:
            print(item.getName())
        print()

    def inString(self, string):
        """Stores the raw input from the command line as a string."""
        self.string = string

    def list(self):
        self.printList()
            
    def swap(self, cmd):
        """Swaps two items in the list."""
        term1, term2 = eval(cmd[1])-1, eval(cmd[2])-1
        self.mainList[term1], self.mainList[term2] = self.mainList[term2], self.mainList[term1]
        self.sel = False
        self.printList()

    def select(self, cmd):
        """Creates a sublist between the two selected elements (1 indexed all inclusive)."""
        self.subList = []
        self.term1, self.term2 = eval(cmd[1]), eval(cmd[2])
        self.term1 -= 1
        self.subList = self.mainList[self.term1 : self.term2]
        self.sel = True
        self.printSubList()

    def insert(self, cmd):
        """Inserts the sublist into the selected place
the sublist cannot be inserted into itself

If the insert position is an element element of the list than the first item of the sublist
the first item of the sublist shall be at the insert position

If the insert position is an element greater than the last item of the sublist
the last item of the sublist will be at the insert position."""

        if self.sel == True:
            iIn = eval(cmd[1])
            if iIn > self.term1 and iIn <= self.term2:
                print("Cannot insert the selected list into itself")
            elif iIn <= self.term1:
                self.mainList[self.term1 : self.term2] = []
                for j in range(len(self.subList)):
                    self.mainList.insert(iIn-1+j, self.subList[j])
                self.printList()
                self.sel = False
            elif iIn > self.term2:
                self.mainList[self.term1 : self.term2] = []
                for j in range(len(self.subList)):
                    self.mainList.insert(iIn-len(self.subList)+j, self.subList[j])
                self.printList()
                self.sel = False                
        elif len(cmd) == 3: #Insersts first term into second one so user does not need to use sel
            if eval(cmd[1]) != eval(cmd[2]):
                self.select(["sel", cmd[1], cmd[1]])
                self.insert(["ins", cmd[2]])

        else:
            print("Nothing is selects to insert")

    def showList(self):
        self.printList()

    def set(self, cmd):
        """Input commands that determine how renamer will function."""
        if cmd[1] == "name":
           self.setName(cmd)
        if cmd[1] == "start":
            self.setStart(cmd)
        if cmd[1] == "mode":
            self.setMode(cmd)

    def setName(self, cmd):
        """Allows the user to set the name that the files will be renamed to."""
        self.toName = self.string[len(cmd[0]) + len(cmd[1]) + 2:]
        self.printList()
        print()
        print("New name set to: " + self.toName)
        print("Example: " + self.toName + str(1).zfill(self.fill))
        print()

    def setStart(self, cmd):
        """Sets the starting number from which the files will be renamed."""
        self.startNum = eval(cmd[2])
        self.checkZFill()
        print()
        print("New starting number is " + str(self.startNum))
        print("zfill is " + str(self.fill))
        print("Example: " + self.toName + str(1).zfill(self.fill))

    def checkZFill(self):
        """Check the zfill so that it is correct when a new start number has been added."""
        fill    = self.fill
        newFill = fill        

        if len(str(self.startNum)) > fill:
            newFill = len(str(self.startNum))

        if (len(self.mainList) + self.startNum) > 10**(newFill):
            newFill += 1

        self.fill = newFill

    def setMode(self, cmd):
        if cmd[2] == "prefix":
            self.setModePrefix()

    def setModePrefix(self):
        self.prefixMode = not self.prefixMode
        print()
        print("Renamer will now append a number to the file name instead of renaming files")
        print()


    def show(self, cmd):
        """Shows aspects of the program depend on the command entered after show."""
        if   cmd[1] == "ext":
            i = 1
            for item in self.mainList:
                print(str(i).zfill(self.fill) + ": " + item.getFileExt())
                i += 1
        elif cmd[1] == "file":
            i = 1
            for item in self.mainList:
                print(str(i).zfill(self.fill) + ": " + item.getFileName())
                i +=1

    

    def sort(self):
        """Used to set the current directory to that in which the files shall be renamed."""
        mainList = []
        dirList = os.listdir(os.getcwd())
        for i in dirList:
            if os.path.isfile(i):
                fileName = RenamerFile(i, self)
                self.mainList.append(fileName)
        
        self.fill = len(str(len(self.mainList)))
        i = 1
        for item in self.mainList:
            print(str(i).zfill(self.fill) + ": " + item.getName())
            i += 1
        self.canRename = True

    def remove(self, cmd):
        """If a single number is passed then that number is removed from the list
        If two numbers are passed than the range of those numbers is removed from the list"""
        if len(cmd) == 2:
            self.mainList.pop(eval(cmd[1])-1)
            self.printList()
        elif len(cmd) == 3:
            if eval(cmd[1]) < eval(cmd[2]):
                list1 = self.mainList[0:eval(cmd[1])-1]
                list2 = self.mainList[eval(cmd[2]):len(self.mainList)]
                self.mainList = list1 + list2
                self.printList()
            else:
                print("Number range for removal is incorrect err#5")

    def rename(self):
        """Renames the files in the list to their new name."""
        #Need to update to deal with naming conflicts.
        if self.canRename:
            i = self.startNum
            if not self.prefixMode:
                for item in self.mainList:
                    item.setFileName(self.toName + str(i).zfill(self.fill))
                    item.renamePrint()
                    # except FileExistsError:
                    #     print("Catching exception here")
                    i += 1
                #self.printList()
            else:
                for item in self.mainList:
                    item.setFileName(str(i).zfill(self.fill) + ' ' + item.getFileName())
                    item.renamePrint()
                    # except FileExistsError:
                    #     print("Catching exception here")
                    i += 1
            self.canRename = False

        else:
            print('No files have been selected be to renamed. Use sort before rename.')

    def help(self, cmd):
        """Shows help depending on what the user enters."""
        RenamerHelp.help(cmd)

    def dir(self):
        """An attempted to replicate the command line dir function for navigation."""
        print(os.getcwd())
        print()
        dirList = os.listdir(os.getcwd())
        for i in dirList:
            print(i)

    def cd(self, cmd):
        """An attempted to replicate the command line cd function for navigation."""
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
           

    def processInput(self, cmd):
        """Takes a list of the command input split by spaces and calls functions according to the input.""" 
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
    print("""Renamer

Copyright (c) 2014 Julian Pritchard""")
    print()
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
