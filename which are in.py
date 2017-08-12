def in_array(array1, array2):
    result = []
    for sub_str in array1:
        for str in array2:
            if sub_str in str and sub_str not in result:
                result.append(sub_str)
                break
    return sorted(result)


if __name__ == '__main__':
    a1 = ["live", "arp", "strong"]
    a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
    r = ['arp', 'live', 'strong']
    print(in_array(a1, a2))
    print(r)