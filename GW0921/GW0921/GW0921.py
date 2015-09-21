#class Movie :
#    '''영화클래스입니다.'''
#    title = "앤트맨"
#    director = "모름"
#    def __init__(self, title, director) :
#        self.title = title
#        self.director = director
#        print(self.title + " 생성")

#    def showInfo(self) :
#        print(self.title + ", " + self.director)

#    def __del__(self) : #소멸자
#        print(self.title + " 소멸")

#m1 = Movie("설국열차1","봉준호")
#m2 = Movie("쥬라기공원2","스티븐스필버그")

#m1.age = 20 #인스턴스에서만 사용할 수 있는 변수 추가
#m1.showInfo()
#print(m1.age)
#print(m1.title)
#m1.__class__.title = "암살" #인스턴스에서 클래스의 값 변경
#print(m1.title)
#print(m1.__class__.title)
#print(m2.__class__.title)
#print(m1.__doc__) # 주석 출력
#print(type(m2))
#m2 = m1#얕은복사, 같은 주소를 가르키게됨
#m2.showInfo()
#print(m2.age)
#print(id(m1)) #id()주소값
#print(id(m2))

######################################

class Movie :
    count = 0
    def __init__(self, title, director) :
        self.title = title
        self.director = director
        __class__.count+=1
        print(self.title + " 생성")
    
    @staticmethod
    def showCount1() :
        print(Movie.count)

    @classmethod
    def showCount2(cls) :
        print(cls.count)


m1 =Movie("a","b")
print(m1.count)
Movie.showCount1()
Movie.showCount2()
m1.showCount1()
m1.showCount2()
m2 =Movie("c","d")
print(m2.count)
Movie.showCount1()
Movie.showCount2()
m1.showCount1()
m1.showCount2()