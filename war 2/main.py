def digital_root(n):
    if (n > 9):
        n = str(n)
        result = 0
        for i in n:
            result += int(i)
        return digital_root(result)
    else:
        return n

if __name__ == '__main__':
    print(digital_root(167))