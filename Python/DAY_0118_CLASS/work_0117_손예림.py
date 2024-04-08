# 34장 연습문제 =====================================================================================
class knight:
    def __init__(self,health,mana,armor):
        self.health=health
        self.mana=mana
        self.armor=armor

    def slash(self):
        print('베기')
x = knight(542.4,210.3,38)
print(x.health,x.mana, x.armor)
x.slash()

# 34장 심사문제 ==================================================================================
class Annie:
    def __init__(self,health,mana,ability_power):
        self.health=health
        self.mana=mana
        self.__ability_power=ability_power # ability_power을 비공개 속성으로 만든다

    def tibbers(self):
        self.__ability_power=self.__ability_power * 0.65 + 400
        print('티버 피해량:{0}'.format(self.__ability_power))

health, mana, ability_power = map(float,input().split())

x = Annie(health=health, mana=mana, ability_power=ability_power)
x.tibbers()

# 35장 연습문제===============================================================================
class Date:
    @staticmethod
    def is_date_valid(date_string):
        year,month,day=map(int,date_string.split('-')) # date_string에 어떻게 써넣을 것인지
        return month <= 12 and day <=31 # 월은 12월까지 일은 31일까지 검사 후 결과 반환
if Date.is_date_valid('2000-01-31'):
    print('올바른 날짜 형식입니다.')
else:
    print('잘못된 날짜 형식입니다.')

# 35장 심사문제 ==============================================================================
class Time:
    def __init__(self, hour, minute,second):
        self.hour=hour
        self.minute=minute
        self.second=second

    @staticmethod
    # is_time_vaild = 문자열이 올바른 시간인지 검사하는 메서드
    def is_time_vaild(time_string):
        return int(time_string.split(':')[0])<=24 and int(time_string.split(':')[1]) <=59 and int(time_string.split(':')[2]) <=60

    @classmethod
    #from_String=문자열로 인스턴스를 만드는 메서드
    def from_sting(cls,time_string):
        hour, minute, second = map(int, time_string.split(':'))
        time=cls(hour,minute,second)
        return time

time_string= input()
if Time.is_time_vaild(time_string):
    t = Time.from_sting(time_string)
    print(t.hour,t.minute,t.second)
else:
    print('잘못된 시간 형식입니댜.')
