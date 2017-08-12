def order_weight(strng):
    if strng == '':
        return ''
    temp_result = sorted(map(int, strng.split(' ')), key=lambda i: sum(map(int, str(i))))
    str_array = []
    for i in temp_result:
        str_array.append(str(i))
    i = 0
    while i < len(str_array)-1:
        count = same_weight(str_array, i, len(str_array))
        str_array[i:i+count] = sorted(str_array[i:i+count])
        i += count
    result = []
    for i in str_array:
        result.append(str(i))
    return ' '.join(result)

def same_weight(array, i, length):
    current_weight = sum(map(int, array[i]))
    x = 1
    count = 1
    while i + x < length:
        if sum(map(int, array[i+x])) == current_weight:
            count += 1
            x += 1
        else:
            return count
    return count

if __name__ == '__main__':
    print(order_weight("1 2 200 4 4 6 6 7 7 27 72 18 81 9 91 425 31064 7920 67407 96488 34608557 71899703"))
    print('1 2 200 4 4 6 6 7 7 18 27 72 81 9 91 425 31064 7920 67407 96488 34608557 71899703')