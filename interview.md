
### **Python Basics Viva Questions:**

#### 1. **What is Python?**
Python is a high-level, interpreted programming language known for its easy-to-read syntax and dynamic typing.

#### 2. **What are the key features of Python?**
- Interpreted language
- Dynamically typed
- Supports OOP
- High-level data structures (like lists, dictionaries)
- Extensive libraries and modules

#### 3. **What are Python data types?**
Some common Python data types are:
- Integer (int)
- Float (float)
- String (str)
- List (list)
- Tuple (tuple)
- Dictionary (dict)
- Set (set)
- Boolean (bool)

#### 4. **What is a list? How is it different from a tuple?**
A **list** is mutable, meaning it can be changed after its creation, whereas a **tuple** is immutable.

#### 5. **What are modules in Python?**
A module is a file that contains Python code (functions, variables, classes, etc.). Modules allow code reuse across different programs by importing them using the `import` keyword.

#### 6. **What are functions in Python?**
Functions are blocks of reusable code that perform a specific task. They are defined using the `def` keyword.

#### 7. **Explain the difference between `==` and `is` operators.**
- `==` checks for **value equality**.
- `is` checks for **reference equality** (i.e., whether both operands refer to the same object in memory).

#### 8. **What are decorators in Python?**
Decorators are a way to modify the behavior of a function or class without modifying the source code. They are often used in metaprogramming.

#### 9. **What are global and local variables?**
- **Global variables**: Variables declared outside a function and accessible anywhere in the script.
- **Local variables**: Variables declared inside a function and accessible only within that function.

### **OOP in Python Viva Questions:**

#### 1. **What is Object-Oriented Programming (OOP)?**
OOP is a programming paradigm based on the concept of objects, which can contain data (attributes) and methods (functions).

#### 2. **Explain the concept of Inheritance.**
Inheritance allows a class to inherit attributes and methods from another class, promoting code reuse.

#### 3. **What is polymorphism?**
Polymorphism allows functions or methods to operate on objects of different classes in the same way, as long as they share the same interface.

#### 4. **What is encapsulation?**
Encapsulation restricts access to some of the object’s components and can prevent accidental modification of data.

#### 5. **What is the difference between `__init__` and `__new__` in Python?**

| Feature                  | `__init__`                                 | `__new__`                                |
|--------------------------|--------------------------------------------|------------------------------------------|
| **Purpose**               | Initializes the object after it's created  | Creates the object itself                |
| **Called When**           | After the object has been created          | Before `__init__`, during object creation|
| **Arguments**             | Takes `self` and other arguments           | Takes `cls` and other arguments          |
| **Usage**                 | Used to initialize instance variables      | Used in custom object creation scenarios |
| **Return Type**           | Does not return anything (`None`)          | Must return a new object                 |
| **Modifiable**            | Can modify the attributes of the instance  | Used rarely, in cases of singleton, metaclasses |
| **Default Behavior**      | Automatically called on object creation    | Can be overridden for custom behavior    |

#### 6. **What are class methods and static methods?**
- **Class methods**: Defined using `@classmethod`. They take `cls` as the first argument and can modify class state.
- **Static methods**: Defined using `@staticmethod`. They don’t take `self` or `cls` and cannot modify object or class state.

### **Modules in Python Viva Questions:**

#### 1. **What is a Python module?**
A Python module is a file containing Python definitions and statements. A module allows you to organize and reuse code by importing it into other programs.

#### 2. **What are some commonly used built-in Python modules?**
- **os**: Provides functions to interact with the operating system.
- **sys**: Provides access to some variables used or maintained by the Python interpreter.
- **math**: Provides mathematical functions like `sqrt`, `sin`, etc.
- **random**: Implements pseudo-random number generators.
- **datetime**: Supplies classes for manipulating dates and times.

#### 3. **How do you import a module in Python?**
- To import the entire module: `import module_name`
- To import a specific function from a module: `from module_name import function_name`

#### 4. **What is `__name__ == "__main__"` in Python?**
This expression checks whether the Python script is being run as the main program or being imported as a module.

### **Advanced OOP Viva Questions:**

#### 1. **What is method overloading and does Python support it?**
Method overloading allows multiple methods in the same class to have the same name but different parameters. Python doesn’t support method overloading in the traditional sense, but you can achieve it using default arguments.

#### 2. **Explain `super()` in Python.**
`super()` is used to call methods from the parent class in child classes, especially in the context of inheritance.

#### 3. **What are abstract classes in Python?**
Abstract classes are classes that cannot be instantiated. They are used as blueprints for other classes. They are defined using the `abc` module.

---

