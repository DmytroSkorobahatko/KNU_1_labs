import math

a, b = -0.9, 0.9


def main():
    """catches excepts, calls introduction and calculations"""
    _introduction_()
    try:
        x = float(input("Enter a real from [-0.9; 0.9]: "))
        _checker_x_(x)
        eps = float(input("Enter positive eps: "))
        _checker_eps(eps)
        res = _calculations_(x, eps)
        print("done", f"for x = {x:.5f}", f"for eps = {eps:.4e}", f"result = {res:.9f}", sep='\n')
    except ValueError:
        print("***** error")
    except KeyboardInterrupt:
        print("program aborted")
    except EOFError:
        print("***** error")


def _introduction_():
    """prints author name and variant"""
    author_name, variant = "Dmytro Skorobahat'ko", 24
    print('The author of this program is %s.' % author_name,
          'This program calculates the value of the series for lab2. Variant %d.' % variant, sep='\n')


def _checker_x_(x: float):
    """checks if x in domain """
    if not _domain_x_(x):
        raise ValueError


def _checker_eps(eps: float):
    """checks if eps in domain"""
    if not _domain_eps_(eps):
        raise ValueError


def _calculations_(x: float, eps: float) -> float:
    """starts calculation, calls checker"""
    print("***** do calculations ... ", end="")
    return s(x, eps)


def _domain_x_(x: float):
    """domain for x"""
    return a <= x <= b


def _domain_eps_(eps: float):
    """domain for eps"""
    return eps > 0


def s(x: float, eps: float) -> float:
    """
    Обчислення функції s з точністю eps.
    """
    a = -1 / (7 * 11) * (math.pow(x, 11))
    s = a
    n = 2
    while math.fabs(a) <= eps:
        a *= math.pow(-1, n) / ((4 * n + 3) * (4 * n + 7)) * math.pow(x, 4 * n + 7)
        prev_s = s
        s += a
        n += 1
        if prev_s == s:
            break

    return float(s)


if __name__ == '__main__':
    main()
