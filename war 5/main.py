def remove_smallest(numbers):
    if len(numbers) == 0:
        return numbers
    index = 0
    i = 0
    while i < len(numbers):
        if numbers[i] < numbers[index]:
            index = i
        i += 1
    del numbers[index]
    return numbers

if __name__ == '__main__':
    print(remove_smallest([]))