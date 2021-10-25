def change_k(n, k):
    arr = ''
    while n > 0:
        arr = str(n % k) + arr
        n //= k
    return arr

def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(2*i, n, i):
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]

def solution(n, k):
    answer = 0
    n_to_k = change_k(n, k)
    n_to_k = list(map(int, n_to_k.split('0')))
    n_to_k = list(set(n_to_k))
    n_to_k.sort(reverse=True)
    arr = prime_list(n_to_k[0]+1)
    for i in n_to_k:
        if i in arr:
            answer += 1
    return answer


print(solution(110011, 10))
