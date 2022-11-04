# Юзер-интерфейс, то что будет видеть пользователь, его взаимодействие с программой


def print_data(data):
    print(data)

# Функция для ввода данных
def input_data(data):
    input(f"{data}")

# Функция за ввод данных абонента
def input_phonebook():
    phone = check_phone()
    surname = input("Фамилия: ")
    name = input("Имя: ")
    patronymic = input("Отчество: ")
    return f"Телефон: +7{phone} Фамилия: {surname} Имя: {name} Отчество: {patronymic}"

# Функция проверки корректность ввода номера телефона
def check_phone():
    flag = False
    while flag == False:
        phone = input("Телефон: +7 ")
        if phone.isdigit():
            flag = True
            return phone
        else:
            print("Некорректный ввод, повторите попытку.")

# Функция проверки вводимой пользователем цифры
def input_check_choice(text):
    flag = False
    while flag == False:
        user_answer = input(text)
        try:
            int(user_answer)
            if 0 < int(user_answer) < 5:
                return int(user_answer)
            else:
                flag == False
        except ValueError:
            flag == False

# Функция, отвечающая за поиск телефона для удаления
def del_phone():
    d_phone = int(input("Введите номер телефона для удаления записи: "))
    return d_phone

# Функция, отвечающая за поиск телефона в списке
def find_data():
    f_data = input("Введите номер телефона для поиска: ")
    return f_data
