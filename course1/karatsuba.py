

def integer_multiplication(number1, number2):

    digits1 = int(len(str(number1)))
    digits2 = int(len(str(number2)))
    if digits1 == 1 and digits2 == 1:
        return number1*number2

    assert digits1 % 2 == 0, "Length {} of number1 {} must be diviseable by 2".format(digits1, number1)
    assert digits2 % 2 == 0, "Length {} of number2 {} must be diviseable by 2".format(digits2, number2)

    digits1_by_2 = int(digits1/2)
    a = int(str(number1)[:digits1_by_2])
    b = int(str(number1)[digits1_by_2:])

    split = int(digits2/2)
    c = int(str(number2)[:split])
    d = int(str(number2)[split:])

    ac = integer_multiplication(a, c)
    bd = integer_multiplication(b, d)
    # Gauss trick can be implemented here for 3 recursive calls and not 4
    ad_plus_bc = integer_multiplication(a, d) + integer_multiplication(b, c)
    return int((10**digits1)*ac + (10**(digits1/2))*ad_plus_bc + bd)


# def karatsuba(x, y):
#     """
#     karatsuba implement the karatsuba algorithm for multiplication of two integers
#     """
#     if x < 10 or y < 10:
#         # base case
#         return int(x * y)
#     else:
#
#         # add digits if digits of x and y are not the same or
#         # not equal to the exponential of 2
#         len_max = max(len(str(x)), len(str(y)))
#         log_len_max = np.log2(len_max)
#
#         if np.floor(log_len_max) - log_len_max != 0:
#             len_max = int(2 ** (np.ceil(log_len_max)))
#
#         x = '0' * (len_max - len(str(x))) + str(x)
#         y = '0' * (len_max - len(str(y))) + str(y)
#
#         m2 = int(len_max / 2)
#
#         # split the integer
#         high_1 = int(x[:m2])
#         low_1 = int(x[m2:])
#
#         high_2 = int(y[:m2])
#         low_2 = int(y[m2:])
#
#         # recursively call karatsuba function
#         z_0 = karatsuba(high_1, high_2)
#         z_1 = karatsuba(low_1, low_2)
#         z_2 = karatsuba(high_1 + low_1, high_2 + low_2)
#
#         # compute multiplication using gaussian trick
#         return int((z_0 * 10 ** (2 * m2)) + ((z_2 - z_1 - z_0) * 10 ** m2) + (z_1))


if __name__ == '__main__':
    print(integer_multiplication(5678,
                                 1234))
