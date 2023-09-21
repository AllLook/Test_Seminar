class ValueExeptions(Exception):
    pass


class ValuePositiveExtptions(ValueExeptions):
    def __int__(self, value):
        self.value = value

    def __str__(self):
        return f'Значения заказа или скидки имеют не верное значение  !'
