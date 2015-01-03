def stitch(toName, oldName, num):
    """Function to allow the new name of the file to contain the number at an arbitrary position
    or the old name of the file at an arbitrary position in the string of the new file name."""
    if len(toName) > 0:

        # We have 5 potential parts in the final string that revolve around two points.
        # The points are are the former string and the position of the number.
        # It is not know which of the two points will come first, or either exist.
        # If neither point exists we simply add the number to the end of the string.
        # Else we divide the string into the following parts:
        #
        # part[0] That which comes before the first point.
        # part[1] The first point.
        # part[2] That which is between the first and second point.
        # part[3] The second point.
        # part[4] That which comes after the second point.
        #
        # posNum and posName are the points.
        # We look for them in toName which is the user's input.
        parts = []
        posNum = toName.find('*')
        posName = toName.find('<')

        # Check is the name or the num come first.
        # (Check in which order the points are.)
        if posNum < posName:
            first, second = posNum, posName
            find = 0
        else:
            first, second = posName, posNum
            find = 1

        # Zero the unfound so we don't cause issues with the string copying.
        if first == -1:
            first = 0
        if second == -1:
            second = 0

        # Only copy what is before the first point if there is something.
        if first != 0:
            parts.append(toName[:first])
        else:
            parts.append('')
        parts.append(toName[first])
        parts.append(toName[first+1:second])
        parts.append(toName[second])
        parts.append(toName[second+1:])

        # Add the former string if there is a place for it.
        if posName != -1:
            if find == 0:
                parts[3] = oldName
            else:
                parts[1] = oldName

        # Add the number in its place. Otherwise it will be added at the end later.
        if posNum != -1:
            if find == 0:
                parts[1] = num
            else:
                parts[3] = num

        string = ''

        # Congeal the parts into a usable string.
        for part in parts:
            if part != ' ':
                string += part

        # This will only be true if first and second are 0 (there is no * and <)
        # or one is the first character and the other does not exist.
        # Either way it causes an errant first character (either the first character or repeated symbol)                
        if first == second:
            string = string[1:]

        # If no number place was given then we auto append one.
        if posNum == -1:
            string += num
    else:
        # If the user didn't enter a name we use the number as the new name.
        string = num

    return string
