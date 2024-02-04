#--------------------------------------------------------
# 전역 변수(Global Variable)와 지역 변수(Local Variable)
# - 함수 내에서 전역 변수 값 변경 하고자 하는 경우는 추가 코드 필요
# - 추가 코드: global 전역 변수명
# -> 주의: 전역변수 값이 언제든지 함수로 변경이 될 수 있는 상황
#          사용 시 주의 필요
# 지역 변수(Local Variable)
#   - 함수에 존재 하는 변수
#   - 함수에서만 사용 가능한 변수
#   - 함수가 종료되면 변수들은 메모리에서 사라짐
#--------------------------------------------------------
# 사용자 정의 함수 ----------------------------------------
def currentDate(year, month, day):
    # year, month, day => 지역 변수
    print(f'Today: {year}/{month:0>2}/{day: 0>2}')

def currentDate2(month, day):
    # month, day => 지역 변수
    # year => 전역 변수
    # 함수 내에서 전역 변수 값을 변경하고자 하는 경우는 global 전역변수명
    global year
    year = year + 10
    print(f'Today: {year}/{month:0>2}/{day: 0>2}')

# 전역변수---------------------------------------------------
year, month, day = 2024, 1, 8


# 변수 값 확인 출력 ------------------------------------------
print(f'year: {year}, month: {month} day: {day}')
currentDate2(month,day)
print(f'year: {year}, month: {month} day: {day}')
