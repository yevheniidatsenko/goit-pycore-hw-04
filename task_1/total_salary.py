def total_salary(path: str) -> tuple:

    total_salary = 0
    count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                _, salary = line.strip().split(',')
                total_salary += int(salary)
                count += 1
    except FileNotFoundError:
        print(f"Error: File not found at {path}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

    if count == 0:
        return 0, 0

    average_salary = total_salary / count
    return total_salary, average_salary

# Example of using the function
total, average = total_salary("task_1/salaries.txt")
print(f"Total salary: {total}, Average salary: {average}")