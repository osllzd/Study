# 18 break, continue로 반복문 제어하기

# while 에서 break로 반복문 끝내기
i = 0
while True:
    print(i)
    i += 1
    if i ==100:
        break

# for 에서 break로 반복문 끝내기
for i in range(10000):
    print(i)
    if i ==100:
        break

# for에서 continue로 실행 코드 건너뛰기
for i in range(100):
    if i % 2 == 0:
        continue
    print(i)

# while 반복문에서 continue로 코드 실행 건너뛰기
i = 0
while i < 100:
    i += 1
    if i % 2 ==0:
        continue
    print(i)

# 입력한 횟수대로 반복하기
count = int(input('반복할 횟수를 입력하세요: '))
i = 0
while True:
    print(i)
    i +=1
    if i==count:
        break


# 입력한 숫자까지 홀수 출력하기
count = int(input("반복할 횟수를 입력하세요: "))

for i in range(count +1):
    if i % 2 ==0:
        continue
    print(i)

# 18강 연습문제
i = 0
while True:
    if i % 10 != 3:
        i += 1
        continue

    if i>73:
        break
    print(i,end=' ')
    i += 1

# 두 수 사이의 숫자 중 3으로 끝나지 않는 숫자 출력하기
start, stop = map(int,input().split())

i = start

while True:

    if i%10==3:
        i += 1
        continue
    if i>stop:
        break
    print(i,end=' ')
    i += 1

