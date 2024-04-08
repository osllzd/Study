# 연습문제
maria = {'korean': 94, 'english': 91, 'mathmatics': 89, 'science': 83}
average = sum(maria.values()) /4 # 또는 sum(maria.values()) / len(maria) 키의 갯수를 길이로 생각함
print(average)

# 심사문제
keys = input().split()
values = map(int,input().split())
x = dict(zip(keys,values))
x = {keys: values for keys, values in x.items() if values!=30 and keys!='delta'}
print(x)
