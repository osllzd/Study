# ---------------------------------------------------------------------------
# 자동차 클래스
# 클래스 이름 : car
# 클래스 속성 : 바퀴, 색상,차번호, 차종류(인스턴스 속성) , 제조사(클래스 속성)
#              12, 빨강, 1111, 세단, 현대
#              12, 빨강, 1111, 세단, 현대
# 클래스 기능 : 주행, 정지, 후진
# ---------------------------------------------------------------------------
class car:
    # 클래스 속성
    maker='현대'

    # 생성자 메서드 => 객체 즉, 인스턴스 생성 메서드
    def __init__(self, wheel, color, number, kind):
        #힙 영역에 저장
        self.wheel=wheel
        self.color=color
        self.number=number
        self.kind=kind

    # 객체 즉, car 인스턴스 메서드
    def driving(self, where):
        print(f'{self.wheel}에 {self.number}차가 드라이빙 하고 있다.')

    def stop(self):
        print(f'{self.number}차가 정지한다.')

    def back(self):
        print(f'{self.number}차가 후진한다.')


# ---------------------------------------------------------------------------
# 자동차 인스턴스 생성
# ---------------------------------------------------------------------------
mycar=car(19,'red',111,'세단')
secondcar=car(20,'pink',222,'SUV')


# ---------------------------------------------------------------------------
# 사랑 클래스
# 클래스 이름 : love
# 클래스 속성 : kind
# 클래스 기능 : 새우까주기, 깻잎떼주기, 금융치료, 데려다주기, 데이트하기, 같이아프기
#              대신 희생하기
# ---------------------------------------------------------------------------
class love:

    def __init__(self,kind):
        self.kind=kind

    def date(self):
        print(f'{self.kind}하는 것')

# ---------------------------------------------------------------------------
# 계산기 클래스
# 클래스 이름 : cals
# 클래스 속성 : 브랜드, 종류, 색상, 크기, 가격
# 클래스 기능 : 덧셈, 뺄셈, 곱셈, 나눗셈
# -데이터 => 속성 또는 기능에서 매개변수
# ---------------------------------------------------------------------------
class calc:
    # 클래스 변수
    maker ='카시오'
    __size=(7,15) #비공개 속성 __속성명: 클래스 밖에서 속성 읽거나/쓰기 불가
    # 객체 인스턴스 생성 메서드
    def __init__(self, kind, color, price,info):
        self.kind=kind
        self.color=color
        self.price=price
        self.__info=info        # 인스턴스 생성 시 계산기에 각인되는 정보
        self.data=0             # 전부다 매개변수로 받지 않아도 됨 !

    # 비공개 인스턴스 속성 읽기/쓰기 메서드
    def getinfo(self):
        return self.__info

    def setinfo(self,info):
        self.__info=info

    # 비공개 인스턴스 속성 읽기/쓰기 메서드
    # => 속성 읽기/쓰기 방식으로 동작하도록 설정
    @property
    def info(self):
        return self.__info

    @info.setter # 위가 info라서 여기도 info를 사용해야함 , 형식 맞출려고 추가
    def info(self,info):
        self.__info=info


    # 덧셈 기능
    def plus(self,nums):
        self.data += nums

    def minus(self,nums):
        self.data -= nums

    def multi(self,nums):
        self.data *= nums

    def div(self,nums):
        if not nums: return '0으로 나눌 수 없습니다.'
        self.data = self.data/nums

    def result(self,nums):
        return self.data


# ---------------------------------------------------------------------------
# calc 클래스로 인스턴스 생성 => 힙에 생성:인스턴스 변수 * 클래스 변수
#                                      인스턴스 메서드 사용 가능
# ---------------------------------------------------------------------------
c1=calc('공학용','블랙',10000,'손예림계산기')

# 인스턴스 속성 읽기 => 공개 속성만 읽기 가능
print(c1.data,c1.color,c1.kind)

# 인스턴스 속성 읽기 => 공개 속성만 읽기 가능
c1.color='빨간색'

# 인스턴스 비공개 속성 읽기 => 전용 메소드 getter/setter 통해서 읽기/쓰기
print(c1.getinfo(), c1.info)

# 인스턴스 비공개 속성 변경 => 전용 메소드 getter/setter 통해서 읽기/쓰기
c1.setinfo("내꺼")
c1.info='내꺼야' # => info setter 속성을 맞춰주는 것!



# ---------------------------------------------------------------------------
# calc 클래스로 계산기 정보 확인 => 클래스 변수만 확인 가능
#                                인스턴스 변수나 메서드 사용 불가능 !!
#                                self 값이 없음 !
# ---------------------------------------------------------------------------
print(calc.maker)

# 인스턴스 메서드에 접근 불가!
#print(calc.plus(10,20))

