from py_exercises.ex1 import add_one


def test_with_last_nine():
    input_vec = [1, 2, 9]
    result = add_one(input_vec)
    expected = [1, 3, 0]

    assert result == expected


def test_without_nines():
    input_vec = [6, 5, 4]
    result = add_one(input_vec)
    expected = [6, 5, 5]

    assert result == expected


def test_with_all_nines():
    input_vec = [9, 9, 9]
    result = add_one(input_vec)
    expected = [1, 0, 0, 0]

    assert result == expected


def test_with_nines_at_the_end():
    input_vec = [8, 9, 9]
    result = add_one(input_vec)
    expected = [9, 0, 0]

    assert result == expected


def test_with_zeros():
    input_vec = [0, 0, 0]
    result = add_one(input_vec)
    expected = [0, 0, 1]

    assert result == expected
