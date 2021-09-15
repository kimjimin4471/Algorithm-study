# 위장

def solution(clothes):
    answer = 1
    clothes_dic = {}
    for i, j in clothes:
        clothes_dic[j] = 0

    for i, j in clothes:
        clothes_dic[j] += 1

    for i in clothes_dic:
        answer *= clothes_dic[i] + 1
    return answer - 1


print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))
