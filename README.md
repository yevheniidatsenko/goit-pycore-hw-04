## Python Homework: Data Processing, File Handling, and CLI Application

### Task 1: Total and average salary

**Description:**

Write a function `total_salary(path)` that takes a path to a text file containing information about the monthly salaries of developers in your company. Each line in the file contains a developer's last name and salary separated by a comma.

```
Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000
```

Your task is to calculate the total and average salary of all developers.

**Requirements:**

- The function `total_salary(path)` should take one argument - the path to the text file (path).
- The file contains data about the salaries of developers, separated by commas. Each line indicates one developer.
- The function should parse the file, calculate the total and average salary.
- The result of the function is a tuple of two numbers: total salary and average salary.

**Example of function usage:**

```python
total, average = total_salary("path/to/salary_file.txt")
print(f"Total salary: {total}, Average salary: {average}")
```

**Expected result:**

```
Total salary: 6000, Average salary: 2000
```

### Task 2: Get information about cats

**Description:**

Write a function `get_cats_info(path)` that reads a text file containing information about cats. Each line in the file contains a unique cat ID, its name, and age, separated by commas.

```
60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5
```

Your task is to write a function that reads this file and returns a list of dictionaries with information about each cat.

**Requirements:**

- The function `get_cats_info(path)` should take one argument - the path to the text file (path).
- The file contains data about cats, where each record contains a unique identifier, cat name, and its age.
- The function should return a list of dictionaries, where each dictionary contains information about one cat.

**Example of function usage:**

```python
cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)
```

**Expected result:**

```
[
    {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
    {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
    {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
    {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
    {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
]
```

**Task 3: Directory Tree Visualization**

**Description:**

Create a script that takes a directory path as a command-line argument and visualizes the directory tree structure, displaying the names of all subdirectories and files. For better visual perception, directory names and file names should be displayed in different colors.

**Requirements:**

- Create a Python virtual environment to isolate project dependencies.
- The script should receive the directory path as an argument when running. This path indicates the directory whose structure needs to be displayed.
- Use the colorama library to implement color output.
- The script should correctly display both directory names and file names, using a recursive directory traversal approach (non-recursive approach is optional).
- Error handling and processing should be implemented, such as handling situations where the provided path doesn't exist or doesn't point to a directory.

**Example usage:**

Running the script and passing it the absolute path to a directory as a parameter:

```python
hw03.py /path/to/your/directory
```

This should result in the terminal displaying a list of all subdirectories and files within the specified directory, with directory.

## Task 4: Console Assistant Bot

**Description:**

Create a simple console-based assistant bot that can recognize user commands and respond accordingly. This bot will serve as the foundation for a more advanced application assistant that we will develop in subsequent assignments. In its initial implementation, the assistant should be able to manage a contact book and calendar.

**Requirements:**

- **Command Parser:** Implement a command parser that can extract the command and its arguments from the user's input. The parser should be case-insensitive.
- **Command Handlers:** Create separate functions to handle each command, such as `add_contact()`, `change_contact()`, `show_phone()`, and `show_all()`.
- **Contact Book:** Use a data structure, such as a dictionary, to store contacts. Each contact should have a name and a phone number.
- **Main Loop:** Implement a main loop that continuously prompts the user for commands and processes their input using the appropriate command handler.
- **Error Handling:** Implement basic error handling to gracefully handle invalid commands and unexpected input.

**Example Usage:**

```
Welcome to the assistant bot!

Enter a command: add John 1234567890
Contact added.

Enter a command: phone John
1234567890

Enter a command: all
John: 1234567890

Enter a command: exit
Good bye!
```
