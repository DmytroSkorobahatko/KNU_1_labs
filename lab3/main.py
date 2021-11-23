import numpy as np


def main():
    """catches excepts, calls introduction and some stuff"""
    _intro_()
    try:
        input_str = input("Enter some numbers:")
        sequence = _get_sequence_(input_str)
        sequence = _delete_trash_(sequence)
        answer = parna_plytka(sequence)
        print("parna_plytka: ", answer)
    except ValueError:
        print("***** error")
    except KeyboardInterrupt:
        print("program aborted")
    except EOFError:
        print("***** error")
    else:
        print("The work is done.")


def _intro_():
    """prints author name and variant"""
    author_name, variant = "Dmytro Skorobahat'ko", 24
    print(f'The author of this program is {author_name}.',
          f'This program for lab3. Variant {variant}.', sep='\n')


def parna_plytka(sequence):
    """looks for First MaxLen parna plytka in string"""
    ans, temp = [], []
    pre_n = sequence[0]

    for i in range(len(sequence)):
        temp.append(sequence[i])

        if i + 1 % 2 == 0 and sequence[i] > pre_n:
            temp = [sequence[i]]
        elif i + 1 % 2 == 1 and sequence[i] < pre_n:
            temp = [sequence[i]]

        if len(ans) < len(temp):
            ans = []
            [ans.append(x) for x in temp]

    if ans[-2] < ans[-1]:
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
    for num in sequence:
        num_base7 = np.base_repr(num, base=7)
        if not _odd_digits_check_(num_base7):
            sequence.remove(num)
    return sequence


def _odd_digits_check_(num7):
    """checks if in num_base7 at list one odd digit"""
    for digit in str(num7):
        if int(digit) % 2 == 1:
            return True
    return False


"""program starts here"""
if __name__ == '__main__':
    main()
