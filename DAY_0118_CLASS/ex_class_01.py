# ---------------------------------------------------------------------------------
# 사용자 정의 클래스
# ---------------------------------------------------------------------------------
# 클래스 정의 : 밤 하늘의 별을 저장 하는 데이터
# 클래스 이름 : Star
# 클래스 속성 : 크기, 색상, 밝기 => 속성(attribute), 필드(field) => 변수
# 클래스 기능 : 반짝 거린다, 떨어 진다 => 함수(function), 메서드(method)=> 함수
# ---------------------------------------------------------------------------------
class star:
    # 클래스 변수/속성 필드 => 해당 클래스 생성된 객체 즉 인스턴스가 공유하는 속성
    timezone='밤'
    __privatevalue=77

    # 최상위 부모클래스 object로부터 상속받은 함수 즉 메서드
    # 형태 def_ _XXX_ _()
    # 나의 클래스에 맞도록 수정 , 즉 리모델링해서 사용 => 오버라이딩(override)
    def __init__(self,size,color,brightness,name='알수없음',timezone='밤'):
        print(f'__init__():{size},{color},{brightness},{name}')
        # 힙 메모리 영역에 저장 => 속성 데이터의 주소 저장
        self.__size=size # __size => 비공개
        self.color=color
        self.brightness=brightness
        self.name=name


    # 별 클래스의 기능 => 메서드
    def drop(self):
        print(f'{self.name}별이 하늘에서 떨어집니다. 소원 빌어요~!^^')
        print(f'{self.color}별이 하늘에서 떨어집니다. 소원 빌어요~!^^')

    # 비공개 인스턴스 속성에 접근하기 위한 메서드 => getter/setter 메서드
    # 비공개 인스턴스 속성 읽어오는 메서드 get(속성명() ==> 속성값
    # 비공개 인스턴스 속성에 값 설정하는 메서드 set(속성명(새로운값)
    def getsize(self):
        return self.__size

    def setsize(self, size):
        self.__size=size
     # 비공개 인스턴스 메서드 => 클래스 내부에서만 호출되는 메서드 ---------
    def __inner(self):
        print('비공개 인스턴스 메서드')

    # 객체 즉 인스턴스 생성 없이 사용하는 메서드
    # 속성이 없는 클래스도 있음 즉 인스턴스 생성 할 필요 없을 때 staticmethod를 사용함
    @staticmethod
    def add():
        pass

    @classmethod # 클래스 정보가 붙는 메서드임
    def cc(cls):
        pass

#---------------------------------------------------------------------
# 객체 생성 => 클래스에 정의된 속성 즉 변수와 함수들이 메모리 힙 영역에 생성
# 생성 방법 => 클래스명() <- 생성자 함수/메서드
#             클래스명(매개변수1) 생성자 함수/메서드
#             클래스명(매개변수1, 매개변수2, ..., 매개변수N) 생성자 함수/메서드
#---------------------------------------------------------------------


if __name__ == '__main__':
    mystar=star(5, "dark_yellow",10) # 힙 영역에 만들어졌고, 스택에서 myStar의 주소를 저장하고 있다
    yourstar=star(10,"red",20, "RedStar")
    yourstar.drop()


# ---------------------------------------------------------------------------------
# 객체의 메서드 실행 => 객체변수명.메서드명()
# ---------------------------------------------------------------------------------
mystar.drop()
yourstar.drop()
star
# ---------------------------------------------------------------------------------
# 객체의 속성 정보 읽기 => 객체변수명.속성명
# ---------------------------------------------------------------------------------
# 인스턴스 속성에 직접 접근
print(mystar.color, mystar.brightness,star.timezone)
print(yourstar.color,yourstar.brightness,star.timezone)

# 인스턴스 속성에 간접 접근 => 메서드 제공 필수
print(f'현재 속성값 읽기:{mystar.getsize()}')
# 전체 비공개 속성값 변경
mystar.getsize(100)

print(f'현재 비공개 속성값 읽기:{mystar.getsize()}')


# ---------------------------------------------------------------------------------
# 객체의 속성 정보 읽기 => 객체변수명.속성명 = 새로운 값
# ---------------------------------------------------------------------------------
mystar.brightness=7
print(mystar.color, mystar.brightness)

# ---------------------------------------------------------------------------------
# 객체의 속성 정보 읽기 => 객체변수명.속성명 = 새로운 값
# ---------------------------------------------------------------------------------
print(f'클래스명.__dict__:\n{star.__dict__}')
print(f'인스턴스명.__dict__:\n{mystar.__dict__}')
print(f'인스턴스명.__dict__:\n{yourstar.__dict__}')