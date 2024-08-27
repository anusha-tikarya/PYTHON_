
### 1. **Basic Python Operations:**
   - **Variables and Printing:**
     ```python
     name = "Anu"
     age = 21
     print("name")
     print(name)
     print("My name is:", name)
     print("My age is:", age)
     ```
   - **Simple Arithmetic Operations:**
     ```python
     print(1111)
     print(11+11)
     ```

### 2. **Strings and Conditional Statements:**
   - **String Operations:**
     ```python
     str1 = "this is str"
     print(a+b)  # Concatenation
     print(len(str1))  # Length of string
     print(a[3])  # Indexing
     print(a[1:4])  # Slicing
     ```
   - **String Methods:**
     ```python
     print(a.endswith("a"))
     print(a.capitalize())
     print(a.replace("a", "o"))
     print(a.find("d"))
     print(a.count("a"))
     ```

### 3. **Lists and Tuples:**
   - **List Operations:**
     ```python
     marks = [91.2, 3.4, 4.4]
     print(marks)
     marks.append(3)
     marks.sort()
     marks.reverse()
     ```
   - **Tuple Operations:**
     ```python
     tup = (1, 2, 3, 4, 5, 6)
     print(tup[1])
     print(tup.index(3))
     print(tup.count(1))
     ```

### 4. **Functions & Recursion:**
   - **Defining Functions:**
     ```python
     def sum(a, b):
         return a + b
     ```
   - **Recursion Example:**
     ```python
     def fact(n):
         if n == 0 or n == 1:
             return 1
         else:
             return n * fact(n-1)
     ```

### 5. **Object-Oriented Programming (OOP):**
   - **Classes and Objects:**
     ```python
     class Student:
         def __init__(self, name, marks):
             self.name = name
             self.marks = marks

         def hello(self):
             print("Welcome Student", self.name)

     s1 = Student("Anu", 89)
     s1.hello()
     ```
   - **Inheritance:**
     ```python
     class Car:
         @staticmethod
         def start():
             print("car started...")

     class Toyotacar(Car):
         pass
     ```

### 6. **File Handling:**
   - **Reading a File:**
     ```python
     f = open("demo.txt", "r")
     data = f.read()
     print(data)
     f.close()
     ```

### 7. **Control Statements:**
   - **If-Else and Elif:**
     ```python
     if n >= 90:
         print("GRADE A")
     elif n >= 80:
         print("GRADE B")
     else:
         print("GRADE D")
     ```
   - **Loops:**
     ```python
     for i in range(10):
         print(i)
     ```

### 8. **Advanced Concepts:**
   - **Abstraction and Encapsulation:**
     ```python
     class Car:
         def __init__(self):
             self.acc = False
             self.brk = False
             self.clutch = False

         def start(self):
             self.clutch = True
             self.acc = True
             print("car started")
     ```

