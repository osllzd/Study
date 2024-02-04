#---------------------------
# 클래스와 메서드 만들기
#---------------------------
class person:
    def greeting(self):
        print('Hello')
james=person() # james=인스턴스
james.greeting() #greeting=메서드

# 속성 사용하기
class person:
    def __init__(self):
        self.hello='안녕하세요.'

    def greeting(self):
        print(self.hello)
james=person()
james.greeting()

# 인스턴스를 만들 때 값 받기
class person:
    def __init__(self,name,age,address):
        self.hello = '안녕하세요.'
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print('{0}저는 {1}입니다.'.format(self.hello,self.name))
        # 0 => self.hello
        # 1 => self.name

maria = person('마리아',20,'서울시 서초구 반포동')
maria.greeting()

# person으로 만들었던 인스턴스를 만들었을 때 넣었던 값이 출력됨
print('이름:', maria.name) # 마리아
print('나이:', maria.age) # 20
print('주소:', maria.address) # 서울시 서초구 반포동'''

# self는 person을 의미함
# 추가한 속성은 해당 인스턴스에서만 생성됨
# 클래스로 다른 인스턴스를 만들었을 때 추가한 속성은 생성되지 않음
# class person:
#       pass
# maria = person()
# maria.name = '마리아'
# maria.name
# => '마리아' 출력됨
# james = person()
# james.name => 오류 남

# 인스턴스는 생성한 뒤에 속성을 추가 할 수 있음!
# __init__ 메서드가 아닌 다른 메서드에서도 속성을 추가 가능
# 단 이때는 메서드를 호출해야 속성이 생성됨

# ------------------------------------------------------------------
# 비공개 속성 사용하기
# ------------------------------------------------------------------
# 클래스 바깥에서는 접근 불가능 !
class person:
    def __init__(self,name,age,address,wallet):
        self.name=name
        self.age=age
        self.address=address
        self.__wallet=wallet # 변수 앞에 __를 붙여서 비공개 속성으로 만듦

    # 비공개 속성 사용하기
    def pay(self,amount):
        if amount > self.__wallet:
            print('돈이 모자라네....')
            return
        self.__wallet -=amount
        print('이제 {0}원 남았네요.'.format(self.__wallet))




maria = person('마리아','20','서울시 서초구 반포동',10000)
# maria.__wallet = wallet => 클래스 바깥에서 비공개 속성에 접근하면 에러가 발생함
maria.pay(8000) # 3000원이 amount임 따라서 10000-3000 = 7000원이 출력이 됨

