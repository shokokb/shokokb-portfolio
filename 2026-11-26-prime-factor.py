def prime_factors(n: int) -> list[int]:
    ret = []
    for i in range(2, n+1):
        if i * i > n:
            break
        while n % i == 0:
            ret.append(i)
            n //= i
    if n > 1:
        ret.append(n)
    return ret