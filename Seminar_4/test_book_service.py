import unittest
from unittest.mock import Mock, patch

from Test_Seminar.Seminar_4.receiving_books import BookService


class TestBookService(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = {
            'Л.Толстой': ['Детство', 'Два гусара'], 'Н.Гоголь': ['Мёртвые души', 'Коляска'],
            'А.Чехов': ['Свадьба', 'Юбилей']
        }
        self.book_service = Mock()
        self.book_service = BookService(self.temp)


    def test_book_service(self):
        self.assertEqual(self.book_service.book_info('Н.Гоголь', self.temp), ['Мёртвые души', 'Коляска'])
