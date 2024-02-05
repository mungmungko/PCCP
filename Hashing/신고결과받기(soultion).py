import collections
def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    reportHash = collections.defaultdict(set)
    stoped = collections.defaultdict(int) # 0으로 기본 초기화

    for x in report:
        a, b = x.split(' ')
        reportHash[a].add(b)
        stoped[b] += 1
    
    for name in id_list:
        mail = 0
        for user in reportHash[name]:
            if stoped[user] >= k:
                mail += 1
        
        answer.append(mail)

    return answer