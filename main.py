import csv

student_data = [
    {"name": "Андрей", "surname": "Попов", "grade": 5, "project_id": "1"},
    {"name": "Степан", "surname": "Васильев", "grade": None, "project_id": "2"},
    {"name": "Владимир", "surname": "Хадаров", "grade": 4, "project_id": "3"}
]

def calculate_average_grade(grades_list):
    """
    Вычисляем среднюю оценку из списка оценок.

    Args:
    grades_list (list): Список оценок.

    Returns:
    float: Средняя оценка.
    """

    valid_grades = [grade for grade in grades_list if grade is not None]

    return round(sum(valid_grades)/len(valid_grades), 3) if valid_grades else 0

def process_student_data(student_data):
    """
    Обрабатывает данные студентов, заменяя битые оценки средним значением.

    Args:
    student_data (list of dict): Список словарей, каждый из которых содержить данные студентво.
    
    Returns:
    list of dict: Обработанный список с данными студентов.
    """

    grades = [student.get("grade") for student in student_data]

    avarage_grade = calculate_average_grade(grades)

    for student in student_data:
        if student["grade"] is None:
            student["grade"] = avarage_grade

    return student_data

def save_to_csv(data, filename):
    """
    Запись данный в CSV формате в файл.

    Args:
    student_data (list of dict): Список словарей, каждый из которых содержить данные студентво.
    filename (str): Имя файла для сохранения.
    """
    
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def read_csv(file_path):
    """
    Чтение данных из CSV файла.

    Args:
        file_path (str): Путь к файлу.
    Returns:
        student_data (list of dict): Список словарей, каждый из которых содержить данные студентво.
    """
    
    student_data = []

    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            student_data.append(row)
    
    return student_data

def insertion_sort(student_data, key):
    """
    Алгоритм сортировки вставками.

    Args:
        student_data (list of dict): Список словарей, каждый из которых содержить данные студентво.
        key (str): Ключ по которому будет провилиться сортировка.

    Returns:
        student_data (list of dict): Перевернутый и отсортированый список словорей.
    """
    
    for i in range(1, len(student_data)):
        current_value = student_data[i]
        position = i

        while position > 0 and student_data[position - 1][key] > current_value[key]:
            student_data[position] =  student_data[position - 1]
            position -= 1

        student_data[position] = current_value
        
    return student_data[::-1]


def print_top_students(student_data, count, student_class):
    """
    Вывод топ студентов.

    Args:
        student_data (list of dict): Список словарей, каждый из которых содержить данные студентво.
        count (int): Кол-во топ студентов.
        student_class (str): Класс студентов.
    """

    place = 1

    print(f"{student_class} класс:")
    
    for student in student_data[:count]:
        print(f"{place} место: {student['name'][0]}.{student['surname']}")
        place += 1


def main():
    student_data_from_csv = read_csv("student_new.csv")
    sorted_student_data = insertion_sort(student_data_from_csv, "grade")
    print_top_students(sorted_student_data, 3, "11")
    
    

    


    # clear_data = process_student_data(student_data)

    # save_to_csv(clear_data, "student_new.csv")

    # for student in clear_data:
    #     if student["name"] == "Владимир" and student["surname"] == "Хадаров":
    #         print(f"Ты получил {student['grade']}, за проект - {student['project_id']}")


main()


# {"name": "Андрей", "surname": "Попов", "grade": 5, "project_id": "1"}



    