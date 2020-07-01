n = int(input('작업 수를 입력하세요 : ')) 
m = int(input('작업 번호를 입력하세요 : ')) 
priority = list(map(int(input('작업 우선순위를 입력하세요 : ').split())))
num = list(range(len(priority))) 
time = 0

while True:
    if priority[0] == max(priority): 
        time += 1
        if num[0] == m:
            print('작업 소요 시간은', time, '분 입니다')
            break
        else:
            num.pop(0)
            priority.pop(0)
    else:
        num.append(num.pop(0))
        priority.append(priority.pop(0))
