"""
The author of this program is Dmytro Skorobahat'ko
This program for lab3. Variant 24
"""


def subsequence(tuple_sequence):
    """calls some stuff"""
    return _plytka_(tuple_sequence)


def _plytka_(sequence):
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
                [ans.append(x) for x in temp]

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
    not_odd = 0
    if num < 0:
        num *= -1
    num_base7 = int(_convert_(num))

    for digit in str(num_base7):
        if int(digit) % 2 == 0:
            not_odd += 1
    return not_odd != len(str(num_base7))


def _convert_(num, base=7):
    """convert num to base 7"""
    alpha = "0123456789"
    converted = ""
    while num > 0:
        converted += alpha[num % base]
        num //= base
    if len(converted) == 0:
        return "0"
    return converted[::-1]
