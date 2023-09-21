"""Задание
1. ** В
классе
Calculator
создайте
метод
calculateDiscount, который
принимает
сумму
покупки
и
процент
скидки
и
возвращает
сумму
с
учетом
скидки.Ваша
задача - проверить
этот
метод
с
использованием
библиотеки
AssertJ.Если
метод
calculateDiscount
получает
недопустимые
аргументы, он
должен
выбрасывать
исключение
ArithmeticException.Не
забудьте
написать
тесты
для
проверки
этого
поведения."""

from ValueException import ValuePositiveExtptions


class Calculater:
    def calculate_discount(self, sum_order: float, discount: int):
        if sum_order <= 0 or discount <= 0:
            raise ValuePositiveExtptions(f'неверное значение или 0 для {sum_order} или {discount}')

        else:

            return sum_order / 100 * discount

    def calculate_discount_2(self, sum_order: float, discount: int):
        # try:
        return sum_order / 100 * discount

    # except TypeError:
    #     print(f'Недопустимое значение аргумента!')


c1 = Calculater()


def test_calculate_discount_positive():
    assert c1.calculate_discount(1000, 7) == 70, 'Тест провален по значению аргумента'
    print('тест пройден')


def test_calculate_discount_value():
    try:
        c1.calculate_discount_2(1000, '60')
    except TypeError:
        print('Тест пройден, ошибка должна возникнуть')


if __name__ == '__main__':
    # c1 = Calculater()
    # print(c1.calculate_discount(1000, 9))
    # print(c1.calculate_discount_2('90', 0))
    test_calculate_discount_positive()
    test_calculate_discount_value()
