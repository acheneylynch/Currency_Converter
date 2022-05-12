"""
Module for currency exchange

This module provides several string parsing functions to implement a simple
currency exchange routine using an online currency service. The primary function
in this module is exchange().

Author: Aidan Cheney-Lynch
Date: August 16, 2021
"""

#import module introcs
import introcs

#assignment statement to create global variable for API Passkey
APIKEY = ("wlDgusbvh8n8b8jXNqUY06vfEjLIVxSOnLwp434REcIe")

#begin code

def before_space(s):
    """
    Returns the substring of s up to, but not including, the first space.

    Example: before_space('Hello World') returns 'Hello'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it

    """

    #assert statements

    assert type(s) == str, 'Precondition Violation 1'

    assert introcs.count_str(s, ' ') >= 1, 'Precondition Violation 2'

    #implement function

    #find the first space
    find_space = introcs.find_str(s, ' ')

    #extract string portion before the space
    string_before_space = s[:find_space]



    #assign to variable result
    result = string_before_space

    #return that result
    return result


def after_space(s):
    """
    Returns the substring of s after the first space

    Example: after_space('Hello World') returns 'World'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it

    """

    # assert statements
    assert type(s) == str, 'Precondition Violation 1'
    assert introcs.count_str(s, ' ') >= 1, 'Precondition Violation 2'

    # implement function

    # find the first space
    find_space = introcs.find_str(s, ' ')

    # extract the string after the first space
    string_after_space = s[find_space+1: ]


    # assign to variable the result
    result = string_after_space

    # return the result
    return result


def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quote characters

    Note that the double quotes must be part of the string.  So "Hello World" is a
    precondition violation, since there are no double quotes inside the string.

    Example: first_inside_quotes('A "B C" D') returns 'B C'
    Example: first_inside_quotes('A "B C" D "E F" G') returns 'B C', because it only
    picks the first such substring.

    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters inside

    """

    # assert statements
    assert type(s) == str, 'Precondition Violation 1'
    assert introcs.count_str(s, '"') >= 2, 'Precondition Violation 2'

    # implement function

    # find the first pair of quotes
    find_first_quote = introcs.find_str(s, '"')
    # introcs.index_str() also works here

    find_second_quote = introcs.find_str(s, '"', find_first_quote+1, )
    # introcs.index_str() also works here

    # extract the substring with quotes from string
    string_twixt_quotes = s[find_first_quote+1 : find_second_quote]

    # assign to variable the result
    result = string_twixt_quotes

    # return the result
    return result


def get_src(json):
    """
    Returns the src value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"src"'. For example,
    if the json is

        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns '2 United States Dollars' (not '"2 United States Dollars"').
    On the other hand if the json is

        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)

    """

    # implement function

    find_src = introcs.index_str(json, '"src":')

    find_start_of_quotes = json[find_src+5 : ]

    string_twixt_quotations = first_inside_quotes(find_start_of_quotes)

    result = string_twixt_quotations

    return(result)


def get_dst(json):
    """
    Returns the dst value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"dst"'. For example,
    if the json is

    '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns '1.772814 Euros' (not '"1.772814 Euros"'). On the other
    hand if the json is

    '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON

    '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)

    """

    # implement function

    # find '"dst":' location
    find_dst = introcs.index_str(json, '"dst":')

    #find start of quotes
    find_start_of_quotes = json[find_dst+6 : ]

    #extract string between quotes
    string_twixt_quotes = first_inside_quotes(find_start_of_quotes)

    result = string_twixt_quotes

    return result


def has_error(json):
    """
    Returns True if the response to a currency query encountered an error.

    Given a JSON string provided by the web service, this function returns True if the
    query failed and there is an error message. For example, if the json is

    '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns True (It does NOT return the error message
    'Source currency code is invalid'). On the other hand if the json is

    '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns False.

    The web server does NOT specify the number of spaces after the colons. The JSON

    '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)

    """

    #assert statements
    assert type(json) == str, 'Precondition Violation 1'

    #implement function

    #find "error:" in string
    find_error_in_string = introcs.index_str(json, '"error":')

    #find start of quotes
    find_start_of_quotes = first_inside_quotes(json[find_error_in_string+7:])

    result = find_start_of_quotes

    return result != ''


def service_response(src, dst, amt):
    """
    Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency src to the currency dst. The response
    should be a string of the form

    '{"success": true, "src": "<src-amount>", dst: "<dst-amount>", error: ""}'

    where the values src-amount and dst-amount contain the value and name for the src
    and dst currencies, respectively. If the query is invalid, both src-amount and
    dst-amount will be empty, and the error message will not be empty.

    There may or may not be spaces after the colon.  To test this function, you should
    chose specific examples from your web browser.

    Parameter src: the currency on hand
    Precondition src is a nonempty string with only letters

    Parameter dst: the currency to convert to
    Precondition dst is a nonempty string with only letters

    Parameter amt: amount of currency to convert
    Precondition amt is a float or int
    """

    # assert statements
    assert type(amt) == float or int

    # implement function

    url_read_result = introcs.urlread('https://ecpyfac.ecornell.com/python/curr' +
    'ency/fixed?src=' + str(src) + '&dst=' + str(dst) + '&amt=' + str(amt) + '&key=wlDgusbvh8n8b8jXNqUY06vfEjLIVxSOnLwp434REcIe ')

    result = url_read_result

    return result


def iscurrency(currency):
    """
    Returns True if currency is a valid (3 letter code for a) currency.

    It returns False otherwise.

    Parameter currency: the currency code to verify
    Precondition: currency is a nonempty string with only letters
    """

    # assert statements

    assert introcs.isalpha(currency), 'Precondition Violation 1'

    assert introcs.isupper(currency), 'Precondition Violation 2'

    # implement the function

    # the generic variables don't work, neither do specific "hardcoded" ones

    valid_currency_check = service_response(currency, 'EUR', 2)

    find_error_word = introcs.index_str(valid_currency_check, '"error":')

    error_or_not = introcs.find_str(valid_currency_check, '"The rate for curren' +
    'cy AAA is not present."' [find_error_word: ])

    return error_or_not == -1


def exchange(src, dst, amt):
    """
    Returns the amount of currency received in the given exchange.

    In this exchange, the user is changing amt money in currency src to the currency
    dst. The value returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter src: the currency on hand
    Precondition src is a string for a valid currency code

    Parameter dst: the currency to convert to
    Precondition dst is a string for a valid currency code

    Parameter amt: amount of currency to convert
    Precondition amt is a float or int
    """

    # assert statements
    assert type(amt) == float or int, 'Precondition Violation 5'

    #implement the function

    # make the query
    x = service_response(src, dst, amt)

    # retrieve dst
    to_get_dst = get_dst(x)

    #slice dst string
    str_before_space = before_space(to_get_dst)

    #result must be string
    result = float(str_before_space)

    return result
