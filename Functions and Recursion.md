## Functions and Recursion

```python
# Functions
def sum(a,b):
    return a+b

a=int(input("enter 1st num: "))
b=int(input("enter 2nd num: "))
print("sum of these 2 num. is:",sum(a,b))

def noreturn():
    print("No return")

a=noreturn()
print(a)  # None

# Average of 3 numbers
def avg(a,b,c):
    return (a+b+c)/3

a=int(input("enter 1st num: "))
b=int(input("enter 2nd num: "))
c=int(input("enter 3rd num: "))
print("avg of these 3 num. is:",avg(a,b,c))

# Using end parameter in print
print("hii", end=" ")
print("people")  # hii people

# Default parameters
def mul(a=1,b=1):
    return a*b

print(mul())  # 1

# Recursion
def show(n):
    if(n==0):
        return()
    print(n)
    show(n-1)

show(5)  # 54321

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)

print(fact(5))  # 120
```
