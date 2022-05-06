def load_students(file: str) -> dict:
    """Загрузить студентов из файла в словарь.\n
    file: Путь к файлу. (students.txt)"""

    std = {}
    std_key = 1
    with open(file, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            l = line.rstrip().split(', ')
            std[std_key] = {'Full Name': l[0],
                            'Age': l[1],
                            'Group': l[2],
                            'Speciality': l[3],
                            'Qualification': l[4]}
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
        '№', *students[1].keys()))
    print(str_equals)

    for k, v in students.items():
        print('| {:>2} | {:<35} | {:>7} | {:>6} | {:<25} | {:^12} |'.format(
            k, *v.values()))
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

    std_keys = students[1].keys()
    new_index, last_index = 0, len(students) + 1
    students[last_index] = {}
    for i in std_keys:
        students[last_index][i] = new_student[new_index]
        new_index += 1


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
    new_index, std_keys = 0, students[1].keys()
    for i in std_keys:
        students[number_student][i] = edit_student[new_index]
        new_index += 1


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
