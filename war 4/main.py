def namelist(names):
    if len(names) == 0:
        return ''
    elif len(names) == 1:
        return names[0]['name']
    elif len(names) == 2:
        return names[0]['name'] + ' & ' + names[1]['name']
    else:
        result = ''
        i = 0
        while i < len(names)-2:
            result += (names[i]['name'] + ', ')
            i += 1
        result += (names[i]['name'] + ' & ' + names[i+1]['name'])
        return result

if __name__ == '__main__':
    print(namelist([]))