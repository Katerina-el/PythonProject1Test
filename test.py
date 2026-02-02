import random

students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
students.sort()
classes = ['Математика', 'Русский язык', 'Информатика']
students_marks = {}
for student in students:
    students_marks[student] = {}
    for class_ in classes:
        marks = [random.randint(2, 5) for i in range(3)]
        students_marks[student][class_] = marks
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        --- Блок "Добавить"
        1. Добавить новый предмет
        2. Добавить нового ученика
        3. Добавить оценки ученика по предмету
        --- Блок "Редактировать"
        4. Редактировать предметы
        5. Редактировать учеников
        6. Редактировать оценки ученика по предмету
        --- Блок "Удалить"
        7. Удалить предмет
        8. Удалить ученика
        9. Удалить оценки ученика по предмету
        --- Блок "Оценки" для аналитики
        10. Вывести средний балл по всем предметам по каждому ученику
        11. Вывести средний балл по всем предметам по определённому ученику
        12. Вывести все оценки по всем ученикам
        13. Вывести все оценки по определённому ученику
        --- Блок "Технический"
        14. Выход из программы''')

while True:
    print()
    command = int(input('Введите команду: '))
    if command == 1:
        print()
        print('1. Добавить новый предмет')
        new_class = input("Введите новый предмет: ")
        print()
        if new_class.title() not in classes:
            classes.append(new_class)
            print('Список предметов: ')
            for i in range(len(classes)):
                print(f"{i + 1}. {classes[i]}")
        else:
            print('ОШИБКА: данный предмент уже есть в списке')

    elif command == 2:
        print()
        print('2. Добавить нового ученика')
        new_name = input("Введите нового ученика: ")
        print()
        students.append(new_name)
        print('Список учеников: ')
        for i in range(len(students)):
            print(f"{i + 1}. {students[i]}")

    elif command == 3:
        print('3. Добавить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        mark = int(input('Введите оценку: '))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')

    elif command == 4:
        print()
        print('4. Редактировать предметы')
        print()
        for i in range(len(classes)):
            print(f"{i + 1}. {classes[i]}")
        print()
        index_class = int(input("Введите номер предмета для редактирования: "))
        if index_class - 1 < len(classes):
            new_name_class = input("Введите новое наименование предмета: ")
            classes[index_class - 1] = new_name_class
            print()
            for i in range(len(classes)):
                print(f"{i + 1}. {classes[i]}")
        else:
            print('ОШИБКА: индекс предмета выходит за размер списка предметов')

    elif command == 5:
        print()
        print('5. Редактировать учеников')
        print()
        for i in range(len(students)):
            print(f"{i + 1}. {students[i]}")
        print()
        index_student = int(input("Введите номер ученика для редактирования: "))
        if index_student - 1 < len(students):
            new_name_student = input("Введите имя ученика: ")
            students[index_student - 1] = new_name_student
            print()
            for i in range(len(students)):
                print(f"{i + 1}. {students[i]}")
        else:
            print('ОШИБКА: индекс ученика выходит за размер списка учеников')

    elif command == 6:
        print('6. Редактировать оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            print(f"{student}. {class_}. Оценки: {students_marks[student][class_]}")
            index_mark_ = int(input('Введите порядковый номер оценки для редактирования (от 1): '))
            if index_mark_ - 1 < len(students_marks[student][class_]):
                mark = int(input('Введите исправленную оценку: '))
                old_mark = students_marks[student][class_][index_mark_ - 1]
                print()
                students_marks[student][class_][index_mark_ - 1] = mark
                print(f'Для {student} по предмету {class_} была исправлена оценка {old_mark} на {mark}')
                print(f"{student}. {class_}. Оценки: {students_marks[student][class_]}")
            else:
                print(f'ОШИБКА: оценки под №{index_mark_} нет')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')

    elif command == 7:
        print()
        print('7. Удалить предмет')
        print()
        for i in range(len(classes)):
            print(f"{i + 1}. {classes[i]}")
        print()
        index_class = int(input("Введите номер предмета для удаления: "))
        if index_class - 1 < len(classes):
            qwerty = input(f"Вы уверены, что хотите удалить предмет {classes[index_class - 1]}? Процесс необратим. "
                           f"Ответьте: Да / Нет: ")
            if qwerty.lower() == "да":
                delete = classes.pop(index_class - 1)
                print(f"Предмет {delete} удалён из списка")
                print()
                for i in range(len(classes)):
                    print(f"{i + 1}. {classes[i]}")
            elif qwerty.lower() == "нет":
                print("Процесс удаления отменён. Список предметов остался прежним")
                for i in range(len(classes)):
                    print(f"{i + 1}. {classes[i]}")
            else:
                print("Необходимо было написать Да / Нет. Попробуйте снова")
        else:
            print('ОШИБКА: индекс предмета выходит за размер списка предметов')

    elif command == 8:
        print()
        print('8. Удалить ученика')
        print()
        for i in range(len(students)):
            print(f"{i + 1}. {students[i]}")
        print()
        index_student = int(input("Введите номер ученика для удаления: "))
        if index_student - 1 < len(students):
            qwerty = input(f"Вы уверены, что хотите удалить ученика {students[index_student - 1]}? Процесс необратим. "
                           f"Ответьте: Да / Нет: ")
            if qwerty.lower() == "да":
                delete = students.pop(index_student - 1)
                print(f"Ученик {delete} удалён из списка")
                print()
                for i in range(len(students)):
                    print(f"{i + 1}. {students[i]}")
            elif qwerty.lower() == "нет":
                print("Процесс удаления отменён. Список учеников остался прежним")
                for i in range(len(students)):
                    print(f"{i + 1}. {students[i]}")
            else:
                print("Необходимо было написать Да / Нет. Попробуйте снова")
        else:
            print('ОШИБКА: индекс ученика выходит за размер списка предметов')

    elif command == 9:
        print('9. Удалить оценки ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            print(f"{student}. {class_}. Оценки: {students_marks[student][class_]}")
            index_mark_ = int(input('Введите порядковый номер оценки для удаления (от 1): '))
            if index_mark_ - 1 < len(students_marks[student][class_]):
                delete = students_marks[student][class_].pop(index_mark_ - 1)
                print(f'Для {student} по предмету {class_} была удалена оценка {delete}]')
                print(f"{student}. {class_}. Оценки: {students_marks[student][class_]}")
            else:
                print(f'ОШИБКА: оценки под №{index_mark_} нет')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')

    elif command == 10:
        print('10. Вывести средний балл по всем предметам по каждому ученику')
        for student in students:
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {marks_sum // marks_count}')
            print()

    elif command == 11:
        print('10. Вывести средний балл по всем предметам по определённому ученику')
        for i in range(len(students)):
            print(f"{i + 1}. {students[i]}")
        index_student = int(input("Введите порядковый номер ученика: "))
        if index_student - 1 < len(students):
            student = students[index_student - 1]
            print(f'Средний бал у {student}:')
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {marks_sum // marks_count}')
            print()
        else:
            print('ОШИБКА: индекс ученика выходит за размер списка предметов')

    elif command == 12:
        print('12. Вывести все оценки по каждому ученику')
        for student in students:
            print(student)
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()

    elif command == 13:
        print('13. Вывести все оценки по определённому ученику')
        for i in range(len(students)):
            print(f"{i + 1}. {students[i]}")
        index_student = int(input("Введите порядковый номер ученика: "))
        if index_student - 1 < len(students):
            student = students[index_student - 1]
            print(f'Оценки у {student}:')
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
        else:
            print('ОШИБКА: индекс ученика выходит за размер списка предметов')

    elif command == 14:
        print('14. Выход из программы')
        break