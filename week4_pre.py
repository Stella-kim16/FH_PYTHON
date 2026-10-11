class Myclass:
    def __init__(self,i,j): # 객체가 생성될때 초기화 하는 매서드
        self.name1 = i  # 객체 속성에 값 저장 
        self.name2 = j

    def show(self):
       #객체에 저장된 속성에 접근 
        print(self.name1, self.name2)

obj = Myclass(10,20)
obj1 = Myclass(10,20)

obj.show()


class Parent:
    def hello(self):
        print("hello from parent")


class Child(Parent):
    pass

x = Child()
x.hello()


#e.g

class Parent:
    def __init__(self,name):
        self.name= name 
# 자식 클래스에 init 가 없어도 parent 의 init 가 나옴 

class Child(Parent):
    def __init__(self, name,age):
        # 자식 클래스에 init 이 들어오면 여기의 init 로 나옴 
        # 
        # 부모의 초기화가 필요할때 
        super().__init__(name)
        self.age = age

    def show(self):
        print(self.name, self.age)


obj = Child("kim",20)
obj.show()