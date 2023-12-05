def mod_2(num, div):
    """Remainder after modulo_2 for binar nums"""
    # change to list for better iteration
    num = list(num)
    div = list(div)

    # till i can divide -> mod2
    while len(num) >= len(div):
        # XOR
        for i in range(0, len(div)):
            num[i] = str(int(num[i]) ^ int(div[i]))

        # delete '0' at start
        while len(num) >= len(div) and num[0] == "0":
            num.pop(0)

    # make remainder as str
    remainder = "".join(num)

    return remainder


def encoder(message, poly):
    """Encode message with gen.pol."""
    # add '0' to end of msg
    exp_mess = message + "0" * (len(poly) - 1)

    # get remainder and add to msg
    remainder = mod_2(exp_mess, poly)
    code_message = message + remainder

    return code_message


def all_poly(degree):
    """Generate all pol. of certain degree"""
    all_poly = []

    for i in range(2**(degree)):
        # create all options of pol. with '1' at start
        poly = "1" + bin(i)[2:].zfill(degree)
        all_poly.append(poly)

    return all_poly


def find_gen_poly(n, k):
    """Find gen.poly for 'n,k' code"""
    # create pol. z^n - 1 as bin
    n_poly = "1" + "0"*(n-1) + "1"
    all_polynomials = all_poly(n-k)

    gen_poly = []
    # fromm all pol. of certain degree check remainder of z^n - 1 mod2 pol
    for i in all_polynomials:
        remainder = mod_2(n_poly, i)

        if int(remainder) == 0:
            gen_poly.append(i)

    return gen_poly


def bin_to_poly(bin_num):
    """Create pol. form from binary"""
    poly = ""
    # first part with max degree
    poly += f"x^{len(bin_num) - 1}"

    # change '1' to x^n
    for i in range(1, len(bin_num) - 2):
        if bin_num[i] == "1":
            poly += f" + x^{len(bin_num) - i - 1}"

    # x^1
    if bin_num[len(bin_num) - 2] == "1":
        poly += " + x"

    # x^0
    if bin_num[len(bin_num) - 1] == "1":
        poly += " + 1"

    return poly


def find_mistake(message, key):
    """Find error and give possible correct msgs"""
    remainder = mod_2(message, key)
    message = list(message)
    correct_messages = []

    for i in range(len(message)):
        # create x^i as binary
        check_bit = "1" + "0" * i

        # check remainders and XOR the wrong bit
        if int(mod_2(check_bit, key)) == int(remainder):
            temp = message.copy()
            temp[len(temp) - i - 1] = str(int(temp[len(temp) - i - 1]) ^ int("1"))
            temp = ''.join(temp)

            # add correct message cause more corrections are possible
            correct_messages.append(temp)

    return correct_messages