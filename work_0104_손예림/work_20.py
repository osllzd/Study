# fizzbuzz 문제 출력하기

# 3의 배수일 때와 5의 배수일 때 처리하기
for i in range(1,101):
    if i % 3 ==0:
        print('Fizz')
    elif i % 5 ==0:
        print('Buzz')
    else:
        print(i)
# 3과 5의 공배수 처리하기
# 연산자 and 사용
for i in range(1,101):
    if i % 3 == 0 and i % 5 ==0: #and 사용 x => if i % 15 ==0:
        print('FizzBuzz')
    elif i % 3 ==0:
        print('Fizz')
    elif i % 5 ==0:
        print('Buzz')
    else:
        print(i)

# 코드 단축하기
for i in range(1, 101):
    print('Fizz' * ( i % 3 == 0) + 'Buzz'*(i % 5 ==0) or i)

# 18 연습문제
for i in range(1,101):
    if i % 2 ==0 and i % 11 ==0:
        print('Fizzbuzz')
    elif i % 2 ==0:
        print('Fizz')
    elif i % 11 ==0:
        print('Buzz')
    else:
        print(i)

# 심사문제

start, stop = map(int,input().split())
i = start
while True:
    if i>stop: break
    print('Fizz' * (i % 5 == 0) + 'Buzz' * (i % 7 == 0) or i)

    i += 1

