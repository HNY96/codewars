def find_it(seq):
    resultDict = {}
    i = 0
    while i < len(seq):
        if (seq[i] not in resultDict):
            resultDict[seq[i]] = 1
        else:
            resultDict[seq[i]] += 1
        i += 1
    values = resultDict.values()
    keys = resultDict.keys()
    resultValues = list(values)
    flag = 0
    for i in resultValues:
        if (i % 2 == 1):
            break
        else:
            flag += 1
    return list(keys)[flag]


if __name__ == '__main__':
    print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))
