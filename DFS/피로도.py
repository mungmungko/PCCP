answer = 0
def DFS(k, cnt, dungeons, ch):
    global answer
    answer = max(answer, cnt)
    for i in range(len(dungeons)):
        if k >= dungeons[i][0] and ch[i] == 0:
            ch[i] = 1
            DFS(k-dungeons[i][1], cnt+1, dungeons, ch)
            ch[i] = 0

def solution(k, dungeons):
    ch = [0]*len(dungeons)
    DFS(k, 0, dungeons, ch)

    return answer

if __name__ == '__main__':
    k = 80 # 현재 피로도
    dungeons = [[80,20],[50,40],[30,10]]
    print(solution(k, dungeons))