def mod_2(num, div):
    """Remainder after modulo_2 for binar nums"""
    num = list(num)
    div = list(div)

    while len(num) >= len(div):
        for i in range(0, len(div)):
            num[i] = str(int(num[i]) ^ int(div[i]))

        while len(num) >= len(div) and num[0] == "0":
            num.pop(0)

    remainder = "".join(num)

    return remainder


def encoder(message, poly):
    """Encode message with gen.pol."""
    exp_mess = message + "0" * (len(poly) - 1)

    remainder = mod_2(exp_mess, poly)
    code_message = message + remainder

    return code_message


def all_poly(degree):
    """Generate all pol. of certain degree"""
    all_poly = []

    for i in range(2**(degree)):
        poly = "1" + bin(i)[2:].zfill(degree)
        all_poly.append(poly)

    return all_poly


def find_gen_poly(n, k):
    """Find gen.poly for 'n,k' code"""
    n_poly = "1" + "0"*(n-1) + "1"
    all_polynomials = all_poly(n-k)

    gen_poly = []

    for i in all_polynomials:
        remainder = mod_2(n_poly, i)

        if int(remainder) == 0:
            gen_poly.append(i)

    return gen_poly


def bin_to_poly(bin_num):
    """Create pol. form from binary"""
    poly = ""

    poly += f"x^{len(bin_num) - 1}"

    for i in range(1, len(bin_num) - 2):
        if bin_num[i] == "1":
            poly += f" + x^{len(bin_num) - i - 1}"

    if bin_num[len(bin_num) - 2] == "1":
        poly += " + x"

    if bin_num[len(bin_num) - 1] == "1":
        poly += " + 1"

    return poly


def find_mistake(message, key):
    """Find error and give possible correct msgs"""
    remainder = mod_2(message, key)
    message = list(message)
    correct_messages = []

    for i in range(len(message)):
        check_bit = "1" + "0" * i

        if int(mod_2(check_bit, key)) == int(remainder):
            temp = message.copy()
            temp[len(temp) - i - 1] = str(int(temp[len(temp) - i - 1]) ^ int("1"))
            temp = ''.join(temp)

            correct_messages.append(temp)

    return correct_messages