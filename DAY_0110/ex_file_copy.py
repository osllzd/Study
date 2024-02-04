# ------------------------------------------------
# 파일 하나 선택 후 복사본 파일 생성 하기
# - 예) message.txt ===> message_copy.txt
# ------------------------------------------------
filename = 'message.txt'

# 1. 원본 파일에 내용을 읽은 후 저장
with open(filename,mode='r',encoding='utf8') as f:
    data=f.read()

# 2. 복사본 파일에 내용 쓰기
with open('message_copy.txt',mode='w',encoding='utf8') as f:
    f.write(data)

# 3. 원본 파일에 내용 읽은 후 새 파일에 바로 저장
with open(filename, mode='r', encoding='utf8') as of:
    with open('message_copy.txt', mode='w', encoding='utf8') as nf:
        nf.write(of.read())


