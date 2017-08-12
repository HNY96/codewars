def order(sentence):
    result = ['', '', '', '', '', '', '', '', '', '']
    if sentence == '':
        return ''
    else:
        process = sentence.split(' ')
        for i in process:
            num = find_num(i)
            result[num] = i
    i = 1
    result_str = ''
    while i < len(result):
        if (result[i] != ''):
            result_str += result[i] + ' '
        i += 1
    return result_str.rstrip();

def find_num(str):
    i = 0
    while i < len(str):
        if (str[i].isdigit()):
            return int(str[i])
        else:
            i += 1

if __name__ == '__main__':
    print(order("is2 Thi1s T4est 3a"))