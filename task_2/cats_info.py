from typing import List

def get_cats_info(path: str) -> List[dict]:
 
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_data = line.strip().split(',')
                cat_id = cat_data[0]
                cat_name = cat_data[1]
                cat_age = cat_data[2]

                cat_info = {"id": cat_id, "name": cat_name, "age": cat_age}
                cats_info.append(cat_info)

    except FileNotFoundError:
        print(f"The file {path} was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

    return cats_info

# Example of using the function
cats_info = get_cats_info("task_2/cats.txt")
print(cats_info)