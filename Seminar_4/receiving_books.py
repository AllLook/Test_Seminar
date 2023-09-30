# У вас есть класс BookService, который использует интерфейс BookRepository для получения информации о книгах из базы данных.
# Ваша задача написать unit-тесты для BookService, используя Mockito для создания мок-объекта BookRepository

import abc


class BookRepository(abc.ABC):
    def __init__(self, book_repository: dict):
        self.book_repositorty = book_repository

    def book_info(self, author, book_repositorty: dict):
        self.book_repositorty = book_repositorty
        book_temp = []
        for temp_author, temp_list in book_repositorty.items():
            if temp_author == author:
                for item in temp_list:
                    book_temp.append(item)
        return book_temp


# temp = {
#     'Л.Толстой': ['Детство', 'Два гусара'], 'Н.Гоголь': ['Мёртвые души', 'Коляска'], 'А.Чехов': ['Свадьба', 'Юбилей']
# }
# b1 = BookRepository(temp)
# print(b1.book_info('Н.Гоголь', temp))


class BookService(BookRepository):
    def __init__(self, *args):
        super().__init__(*args)
