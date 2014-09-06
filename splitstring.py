def stitch(toName, oldName, num):
    parts = []
    initialString = toName
    posNum = toName.find('*')
    posName = toName.find('%')

    if posNum < posName:
        first, second = posNum, posName
        find = 0
    else:
        first, second = posName, posNum
        find = 1

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
        if find == 0:
            parts[3] = oldName
        else:
            parts[1] = oldName
    else:
        if find == 0:
            parts[3] = ''
        else:
            parts[1] = ''

    if find == 0:
        parts[1] = num
    else:
        parts[3] = num

    string = ''

    for part in parts:
        string += part

    if posNum == -1:
        string += num

    return string