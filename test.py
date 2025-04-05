# # import pytest
# # #from main import check
# # from main import is_palindrome
# # #
# # # def test_check():
# # #     assert check(2) == True
# # # #
# # # #
# # # # def test_check2():
# # # #    assert check(3) == False
# # #
# # #
# # # @pytest.mark.parametrize("number, expected", [(4, True), (5, False), (6, True), (-7, False), (0, True)])
# # # def test_check3(number, expected):
# # #     assert check(number) == expected
# #
# # def test_is_palindrome():
# #     assert is_palindrome("racecar") == True
# #
# # def test_is_palindrome2():
# #     assert is_palindrome("hello") == False
# #
# # @pytest.mark.parametrize("text_input, expected", [
# #                          ("level", True),
# #                          ("racecar", True),
# #                          ("hello", False),
# #                          ("mama", False),
# #                          ("dad", True),
# #                          ("mom", True),
# #                          ("abba", True),
# #                          ("racecar", True),
# #                          ("hello", False)
# # ])
# #
# # def test_is_palindrome3(text_input, expected):
# #     assert is_palindrome(text_input) == expected
#
# import pytest
# from main import sort_list
#
# def test_sort_list():
#     assert sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# def test_sort_list2():
#     assert sort_list([-1, 2, -3, 4, -5, 6, 7, 8, 9, 10]) == [-5, -3, -1, 2, 4, 6, 7, 8, 9, 10]

import pytest
from main import get_users, add_user, init_db

@pytest.fixture
def conn():
    conn = init_db()
    yield conn
    conn.close()

def test_get_users(conn):
    add_user(conn, "Alice", 25)
    user = get_users(conn, "Alice")
    assert user == (1, "Alice", 25)
