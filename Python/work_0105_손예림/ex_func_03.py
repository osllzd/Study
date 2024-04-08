# ---------------------------------------------------------------------
# 다양한 함수의 형태 - (2) 반환값 없는 함수

# - 함수 생성 문법
# def 함수이름(매개변수1, 매개변수2, ..., 매개변수):
#     실행코드
#     실행코드
# ---------------------------------------------------------------------
# 함수 기능: 2개의 정수를 덧셈 후 출력
# 함수 이름: addTwo
# 매개 변수: x, y
# 반 환 값:없음
# ---------------------------------------------------------------------
def addTwo(x,y):
    value=x+y
    print(f'{x}+{y}={value}')

# 함수 사용 즉 함수 호출--------------------------------------------------
addTwo(10,3)

# 함수 호출 시에 매개변수 갯수와 동일하게 데이터 전달해야 함 ------------------
#addTwo(10)
#addTwo(10, 10, 10)
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# 함수 기능: 영어 단어를 입력 받아서 모두 대문자로 변환해주는 기능
# 함수 이름: ConvertCase
# 매개 변수: word
# 반 환 값:없음 => 함수가 아무 일을 안하게 됨 =>return 하기
# ---------------------------------------------------------------------
def ConvertCase(word):
    return word.upper()


# ---------------------------------------------------------------------
# 함수 기능: 시퀀스 객체의 모든 원소를 대문자로 변환해주는 기능
# 함수 이름: ConvertCase2
# 매개 변수: str 타입의 원소로 구성된 list
# 반 환 값:없음
# ---------------------------------------------------------------------
def convertCase2(datalist):
    for data in datalist:
        data.upper
# 첫번째 방법
    for idx in range(len(datalist)): #datalist의 길이를 가져옴
        datalist[idx] = datalist[idx].upper()

# 두번째 방법
#2.    for idx, data in enumerate(datalist):
#        datalist[idx] = data.upper()

datas=['Apple' , 'Banana', 'Mango']
#for data in datas:
#    print(data,data.upper())
#for idx in range(len(datas)):
#    datas[idx]=datas[idx].upper()

for idx, data in enumerate(datas):
    datas[idx]=data.upper()

print(datas)

# 함수 사용 즉, 함수 호출--------------------------------------------------------
datas=['Apple' , 'Banana', 'Mango']

print(f'[BF] {datas}')

convertCase2(datas)

print(f'[AF]{datas}')

