def tribonacci(signature,n):
    if n <= 3:
        return signature[0:n]
    else:
        for i in range(n-3):
            signature.append(sum(signature[i:i+3]))
        return signature

if __name__ == '__main__':
    print(tribonacci([1,1,1],10))