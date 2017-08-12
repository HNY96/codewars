def tickets(people):
    money = {25:0, 50:0}
    for i in people:
        if i == 25:
            money[25] += 1
        elif i == 50:
            if money[25] > 0:
                money[25] -= 1
                money[50] += 1
            else:
                return 'NO'
        else:
            if money[50] > 0 and money[25] > 0:
                money[50] -= 1
                money[25] -= 1
            elif money[25] > 2:
                money[25] -= 3
            else:
                return 'NO'
    return 'YES'

if __name__ == '__main__':
    print(tickets([25, 25, 100]))