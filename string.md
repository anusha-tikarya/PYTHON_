## Strings and Conditional Statements
# Different ways to define a string
str1 = "this is str"
str1 = 'this is str'
str1 = """this is str"""

# Escape sequences for formatting
# \n : next line
# \t : tab space

# Concatenation: Adding two strings
a="anu"
b="sha"
print(a+b)  # anusha
print(a+" "+b)  # anu sha

# Length of string
print(len(str1))  # 11

# Indexing: accessing characters
a="asfhjkl"
ch=a[3]
print(ch)  # h
ch=a[-1]
print(ch)  # l

# Slicing: accessing parts of string
a= "Anusha"
b = a[1:4]
print(b)  # nus
print(a[4:len(a)])  # ha
print(a[:3])  # Anu
print(a[3:])  # sha

# Negative Indexing
a="Apple"
print(a[-4:-1])  # ppl
print(a[-1:])  # e
print(a[:-3])  # Ap

# String Methods
a="asdfghj"
print(a.endswith("a"))  # False

a="i am anu"
print(a.capitalize())  # I am anu

a="asdfghj asdfghjj asdfghj"
print(a.replace("a","o"))  # osdfghj osdfghjj osdfghj

a="asdfghj from"
print(a.find("d"))  # 2
print(a.find("from"))  # 8
print(a.find("b"))  # -1

a="asbh abyucdi axsnaI"
print(a.count("a"))  # 4
