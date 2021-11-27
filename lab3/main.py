"""
The author of this program is Dmytro Skorobahat'ko
This program for lab3. Variant 24
"""


def main():
    """catches excepts, calls introduction and some stuff"""
    #input_str = input()
    sequence = _get_sequence_(input_str)
    sequence = _delete_trash_(sequence)

    answer = subsequence(sequence)


def subsequence(sequence):
    """looks for First MaxLen parna plytka in string"""
    ans, temp = [], []
    pre_n = sequence[0]

    for i in range(len(sequence)):
        temp.append(sequence[i])

        if i % 2 == 0 and sequence[i] > pre_n:
            temp = [sequence[i]]
        if i % 2 == 1 and sequence[i] < pre_n:
            temp = [sequence[i]]

        if len(ans) < len(temp):
            ans = []
            [ans.append(x) for x in temp]

        pre_n = sequence[i]

    if len(ans) < 2:
        ans = []
    elif ans[-2] < ans[-1]:
        ans.pop()

    return ans


def _get_sequence_(input_str):
    """transform input to list of ints"""
    sequence = []
    for element in input_str.split():
        sequence.append(int(element))
    return sequence


def _delete_trash_(sequence):
    """removes a number without odd digit"""
    new_sequence = []
    for num in sequence:
        not_odd = 0

        num_base7 = int(_convert_(num))
        for digit in str(num_base7):
            if int(digit) % 2 == 0:
                not_odd += 1
        if not_odd != len(str(num_base7)):
            new_sequence.append(num)
    return new_sequence


def _convert_(num, base=7):
    alpha = "0123456789"
    converted = ""
    while num > 0:
        converted += alpha[num % base]
        num //= base

    if len(converted) == 0:
        return "0"
    return converted[::-1]


"""program starts here"""
if __name__ == '__main__':
    main()
