import itertools

def solution(numbers):
    ls = [n for n in numbers]
    answer = []
    asdd = []
    for i in range(1, len(numbers) + 1):
        asdd += list(itertools.permutations(ls, i))
    asd = [int("".join(p)) for p in asdd]

    for i in asd:
        if i < 2:
            continue
        check = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                check = False
                break
        if check:
            answer.append(i)

    return len(set(answer))

print(solution("17"))