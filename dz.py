import random

# Список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
students.sort()

# Список предметов
subjects = ['Математика', 'Русский язык', 'Информатика']

# Генерация оценок
students_marks = {student: {subject: [random.randint(1, 5) for _ in range(3)] for subject in subjects} for student in students}

def print_menu():
    print('\nСписок команд:')
    print('1. Добавить оценку ученику по предмету')
    print('2. Удалить оценку ученика по предмету')
    print('3. Редактировать оценку ученика по предмету')
    print('4. Вывести средний балл каждого ученика')
    print('5. Вывести все оценки для ученика')
    print('6. Вывести средний балл по предмету для ученика')
    print('7. Добавить ученика')
    print('8. Удалить ученика')
    print('9. Добавить предмет')
    print('10. Удалить предмет')
    print('11. Вывести все оценки')
    print('12. Выход')

def add_mark():
    student = input('Введите имя ученика: ')
    subject = input('Введите предмет: ')
    mark = int(input('Введите оценку: '))
    if student in students_marks and subject in students_marks[student]:
        students_marks[student][subject].append(mark)
        print(f'Добавлена оценка {mark} для {student} по {subject}')
    else:
        print('Ошибка: Неверное имя ученика или предмет')

def delete_mark():
    student = input('Введите имя ученика: ')
    subject = input('Введите предмет: ')
    if student in students_marks and subject in students_marks[student]:
        if students_marks[student][subject]:
            students_marks[student][subject].pop()
            print(f'Удалена последняя оценка по {subject} у {student}')
        else:
            print('Ошибка: У ученика нет оценок по этому предмету')
    else:
        print('Ошибка: Неверное имя ученика или предмет')

def edit_mark():
    student = input('Введите имя ученика: ')
    subject = input('Введите предмет: ')
    if student in students_marks and subject in students_marks[student]:
        print(f'Текущие оценки: {students_marks[student][subject]}')
        index = int(input('Введите индекс оценки (0, 1, 2...): '))
        if 0 <= index < len(students_marks[student][subject]):
            new_mark = int(input('Введите новую оценку: '))
            students_marks[student][subject][index] = new_mark
            print('Оценка изменена!')
        else:
            print('Ошибка: Неверный индекс')
    else:
        print('Ошибка: Неверное имя ученика или предмет')

def print_avg_marks():
    for student, subjects in students_marks.items():
        avg = sum(sum(marks) for marks in subjects.values()) / sum(len(marks) for marks in subjects.values())
        print(f'{student}: {avg:.2f}')

def print_student_marks():
    student = input('Введите имя ученика: ')
    if student in students_marks:
        for subject, marks in students_marks[student].items():
            print(f'{subject}: {marks}')
    else:
        print('Ошибка: Ученик не найден')

def print_avg_subject():
    student = input('Введите имя ученика: ')
    subject = input('Введите предмет: ')
    if student in students_marks and subject in students_marks[student]:
        avg = sum(students_marks[student][subject]) / len(students_marks[student][subject])
        print(f'Средний балл {student} по {subject}: {avg:.2f}')
    else:
        print('Ошибка: Ученик или предмет не найден')

def add_student():
    student = input('Введите имя нового ученика: ')
    if student not in students_marks:
        students_marks[student] = {subject: [] for subject in subjects}
        print(f'Ученик {student} добавлен')
    else:
        print('Ошибка: Ученик уже существует')

def delete_student():
    student = input('Введите имя ученика для удаления: ')
    if student in students_marks:
        del students_marks[student]
        print(f'Ученик {student} удален')
    else:
        print('Ошибка: Ученик не найден')

def add_subject():
    subject = input('Введите название нового предмета: ')
    if subject not in subjects:
        subjects.append(subject)
        for student in students_marks:
            students_marks[student][subject] = []
        print(f'Предмет {subject} добавлен')
    else:
        print('Ошибка: Предмет уже существует')

def delete_subject():
    subject = input('Введите название предмета для удаления: ')
    if subject in subjects:
        subjects.remove(subject)
        for student in students_marks:
            del students_marks[student][subject]
        print(f'Предмет {subject} удален')
    else:
        print('Ошибка: Предмет не найден')

def print_all_marks():
    for student, subjects in students_marks.items():
        print(f'{student}:')
        for subject, marks in subjects.items():
            print(f'  {subject}: {marks}')

commands = {
    1: add_mark,
    2: delete_mark,
    3: edit_mark,
    4: print_avg_marks,
    5: print_student_marks,
    6: print_avg_subject,
    7: add_student,
    8: delete_student,
    9: add_subject,
    10: delete_subject,
    11: print_all_marks
}

while True:
    print_menu()
    try:
        command = int(input('Введите команду: '))
        if command == 12:
            print('Выход из программы')
            break
        elif command in commands:
            commands[command]()
        else:
            print('Ошибка: Неверная команда')
    except ValueError:
        print('Ошибка: Введите число')
