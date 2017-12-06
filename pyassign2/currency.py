"""currency.py: This module is to calculate the amount of new currency you want convert to, from a certain amount of the old currency on hand.
This module contains 4 functions and 5 test-functions, they are get_from(json), get_to(json), has_error(json), exchange(currency_from, currency_to, amount_from),
and test_get_from(), test_get_to(), test_has_error(), test_exchange() and testAll().

__author__ = "Zhou Yangfan"
__pkuid__  = "1600017735"
__email__  = "pkuzyf@pku.edu.cn"
"""

from urllib.request import urlopen

def get_to(json):
    """This function is to get the TO value in the response to a currency query.
    Returns: The TO value in the response to a currency query.
    Given a JSON response to a currency query, this returns the string inside double quotes (") immediately following the keyword "to".
    For example, if the JSON is '{"from":"2 United States Dollars","to":"2.0952375 Euros","success":true,"error":""}'
    then this function returns '2.0952375 Euros'. It returns the empty string if the JSON is the result of on invalid query. 
    
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""
    alist = json.split('"') 
    return alist[7]  # We can know that the value (which is a string like '2.0952375 Euros') following the keyword "to" is the eighth element in alist.

def has_error(json):
    """This function is to check whether the currency query has an error or not.
    Returns: True if the query has an error; False otherwise. 
    For example, if the JSON is '{"from":"","to":"","success":false,"error":"Source currency code is invalid."}'
    then the query is not valid, so this function returns True. 
    
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""
    alist = json.split('"')
    if alist[-2] == '':  # We can know that the value following the keyword "error" is the penultimate element in alist.
        return False  # Given a JSON response to a currency query, if the value (a string) following the keyword "error" is "", that means there isn't any error.
    else:
        return True

def exchange(currency_from, currency_to, amount_from):
    """This function is to calculate the amount of currency received in the given exchange.
    Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    url_str = "http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=%(from)s&to=%(to)s&amt=%(amt).2f" % {"from":currency_from, "to":currency_to, "amt":amount_from}
    doc = urlopen(url_str)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode("ascii")
    if not has_error(jstr):  # Only if currency query is valid (that is to say, currency_from and currency_to are both valid 3 letter codes for currency), we can get the amount we want.
        num = get_to(jstr).find(" ")  # get_to(jstr) is a string like '2.0952375 Euros', so we can get the target amount by getting a slice of the string.
        amount_str = get_to(jstr)[:num]
        amount = float(amount_str)  # To change the string into a float.
        return amount
    else:  # If currency is invalid, we will let the user know.
        print("Your currency query has an error, which means the parameter 'currency_from' or 'currency_to' you give is not a valid currency code.")

def test_get_to():
    """This function is to test the function--get_to(json)
    I use a case--1 United States Dollar = 6.52615 Chinese Yuan--to test it"""
    doc = urlopen("http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to=CNY&amt=1")
    docstr = doc.read()
    doc.close()
    json = docstr.decode("ascii")
    assert("6.52615 Chinese Yuan" == get_to(json))  # If the fuction is right, its return should be "6.52615 Chinese Yuan".
    
def test_has_error():
    """This function is to test the function--has_error(json)
    I use two valid currency codes--"USD" and "CNY""--to test it"""
    doc = urlopen("http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to=CNY&amt=1")
    docstr = doc.read()
    doc.close()
    json = docstr.decode("ascii")
    assert(False == has_error(json))  # If the fuction is right, its return should be False.
    
def test_exchange():
    """This function is to test the function--wxchange(json)
    I use a case--1 United States Dollar = 6.52615 Chinese Yuan to test it"""
    assert(6.52615 == exchange("USD", "CNY", 1))  # If the fuction is right, its return should be 6.52615.
    
def testAll():
    """test all cases"""
    test_get_to()
    test_has_error()
    test_exchange()
    print("All tests passed")
        
def main():
    testAll()  # Test all the fuctions.
    dollar = exchange("CNY", "USD", 10)  # Calculate 10 Chinese Yuan = ? United States Dollar.
    print(dollar)
    
if __name__ == '__main__':
    main()
