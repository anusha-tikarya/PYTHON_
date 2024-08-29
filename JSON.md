JSON (JavaScript Object Notation) is a lightweight data format used for exchanging data between a server and a client, or between different parts of a program. It's easy for both humans and machines to read and write, which makes it a popular choice for data storage and communication.

### Basics of JSON in Python

1. **JSON Structure:**
   JSON data is organized in key-value pairs, similar to a Python dictionary. It can include different data types like strings, numbers, lists, and even nested objects. Here's an example:

   ```json
   {
     "name": "John",
     "age": 30,
     "is_student": false,
     "hobbies": ["reading", "coding", "hiking"]
   }
   ```

2. **Using JSON in Python:**
   Python has a built-in `json` module to work with JSON data. This module provides methods to convert Python objects to JSON format (serialization) and to convert JSON data back into Python objects (deserialization).

3. **Common Functions in `json` Module:**

   - **`json.dumps()`**: Converts a Python object (like a dictionary) into a JSON-formatted string.
     ```python
     import json

     data = {"name": "John", "age": 30, "is_student": False}
     json_string = json.dumps(data)
     print(json_string)
     # Output: {"name": "John", "age": 30, "is_student": false}
     ```

   - **`json.loads()`**: Converts a JSON-formatted string back into a Python object.
     ```python
     json_data = '{"name": "John", "age": 30, "is_student": false}'
     python_object = json.loads(json_data)
     print(python_object)
     # Output: {'name': 'John', 'age': 30, 'is_student': False}
     ```

   - **`json.dump()`**: Writes JSON data to a file.
     ```python
     with open("data.json", "w") as file:
         json.dump(data, file)
     ```

   - **`json.load()`**: Reads JSON data from a file and converts it into a Python object.
     ```python
     with open("data.json", "r") as file:
         data_from_file = json.load(file)
     print(data_from_file)
     ```

### Key Points to Remember
- JSON is used to store and exchange data.
- Python’s `json` module makes it easy to convert Python objects to JSON and vice versa.
- JSON format is easy to read and write, both for humans and machines.

![image](https://github.com/user-attachments/assets/f0159657-1749-41f1-87b4-545da605a2cd)

![image](https://github.com/user-attachments/assets/e63ea8df-c5d5-4e33-b1df-764ea3fda9c4)

![image](https://github.com/user-attachments/assets/2ee3297a-aeee-412a-923d-ddf4d024556e)


