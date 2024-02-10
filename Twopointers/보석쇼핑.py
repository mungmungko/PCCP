import collections
def solution(gems):
    answer = [0, 0]
    sH = collections.defaultdict(int)
    k = len(set(gems))
    lt = 0
    maxL = 1000000

    for rt in range(len(gems)):
        sH[gems[rt]] += 1
        while(len(sH) == k):
            if rt-lt+1 < maxL:
                maxL = rt-lt+1
                answer = [lt+1, rt+1]
            sH[gems[lt]]-=1
            if sH[gems[lt]] == 0: # 0이되면 dict 원소인 lt를 제거시켜줘야 함
                del sH[gems[lt]]
            lt +=1
    return answer

if __name__ == '__main__':
    # gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
    # gems = ["AA", "AB", "AC", "AA", "AC"]
    # gems = ["XYZ", "XYZ", "XYZ"]
    gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
    print(solution(gems))