from lesson_7_dz import sort_list_growth
from lesson_7_dz import sort_list_desc
from lesson_7_dz import sort_list_words
from lesson_7_dz import list_growth
from lesson_7_dz import list_words


def test_sort_list_growth():
    assert sort_list_growth(list_growth) == [1, 13, 25, 79, 100]


def test_sort_list_desc():
    assert sort_list_desc(list_growth) == [100, 79, 25, 13, 1]


def test_sort_list_words():
    assert sort_list_words(list_words) == ['мило', 'вікно', 'яблоко', 'апельсин', 'гелікоптер']
