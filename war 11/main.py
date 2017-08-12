def duplicate_count(text):
    i = 0
    result_dict = {}
    text = text.lower()
    while i < len(text):
        if text[i] not in result_dict.keys():
            result_dict[text[i]] = 1
        else:
            result_dict[text[i]] += 1
        i += 1
    value_list = result_dict.values()
    count = 0
    i = 0
    while i < len(value_list):
        if value_list[i] > 1:
            count += 1
        i += 1
    return count

if __name__ == '__main__':
    print(duplicate_count('abcdea'))
