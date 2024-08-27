## OOPS
```python
# Basic Class and Object
class Student:
    name="anu"
    roll=39

s1= Student()
print(s1.name)  # anu
print(s1.roll)  # 39

# Constructor and Methods
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def hello(self):
        print("Welcome Student",self.name)

s1=Student("Anu",89)
s2=Student("Anusha",90)
print(s1.name, s1.marks)  # Anu 89
print(s2.name, s2.marks)  # Anusha 90
s1.hello()  # Welcome Student Anu

# Inheritance
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

class Subjects(Student):
    def hello(self):
        print("Student",self.name, "has",self.marks,"marks")

s1=Subjects("Anu",89)
s1.hello()  # Student Anu has 89 marks
```
