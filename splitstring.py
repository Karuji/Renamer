def stitch(toName, oldName, num):
    parts = []
    initialString = toName
    posNum = toName.find('*')
    posName = toName.find('%')

    if posNum < posName:
        first, second = posNum, posName
        posNum = 0
    else:
        first, second = posName, posNum
        posNum = 1

    if first == -1:
        first = 0
    if second == -1:
        second = 0

    parts.append(toName[:first])
    parts.append(toName[first])
    parts.append(toName[first+1:second])
    parts.append(toName[second])
    parts.append(toName[second+1:])

    if posName != -1:
        if posNum == 0:
            parts[3] = oldName
        else:
            parts[1] = oldName
    else:
        if posNum == 0:
            parts[3] = ''
        else:
            parts[1] = ''

    if posNum == 0:
        parts[1] = num
    else:
        parts[3] = num

    string = ''

    for part in parts:
        string += part

    return string