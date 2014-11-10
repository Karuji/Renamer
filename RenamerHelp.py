def help(cmd):
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
            if len(cmd) == 2:
                print("Set has a variety of sub commands.")
                print("These are name, start, and zfill")
                print("Type help set <subcommand> for the help on the topic")
                print()
            else:
                if cmd[2] == "name":
                    print("set name")
                    print("Sets the name of the listed output with * being the position of the number")
                    print("It can be left blank if you want the list to simply be numbers")
                    print("If no * is placed then the number will be placed at the end without a space")
                    print("% may be placed in the name to use the current name of the file")
                    print("So if you wanted to prepend the current file with a number you can use:")
                    print("\'set name * %\'")
                    print()
                elif cmd[2] == "start":
                    print("set start")
                    print("Sets the number at which the list will start the renaming")
                    print("By default the renaming starts at 1, using start you can set this to any integer")
                    print("Start does not affect the numbers which are used for input")
                    print()
                elif cmd[2] == "zfill":
                    print("set zfill")
                    print("Sets the amount of zeros (0) that are placed before the number")
                    print("zfill can only increase the number of zeros")
                    print("zfill works for the number of characters in the item as oppose only the number of zeros")
                    print("If you had a list of 8 items and wanted a zero befor the item you would use:")
                    print("\'set zfill 2\'")
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
            