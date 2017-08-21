def times(list):
    temp = 1
    for i in list:
        temp *= i
    return temp

def factorial(x):  
    result = 1  
    for i in range(2, x + 1):  
        result *= i  
    return result  

def listPosition(word):
    result = 1
    result = position(word, result)
    return result

def position(word, result):
    if len(word) == 1:
        return result
    letter_dict = {}
    count = 0
    for i in word:
        if i in letter_dict.keys():
            letter_dict[i] += 1
        else:
            letter_dict[i] = 1
        count += 1

    gap = ((factorial(count) / times(factorial(i) for i in letter_dict.values())) * sum(letter_dict[i] for i in letter_dict.keys() if i < word[0])) / sum(letter_dict.values())
    result += gap
    return position(word[1:], result)

if __name__ == '__main__':
    print(listPosition('question'))
