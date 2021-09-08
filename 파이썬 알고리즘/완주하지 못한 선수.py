# 완주하지 못한 선수
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for i in range(0, completion.__len__()):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    if answer == '':
        answer = participant[participant.__len__()-1]
    return answer


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))