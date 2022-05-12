"""
32. Написати функцію, що перевіряє чи складаються дві послідовності з однакових елементів з точністю
до кількості входжень кожного елемента в послідовність. Порядок елементів у послідовності несуттєвий.
"""
def solution_by_sort(input1, input2) -> bool:
    """
    checks if inputs are equal
    O(logn)
    """
    return sorted(list(input1)) == sorted(list(input2))


def solution_by_dict(input1, input2) -> bool:
    """
    checks if inputs contain same elements
    O(n) - but could solve mixed types sequences
    """
    return counter(input1) == counter(input2)

def counter(input) -> dict:
    """count elements in input"""
    el_counter = dict()

    for i in input:
        if i not in el_counter:
            el_counter[i] = 1
        else:
            el_counter[i] += 1

    return el_counter


def test_part1():
    """tests solutions for part 1"""
    assert solution_by_dict([5, 5, 3, 2, 5, 1, 2, 3, 0], [5, 3, 5, 2, 5, 1, 2, 3, 0]), "list of ints"
    assert solution_by_dict(["5 5", 3, 2, 5, 1, 2, 3], [3, 2, "5 5", 1, 5, 2, 3]), "mixed list"
    assert solution_by_dict(("5 5", 3, 2, 5, 1, 2, 3), (3, 2, "5 5", 1, 5, 2, 3)), "mixed tuple"
    assert solution_by_dict(["1", "2", "3", "1"], ["1", "1", "3", "2"]), "list of strs"
    assert solution_by_dict({1, 2, 3, 4, 5, 1, 2, 3, 4, 5}, {1, 1, 2, 2, 3, 3, 4, 4, 5, 5}), "set"
    assert solution_by_dict((1, 2, 3, 4, 1, 2, 3, 4), (1, 2, 3, 4, 4, 3, 2, 1)), "tuple of ints"
    assert solution_by_dict((1, 2, "34", 1, 2, 3, 4), (1, 2, 3, 4, "34", 2, 1)), "mixed tuple"
    assert solution_by_dict(("1", "1", "2", "2", "3"), ("1", "1", "3", "2", "2")), "tuple of strs"

    assert solution_by_sort([5, 5, 3, 2, 5, 1, 2, 3, 0], [5, 3, 5, 2, 5, 1, 2, 3, 0]), "list ints"
    assert solution_by_sort(["1", "2", "3", "1"], ["1", "1", "3", "2"]), "list of strs"
    assert solution_by_sort((1, 2, 3, 4, 1, 2, 3, 4), (1, 2, 3, 4, 4, 3, 2, 1)), "tuple of ints"
    assert solution_by_sort(("1", "1", "2", "2", "3"), ("1", "1", "3", "2", "2")), "tuple of strs"


if __name__ == '__main__':
    test_part1()