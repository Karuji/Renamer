#!/usr/bin/env python3
"""Program for the bulk renaming of files in an ordered manner."""

import os

class FileName(object):
    """Class to hold the name of the file to be renamed."""
    string    = "" #not to be changed
    file      = ""
    extention = ""
    newName   = ""
    hasExt    = False

    def __init__(self, string):
        """Allows passing the current file name when creating the object."""
        self.string = string
        pos = 0

        if '.' in self.string:
            for i in range(1, len(self.string)):
                if self.string[-i] == ".":
                    pos = i
                    break
            self.file = self.string[:len(self.string)-pos]
            self.extention = self.string[-pos:]
        else:
            self.file = self.string

    def setFileName(self, name):
        """Sets a new file name for the rename function."""
        self.file = name

    def getName(self): 
        """Returns the current full name of the file."""
        return self.string

    def setName(self, string):
        """Sets the member string var."""
        self.string = string

    def getFileName(self): 
        """Returns the current file name that it shall be renamed to."""
        return self.file

    def getFileExt(self):
        """Returns the current file extention."""
        return self.extention

    def rename(self):
        """renames the file from the current name (string) to the new one (file)."""
        self.newName = self.file + self.extention
        os.rename(self.string, self.newName)
        print(self.string + "-->" + self.newName)
            

class Renamer(object):
    """Takes a directory and renams the files in that directory in an ordered manner."""
    mainList     = []
    subList      = []
    fill         = 0
    toName       = ""
    string       = ""
    sel          = False
    term1, term2 = 0, 0
    canRename    = False

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
        """Allows the user to set the name that the files will be renamed to."""
        if cmd[1] == "name":
            self.toName = self.string[len(cmd[0]) + len(cmd[1]) + 2:]
            self.printList()

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
        elif cmd[1] == "w":
            print("""This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    """)
        elif cmd[1] == "c":
            print("""Renamer is a program for the bulk renaming of files.
    Copyright (C) 2013  Julian Prithard

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    """)

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

    def sort(self):
        """Used to set the current directory to that in which the files shall be renamed."""
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
        self.canRename = True

    def remove(self, cmd):
        """Removes an element from the list."""
        self.mainList.pop(eval(cmd[1])-1)
        self.printList()

    def rename(self):
        """Renames the files in the list to their new name."""
        if self.canRename:
            i = 1
            for item in self.mainList:
                item.setFileName(self.toName + str(i).zfill(self.fill))
                item.rename()
                i += 1
            self.printList()
            self.canRename = False
        else:
            print('No files have been selected be to renamed. Use sort before rename.')

    def help(self, cmd):
        """Shows help depending on what the user enters."""
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
    print("""Renamer  Copyright (C) 2013  Julian Pritchard
    This program comes with ABSOLUTELY NO WARRANTY; for details type 'show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type 'show c' for details.""")
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
