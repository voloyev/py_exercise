from py_exercises.ex2 import max_sum_subvector


def test_with_provided_example():
    provided_vector = [1, 2, -3, 0, 4, 7, -2]

    expected = [4, 7]
    result = max_sum_subvector(provided_vector)

    assert expected == result


def test_with_empty_vector():
    provided_vector = []

    expected = []
    result = max_sum_subvector(provided_vector)

    assert expected == result


def test_with_mixed_values():
    provided_vector = [0, 4, -2, 5, -4, -7, -55]

    expected = [4, -2, 5]
    result = max_sum_subvector(provided_vector)

    assert expected == result


def test_with_same_negative_values():
    provided_vector = [-2, -2, -2, -2, -2, -2]

    expected = [2, 2, 2, 2, 2, 2]
    result = max_sum_subvector(provided_vector)

    assert expected == result


def test_with_same_positive_values():
    provided_vector = [2, 2, 2, 2, 2, 2]

    expected = [2, 2, 2, 2, 2, 2]
    result = max_sum_subvector(provided_vector)

    assert expected == result


def test_with_almost_the_same_positive_values():
    provided_vector = [2, 2, 1, 2, 2, 1]

    expected = [2, 2, 1, 2, 2, 1]
    result = max_sum_subvector(provided_vector)

    assert expected == result


def test_with_almost_the_same_negative_values():
    provided_vector = [-2, -2, -3, -2, -2, -1]

    expected = [2, 2, 3, 2, 2, 1]
    result = max_sum_subvector(provided_vector)

    assert expected == result
