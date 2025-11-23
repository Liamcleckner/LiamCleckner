"""Unit test module for cups
"""

from cups import sort_cups


def test_sort_cups_1() -> None:
    """test if the cups are sorted correclty.
    """
    cups = {100: 'red', 10: 'blue', 50: 'yellow'}
    sorted_cups = sort_cups(cups)
    expected = ['blue', 'yellow', 'red']
    assert sorted_cups == expected


# FIXME6 : add a unit test function
def test_sort_cups_2() -> None:
    """test if the cups are sorted correclty.
    """
    cups = {10: 'yellow'}
    sorted_cups = sort_cups(cups)
    expected = ['yellow']
    assert sorted_cups == expected

# FIXME7 : add a unit test function
def test_sort_cups_3() -> None:
    """test if the cups are sorted correclty.
    """
    cups = {5: 'red', 10: 'blue'}
    sorted_cups = sort_cups(cups)
    expected = ['red', 'blue']
    assert sorted_cups == expected

# FIXME8 : add a unit test function
def test_sort_cups_4() -> None:
    """test if the cups are sorted correclty.
    """
    cups = {30: 'green', 10: 'blue', 20: 'yellow'}
    sorted_cups = sort_cups(cups)
    expected = ['blue', 'yellow', 'green']
    assert sorted_cups == expected

# FIXME9 : add a unit test function
def test_sort_cups_5() -> None:
    """test if the cups are sorted correclty.
    """
    cups = {10: 'blue', 5: 'red'}
    sorted_cups = sort_cups(cups)
    expected = ['red', 'blue']
    assert sorted_cups == expected

# FIXME10 : add a unit test function
def test_sort_cups_6() -> None:
    """test if the cups are sorted correclty.
    """
    cups = {200: 'black', 50: 'white', 150: 'gray'}
    sorted_cups = sort_cups(cups)
    expected = ['white', 'gray', 'black']
    assert sorted_cups == expected
