"""
Unit tests for module currency

When run as a script, this module invokes several procedures that test
the various functions in the module currency.

Author: Aidan Cheney-Lynch
Date: August 16, 2021
"""

import introcs

import currency


def test_before_space():
    """Test procedure for before_space"""

    print("Testing before_space")

    result = currency.before_space('The dog')
    introcs.assert_equals('The', result)

    result = currency.before_space('The  bird')
    introcs.assert_equals('The', result)

    result = currency.before_space('The dog barks')
    introcs.assert_equals('The', result)

    result = currency.before_space(' The')
    introcs.assert_equals('', result)

    return result


def test_after_space():
    """Test procedure for after_space"""

    print("Testing after_space")

    result = currency.after_space('The fish')
    introcs.assert_equals('fish', result)

    result = currency.after_space('The  fish')
    introcs.assert_equals(' fish', result)

    result = currency.after_space('The ')
    introcs.assert_equals('', result)

    result = currency.after_space(' The fish swims')
    introcs.assert_equals('The fish swims', result)

    return result


def test_first_inside_quotes():
    """Test procedure for first_inside_quotes"""

    print("Testing first_inside_quotes")

    result = currency.first_inside_quotes('"The" rabbit')
    introcs.assert_equals('The', result)

    result = currency.first_inside_quotes('"The" "rabbit"')
    introcs.assert_equals('The', result)

    result = currency.first_inside_quotes(' "" ')
    introcs.assert_equals('', result)

    result = currency.first_inside_quotes('"The rabbit"')
    introcs.assert_equals('The rabbit', result)

    return result


def test_get_src():
    """Test procedure for get_src"""

    print("Testing get_src")


    result = currency.get_src('{"success": true, "src": "2 United States Dollars",' +
    '"dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('2 United States Dollars', result)

    result = currency.get_src('{"success":true, "src":"2 United States Dollars",' +
    '"dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('2 United States Dollars', result)

    result = currency.get_src('{"success":false,"src":"","dst":"","error":' +
    '"Source currency code is invalid."}')
    introcs.assert_equals('', result)

    result = currency.get_src('{"success":false,"src": "","dst":"","error":' +
    '"Source currency code is invalid."}')
    introcs.assert_equals('', result)

    return(result)


def test_get_dst():
    """Test procedure for get_dst"""

    print("Testing get_dst")

    result = currency.get_dst('{"success": true, "src": "2 United States Dollars",' +
    '"dst": "1.772814 Euros", "error": ""}')

    introcs.assert_equals('1.772814 Euros', result)

    result = currency.get_dst('{"success":true, "src":"2 United States Dollars",' +
    '"dst":"1.772814 Euros", "error": ""}')
    introcs.assert_equals('1.772814 Euros', result)

    result = currency.get_dst('{"success":false,"src":"","dst":"","error":' +
    '"Source currency code is invalid."}')
    introcs.assert_equals('', result)

    result = currency.get_dst('{"success":false,"src": "","dst": "","error":' +
    '"Source currency code is invalid."}')
    introcs.assert_equals('', result)


def test_has_error():
    """Test procedure for has_error"""

    print("Testing has_error")

    result = currency.has_error('{"success": true, "src": "2 United States Dollars",' +
    '"dst": "1.772814 Euros", "error": ""}')
    introcs.assert_true(True, result)

    result = currency.has_error('{"success":true, "src":"2 United States Dollars",' +
    '"dst":"1.772814 Euros", "error":""}')
    introcs.assert_true(True, result)

    result = currency.has_error('{"success":false,"src":"","dst":"","error":' +
    '"Source currency code is invalid."}')
    introcs.assert_true(True, result)

    result = currency.has_error('{"success": false,"src": "","dst": "","error": "Sou' +
    'rce currency code is invalid."}')
    introcs.assert_true(True, result)


def test_service_response():
    """Test procedure for service_response"""

    print("Testing service_response")

    #1st test case
    result = currency.service_response('USD','EUR',5)
    introcs.assert_equals('{"success": true, "src": "5.0 United States Dol' +\
    'lars", "dst": "4.432035 Euros", "error": ""}', result)


    #2nd test case
    result = currency.service_response('EUR','USD',-7.5)
    introcs.assert_equals('{"success": true, "src": "-7.5 Eur' +
    'os", "dst": "-8.461124517292847 United States Dollars", "error": ""}', result)


    #3rd test case
    result = currency.service_response('AAA','USD',5)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", "er' +
    'ror": "The rate for currency AAA is not present."}', result)

    #4th test case
    result = currency.service_response('USD','BBB', -7.5)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", "er' +
    'ror": "The rate for currency BBB is not present."}', result)


def test_iscurrency():
    """Test procedure for iscurrency"""

    print("Testing iscurrency")

    #1st test case
    result = currency.iscurrency('USD')
    introcs.assert_true(True, result)

    #2nd test case
    result = currency.iscurrency('AAA')
    introcs.assert_true(True, result)


def test_exchange():
    """Test procedure for exchange"""

    print("Testing exchange")

    #1st test case

    result = currency.exchange('USD', 2, 'EUR')
    introcs.assert_equals(1.772814, result)

    #2nd test case

    result = currency.exchange('USD', 'EUR', -2)
    introcs.assert_floats_equal(-1.772814, result)


test_before_space()
test_after_space()
test_first_inside_quotes()
test_get_src()
test_get_dst()
test_has_error()
test_service_response()
test_iscurrency()
test_exchange()


print("All tests completed successfully")
