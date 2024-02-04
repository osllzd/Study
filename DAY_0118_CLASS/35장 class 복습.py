# -------------------------------------------------------
# 클래스 속성 사용하기
# -------------------------------------------------------
class person:
    Bag = []

    def put_Bag(self,stuff):
        #self.Bag.append(stuff) self는 현재 인스턴스를 칭하므로 속성을 지칭하기엔 모호함
        person.Bag.append(stuff) # person에 속한 bag속성

james=person()
james.put_Bag('책')

maria=person()
maria.put_Bag('열쇠')

print(james.Bag)
print(maria.Bag)

# 클래스 속성은 클래스에 속해 있으며 모든 인스턴스에서 공유한다
# 속성 bag에 인스턴스를 집어넣기 위해 put_bag 메서드를 이용해서 집어넣었다.

# -------------------------------------------------------
# 인스턴스 속성 사용하기
# -------------------------------------------------------
class person:
    def __init__(self):
        self.bag =[]

    def put_bag(self,stuff):
        self.bag.append(stuff)


james = person()
james.put_bag('책')

maria = person()
maria.put_bag('열쇠')

print(james.bag)
print(maria.bag)

# 인스턴스 속성은 인스턴스별로 독립되어 있으며 서로 영향을 주지 않는다

#클래스 속성 => 모든 인스턴스 공유, 인스턴스 전체가 사용해야 하는 값을 저장할 때 사용
#인스턴스 속성 => 인스턴스별로 독립, 각 인스턴스가 값을 따로 저장해야 할 때 사용

# -------------------------------------------------------
# 비공개 클래스 속성 사용하기
#   -클래스 안에서만 접근 가능, 클래스 바깥에서는 접근 불가능
#   -바깥으로 드러내고 싶지 않은 값에 사용
# -------------------------------------------------------

class knight:
    __item_limit = 10

    def print_item_limit(self):
        print(knight.__item_limit)

x = knight()
x.print_item_limit()

# print(knight.__item_limit) => 클래스 밖에서는 접근 불가능

# -----------------------------------------------------------------------------
# 정적 메서드 사용하기
#   : 정적 메서드는 매개변수에 self를 지정하지 않으므로 인스턴스 속성에 접근 불가능
# ------------------------------------------------------------------------------
class Calc:
    @staticmethod # 데코레이터
    def add(a,b):
        print(a+b)
    @staticmethod
    def mul(a,b):
        print(a*b)

# 정적 메서드가 붙은 경우 클래스에서 바로 메서드 호출

Calc.add(10,20)
Calc.mul(10,20)

# 정적 메서드는 메서드의 실행이 외부 상태에 영향을 끼치지 않는 '순수함수'를 만들 때 사용
# '순수함수'는 부수효과가 없고 입력값이 같으면 언제나 같은 출력 값 반환
# 정적 메서드는 인스턴스의 상태를 변화시키지 않는 메서드 만들 때 사용

# -----------------------------------------------------------------------------
# 클래스 메서드 사용하기
#
# ------------------------------------------------------------------------------
class person:
    count = 0 # 클래스 속성
    def __init__(self):
        person.count += 1 # 인스턴스가 만들어질 때 클래스 속성에 1을 더함

    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count)) # cls로 클래스 속성 접근

james=person() # 인스턴스 +1
maria=person() # 인스턴스 +2
yerim=person() # 인스턴스 +3
heejin=person() # 인스턴스 +4

person.print_count()

#cls() = person()과 같다
# 클래스 메서드는 정적 메서드 처럼 인스턴스 없이 호출 가능
# 클래스 메서드 안에서 클래스 속성, 클래스 메서드에 접근해야 할 때 사용