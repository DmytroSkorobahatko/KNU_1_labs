"""
The author of this program is Dmytro Skorobahat'ko
This program for lab3. Variant 24
"""


def subsequence(tuple_sequence: tuple) -> list:
    """calls some stuff"""
    return _plytka_(tuple_sequence) if len(tuple_sequence) > 1 else []


def _plytka_(sequence: tuple):
    """looks for First MaxLen parna plytka in string"""
    ans, temp = [], []
    pre_n = sequence[0]
    n = 0
    for i in range(len(sequence)):
        if _not_trash_(int(sequence[i])):
            n += 1
            temp.append(sequence[i])

            if (n % 2 == 0 and sequence[i] > pre_n) or (n % 2 == 1 and sequence[i] < pre_n):
                temp, n = [sequence[i]], 0

            if len(ans) < len(temp):
                ans = []
                ans.extend(temp)

            pre_n = sequence[i]
    return _parna_(ans)


def _parna_(sequence):
    """makes our plytka parna"""
    if len(sequence) < 2:
        sequence = []
    elif sequence[-2] < sequence[-1]:
        sequence.pop()
    return sequence


def _not_trash_(num: int):
    """check if num include odd digits"""
    if num < 0:
        num *= -1
    num_base7 = _convert_(num)[0]

    while (num_base7 % 10) % 2 == 0 and num_base7 > 0:
        num_base7 //= 10

    return (num_base7 % 10) % 2 != 0


def _convert_(num: int, base=7):
    """convert num to base 7 or any other"""
    if num == 0:
        return [0]
    digits = []
    while num:
        digits.append(int(num % base))
        num //= base
    return digits[::-1]
