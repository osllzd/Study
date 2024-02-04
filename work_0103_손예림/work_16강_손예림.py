# 16장 복습 -----------------------------------------------
#for 와 range 사용하기
for i in range(100):
    print('Hello, world')

print()

# 반복분에서 변수의 변화 알아보기
for i in range(100):
    print('Hello, world!', i)
print('-'*50)

# 시작하는 숫자와 끝나는 숫자 지정하기
for i in range(5,12):
    print('Hello world', i)
print('-'*50)

# 증가폭 사용하기
# for 변수 in range(시작, 끝, 증가폭):
for i in range(0, 10, 2):
    print('Hello, world')
print('-'*50)

# 숫자 감소 시키기
for i in range(10,0,-1):
    print('Hello, world!', i)
print('-'*50)

# reversed 이용하기
for i in reversed(range(10)):
    print('Hello, world!', i)
print('-'*50)

# 시퀀스 객체로 반복하기=============================================
#list
a= [10, 20, 30, 40, 50]
for i in a:
    print(i)
print('-'*50)

# Tuple
fruits = ('apple', 'orange', 'grape')
for fruit in fruits:
    print(fruit)
print('-'*50)

# 문자열
for letter in 'python':
    print(letter, end=' ')
print()
print('-'*50)

#reverse 함수를 써서 문자열을 거꾸로 출력하기
for letter in reversed('python'):
    print(letter, end=' ')
print()
print('-'*50)

for i in reversed(range(10,20)):
    print(i)

# 16 연습문제
x = [49, -17, 25, 102, 8, 62, 21]
for i in x:
    print( i*10, end=' ')

# 16 심사문제
dan = input() # 출력할 구구단을 입력받는다.
dan = int(dan) # input 으로 받은 단을 int함수를 써서 정수로 바꿔준다.
for num in range(1,10): #변수 num에 1~10까지의 숫자를 넣어준다.
    print(f'{dan}*{num}={dan * num}') # 출력!
