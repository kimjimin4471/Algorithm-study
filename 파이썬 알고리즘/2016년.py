def solution(a, b):
    week = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 0
    for i in range(a - 1):
        day += month[i]
    day += b
    return week[day % 7]


print(solution(1, 1))
