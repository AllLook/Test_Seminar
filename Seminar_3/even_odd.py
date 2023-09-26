# *Задание 1.
#
# Напишите тесты, покрывающие на 100% метод evenOddNumber, который проверяет, является ли переданное число четным или нечетным. (код приложен в презентации)
#
# Задание 2.
#
# Разработайте и протестируйте метод numberInInterval, который проверяет, попадает ли переданное число в интервал (25;100). (код приложен в презентации)




def even_odd_num(num: int):
    return num % 2 == 0


def numberInInterval(num: int):
    if num >= 25 and num <= 100:
        return True
    else:
        return False


# if __name__ == '__main__':
#     print(even_odd_num(6))
#     print(numberInInterval(3))
