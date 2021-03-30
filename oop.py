class Person():
    def __init__(self,name,age):
        self.f_name=name
        self.age=age


p1=Person("Jane",20)

print(f"{p1.f_name} is {p1.age} old")
        

class animal():
    def __init__(self, name,age):
        self.a_name= name
        self.a_age=age
a1=animal("Tiger",15)
a2= animal("lion",20)
print(f"{a1.a_name} is {a1.a_age} years old")
print(f"{a2.a_name} is {a2.a_age} years old")
        
