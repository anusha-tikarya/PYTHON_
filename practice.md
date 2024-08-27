
**Question:** Write a function to sum two numbers and return the result.  
**Solution:**
```python
def sum(a, b):
    sum = a + b
    return sum

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
print("Sum of these 2 numbers is:", sum(a, b))  # Example Output: 5
```

---

**Question:** Write a function to calculate the average of three numbers.  
**Solution:**
```python
def avg(a, b, c):
    avg = (a + b + c) / 3
    return avg

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
print("Average of these 3 numbers is:", avg(a, b, c))  # Example Output: 3
```

---

**Question:** Write a function to calculate the factorial of a number using recursion.  
**Solution:**
```python
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

print(fact(5))  # Example Output: 120
```

---

**Question:** Demonstrate string concatenation and length calculation.  
**Solution:**
```python
a = "anu"
b = "sha"
print(a + b)  # Output: anusha
print(a + " " + b)  # Output: anu sha

str1 = "this is str"
print(len(str1))  # Output: 11
```

---

**Question:** Demonstrate list slicing and methods like append, sort, reverse, insert, remove, and pop.  
**Solution:**
```python
a = [1, 2, 3, 45, 56, 45]
print(a[:5])  # Output: [1, 2, 3, 45, 56]
print(a[-4:-2])  # Output: [3, 45]

l = [1, 2, 3, 45, 6, 6, 7]
l.append(3)
print(l)  # Output: [1, 2, 3, 45, 6, 6, 7, 3]
l.sort()
print(l)  # Output: [1, 2, 3, 3, 6, 6, 7, 45]
l.sort(reverse=True)
print(l)  # Output: [45, 7, 6, 6, 3, 3, 2, 1]

a = ["apple", "lichi", "mango", "banana"]
a.sort()
print(a)  # Output: ['apple', 'banana', 'lichi', 'mango']
a.sort(reverse=True)
print(a)  # Output: ['mango', 'lichi', 'banana', 'apple']

a = [1, 'assd', 2, 3, 4, 5]
a.reverse()
print(a)  # Output: [5, 4, 3, 2, 'assd', 1]

a.insert(1, 4)
print(a)  # Output: [5, 4, 4, 3, 2, 'assd', 1]

a.remove(4)
print(a)  # Output: [5, 4, 3, 2, 'assd', 1]

a.pop(4)
print(a)  # Output: [5, 4, 3, 2, 1]
```

---

**Question:** Write a function that demonstrates the usage of range() in loops.  
**Solution:**
```python
seq = range(10)
for i in seq:
    print(i)  # Output: 0 1 2 3 4 5 6 7 8 9

for i in range(10):
    print(i)  # Output: 0 1 2 3 4 5 6 7 8 9
```

---

**Question:** Implement a recursive function to print numbers from 5 to 1.  
**Solution:**
```python
def show(n):
    if n == 0:  # Base case
        return
    print(n)
    show(n - 1)

show(5)  # Output: 5 4 3 2 1
```

---

**Question:** Demonstrate the use of if-else conditional statements for grading based on marks.  
**Solution:**
```python
n = int(input("Enter marks: "))
if n >= 90:
    print("GRADE A")
elif n >= 80 and n < 90:
    print("GRADE B")
elif n >= 70:
    print("GRADE C")
else:
    print("GRADE D")
```

---

**Question:** Create a class `Student` with a constructor and methods to display student information.  
**Solution:**
```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def hello(self):
        print("Welcome Student", self.name)

    def get_marks(self):
        return self.marks

s1 = Student("karan", 97)
s1.hello()  # Output: Welcome Student karan
print(s1.get_marks())  # Output: 97
```

---

**Question:** Demonstrate the use of list slicing, indexing, and tuple methods like index and count.  
**Solution:**
```python
tup = (1, 2, 3, 4, 5, 6)
print(tup[1])  # Output: 2
print(tup[:4])  # Output: (1, 2, 3, 4)

a = (1, 2, 3, 4, 1)
print(a.index(3))  # Output: 2
print(a.count(1))  # Output: 2
```

---

**Question:** Demonstrate dictionary operations like accessing, updating, and adding key-value pairs.  
**Solution:**
```python
dict = {
    "name": "Anu",
    "CGPA": 8.9,
    "marks": [99, 89, 78, 67],
    "Subjects": ('Python', 'c')
}

print(dict["Subjects"])  # Output: ('Python', 'c')

dict["name"] = "Anusha"
print(dict["name"])  # Output: Anusha

dict["Surname"] = "Tikarya"
print(dict)  # Output: {'name': 'Anusha', 'CGPA': 8.9, 'marks': [99, 89, 78, 67], 'Subjects': ('Python', 'c'), 'Surname': 'Tikarya'}

null_dict = {}
null_dict["Name"] = "Anu"
print(null_dict)  # Output: {'Name': 'Anu'}

Stu = {
    "name": "Anu",
    "Marks": {"Python": 98, "DSA": 89, "SQL": 88},
    "Experience": 2,
}

print(Stu["Marks"])  # Output: {'Python': 98, 'DSA': 89, 'SQL': 88}
print(Stu["Marks"]["DSA"])  # Output: 89
```

---

