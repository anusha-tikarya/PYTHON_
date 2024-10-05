
### **Basic Python Programming Questions**

1. **Write a Python program to check if a number is odd or even.**

```python
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
```

2. **Write a Python program to reverse a string.**

```python
string = input("Enter a string: ")
reversed_string = string[::-1]
print(f"Reversed string: {reversed_string}")
```

3. **Write a Python program to find the factorial of a number using recursion.**

```python
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")
```

4. **Write a Python program to swap two variables without using a third variable.**

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a, b = b, a
print(f"After swapping: a = {a}, b = {b}")
```

5. **Write a Python program to find the largest of three numbers.**

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
largest = max(a, b, c)
print(f"Largest number is {largest}")
```

### **Intermediate Python Programming Questions**

1. **Write a Python program to check if a string is a palindrome.**

```python
def is_palindrome(s):
    return s == s[::-1]

string = input("Enter a string: ")
if is_palindrome(string):
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")
```

2. **Write a Python program to count the occurrences of each character in a string.**

```python
from collections import Counter

string = input("Enter a string: ")
counter = Counter(string)
print(dict(counter))
```

3. **Write a Python program to sort a list of tuples based on the second element.**

```python
tuples_list = [(1, 2), (3, 1), (5, 4), (2, 3)]
sorted_list = sorted(tuples_list, key=lambda x: x[1])
print(f"Sorted list: {sorted_list}")
```

4. **Write a Python program to find the sum of digits of a number.**

```python
num = int(input("Enter a number: "))
sum_digits = sum(int(digit) for digit in str(num))
print(f"Sum of digits: {sum_digits}")
```

5. **Write a Python program to check if a number is prime.**

```python
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
```

### **Advanced Python Programming Questions**

1. **Write a Python program to merge two dictionaries.**

```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = {**dict1, **dict2}
print(f"Merged dictionary: {merged_dict}")
```

2. **Write a Python program to remove duplicates from a list.**

```python
lst = [1, 2, 2, 3, 4, 4, 5]
unique_lst = list(set(lst))
print(f"List after removing duplicates: {unique_lst}")
```

3. **Write a Python program to find the second largest number in a list.**

```python
lst = [10, 20, 4, 45, 99]
unique_lst = list(set(lst))
unique_lst.sort()
print(f"Second largest number: {unique_lst[-2]}")
```

4. **Write a Python program to generate Fibonacci sequence up to n terms.**

```python
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter the number of terms: "))
fibonacci(n)
```

5. **Write a Python program to count the number of vowels in a string.**

```python
def count_vowels(string):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in string if char in vowels)

string = input("Enter a string: ")
vowel_count = count_vowels(string)
print(f"Number of vowels: {vowel_count}")
```

