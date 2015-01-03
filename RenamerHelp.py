def help(cmd):
    """Shows help depending on what the user enters."""
    # Force input to lowercase
    for i in range(len(cmd)):
        cmd[i] = cmd[i].lower()

    if len(cmd) == 1:
        print("This is the help function")
        print("For help on a specific function please type help follow by the function")
        print("Example help swp")
        print("For a list of functions type help functions\n")        
    else:
        if cmd[1] == 'functions':
            print("Renamer functions: \'cd\', \'dir\', \'exit\', \'ins\', \'lst\', \'rename\', \'reset\', \'rm\', \'sel\', \'set\', \'show\', \'srt\', \'swp\'")
            print("Type help followed by the command")
            print("example help swp\n")            
        elif cmd[1] == 'swt' or cmd[1] == 'swp' or cmd[1] == 'swap':
            print("swp, or swt, or swap")
            print("Swaps two items on the list by their indecies")
            print("Example: \'swp 1 5\'")
            print("Will swap the first and fifth items on the list\n")            
        elif cmd[1] == 'sel' or cmd[1] == 'select':
            print("sel or select")
            print("Selects a sub-list from the main list")
            print("This sub-list is the inserted into the main list with the ins commd")
            print("Example: \'sel 4 7\'")
            print("Will select the fourth through sevent elements\n")            
        elif cmd[1] == 'ins' or cmd[1] == 'insert':
            print("ins or insert")
            print("Inserts a selected sublist into a given position")
            print("The sublist cannot be inserted into itself")
            print("So sel 1 4, ins 3 will not work")
            print("If the insert position is higher than the selected position:")
            print("    Then the sublist first element will align with the insert position")
            print("    Example \'sel 4 6\', \'ins 1\'")
            print("    The item in position 4 will be in position 1")
            print("If the insert position is lower than the select position:")
            print("    Then the sublist last element will align with the insert position")
            print("    Example \'sel 1 4\', \'ins 8\'")
            print("    The item in position 4 will be in position 8\n")            
            print("Inset can also be to insert a single item into another place and shift the list")
            print("This is used by typing \'ins 7 1\' which which will insert the items from 7 into 1")
            print("and move items 1 through 6 to the next position in the list\n")
        elif cmd[1] == 'lst' or cmd[1] == 'list':
            print("Prints the list to the command line\n")            
        elif cmd[1] == 'set':
            if len(cmd) == 2:
                print("Set has a variety of subcommands.")
                print("These are \'name\', \'start\', and \'zfill\'")
                print("Type help set <subcommand> for the help on the topic\n")                
            else:
                if cmd[2] == 'name':
                    print("set name")
                    print("Sets the name of the listed output with * being the position of the number")
                    print("It can be left blank if you want the list to simply be numbers")
                    print("If no * is placed then the number will be placed at the end without a space")
                    print("| may be placed in the name to use the current name of the file")
                    print("So if you wanted to prepend the current file with a number you can use:")
                    print("\'set name * |\'\n")                    
                elif cmd[2] == 'start':
                    print("set start")
                    print("Sets the number at which the list will start the renaming")
                    print("By default the renaming starts at 1, using start you can set this to any integer")
                    print("Start does not affect the numbers which are used for input\n")                    
                elif cmd[2] == 'zfill':
                    print("set zfill")
                    print("Sets the amount of zeros (0) that are placed before the number")
                    print("zfill can only increase the number of zeros")
                    print("zfill works for the number of characters in the item as oppose only the number of zeros")
                    print("If you had a list of 8 items and wanted a zero befor the item you would use:")
                    print("\'set zfill 2\'\n")
                else:
                    print("Invalid set subcommand\n type\'help set\' for a list of subcommands\n")                  
        elif cmd[1] == 'dir' or cmd[1] == 'ls':
            print("dir or ls")
            print("Functions similar to the operating system function in that it will list the contents of the current directory\n")            
        elif cmd[1] == 'cd':
            print("cd")
            print("Functions like the os cd in that it can take an absolute or relative directory change")
            print("The directory must exist in order for it to change to that directoy\n")            
        elif cmd[1] == 'srt' or cmd[1] == 'sort':
            print("srt or sort")
            print("Signifies to the program that this is the directory in which you want to sort the files to be renamed")
            print("It is normally used after using cd and dir to find the correct directory\n")            
        elif cmd[1] == 'rm' or cmd[1] == 'remove':
            print("rm or remove")
            print("Removes a file from the list so that it will not be renamed\n")
        elif cmd[1] == 'rename':
            print("The final command telling the program that the list is sorted in order, and the name has been set")
            print("Will rename the files, this cannot be undone\n")            
        elif cmd[1] == 'exit':
            print("exit")
            print("Exits the program\n")
        elif cmd[1] == 'reset' or cmd[1] == 'rst':
            print("Reset the program to a starting state.")
        elif cmd[1] == 'shw' or cmd[1] == 'show':
            if len(cmd) == 2:
                print("Show has a variety of subcommands.")
                print("These are \'file\', \'ext\', \'list\', and \'sublist\'")
                print("Type help show <subcommand> for the help on the topic\n")
            else:
                if cmd[2] == 'file':
                    print("show file")
                    print("Shows a list of the file names currently selected by the renamer\n")
                elif cmd[2] == 'ext':
                    print("show ext")
                    print("Shows the extentions of the files currently selected by the renamer\n")
                elif cmd[2] == 'list' or cmd[2] == 'list':
                    print("show list")
                    print("shows the currently ordered renamer list\n")
                elif cmd[2] == 'sublist':
                    print("show sublist")
                    print("Shows the current sublist selected by the \'ins\' command\n")
                else:
                    print("Invalid set subcommand\n type\'help show\' for a list of subcommands\n")
        else:
            print("Help request not recognized")
            print("type help functions")
            print("For a list of functions that help has info on\n")            
            