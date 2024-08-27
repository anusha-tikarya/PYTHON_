## List and tuples
```python
# Lists
marks=[91.2,3.4,4.4]
print(marks)  # [91.2, 3.4, 4.4]
print(type(marks))  # list
print(marks[0])  # 91.2
print(len(marks))  # 3

a=[1,"anu",99.9, "placed"]
print(a[0])  # 1
print(len(a))  # 4

# Lists are mutable
a[0]="college"
print(a[0])  # college

# List Slicing
a=[1,2,3,45,56,45]
print(a[:5])  # [1,2,3,45,56]
print(a[-4:-2])  # [3, 45]

# List Methods
l=[1,2,3,45,6,6,7]
l.append(3)
print(l)  # [1,2,3,45,6,6,7,3]

l.sort()
print(l)  # [1,2,3,3,6,6,7,45]

l.sort(reverse=True)
print(l)  # [45,7,6,6,3,3,2,1]

a=["apple", "lichi", "mango","banana"]
a.sort()
print(a)  # ['apple', 'banana', 'lichi', 'mango']

a.sort(reverse=True)
print(a)  # ['mango','lichi','banana','apple']

a=[1,'assd',2,3,4,5]
a.reverse()
print(a)  # [5,4,3,2,'aasd',1]

a.insert(1,4)
print(a)  # [5,4,4,3,2,'aasd',1]

a.remove(4)
print(a)  # [5,4,3,2,'aasd',1]

a.pop(4)
print(a)  # [5,4,3,2,1]

# Tuples: Immutable
tup= (1,2,3,4,5,6)
print(tup)  # (1,2,3,4,5,6)
print(type(tup))  # tuple
print(tup[1])  # 2
print(tup[:4])  # (1,2,3,4)

# Creating single value tuple
tup=(1,)  # , is necessary

# Tuple methods
a=(1,2,3,4,1)
print(a.index(3))  # 2
print(a.count(1))  # 2
```
