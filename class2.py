# class1.py
# 1) 클래스 정의
class Person:
    def __init__(self):
        self.name = "default name"
        self.title="default title"
    def print(self):
        print("My name is {0}".format(self.name))

#2) 인스턴스 생성  
p1 = Person()
p2=Person()
p1.name="전우치"

#런타임시에 변수 추가
Person.title="new title"
print(p1.title)
print(p2.title)
print(Person.title)


