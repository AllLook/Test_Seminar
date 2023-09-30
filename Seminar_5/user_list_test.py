import unittest
import note_book as nt


class Test_User_List(unittest.TestCase):
    def setUp(self) -> None:
        self.list_data_user = nt.list_data_user
        print(type(self.list_data_user))

    def test_type_list(self):
        self.assertTrue(len(self.list_data_user) == 0)  # простой тест что словарь-список изначально пуст

    def test_add_user(self):
        self.assertEqual(self.list_data_user, nt.add_user(),
                         self.list_data_user)  # ИНТЕГРАЦИОННЫЙ, принимает на вход словарь, работает с ним и проверяет что возвращается словарь

    def test_all_options_user(self):
        self.assertEqual(self.list_data_user, nt.add_user(), self.list_data_user)
        self.assertEqual(nt.del_user(1), 'User 1 del')
        self.assertEqual(nt.user_change(1), 'User 1 change')
