import pytest


def add_one(vec):
    new_vec = vec.copy()
    new_vec.reverse()
    nineth_counter = 0

    for index, el in enumerate(new_vec):
        if el != 9:
            new_vec[index] = (el + 1)
            break

        new_vec[index] = 0
        nineth_counter += 1
        continue

    if nineth_counter == len(new_vec):
        return [1] + new_vec[::-1]

    return new_vec[::-1]
