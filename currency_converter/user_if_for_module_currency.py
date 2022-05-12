"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Aidan Cheney-Lynch
Date: August 16, 2021
"""

import currency

x = input("3-letter code for original currency: ")

y = input("3-letter code for the new currency: ")

z = input("Amount of the original currency: ")

a = currency.exchange(x, y, z)

b = round(a, 3)

print("You can exchange " + str(z) + " " + str(x) + " for " + str(b) + " " + str(y) + ".")
