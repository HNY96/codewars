def pig_it(text):
    process = text.split(' ')
    result = ''
    for i in process:
        if i[-2:] == 'ay' and (i[-3:-2] == '!' or i[-3:-2] == '?'):
            result += i[-3:-2]
        elif i[-2:] == 'ay':
            result += i + ' '
        else:
            result += i[1:] + i[0:1] + 'ay '
    return result.rstrip();

if __name__ == '__main__':
    print(pig_it('uisQay ustodietcay psosiay ustodescay ?ay'))
    print('uisQay ustodietcay psosiay ustodescay ?')