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


def _checker_x_(x):
    """checks if x in domain """
    if not _domain_x_(x):
        raise ValueError


def _checker_eps(eps):
    """checks if eps in domain"""
    if not _domain_eps_(eps):
        raise ValueError


def _calculations_(x, eps):
    """starts calculation, calls checker"""
    print("***** do calculations ... ", end="")
    return s(x, eps)


def _domain_x_(x):
    return a <= x <= b


def _domain_eps_(eps):
    return eps > 0


def s(x, eps):
    return 13.131313000


if __name__ == '__main__':
    main()
