"""
Запись и чтение из Cmake файлов
"""


def _make_string(data: list):
    """
    Функция принимает список строк и
    превращает его в одну строку
    :param data: Список строк
    :return: Строка из исписка
    """
    string_data = ''
    for i in data:
        string_data += i
    return string_data


def read_file(path: str):
    """
    Функция чтения файла Cmake
    :param path: Путь к файлу
    :return: Список строк файла, результат чтения
    """
    data = []
    # Открытие файла на чтение
    try:
        file = open(path, 'r', encoding='utf-8')
    except IOError as err:
        print(f"Не удалось открыть файл: {path}\n{err}")
        return data, 1
    else:
        with file:
            for string in file.readlines():
                data.append(string)
    return data, 0


def write_file(path: str, data: list):
    """
    Функция записи в файл данных
    :param data: Данные для записи
    :param path: Путь к файлу
    :return: Статус записи
    """
    try:
        file = open(path, 'w', encoding='utf-8')
    except IOError as err:
        print(f"Не удалось открыть файл: {path}\n{err}")
        return 1
    else:
        with file:
            write_data = _make_string(data)
            file.write(write_data)
    return 0


if __name__ == "__main__":
    file_data, status_operation = read_file('d:/C++/Progect_2/CMakeLists.txt')
    print(file_data)
    print(f"Статус чтения: {status_operation}")
    status_operation = write_file('d:/C++/Progect_2/CMakeLists.txt', file_data)
    print(f"Статус записи: {status_operation}")
    quit(0)
