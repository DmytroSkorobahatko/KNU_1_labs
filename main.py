import math


def main():
    """catches excepts, calls introduction and calculations"""
    introduction()
    try:
        x = float(input("Enter x: "))
        calculations(x)
    except ValueError:
        print("wrong input")
    except KeyboardInterrupt:
        print("program aborted")
    except EOFError:
        print("wrong input")


def introduction():
    """prints author name and variant"""
    author_name, variant = 'Dmytro Skorobahatko', 24
    print('The author of this program is %s.' % author_name,
          'This program calculates the value of the lab1 by given x. Variant %d.' % variant,
          '{x | x >= -7, x != -8, 11, 13}', sep='\n')


def calculations(x: float):
    """prints all 'magical' phrases and result"""
    print("***** do calculations ... ", end="")
    res = check_x(x)
    print(f"done\nfor x = {x:.8f}")
    print(f"result = {res:.8f}") if res is float else print(f"result = {res}")


def check_x(x: float):
    """calculates the value of x"""
    return f(x) if domain(x) else 'undefined'


def domain(x: float) -> bool:
    """checks if x is in domain"""
    return x not in (-8, 11, 13) and x >= -7


def f(x: float) -> float:
    """returns value of my variant"""
    return math.cos(25 / 58) - ((15 * math.e) / (54 * math.pi)) * (9 / (x - 11) * (x + 8)) - 12 * math.atan(
        x + 14) - (5 + math.sqrt(x + 7)) / (x - 13)


"""starts program by calling main"""
if __name__ == '__main__':
    main()
