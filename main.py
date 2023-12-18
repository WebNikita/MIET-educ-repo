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

    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def main():
    clear_data = process_student_data(student_data)
    save_to_csv(clear_data, "student_new.csv")

    for student in clear_data:
        if student["name"] == "Владимир" and student["surname"] == "Хадаров":
            print(f"Ты получил {student['grade']}, за проект - {student['project_id']}")


main()




    