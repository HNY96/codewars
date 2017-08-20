def lcs(x, y):
    lenx = len(x)
    leny = len(y)
    route = [[0 for col in range(leny+1)]for row in range(lenx+1)]
    for i in range(1, lenx+1):
        for j in range(1, leny+1):
            if x[i-1] == y[j-1]:
                route[i][j] = route[i-1][j-1] + 1
            else:
                route[i][j] = max(route[i-1][j], route[i][j-1])
    result = printlcs(x, y, route)
    return result[::-1]

def printlcs(x, y, route):
    result = ''
    i = len(x)
    j = len(y)
    while i != 0 and j != 0:
        if x[i-1] == y[j-1]:
            result += x[i-1]
            i -= 1
            j -= 1
        else:
            if route[i][j-1] > route[i-1][j]:
                j -= 1
            else:
                i -= 1
    return result

if __name__ == '__main__':
    print(lcs('abcdef', 'abf'))