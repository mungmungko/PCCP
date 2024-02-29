import sys
from collections import deque

def solution(s, e):
    answer = 0
    queue = deque()
    ch = [0]*10001
    queue.append(s)
    ch[s] = 1
    L = 0
    while queue:
        length = len(queue)
        for _ in range(length):
            v = queue.popleft()
            for nv in [v+1,v-1,v+5]:
                if nv == e:
                    return L+1
                if (0 < nv < 10001) and ch[nv] == 0:
                    queue.append(nv)
                    ch[nv] = 1
        L += 1
    
    return answer


if __name__ == '__main__':
    s, e = map(int, sys.stdin.readline().split())
    solution(s, e)