def solution(id_list, report, k):
    answer = {}
    unique_report = list(set(report))
    dic = {}
    report_num = {}
    for i in id_list:
        dic[i] = []
        report_num[i] = 0
        answer[i] = 0
    for i in unique_report:
        신고자, 신고당한사람 = i.split(" ")
        dic[신고자].append(신고당한사람)
        report_num[신고당한사람] += 1
    for i in report_num:
        if report_num[i] >= k:
            for j in dic:
                if i in dic[j]:
                    answer[j] += 1
    arr = []
    for i in answer:
        arr.append(answer[i])
    return arr

id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 2

print(solution(id_list, report, k))
