import pytest
from vowel_counter import count_russian_vowels

# Тест на базовое слово с двумя гласными
def test_basic_word():
    assert count_russian_vowels("привет") == 2

# Проверка работы с заглавными буквами
def test_uppercase():
    assert count_russian_vowels("ПРИВЕТ") == 2

# Проверка смешанного регистра
def test_mixed_case():
    assert count_russian_vowels("ПрИвЕт") == 2

# Слово без гласных — должно вернуть 0
def test_no_vowels():
    assert count_russian_vowels("глглгл") == 0

# Все русские гласные, в нижнем и верхнем регистре — всего 20
def test_all_vowels():
    assert count_russian_vowels("аеёиоуыэюяАЕЁИОУЫЭЮЯ") == 20

# Пустая строка — результат должен быть 0
def test_empty_string():
    assert count_russian_vowels("") == 0

# Строка с пробелами и знаками препинания — должны учитываться только буквы
def test_with_spaces_and_punctuation():
    assert count_russian_vowels("Привет, как дела?") == 5
