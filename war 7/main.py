import math

def is_prime(num):
    if num <= 1:
        return False
    elif num == 2 or num == 3:
        return True
    else:
        root = math.floor(math.sqrt(num))
        i = 2
        while i <= root:
            if num % i == 0:
                return False
            else:
                i += 1
        return True

if __name__ == '__main__':
    print(is_prime(7))