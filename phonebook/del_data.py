import controller
from UI import del_phone  # забирает функцию поиска для удаления данных из файла UI.py

#  Функция для считывания данных из файла  в виде строки
def open_file(file):
    with open(f"{file}", "r") as text_in:
        str_in = text_in.readline()
    return str_in

# Функция для перезаписи данных в файле после удаления
def write_file(file, data):
    with open(file, "w") as text_out:
        text_out.write(data)

# Функция для удаления данных в файле
def remove_data():
    phone = del_phone()
    lst = open_file("uses.csv").split(",")
    result = 0
    for i in range(0, len(lst)):
        if len(lst) > 0:
            if f"phone: +7 {phone}" in lst[i]:
                del lst[i]
                lst = str(",".join(lst))
                print(f"Абонент с номером {phone} успешно удален из справочника!")
                result = 1
    if result == 0:
        print(f"Абонент с номером {phone} в справочнике не обнаружен!")
    write_file("uses.csv", lst)
    
