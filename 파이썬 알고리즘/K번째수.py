# K번째수
def solution(array, commands):
    answer = []
    for i, j, k in commands:
        box = array[i - 1:j]
        box.sort()
        answer.append(box[k-1])
    return answer


b = [1, 5, 2, 6, 3, 7, 4]
a = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(b, a))