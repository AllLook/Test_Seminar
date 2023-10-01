"""*Задание 1. *Представьте, что вы работаете над разработкой простого приложения для записной книжки,
которое позволяет пользователям добавлять, редактировать и удалять контакты.
Ваша задача - придумать как можно больше различных тестов (юнит-тесты, интеграционные тесты, сквозные тесты)
для этого приложения. Напишите название каждого теста, его тип и краткое описание того, что этот тест проверяет."""
# *Задание 2. *Ниже список тестовых сценариев. Ваша задача - определить тип каждого теста (юнит-тест, интеграционный тест, сквозной тест) и объяснить, почему вы так решили.
# Проверка того, что функция addContact корректно добавляет новый контакт в список контактов"".
# ""Проверка того, что при добавлении контакта через пользовательский интерфейс, контакт корректно отображается в списке контактов"".
# ""Проверка полного цикла работы с контактом: создание контакта, его редактирование и последующее удаление"".

import csv

list_data_user = {}
print(type(list_data_user))


def add_user(*args):
    name = input('Введите имя:')
    surname = input('Введите фамилию:')
    phone_number = input('Введите номер телефона:')
    id_user = 1
    temp_user = [name, surname, phone_number]
    if id_user not in list_data_user:
        list_data_user[id_user] = temp_user
    else:
        id_user += 1
        list_data_user[id_user] = temp_user

    for key, value in list_data_user.items():
        temp = key, value
    # headers = ['id_user', 'data_user']
    with(
        open('user_file.csv', 'a', newline='', encoding='utf-8') as f_write,
    ):
        csv_write = csv.writer(f_write, dialect='excel-tab',
                               quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writerow(temp)
    return list_data_user


def del_user(id_user):
    with(
        open('user_file.csv', 'r', newline='') as f_read
    ):
        csv_read = csv.reader(f_read, dialect='excel-tab',
                              quoting=csv.QUOTE_NONNUMERIC)

        for line in csv_read:
            print(line)
            if int(line[0]) == id_user:
                print(line[0])
                with(
                    open('user_file_output.csv', 'a', newline='', encoding='utf-8') as f_write,
                ):
                    csv_write = csv.writer(f_write,
                                           quoting=csv.QUOTE_NONNUMERIC)
                    csv_write.writerow({f'User id_user {id_user} : del'})
                    return f'User {id_user} del'

    return None


def user_change(id_user):
    with(
        open('user_file.csv', 'r', newline='') as f_read
    ):
        csv_read = csv.reader(f_read, dialect='excel-tab',
                              quoting=csv.QUOTE_NONNUMERIC)

        for line in csv_read:
            if line[0] == id_user:
                line[1] = ['xxx', 'jjjj', '89098']

            with(
                open('user_file_output.csv', 'a', newline='', encoding='utf-8') as f_write,
            ):
                csv_write = csv.writer(f_write,
                                       quoting=csv.QUOTE_NONNUMERIC)
                csv_write.writerow({str(line)})
                return f'User {id_user} change'

# print(add_user(name, surname, phone_number))
# print(del_user(1))
# print(user_change(1))
