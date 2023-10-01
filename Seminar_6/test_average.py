import pytest

from average_value import AverageValue as av


def test_value_average():
    a1 = av()
    assert a1.average([10, 2, 5, 8], [6, 7, 3, 4]) == 'Первый список имеет большее среднее значение'
    assert a1.average([1, 2, 5, 8], [6, 7, 3, 4]) == 'Второй список имеет большее среднее значение'
    assert a1.average([10, 10, 10], [10, 10, 10]) == 'Средние значения равны'


# def test_type():
#     a1 = av()
#     with pytest.raises(TypeError):
#         a1.average(2, 6)

if __name__ == '__main__':
    pytest.main(['-v'])
