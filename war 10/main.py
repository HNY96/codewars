def find_nb(m):
    result = 0
    i = 1
    while result < m:
        result += i*i*i
        i += 1
    if result == m:
        return i-1
    else:
        return -1

if __name__ == '__main__':
    print(find_nb(4183059834009))
    