import sys
from collections import deque

def solution(s, e):
    answer = 0
    ch = [0]*10001 # 인덱스 번호가 10000까지 있으므로
    dQ = deque()
    dQ.append(s)
    ch[s] = 1


if __name__ == '__main__':
    s, e = map(int, sys.stdin.readline().split())