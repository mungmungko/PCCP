def solution(id_list, report, k):
    # 딕셔너리 초기화
    reports_receive ={id: 0 for id in id_list} # 각 사용자가 받은 신고 횟수
    reports_made = {id: set() for id in id_list} # 각 사용자가 만든 신고

    for r in report:
        reporter, reported = r.split()
        
        if reported not in reports_made[reporter]:
            reports_receive[reported] += 1
            reports_made[reporter].add(reported)
    

    # 정지된 사용자 식별(중괄호를 사용해서 중복 없이 유니크한 요소들만 가지는 집합)
    suspened_users = {user for user, count in reports_receive.items() if count >= k}

    # 각 사용자가 받을 정지 통지 수 계산
    result = [len(reports_made[user].intersection(suspened_users)) for user in id_list]

    return result