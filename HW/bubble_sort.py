input_num = list(map(int, input("숫자를 입력하세요.: ").split())) #리스트에 수 입력 받기

print(input_num) #정렬 전 리스트

for i in range(0,len(input_num)): #리스트의 크기만큼 반복
    for j in range(0, len(input_num)-1): 
        if input_num[j] > input_num[j+1]: #현재 인덱스의 값이 다음 인덱스의 값보다 크면 실행
            input_num[j+1], input_num[j] = input_num[j], input_num[j+1] #swap해서 위치 바꾸기
           
print(input_num) #정렬 후 리스트

#feedback
#1. 이중 for문 쓰지 마라
#2. 변수명 길게