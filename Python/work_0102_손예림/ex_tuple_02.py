#------------------------------------------------------
# 튜플과 리스트
#------------------------------------------------------
myData=(10, 20, ['Hong', 30], ('KIM', 12))

# 튜플의 원소/요소 갯수 확인 함수 => len()
print(f'myData 원소 수: {len(myData)}개')

# 인덱스 범위
print(f'myData 인덱스: 0~{len(myData)-1}')

# 튜플에서 원소/요소 데이터 읽기
print(f'myData : {type(myData[2])}')
print(f'myData : {type(myData[3])}')
print(f'myData : {type(myData[0])}')

# 튜플에서 0번쨰 원소의 데이터를 변경하기
#myData[2]='Ten'        #튜플의 2번째 요소 변경 => 미지원
myData[2][0]='PARK'
print(myData)

#---------------------------------------------------
# 튜플과 연산
#---------------------------------------------------
# 1-10 범위에서 2의 배수로 구성된 정수 튜플 1개 => two
# 1-10 범위에서 5의 배수로 구성된 정수 튜플 1개 => five
two = tuple(range(2,11,2))
five = tuple(range(5,11,5))
print(two+five, two, five, sep='\n')

print(two*2, two, sep='\n')
