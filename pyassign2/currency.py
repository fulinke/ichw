"""Module for currency exchange
This module provides several string parsing functions to implement a
simple currency exchange routine using an online currency service.
The primary function in this module is exchange."""


def exchange(currency_from, currency_to, amount_from):
    """generate a URL and use it to get datas from the website"""
    web = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=x&to=y&amt=z'
    web1 = web.replace('x', currency_from)
    web2 = web1.replace('y', currency_to)
    web3 = web2.replace('z', amount_from)
    from urllib.request import urlopen
    doc = urlopen(g)
    strdoc = doc.read()
    doc.close()
    amount_to = strdoc.decode('ascii')
    return amount_to


def test_exchange():
    """to test the function 'exchange' """
    a = "USD"
    b = "EUR"
    c = "2.5"
    x1 = exchange(a, b, c)
    xx1 = '{ "from" : "2.5 United States Dollars", "to" : "2.1589225 Euros","success" : true, "error" : "" }'
    assert (x1 == xx1)
    a = "BWP"
    b = "NZD"
    c = "4.73"
    x2 = exchange(a, b, c)
    xx2 = '{ "from" : "4.73 Botswanan Pula", "to" : "0.66796788832763 New Zealand Dollars", "success" : true, "error" : "" }'
    assert (x2 == xx2)
    a = "CAD"
    b = "CAD"
    c = "10.8"
    x3 = exchange(a, b, c)
    xx3 = '{ "from" : "10.8 Canadian Dollars", "to" : "10.8 Canadian Dollars", "success" : true, "error" : "" }'
    assert (x3 == xx3)


def extract(m):
    """output the result in a proper way"""
    i = m.split('"')
    h = i[7]
    """amount and currency symbols"""
    j = h.partition(' ')
    k = j[0]
    """amount only"""
    return k


def test_extract():
    """test the function 'extract' """
    """test 1"""
    a = "USD"
    b = "EUR"
    c = "2.5"
    x1 = exchange(a, b, c)
    i1 = extract(x1)
    ii1 = '2.1589225'
    assert (i1 == ii1)
    a = "BWP"
    b = "NZD"
    c = "4.73"
    x2 = exchange(a, b, c)
    i2 = extract(x2)
    ii2 = '0.66796788832763'
    assert (i2 == ii2)
    """test 3"""
    a = "CAD"
    b = "CAD"
    c = "10.8"
    x3 = exchange(a, b, c)
    i3 = extract(x3)
    ii3 = '10.8'
    assert (i3 == ii3)


def testAll():
    """test all cases"""
    test_exchange()
    test_extract()
    print("All tests passed")


def main():
    """get the inputs, test all cases, and then output"""
    x = input()
    y = input()
    z = input()
    q = exchange(x, y, z)
    s = extract(q)
    print(s)
    testAll()
if __name__ == "__main__":
    main()
