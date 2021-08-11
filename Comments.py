"""
Формирование строк комментариев
"""


def create_comment(com: str = "", len_com: int = 70,
                   com_sim: str = "#", null_sim: str = "-"):
    """
    Функция которая создает комментарии для Cmake
    :param com:
    :param len_com:
    :param com_sim:
    :param null_sim:
    :return:
    """
    string_com = '#'
    if com == "":
        for i in range(len_com - 1):
            string_com += null_sim
        string_com += f'{com_sim}\n'
    else:
        center_string = com.center(len_com)
        st_sim = center_string.find(com)
        end_sim = st_sim + len(com)
        for i in range(len_com - 1):
            if end_sim < i or i < st_sim:
                string_com += null_sim
            else:
                string_com += center_string[i]
        string_com += f'{com_sim}\n'
    return string_com


if __name__ == "__main__":
    string_1 = create_comment("Линковка библиотек")
    string_2 = create_comment()
    print(f'{string_2}{string_1}{string_2}')
    if len(string_1) != len(string_2):
        print(len(string_1), len(string_2), "Error")
    else:
        print(len(string_1), len(string_2), "all ok!")
    quit(0)
