# -------------------------------------------------------------------
# 참조형 변수 => 데이터의 주소 저장
# -------------------------------------------------------------------

num = 12
print(f'num=>{id(num)}, {type(num)}')

num = 3
print(f'num=>{id(num)}, {type(num)}')

num = 'good'
print(f'num=>{id(num)}, {type(num)}')

num1=[]
print(f'num=>{id(num)}, {type(num)}')

num2 = [11,12,1]
print(f'num2=>{id(num2)}, {type(num2)}')
print(f'num2=>{id(num2[0])}, {type(num2[0])}')
print(f'num2=>{id(num2[1])}, {type(num2[1])}')

print('=======================값 변경=================\n')

num = 'Happy'
print(f'num=>{id(num)}, {type(num)}')

num2[0]=100
print(f'num2=>{id(num2)}, {type(num2)}')
print(f'num2=>{id(num2[0])}, {type(num2[0])}')

# 원소가 바뀐다고 해서 리스트가 바뀌진 않음

num2=num1
print(f'num2=>{id(num2)}, {num2}')
print(f'num1=>{id(num1)}, {num1}')