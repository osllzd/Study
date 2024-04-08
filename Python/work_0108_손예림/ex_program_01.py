# ------------------------------------------------------
# 나의 프로그램-계산기
# [ 계산기 ]
# 1. 입력
# 2. 덧셈
# 3. 뺄셈
# 4. 곱셈
# 5. 나눗셈
# 6. 계산 기록
# 7. 검색
# 8. 삭제
# 9. 종료
# ------------------------------------------------------
# 사용자 정의 함수 ---------------------------------------
# 함수 기능: 연산결과 list에서 검색어에 해당하는 데이터만 출력
# 함수 이름: searchResult
# 매개 변수: search
# 함수 결과: None
# ------------------------------------------------------
def searchResult(search):
    cnt = 0
    for calc in calclist:
        if search in calc:
            print(calc)
            cnt += 1
    print(f'{cnt}개 검색결과가 있습니다' if cnt else '검색결과가 없습니다.')

# 계산 기록 저장할 전역변수 선언 --------------------------
calclist = []
while True:

    print('1. 입력')
    print('2. 덧셈')
    print('3. 뺄셈')
    print('4. 곱셈')
    print('5. 나눗셈')
    print('6. 계산 기록')
    print('7. 검색')
    print('8. 삭제')
    print('9. 종료')

    choice = input('메뉴 선택: ')

    if choice.isdecimal():
        if choice =='1':
            data=input('2개 정수: ')
            n1, n2 = list(map(int, data.split()))
        elif choice =='2':
            calclist.append(f'덧셈 결과: {n1} + {n2} = {n1 + n2}\n')
            print(f'{calclist[-1]}\n')
        elif choice == '3':
            calclist.append(f'뺄셈 결과: {n1} - {n2} = {n1 - n2}\n')
            print(f'{calclist[-1]}\n')
        elif choice == '4':
            calclist.append(f'곱셈 결과: {n1} * {n2} = {n1 * n2}\n')
            print(f'{calclist[-1]}\n')
        elif choice == '5':
            calclist.append(f'나눗셈 결과: {n1} / {n2} = {n1 / n2 if n2 else "0으로 나눌 수 없음"}')
            print(f'{calclist[-1]}\n')
        elif choice == '6':
            print('==>계산 기록 출력')
            calclist.sort(reverse=True)
            for calc in calclist:
                print(calc)
        elif choice == '7':
            search=input('검색: ')
            searchResult(search)
        elif choice == '8':
            calclist.clear()
            print('모든 계산 기록이 삭제 되었습니다.')
        elif choice =='9':
            print('종료합니다')
            break


        else:
            print('메뉴 1~6까지 선택.')
    else:
        print('없는 메뉴입니다.')