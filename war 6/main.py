def dirReduc(arr):
    result = []
    i = 0
    while i < len(arr):
        if len(result) == 0:
            result.append(arr[i])
            i += 1
        else:
            current = result.pop()
            if ((current == 'NORTH' and arr[i] == 'SOUTH') or (current == 'SOUTH' and arr[i] == 'NORTH') or (current == 'WEST' and arr[i] == 'EAST') or (current == 'EAST' and arr[i] == 'WEST')):
                i += 1
            else:
                result.append(current)
                result.append(arr[i])
                i += 1
    return result

if __name__ == '__main__':
    print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))