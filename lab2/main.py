""""domain of x = [A; B]"""
A, B = -0.9, 0.9


def main():
    """catches excepts, calls introduction and calculations"""
    _introduction_()
    inc_error = ""
    v_error = ""
    error_text = "'There are no input or it could not be converted to float'"
    try:
        v_error = "'At time of getting x'"
        x = float(input("Enter a real from [-0.9; 0.9]: "))
        if not _domain_x_(x):
            inc_error = ", 'Incorrect value'"
            stopper = float("")

        v_error = "'At time of getting eps'"
        eps = float(input("Enter positive eps: "))
        if not _domain_eps_(eps):
            inc_error = ", 'Incorrect value'"
            stopper = float("")

        res = _calculation_(x, eps)
        print("done", f"for x = {x:.5f}", f"for eps = {eps:.4e}", f"result = {res:.9f}", sep='\n')
    except ValueError as ve:
        ve_error = f", ValueError({error_text}, ValueError('{ve}'))" if inc_error == "" else ""
        print("***** error", f"\n({v_error}{inc_error}{ve_error})")
    except KeyboardInterrupt:
        print("program aborted")
    except EOFError as eof:
        eof_error = f", EOFError({error_text}, EOFError('{eof}'))" if inc_error == "" else ""
        print("***** error", f"\n({v_error}{eof_error})")
    else:
        print("The work is done.")


def _introduction_():
    """prints author name and variant"""
    author_name, variant = "Dmytro Skorobahat'ko", 24
    print(f'The author of this program is {author_name}.',
          f'This program calculates the value of the series for lab2. Variant {variant}.', sep='\n')


def _calculation_(x: float, eps: float) -> float:
    """magic phrase, calls calculation"""
    print("***** do calculations ... ", end="")
    return s(x, eps)


def _domain_x_(x: float) -> bool:
    """domain for x"""
    return A <= x <= B


def _domain_eps_(eps: float) -> bool:
    """domain for eps"""
    return eps > 0


def s(x: float, eps: float) -> float:
    """calculates series that depends on x with precision eps"""
    x4 = x * x * x * x
    a = x4 * x * x * x / 21
    s = a
    n = 1
    m_eps = eps * -1
    while a >= eps or a <= m_eps:
        a *= ((-1 * x4) * (16 * n * n + 8 * n - 3)) / (16 * n * n + 40 * n + 21)
        s += a
        n += 1
    else:
        return s


"""program starts here"""
if __name__ == '__main__':
    main()
