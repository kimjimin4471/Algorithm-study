def solution(N, stages):
    dic = {}
    k = len(stages)
    for stage in range(1, N + 1):
        if k != 0:
            cnt = stages.count(stage)
            dic[stage] = cnt / k
            k -= cnt
        else:
            dic[stage] = 0
    return sorted(dic, key=lambda x: dic[x], reverse=True)


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
