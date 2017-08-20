def solution(roman):
    result = 0
    i = 0
    flag = True
    while i < len(roman):
        if roman[i] == 'M':
            result += 1000
        elif roman[i] == 'D':
            result += 500
        elif roman[i] == 'C':
            if i+1 < len(roman):
                if roman[i+1] == 'D':
                    result += 400
                elif roman[i+1] == 'M':
                    result += 900
                else:
                    result += 100
                    flag = False
                if flag == True:
                    i += 1
            else:
                result += 100
        elif roman[i] == 'L':
            result += 50
        elif roman[i] == 'X':
            if i+1 < len(roman):
                if roman[i+1] == 'L':
                    result += 40
                elif roman[i+1] == 'C':
                    result += 90
                else:
                    result += 10
                    flag = False
                if flag == True:
                    i += 1
            else:
                result += 10
        elif roman[i] == 'V':
            result += 5
        else:
            if i+1 < len(roman):
                if roman[i+1] == 'V':
                    result += 4
                elif roman[i+1] == 'X':
                    result += 9
                else:
                    result += 1
                    flag = False
                if flag == True:
                    i += 1
            else:
                result += 1
        i += 1
        flag = True
    return result

if __name__ == '__main__':
    print(solution('MMVIII'))