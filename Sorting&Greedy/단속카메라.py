# 그리디
# 정렬 해놓고, 여기서 가장 좋은 방법을 찾는 법
def solution(routes):
    answer = 1
    routes.sort(key=lambda x: x[1])
    points = routes[0][1]
    for i in range(1, len(routes)):
        if routes[i][0] > points:
            points = routes[i][1]
            answer += 1
    return answer
    
if __name__ == '__main__':
    routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
    print(solution(routes))