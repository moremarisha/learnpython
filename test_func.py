def get_vat(price, vat_rate):
    vat = price / 100 * vat_rate
    price_no_vat = price - vat
    print(price_no_vat)


def get_sum(one, two, delimiter=' '):
    mystr = str(one) + str(delimiter) + str(two)
    return mystr.upper()


a = 'lalal'
b = 'pup pup'
string = get_sum(a, b)

print(string)
