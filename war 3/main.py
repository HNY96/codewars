def find_outlier(integers):
    i = 0
    while i < len(integers):
        if (integers[i] % 2) ^ (integers[i+1] % 2) == 1:
            if i != 0:
                return integers[i+1]
            else:
                if (integers[0] % 2) == (integers[2] % 2):
                    return integers[1]
                else:
                    return integers[0]
        else:
            i += 1

if __name__ == '__main__':
    print(find_outlier([17, 18, 20]))