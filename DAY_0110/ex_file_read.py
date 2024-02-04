#-------------------------------------------------------------------------------
# 파일 입출력 => 출력 즉, 읽기(read)
# - 사용 내장 함수 : open(file, mode = 'rt[기본]', encoding='시스템기본기')
# - encoding 설정: 파일에 적용된 인코딩을 설정해야 함!!
#-------------------------------------------------------------------------------
# (1) open
file = open('message.txt', encoding = 'utf8') # 인코딩=utf8로 설정해야 내용이 나옴
print(f'file = > {type(file), file}')

# (2) IO => read() : 파일 안에 모든 내용 다 읽어오기
'''fdata = file.read()
print(f'data => {type(fdata),fdata }') # 에러: 인코딩을 맞춰줘야함
'''
# (2) IO => read(n) : 지정된 숫자 만큼의 문자를 파일에서 읽어옴
'''fdata = file.read(5) #지정된 숫자 만큼만 문자 읽기(5바이트만 출력되므로 Happy만 출력 됨)
print(f'data => {type(fdata),fdata }')

fdata = file.read(5) #공백 포함 5바이트만 출력되므로 New만 출력 됨 공백도 문자로 취급
print(f'data => {type(fdata),fdata }')'''

# (2) IO => readline(): '\n' 기준으로 한 줄 읽어오기
'''datas=[]
while True:
        fline=file.readline()
        if not fline: break
        print(f'fline => {type(fline)} {fline}', end='')
        datas.append(fline)'''
#print(datas)
# (2) IO => readline(): '\n' 기준으로 한 줄씩 읽은 것을 리스트에 담아서 반환
datas =file.readlines()

print(datas)
# (3) close
file.close()