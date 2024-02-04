#--------------------------------------------
# [질문] 10명의 학생에 대한 학점을 저장하기
# - 학생의 이름과 학점
#--------------------------------------------
# 방법 1) 학생 이름 변수 5개 => stdName1 ~ stdName5
#        학점 변수 5개     => stdScore1 ~ stdScore5

# 방법 2) 학생 이름 변수 5개 => stdNames=[학생이름1, ...., 학생이름5]
#        학점 변수 5개     => stdScores=[점수1,...,점수5]
stdNames=['std01','std02','std03','std04','std05']
stdScores=[ 90, 88, 75, 100, 64 ]

# => 학번 03번 학생의 학번과 점수를 출력하시오.
idx=stdNames.index('std03')

print(f'{stdNames[idx]}학번 학생의 점수: {stdScores[idx]}')

# 방법 3) 학생 이름 변수 5개 => stdNames=[학생이름1, ..., 학생이름5]
#        학점 변수 5개 => stdScores=[점수1, ..., 점수5]
stdNumsscore=[['std01',90], ['std02',88], ['std03',75], ['std04',100], ['std05',34]]

#---------------------------------------------------------------------------
# dict 자료형
# - 연관되어 있는 데이터를 하나로 묶어서 저장하는 방식 -> 연관배열
# - 형태 => 키 : 데이터   (예:주민번호:이름, 학번: 전공)
# - 조건 => 키가 중복 되면 안됨!
# - 문법 => {키1: 데이터, 키2: 데이터, ..., 키N:데이터N}
#---------------------------------------------------------------------------
stdNumsscore={'std01':90, 'std02':88, 'std03':75, 'std04':100, 'std05':64}

print(f'stdNumsscore:{len(stdNumsscore)}개, {type(stdNumsscore)},{stdNumsscore}')

# 원소 읽는 방법 => 변수명[키]
print(f'stdNumsscore["std03"] => {stdNumsscore["std03"]}')

# 마지막 원소 지정하는 -1 사용 ==> -1에 대한 키가 없으면 Error 발생
# print(f'stdNumsscore[-1] => {stdNumsscore[-1]}')

#----------------------------------------------------------------------
# 원소/요소 추가 방법 => 변수명[새로운 키] = 데이터
#----------------------------------------------------------------------
# 학번 10인 학생의 점수 99.8 저장 즉 추가하기
stdNumsscore['std10']=99.8
print(f'stdNumsscore:{len(stdNumsscore)}개,{stdNumsscore}')

#----------------------------------------------------------------------
# 원소/요소 데이터 변경 => 변수명[기존 키] = 데이터
#----------------------------------------------------------------------
# 학번 10인 학생의 점수 99점으로 변경
stdNumsscore['std10']=99
print(f'stdNumsscore:{len(stdNumsscore)}개,{stdNumsscore}')

#----------------------------------------------------------------------
# 원소/요소 데이터 삭제 => del 변수명[키] 또는 del(변수명[키])
#----------------------------------------------------------------------
del stdNumsscore['std10']
print(f'stdNumsscore:{len(stdNumsscore)}개,{stdNumsscore}')

del stdNumsscore['std02']
print(f'stdNumsscore:{len(stdNumsscore)}개,{stdNumsscore}')

#del stdNumsscore['std']
#print(f'stdNumsscore:{len(stdNumsscore)}개,{stdNumsscore}')







