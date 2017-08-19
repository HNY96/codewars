def primeFactors(n):
    prime_factors = []
    fac = 2
    while fac * fac <= n:
        while n % fac == 0:
            prime_factors.append(fac)
            n //= fac
        fac += 1
    if n > 1:
        prime_factors.append(n)
    index = 0
    result = ''
    while index < len(prime_factors):
        m = prime_factors.count(prime_factors[index])
        if m == 1:
            result += '({})'.format(prime_factors[index])
        else:
            result += '({}**{})'.format(prime_factors[index], m)
        index += m
    return result

if __name__ == '__main__':
    print(primeFactors(7775460))