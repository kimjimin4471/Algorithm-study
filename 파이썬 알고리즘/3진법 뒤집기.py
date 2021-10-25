def threedecimal(n):
    string = ""
    while n >= 3:
        string = str(n % 3) + string
        n = int(n / 3)
    string = str(n) + string
    return string


def decimal(n):
    x = 0
    digit = 1
    while n > 0:
        x += (n % 10) * digit
        n = n // 10
        digit *= 3
    return x


def solution(n):
    ternary = threedecimal(n)
    ternary = int(ternary[::-1])
    answer = decimal(ternary)
    return answer


print(solution(1))
