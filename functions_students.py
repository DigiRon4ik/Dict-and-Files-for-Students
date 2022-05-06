def load_students(file: str) -> dict:
    """Загрузить студентов из файла в словарь.\n
    file: Путь к файлу. (students.txt)"""

    std = {}
    std_key = 1
    with open(file, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            l = line.rstrip().split(', ')
            std[std_key] = {'ФИО': l[0],
                            'Возраст': l[1],
                            'Группа': l[2],
                            'Специальность': l[3],
                            'Квалификация': l[4]}
            std_key += 1
    return std


def save_students(file: str, students: dict):
    """Сохранить студентов из словаря в файл.\n
    file: Путь к файлу. (students.txt)"""

    with open(file, 'w', encoding='utf-8') as f:
        for v in students.values():
            f.write(', '.join(v.values()) + '\n')


def printer_students(students: dict):
    """Вывести студентов в таблице.\n
    students: Словарь студенов."""

    str_equals = '+' + '='*4 + '+' + '='*37 + '+' + \
        '='*9 + '+' + '='*8 + '+' + '='*27 + '+' + '='*14 + '+'
    str_underline = '+' + '-'*4 + '+' + '-'*37 + '+' + \
        '-'*9 + '+' + '-'*8 + '+' + '-'*27 + '+' + '-'*14 + '+'
    print(str_equals)
    print('| {:>2} | {:^35} | {:^7} | {:^6} | {:^25} | {:^12} |'.format(
        '№', 'ФИО', 'Возраст', 'Группа', 'Специальность', 'Квалификация'))
    print(str_equals)

    for k, v in students.items():
        print('| {:>2} | {:<35} | {:>7} | {:>6} | {:<25} | {:^12} |'.format(
            k, v['ФИО'], v['Возраст'], v['Группа'], v['Специальность'], v['Квалификация']))
        print(str_underline)


def print_student(students: dict, number_student: int = None):
    """Вывести студента из словаря либо напрямую либо через консоль.\n
    students: Словарь студенов.\n
    number_student: Номер студента."""

    if number_student is None:
        number_student = int(input('Введите номер студента: '))
    print('\t' + ', '.join(students[number_student].values()))


def add_student(students: dict, new_student: str = None):
    """Добавить студента либо напрямую либо через консоль.\n
    students: Словарь студенов.\n
    new_student: Нужно вводить через ', '."""

    if new_student is None:
        new_student = input('Вводите данные нового студента через ", ":\n').split(', ')
    else:
        new_student = new_student.split(', ')

    students[len(students) + 1] = {'ФИО': new_student[0],
                                   'Возраст': new_student[1],
                                   'Группа': new_student[2],
                                   'Специальность': new_student[3],
                                   'Квалификация': new_student[4]}


def edit_student(students: dict, edit_student: str = None, number_student: int = None):
    """Редактировать студента либо напрямую либо через консоль.\n
    students: Словарь студенов.\n
    edit_student: Нужно вводить через ', '.\n
    number_student: Номер студента."""

    if number_student is None:
        number_student = int(input('Введите номер студента: '))
        print('\tИз -> ' + ', '.join(students[number_student].values()))

    if edit_student is None:
        edit_student = input('Вводите данные для редактирования через ", ":\n\tНа -> ')

    edit_student = edit_student.split(', ')
    students[number_student] = {'ФИО': edit_student[0],
                                'Возраст': edit_student[1],
                                'Группа': edit_student[2],
                                'Специальность': edit_student[3],
                                'Квалификация': edit_student[4]}


def delet_student(students: dict, number_student: int = None):
    """Удалить студента из словаря либо напрямую либо через консоль.\n
    students: Словарь студенов.\n
    number_student: Номер студента."""

    if number_student is None:
        number_student = int(input('Введите номер студента: '))
        print('\tУдаляется -> ' + ', '.join(students[number_student].values()))

    del students[number_student]
    for k in range(number_student+1, len(students)+2):
        students[k-1] = students.pop(k)
