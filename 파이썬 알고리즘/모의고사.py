# 모의고사
def solution(answers):
    answer = []
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a1 = 0
    a2 = 0
    a3 = 0
    for i in range(0, answers.__len__()):
        if s1[i % 5] == answers[i]:
            a1 += 1
        if s2[i % 8] == answers[i]:
            a2 += 1
        if s3[i % 10] == answers[i]:
            a3 += 1
    arr = [a1, a2, a3]
    a = max(arr)
    for i in range(0, arr.__len__()):
        if arr[i] == a:
            answer.append(i+1)
    return answer

print(solution([1,3,2,4,2]))
