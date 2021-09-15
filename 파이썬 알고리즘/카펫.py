def solution(brown, yellow):
    answer = []
    for w in range(1, 5001):
        for h in range(w+1):
            if (w * 2) + (h - 2) * 2 == brown:
                if w * h - brown == yellow:
                    answer.append(w)
                    answer.append(h)
                    break
    return answer


print(solution(24, 24))
