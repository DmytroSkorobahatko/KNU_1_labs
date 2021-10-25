import math


def main():
    """catches excepts, calls introduction and calculations"""
    _introduction_()
    try:
        x = float(input("Enter x: "))
        res = _calculations_(x)
        print(f"done\nfor x = {x:.8f}")
        print(f"result = {res:.8f}") if res is float else print(f"result = {res}")
    except ValueError:
        print("wrong input")
    except KeyboardInterrupt:
        print("program aborted")
    except EOFError:
        print("wrong input")


def _introduction_():
    """prints author name and variant"""
    author_name, variant = 'Dmytro Skorobahatko', 24
    print('The author of this program is %s.' % author_name,
          'This program calculates the value of the lab1 by given x. Variant %d.' % variant,
          '{x | x >= -7, x != -8, 11, 13}', sep='\n')


def _calculations_(x: float):
    """starts calculation, calls checker"""
    print("***** do calculations ... ", end="")
    return _checker_(x)


def _checker_(x: float):
    """calculates the value of x if it is possible"""
    return f(x) if _domain_(x) else 'undefined'


def _domain_(x: float) -> bool:
    """checks if x is in domain"""
    return x not in (-8, 11, 13) and x >= -7


def f(x: float) -> float:
    """returns value of my variant"""
    return math.cos(25 / 58) - ((15 * math.e) / (54 * math.pi)) * (9 / (x - 11) * (x + 8)) - 12 * math.atan(
        x + 14) - (5 + math.sqrt(x + 7)) / (x - 13)


"""program starts here"""
if __name__ == '__main__':
    main()
