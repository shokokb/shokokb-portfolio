import math

def generate_primes(n: int) -> list[int]:
    ret = []
    # ①長さ n + 1 の真偟値リストを作る。
    is_prime = [True] * (n + 1)
    # ② 0と1を False にする。
    is_prime[0] = is_prime[1] = False
    # ③ 2から√nまで順番に調べる。
    for p in range(2, int(math.sqrt(n)) + 1):
        if is_prime[p]:
            # ④ True なら、その数の二乗から倍数を False にする。
            for m in range(p * p, n + 1, p):
                is_prime[m] = False
    # ⑤ 最後に True のインデックスをリストにして返す。
    for i in range(n + 1):
        if is_prime[i]:
            ret.append(i)
    return ret
