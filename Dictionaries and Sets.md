## Dictionaries and Sets

```python
# Dictionary
dict={
    "name" :"Anu",
    "CGPA"  : 8.9,
    "marks" : [99,89,78,67],
    "Subjects" : ('Python' , 'c')
}

print(dict)  # "name" :"Anu","CGPA"  : 8.9,"marks" : [99,89,78,67],"Subjects" : ('Python' , 'c')
print(type(dict))  # dict


# Accessing values
print(dict["Subjects"])  # ('Python', 'c')
dict["name"]="Anusha"
print(dict["name"])  # Anusha
dict["Surname"] = "Tikarya"
print(dict)  # updated dictionary

# Nested Dictionary
Stu={
    "name" :  "Anu",
    "Marks" : {"Python" : 98,
               "DSA" : 89,
               "SQL" : 88,},
    "Experience" : 2,
}
print(Stu["Marks"])  # {"Python" : 98,"DSA" : 89,"SQL" : 88}
print(Stu["Marks"]["DSA"])  # 89

# Dictionary Methods
a= {"a":1, "b":2}
print(a.keys())  # dict_keys(['a', 'b'])
print(list(a.keys()))  # ['a', 'b']
print(len(a))  # 2
print(a.values())  # dict_values([1, 2])
print(a.items())  # dict_items([('a', 1), ('b', 2)])
print(a.get("a"))  # 1

a.update({"city" : "Indore"})
print(a)  # updated dictionary

a.update({"a" : 2})
print(a)  # updated value for key 'a'
```
