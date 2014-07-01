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