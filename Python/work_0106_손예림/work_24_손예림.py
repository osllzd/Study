print('%.2f'%2.3)
print('%.3f'%2.3)

# format 메서드로 문자열 정렬하기 '{인덱스:<길이}'.format(값)
print('{0:<10}'.format('python'))  #왼쪽으로 정렬하고 남는 공간 공백 채움
print('{0:>10}'.format('python')) #오른쪽으로 정렬하고 남는 공간 공백 채움

# 숫자 개수 맞추기
# '%0개수d'%숫자
# '{인덱스:0개수d}'.format(숫자)

print('%03d' % 1)
print('{0:03d}'.format(35))
print('%04d' % 1)

# '%0개수.자릿수f % 숫자
# '{인덱스:0개수.자릿수f}.format(숫자)

print('%08.2f'% 3.6)
print('%08.3f'% 3.6)
print('{0:08.3f}'.format(3.6))

# 채우기와 정렬을 조합해서 사용하기
# '{인덱스:[채우기][정렬][길이][.자릿수][자료형]}'
print('{0:0<10}'.format(15)) # 길이 10 왼쪽으로 정렬, 남는 공간 0으로 채움
print('{0:0>10}'.format(15)) # 길이 10 오른쪽으로 정렬, 남는 공간 0으로 채움
print('{0:0>10.2f}'.format(15)) # 길이 10 오른쪽으로 정렬, 소수점 자릿수 2자리
print('{0: >10}'.format(15)) # 남는 공간 공백으로 채움
print('{0:>10}'.format(15)) # 채우기 부분 생략하면 공백이 들어감
print('{0:x>10}'.format(15)) # 남는 공간 문자 x로 채움

# 24 심사문제
x = input().split()
count = 0
for words in x:
    if words.strip(',.') == 'the':
        count += 1
print(count)