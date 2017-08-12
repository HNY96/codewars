def sort_array(source_array):
    if source_array == []:
        return []
    else:
        index = []
        sort_array = []
        i = 0
        while i < len(source_array):
            if source_array[i] % 2 == 1:
                index.append(i)
                sort_array.append(source_array[i])
            i += 1
        sort_array.sort()
        i = 0
        while i < len(index):
            source_array[index[i]] = sort_array[i]
            i += 1
        return source_array

if __name__ == '__main__':
    print(sort_array([5, 3, 2, 8, 1, 4]))