def mod_2(num, div):
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
    exp_mess = message + "0" * (len(poly) - 1)

    remainder = mod_2(exp_mess, poly)
    code_message = message + remainder

    return code_message


def all_poly(degree):
    all_poly = []

    for i in range(2**(degree)):
        poly = "1" + bin(i)[2:].zfill(degree)
        all_poly.append(poly)

    return all_poly


def find_gen_poly(n, k):
    n_poly = "1" + "0"*(n-1) + "1"
    all_polynomials = all_poly(n-k)

    gen_poly = []

    for i in all_polynomials:
        remainder = mod_2(n_poly, i)

        if int(remainder) == 0:
            gen_poly.append(i)

    return gen_poly


def bin_to_poly(bin_num):
    rev_num = bin_num[::-1]
    poly = ""



    return poly


