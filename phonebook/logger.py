from datetime import datetime as dt

# Функция для фиксации времени при внесении данных в справочник
def result_loger(data):
    time = dt.now().strftime('%H:%M')
    with open("logbook.txt", 'a') as file:
        file.write(f'{time}: new entry: {data}\n')
#, encoding='utf-8'