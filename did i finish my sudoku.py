def done_or_not(b):
    for i in range(9):
        if sum(b[i]) != 45:
            return 'Try again!'
    result = 0
    for i in range(9):
        for j in range(9):
            result += b[j][i]
        if result != 45:
            return 'Try again!'
        result = 0
    for i in range(3):
        for j in range(3):
            result += sum(b[3*i][3*j:3*(j+1)])
            result += sum(b[3*i+1][3*j:3*(j+1)])
            result += sum(b[3*i+2][3*j:3*(j+1)])
            if result != 45:
                return 'Try again!'
            result = 0
    return 'Finished!'

if __name__ == '__main__':
    print(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]))