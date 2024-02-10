import math
def solution(fees, records):
    answer = []
    IsIn = [0]*10000
    LastInTime = [0]*10000
    SumTime = [0]*10000
    cars = set()

    for record in records:
        T, car_num, flag = record.split()
        h, m = map(int, T.split(":"))   
        cars.add(int(car_num))

        if flag == 'IN': # 입차일 경우
            LastInTime[int(car_num)] = h*60+m
            IsIn[int(car_num)] = 1
        elif flag == 'OUT': # 출차일 경우
            SumTime[int(car_num)] += h*60+m - LastInTime[int(car_num)]
            IsIn[int(car_num)] = 0
    
    cars = sorted(cars) # 차 번호 오름차순 정렬

    # 출차 기록이 없는 경우 계산
    for car in cars:
        sum_fee = 0
        if IsIn[car] == 1:
            SumTime[car] += (23*60+59) - LastInTime[car]
        
        if SumTime[car] > fees[0]:
            sum_fee += math.ceil((SumTime[car]-fees[0])/fees[2])*fees[3]+fees[1]
        else:
            sum_fee += fees[1]
        
        answer.append(sum_fee)

    return answer

if __name__ == '__main__':
    fees = [180, 5000, 10, 600]
    records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

    print(solution(fees, records))