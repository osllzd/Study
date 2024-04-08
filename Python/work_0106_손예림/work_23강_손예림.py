# for와 range 사용하기
a =[[10, 20],[30, 40],[50, 60]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=' ')
    print()

# while 반복문을 한번 사용하기
a =[[10, 20],[30, 40],[50, 60]]
i = 0
while i <len(a): #a의 길이 3 세로 길이
    x,y=a[i] # i에 들어갈 요소 x,y
    print(x,y)
    i += 1
# while 반복문을 두번 사용하기
a =[[10, 20],[30, 40],[50, 60]]
i = 0
while i < len(a):
    j = 0
    while j < len(a[i]):
        print(a[i][j], end=' ')
        j += 1
    print()
    i +=1


# 반복문으로 리스트 만들기
#   for 반복문으로 1차원 리스트 만들기
a = [] # 빈 리스트 생성
for i in range(10): # 10번 반복함
    a.append(0) # 리스트에 0을 추가
print(a)

# for 반복문으로 2차원 리스트 만들기
a = [] #빈 리스트 생성
for i in range(3): # 세번 반복
    line = [ ] #안쪽 리스트로 사용할 빈 리스트 생성
# 빈 리스트가 세개 생김
    for j in range(2): # 두번 반복
        line.append(0) # 안쪽 리스트 line에 0을 추가
    a.append(line) #전체의 빈 리스트에 line 리스트를 추가
print(a)

# 리스트 표현식으로 2차원 리스트 만들기
a = [[0 for j in range(2)] for i in range(3)]
print(a)
b= [[0] * 2 for i in range(3)]
print(b)

# 톱니형 리스트 만들기
a = [3, 1, 2, 2, 5] # 가로 크기를 저장한 리스트
b = [] # 빈 리스트 생성
for i in a : #가로 크기를 저장한 리스트로 반복
    line = [] # 안쪽 리스트로 사용할 빈 리스트 생성
    for j in range(i):# 리스트a에 저장된 가로 크기 만큼 반복
        line.append(0) #안쪽 리스트에 0추가
    b.append(line) #빈리스트에 안쪽리스트 추가

print(b)

a = [[0]*i for i in [3,1,3,2,5]]
print(a)

# 2차원 리스트의 할당과 복사 알아보기
a=[[10,20],[30,40]]
b = a
b[0][0]=500
print(a)
print(b)

a=[[10,20],[30,40]]
b=a.copy()
b[0][0]=500
print(a)
print(b)

# 연습문제 - 3차원 리스트 만들기
# 높이 2, 세로크기 4, 가로크기 3인 3차원 리스트 만들기 => 리스트 표현식 사용
a= [[[0 for col in range(3)]for row in range(4)] for depth in range(2)]
# col - 가로 / row - 세로 / depth - 높이
print(a)