```python
#Exercise 1 Read and print the JSON file
import json


with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)


#Exercise 2
profile = {
    "name": "Jane Smith",
    "age": 28,
    "city": "Los Angeles",
    "hobbies": ["Photography", "Traveling", "Reading"]
}


import json

with open('profile.json', 'w') as file:
    json.dump(profile, file, indent=4)

#Exercise 3
import csv
import json


students = []
with open('students.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        students.append(row)


with open('students.json', 'w') as json_file:
    json.dump(students, json_file, indent=4)


#exercise 4

import json
import csv

with open('data.json', 'r') as json_file:
    data = json.load(json_file)

with open('employees.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    csv_writer.writerow(data.keys())

    csv_writer.writerow(data.values())

#Exercise 5

import json

with open('books.json', 'r') as file:
    books_data = json.load(file)

for book in books_data['books']:
    print(book['title'])
```
