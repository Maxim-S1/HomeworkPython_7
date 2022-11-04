import controller   # забирает данные из controller.py
import UI as ui     # забирает данные и UI.py

#  Функция для считывания данных из файла  в виде строки
def open_file(file):
    with open(f"{file}", "r") as text_in:
        str_in = text_in.readline()
    return str_in

# Функция проверки сотрудника с телефоном в базе данных
def search_phone():
    find_str = ui.find_data()
    lst = open_file("uses.csv").split(",")
    result = 0
    for i in range(0, len(lst)):
        if find_str in lst[i]:
            print(lst[i])
            result = 1
    if result == 0:
        print(f'Сотрудника c телефоном "{find_str}" в базе не обнаружено!')
    controller.button_click()
