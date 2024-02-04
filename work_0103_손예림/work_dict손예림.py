# 12 연습문제
camille = {'health': 575.6,'health regen': 1.7,'mana': 338.0,'mana regen' : 1.63,'melee': 125,
'attack_damage': 60,'attack_speed': 0.625,'armor': 26,'magic resistance': 32.1,'movement _speed': 340}
print(camille['health'])
print(camille['movement _speed'])

# 심사문제------------------------------------------------------
# 문자열 여러개의 실수 숫자 여러개를 두 줄로 입력 받기
# - 첫번째 입력 받은 값은 Key
# - 두번째 입력 받은 값은 Value
# - 딕셔너리로 저장
#--------------------------------------------------------------
twoData = input("문자열 4~5개, 실수, 숫자 4~5개를 두 줄로 입력\n단, 문자열과 실수 갯수는 동일\n: ")

# key와 value로 데이터 분리
keys, values=twoData.split(' , ') # aa, bb, cc, dd, 1.1, 2.2, 3.3, 4.4
keys = keys.split()               # aa, bb, cc, dd
values = values.split()           # 1.1, 2.2, 3.3, 4.4

# 입력 데이터 존재 여부 체크
if (len(keys) == 4 and len(values)==4) or (len(keys)==5 and len(values)==5):
    print('입력ok')
    dataDict={ }
    if len(keys) == 4:
        dataDict[keys[0]] = values[0]
        dataDict[keys[1]] = values[1]
        dataDict[keys[2]] = values[2]
        dataDict[keys[3]] = values[3]
    else:
        dataDict[keys[0]] = values[0]
        dataDict[keys[1]] = values[1]
        dataDict[keys[2]] = values[2]
        dataDict[keys[3]] = values[3]
        dataDict[keys[4]] = values[4]

    print(f'datadict => {dataDict}')
else:
    print('입력된 갯수가 다릅니다.')