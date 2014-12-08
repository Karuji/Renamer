#!/usr/bin/env python3
"""Program for the bulk renaming of files in an ordered manner."""

import os
from FileName import *
import RenamerHelp
import splitstring
import osnav
import random

class RenamerFile(FileName):
    """Modified FileName for renamer."""

    def __init__(self, string, renamer):
        super().__init__(string)
        self.tempName = ""
        self._oldName  = string
        self.renamer = renamer

    def randomUni(self):
        result = ''
        for i in range(16):
            result += chr(random.choice((0x300, 0x2000)) + random.randint(0, 0xff))
        return result

    def rename(self):
        """Renames the file from the current name (string) to the new one (file)."""
        self.newName = self.file + self.extention
        os.rename(self.string, self.newName)
        #print(self.string + "-->" + self.newName)

    def renameBuffer(self):
        self.tempName = self._oldName + " --^^ " + self.file + ' ' + self.randomUni() + self.extention
        try:
            os.rename(self.string, self.tempName)
            self.string = self.tempName
        except FileExistsError:
            remameBuffer()


    def renamePrint(self):
        """Functions like rename but prints the change from original filename to new."""
        self.newName = self.file + self.extention
        os.rename(self.tempName, self.newName)
        print(self._oldName + " --> " + self.newName)

    def setFileName(self, name, num):
        self.file = splitstring.stitch(name, self.file, num)

            
class Renamer(object):
    """Takes a directory and renames the files in that directory in an ordered manner."""
    
    def __init__(self):
        self.restart()

    def restart(self):
        self.mainList     = []
        self.subList      = []
        self.fill         = 0
        self.startNum     = 1
        self.toName       = ""
        self.string       = ""
        self.term1, term2 = 0, 0

    def printList(self):
        """Prints the names of the current files in renamer."""
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

    def printFileName(self):
        """Print a list of file names."""
        i = 1
        for item in self.mainList:
            print(str(i).zfill(self.fill) + ": " + item.getFileName())
            i +=1

    def printFileExt(self):
        """Print the extention of the file."""
        i = 1
        for item in self.mainList:
            print(str(i).zfill(self.fill) + ": " + item.getFileExt())
            i += 1

    def inString(self, string):
        """Stores the raw input from the command line as a string."""
        self.string = string
            
    def swap(self, cmd):
        """Swaps two items in the list."""
        if len(self.mainList) > 0:
            term1, term2 = eval(cmd[1])-1, eval(cmd[2])-1
            check = self._indexCheck
            if check(self.mainList, term1) and check(self.mainList, term2):
                self.mainList[term1], self.mainList[term2] = self.mainList[term2], self.mainList[term1]
                self.printList()
            else:
                print("Must swap items in the list.\n")
        else:
            print("Must have a sorted list before using swap.\n")

    def _indexCheck(self, container, index):
        """Checks the input after it has been converted to container numbers."""
        if index < 0 or index >= len(container):
            return False
        else:
            return True

    def _indexCheckRaw(self, container, index):
        """Checks the input as the user has typed it."""
        if index <= 0 or index > len(container):
            return False
        else:
            return True

    def select(self, cmd):
        """Creates a sublist between the two selected elements (1 indexed all inclusive)."""
        if len(self.mainList) > 0:
            self.subList = []
            # Selects a range of items.
            if len(cmd) == 3:
                self.term1, self.term2 = eval(cmd[1]), eval(cmd[2])
            # Selects a single items.
            elif len(cmd) == 2:
                self.term1, self.term2 = eval(cmd[1]), eval(cmd[1])
            # Tell the user they did something wrong, and end the function.
            else:
                print("Invalid number of terms for select.\n")
                return None
            # Make sure term1 is always the lower term.
            if self.term1 > self.term2:
                self.term1, self.term2 = self.term2, self.term1
            # Check that the numbers are valid list items.
            check = self._indexCheckRaw
            if check(self.mainList, self.term1) and check(self.mainList, self.term2):
                # Select the number(s) and put them into a container.
                self.term1 -= 1
                self.subList = self.mainList[self.term1 : self.term2]
                # Print the selection.
                self.printSubList()
            else:
                print("Must select items in list number\n")
        else:
            print("Must have a sorted list before using select\n")

    def insert(self, cmd):
        """Inserts the sublist into the selected place
the sublist cannot be inserted into itself

If the insert position is an element element of the list than the first item of the sublist
the first item of the sublist shall be at the insert position

If the insert position is an element greater than the last item of the sublist
the last item of the sublist will be at the insert position."""
        if len(self.mainList) > 0:
            if len(cmd) == 2:
                if len(self.subList) > 0:
                    iIn = eval(cmd[1])
                    if iIn > self.term1 and iIn <= self.term2:
                        print("Cannot insert the selected list into itself")
                    else:
                        # Inserting to a number lower than selected.
                        if iIn <= self.term1:
                            self.mainList[self.term1 : self.term2] = []
                            for j in range(len(self.subList)):
                                self.mainList.insert(iIn-1+j, self.subList[j])
                        # Inserting to a humber higher than selected.
                        elif iIn > self.term2:
                            self.mainList[self.term1 : self.term2] = []
                            for j in range(len(self.subList)):
                                self.mainList.insert(iIn-len(self.subList)+j, self.subList[j])
                        # Common to both case hence the else then an if and not an elif
                        self.printList()
                        self.subList = []
                # if len(self.subList) > 0:
                else:
                    print("Nothing to insert\n")                
            # if len(cmd) == 2:
            elif len(cmd) == 3: #Insersts first term into second one so user does not need to use sel
                if eval(cmd[1]) != eval(cmd[2]):
                    self.select(["sel", cmd[1]])
                    self.insert(["ins", cmd[2]])
                else:
                    print("Cannot insert an item into itself\n")
        # if len(self.mainList) > 0:
        else:
            print("Must have a sorted list before using select\n")

    def set(self, cmd):
        """Input commands that determine how renamer will function."""
        if cmd[1] == "name":
           self.setName(cmd)
        if cmd[1] == "start":
            self.setStart(cmd)
        if cmd[1] == "zfill":
            self.setZFill(cmd)
        if cmd[1] == "mode":
            self.setMode(cmd)

    def setName(self, cmd):
        """Allows the user to set the name that the files will be renamed to."""
        if len(self.mainList) > 0:
            self.toName = self.string[self._lenCmdStr(cmd,2):]
            print("\nNew name set to: " + self.toName)
            print("Example: " + splitstring.stitch(self.toName, self.mainList[0].file, self._zFillNum()))
            print()
        else:
            print("Must have a sorted list before setting name\n")

    def setStart(self, cmd):
        """Sets the starting number from which the files will be renamed."""
        if len(self.mainList) > 0:
            self.startNum = eval(cmd[2])
            self._checkZFill()
            print("\nNew starting number is " + str(self.startNum))
            print("zfill is " + str(self.fill))
            print("Example: " + splitstring.stitch(self.toName, self.mainList[0].file, self._zFillNum()))
        else:
            print("Must have a sorted list before setting the start num\n")

    def setZFill(self, cmd):
        """Sets a custom zfill amount greater than the automatic zfill."""
        if len(self.mainList) > 0:
            self._checkZFill()
            if eval(cmd[2]) >= self.fill:
                self.fill = eval(cmd[2])
                print("\nNew zfill set to: " + str(self.fill))
                print("Example: " + splitstring.stitch(self.toName, self.mainList[0].file, self._zFillNum()))
                print()
            else:
                print("Cannot set zfill to be less than the automatic zfill\n")

    def _checkZFill(self):
        """Check the zfill so that it is correct when a new start number has been added."""
        # Value that will eventually be returned, if it is bigger than the fill.
        newFill = self.fill        

        # Check for when the start num is something large.
        if len(str(self.startNum)) > self.fill:
            newFill = len(str(self.startNum))

        # Adjust in case startNum pushed fill to be a new power of 10 (10s to 100s)
        if (len(self.mainList) + self.startNum) > 10**(newFill):
            newFill += 1

        if newFill > self.fill:
            self.fill = newFill

    def _lenCmdStr(self, cmd, ind):
        """Returns the sum of the length of a substring element composed of elements until the index"""
        # This is used in conjunction with the input string to remove the commands from the input
        result = 0
        if len(cmd) >= ind:
            for i in range(ind):
                result += len(cmd[i]) + 1
        return result

    def _zFillNum(self):
        """Shorthand function to keep code clean"""
        return str(self.startNum).zfill(self.fill)

    def setMode(self, cmd):
        #Legacy from when prefix was a command
        pass

    def show(self, cmd):
        """Shows aspects of the program depend on the command entered after show."""
        if len(self.mainList) > 0:
            if len(cmd) > 1:
                if cmd[1] == "ext":
                    self.printFileExt()
                elif cmd[1] == "file":
                    self.printFileName()
                elif cmd[1] == "list" or cmd[1] == "lst":
                    self.printList()
                elif cmd[1] == "sublist":
                    self.printSubList()
            else:
                print("please select a subcommand for show,\nSubcommands are ext or file.")
        else:
            print("Must have a sorted list befor using show.")   

    def list(self, cmd):
        cmd[1] = cmd[1].lower()
        if(cmd[1] == 'folder'):
            self.listFolder(cmd)
            

    def listFolder(self, cmd):
        if len(cmd) == 2:
            dirList = os.listdir(os.getcwd())
            for item in dirList:
                print(item)
        else:
            cmd[2] = cmd[2].lower()
            if cmd[2] == 'numbered':
                dirList = os.listdir(os.getcwd())
                zfill = len(str(len(dirList)))
                for i in range(len(dirList)):
                    print(str(i+1).zfill(zfill) + ': ' + dirList[i])

    def sort(self):
        """Used to set the current directory to that in which the files shall be renamed."""
        self.mainList = []
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

    def _renameList(self):
        #Rename files to a temp name to avoid conflicts
        i = self.startNum
        for item in self.mainList:
            item.setFileName(self.toName, str(i).zfill(self.fill))
            item.renameBuffer()
            i += 1
        #Rename to final name showing change from original name
        i = self.startNum
        for item in self.mainList:
            item.renamePrint()
            i += 1

    def rename(self):
        """Renames the files in the list to their new name."""
        #Need to update to deal with naming conflicts.
        if len(self.mainList) > 0:
            self._renameList()
            self.restart()
        else:
            print('No files have been selected be to renamed. Use sort before rename.')

    def help(self, cmd):
        """Shows help depending on what the user enters."""
        RenamerHelp.help(cmd)

    def dir(self):
        """An attempted to replicate the command line dir function for navigation."""
        osnav.dir()

    def cd(self, cmd):
        """An attempted to replicate the command line cd function for navigation."""
        osnav.cd(self.string)                       

    def processInput(self, cmd):
        """Takes a list of the command input split by spaces and calls functions according to the input."""
        cmd[0] = cmd[0].lower() 
        # Renaming commands.
        if cmd[0] == 'srt' or cmd[0] == 'sort':
            self.sort()
        elif cmd[0] == 'set':
            self.set(cmd)
        elif cmd[0] == 'rename':
            self.rename()
        elif cmd[0] == 'rst' or cmd[0] == 'reset' or cmd[0] == 'restart':
            self.restart()
        # Arranging commands.
        elif cmd[0] == 'ins' or cmd[0] == 'insert':
            self.insert(cmd)
        elif cmd[0] == 'sel' or cmd[0] == 'select':
            self.select(cmd)
        elif cmd[0] == 'swt' or cmd[0] == 'swp' or cmd[0] == 'swap':
            self.swap(cmd)
        elif cmd[0] == 'rm' or cmd[0] == 'remove':
            self.remove(cmd)
        # Display / Help commands.
        elif cmd[0] == 'shw' or cmd[0] == 'show':
            self.show(cmd)
        elif cmd[0] == 'help':
            self.help(cmd)
        # Navigational commands.
        elif cmd[0] == 'dir' or cmd[0] == 'ls':
            self.dir()
        elif cmd[0] == 'cd':
            self.cd(cmd)
        elif cmd[0] == 'lst' or cmd[0] == 'list':
            self.list(cmd)
        
def main():
    renamer = Renamer()
    print("""Renamer

Copyright (c) 2014 Julian Pritchard

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.""")
    print()
    print("Type help functions for a list of commands")
    while True:
            var = input("Enter a Command: ")
            if var.lower() == 'exit':
                    break
            renamer.inString( var)
            var = var.split(" ")
            renamer.processInput( var)
            
if __name__ == '__main__':
    main()
