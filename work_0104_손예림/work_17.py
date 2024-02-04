# 초깃값을 1부터 시작하기
i = 1
while i <= 100:
    print('Hello, world!',i)
    i += 1

# 초깃값을 감소시키기
i = 100
while i > 0:
    print('Hello, wolrd!', i)
    i -= 1

# 입력한 횟수대로 반복하기
count = int(input("반복할 횟수를 입력하세요: "))
i = 0
while i < count:
    print('Hello, wolrd!', i)
    i +=1

# 초깃값을 받은 뒤 초깃값 만큼 출력하기
count = int(input("반복할 횟수를 입력하세요: "))
while count>0:
    print('Hello, wolrd',count)
    count -=1

#===============================================================
# 17강 연습문제
i = 2 # 시작값
j = 5 # 시작값
while i<=32 or j>=1:
    print(i,j)
    i *= 2
    j -= 1
# 17강 심사문제
money = int(input())
while money>0:
    money -=1350

    if money <0:
        break
    print(money)
#================================================================
