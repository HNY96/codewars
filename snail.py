def snail(a):
    l = len(a[0])
    if l == 0:
        return []
    up = 0
    left = 0
    bottom = l - 1
    right = l - 1
    result = []
    result.extend(a[0])
    i = l - 1
    up += 1
    while i > 0:
        for x in range(up, bottom+1):
            result.append(a[x][right])
        right -= 1
        for x in range(right, left-1, -1):
            result.append(a[bottom][x])
        bottom -= 1
        i -= 1
        if i == 0:
            break
        for x in range(bottom, up-1, -1):
            result.append(a[x][left])
        left += 1
        for x in range(left, right+1):
            result.append(a[up][x])
        up += 1
        i -= 1
    return result


if __name__ == '__main__':
    print(snail([[1,2,3],[4,5,6],[7,8,9]]))
