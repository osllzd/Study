# ---------------------------------------------------------------
# 파일 데이터 접근 관련 메서드
# ---------------------------------------------------------------
filename = 'message.txt'

with open(filename, mode='r', encoding='utf8') as f:
    f.seek(5)
    print(f.read(10))
    print(f'현재 위치 : {f.tell()}')


    f.seek(0)
    print(f.read(5))
    print(f'현재 위치 : {f.tell()}')

print(f.name,f.closed) # 중간에 닫을 시 끝나지 않았기 때문에 false가 출력이 됨

