from lesson_7_dz import sort_list_growth
from lesson_7_dz import sort_list_desc
from lesson_7_dz import sort_list_words
from lesson_7_dz import sort_list_growth_for_assert
from lesson_7_dz import list_growth
from lesson_7_dz import list_words
from lesson_7_dz import list_growth_for_assert


def test_sort_list_growth():
    sort_list_growth(list_growth)


def test_sort_list_desc():
    sort_list_desc(list_growth)


def test_sort_list_words():
    sort_list_words(list_words)


# def test_sort_list_words_with_assert():
#     assert "мило" not in sort_list_words(list_words), "Лист містить слово 'мило'"
#
#
# def test_sort_list_growth_with_assert():
#     assert len(sort_list_growth_for_assert(list_growth_for_assert)) != 0, "List is empty"
