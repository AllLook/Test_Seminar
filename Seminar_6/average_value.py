# Задание 1. Создайте программу на Python или Java, которая принимает два списка чисел и выполняет следующие действия:
# a. Рассчитывает среднее значение каждого списка.
# b. Сравнивает эти средние значения и выводит соответствующее сообщение:
# - ""Первый список имеет большее среднее значение"", если среднее значение первого списка больше.
# - ""Второй список имеет большее среднее значение"", если среднее значение второго списка больше.
# - ""Средние значения равны"", если средние значения списков равны.


class AverageValue:
    list_1 = []
    list_2 = []

    def average(self, list_1: list, list_2: list):
        self.list_1 = list_1
        self.list_2 = list_2
        temp_1 = sum(list_1) / len(list_1)
        temp_2 = sum(list_2) / len(list_2)
        print(temp_1, temp_2)
        if temp_1 > temp_2:
            print('Первый список имеет большее среднее значение')
            return 'Первый список имеет большее среднее значение'
        elif temp_1 < temp_2:
            print('Второй список имеет большее среднее значение')
            return 'Второй список имеет большее среднее значение'
        else:
            print('Средние значения равны')
            return 'Средние значения равны'

# a1 = AverageValue()
# a1.average(2, 6)