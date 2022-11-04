# звено связывающие файлы

import reading_data
import print_all_data
import UI
import add_data
import logger
import search_data
import del_data

# Функция определения запроса пользователя
def button_click():
    UI.print_data("Для работы со справочником введите цифру (действие): ")
    answer = UI.input_check_choice(
        "1 - если хотите вывести весь телефонный справочник\n2 - если хотите добавить нового абонента\n"
        + "3 -если хотите найти абонента по номеру телефона\n4 - если хотите удалить абонента по номеру телефона\n"
        + "5 - если хотите завершить работу с системой\nВведите номер действия: "
    )
    if answer == 1:   # Вывод всего телефонного справочника
        list_data = reading_data.get_info("uses.csv")  # читаем
        print_all_data.print_all(list_data)  # печатаем все
        UI.print_data(f"\nВ справочнике {len(list_data)-1} абонентов\n")
        button_click()
    elif answer == 2:   # Добавление нового номера
        user_data = UI.input_phonebook()
        add_data.append_data("uses.csv", user_data)
        logger.result_loger(user_data)
        UI.print_data("\nДанные успешно добавлены в телефонный справочник.")
        button_click()
    elif answer == 3:    # Поиск по номеру телефона.
        search_data.search_phone()
        button_click()
    elif answer == 4:    # Удаление записи по номеру телефона.
        del_data.remove_data()
        button_click()
    elif answer == 5:    # Остановка программы
        exit()
    else:
        print("неправильный ввод")
        button_click()
