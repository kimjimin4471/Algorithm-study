# 체육복
def solution(n, lost, reserve):
    answer = 0
    arr = []
    for i in range(0,  n):
        arr.append(1)
    for i in range(0, lost.__len__()):
        arr[lost[i] - 1] -= 1
    for i in range(0, reserve.__len__()):
        arr[reserve[i] - 1] += 1
    for i in range(0, n):
        if i == 0:
            if arr[i] == 0 and arr[i+1] == 2:
                arr[i] = 1
                arr[i+1] = 1
        elif i == n - 1:
            if arr[i] == 0 and arr[i-1] == 2:
                arr[i] = 1
                arr[i-1] = 1
        elif arr[i] == 0:
            if arr[i-1] == 2:
                arr[i-1] = 1
                arr[i] = 1
            elif arr[i+1] == 2:
                arr[i+1] = 1
                arr[i] = 1

    for i in range(0, n):
        if arr[i] >= 1:
            answer += 1
    return answer

print(solution(3, [3], [1]))