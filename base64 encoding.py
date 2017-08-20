def to_base_64(string):
    bit_str = ''
    base64_str = ''
    flag = 0
    for i in string:
        ascii_num = ord(i)
        bit_str += bin(ascii_num)[2:].zfill(8)
    if len(string) % 3 == 1:
        bit_str += ''.zfill(16)
        flag = 1
    elif len(string) % 3 == 2:
        bit_str += ''.zfill(8)
        flag = 2

    for i in range(0, len(bit_str), 6):
        index = int(bit_str[i:i+6], 2)
        if index < 26:
            base64_str += chr(index+65)
        elif index < 52:
            base64_str += chr(index+71)
        elif index < 62:
            base64_str += chr(index-4)
        elif index == 62:
            base64_str += '+'
        elif index == 63:
            base64_str += '/'
    
    if flag == 1:
        return base64_str[:-2] + '=='
    elif flag == 2:
        return base64_str[:-1] + '='
    else:
        return base64_str

def from_base_64(string):
    bit_str = ''
    result = ''
    for i in string:
        ascii_num = ord(i)
        if ascii_num >= 65 and ascii_num <= 90:
            index = ascii_num - 65
        elif ascii_num >= 97 and ascii_num <= 122:
            index = ascii_num - 71
        elif ascii_num >= 48 and ascii_num <= 57:
            index = ascii_num + 4
        elif ascii_num == 43:
            index = 62
        elif ascii_num == 47:
            index = 63
        else:
            continue
        bit_str += bin(index)[2:].zfill(6)
    
    for i in range(0, len(bit_str), 8):
        temp_bit = bit_str[i:i+8]
        ascii_num = int(temp_bit, 2)
        result += chr(ascii_num)

    return result

if __name__ == '__main__':
    print(to_base_64('I have a dream'))
    print(from_base_64('SSBoYXZlIGEgZHJlYW0='))