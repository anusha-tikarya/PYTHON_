## File I/O
```python
f=open("demo.txt","r")
data=f.read()
print(data)
f.close()

with open("demo.txt","r") as f:
    data=f.read()
    print(data)
```
