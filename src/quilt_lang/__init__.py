"""
This is the one and only Quilt Lang file.
"""
# Python modules
import warnings
import keyword
import importlib

# String modules
import string
import secrets
import textwrap

# System modules
import subprocess
import os
import sys
import logging
import pkg_resources
import pip
import tempfile
import base64

# Math modules
import math
import statistics
import random

# Time modules
import datetime
import time
import calendar

# Web modules
import webbrowser
import urllib
import http.client as httplib
"""
Uncatagorised
"""


def userinput(prompttext="", times=1):
    """
    Get the input of the user via a universally secure method.

    :type prompttext: string
    :param prompttext: The text to display while receiving the data.

    :type times: integer
    :param times: The amount of times to ask the user. If value is not 1, a list will be returned. Default is 1.

    :return: What the user typed in.
    :rtype: string
    """

    # If times is 1
    if times == 1:
        # Return the result
        return input(str(prompttext))

    # Create new empty list
    inputlist = []

    # For each time in range
    for _ in range(times):
        # Append the result of another input request
        inputlist.append(input(str(prompttext)))

    # Return the final result
    return inputlist


def shellinput(initialtext='>> ', splitpart=' '):
    """
    Give the user a shell-like interface to enter commands which
    are returned as a multi-part list containing the command
    and each of the arguments.

    :type initialtext: string
    :param initialtext: Set the text to be displayed as the prompt.

    :type splitpart: string
    :param splitpart: The character to split when generating the list item.

    :return: A string of the user's input or a list of the user's input split by the split character.
    :rtype: string or list
    """

    # Get the user's input
    shelluserinput = input(str(initialtext))

    # Return the computed result
    return shelluserinput if splitpart in (
        '', None) else shelluserinput.split(splitpart)


def leadingzero(number, minlength):
    """
    Add leading zeros to a number.

    :type number: number
    :param number: The number to add the leading zeros to.

    :type minlength: integer
    :param minlength: If the number is shorter than this length than add leading zeros to make the length correct.

    :return: The number with a leading zero
    :rtype: string

    >>> leadingzero(1, 2)
    '01'
    """

    # Return the number as a string with the filled number
    return str(number).zfill(int(minlength))


def splitstring(string, splitcharacter=' ', part=None):
    """
    Split a string based on a character and get the parts as a list.

    :type string: string
    :param string: The string to split.

    :type splitcharacter: string
    :param splitcharacter: The character to split for the string.

    :type part: integer
    :param part: Get a specific part of the list.

    :return: The split string or a specific part of it
    :rtype: list or string

    >>> splitstring('hello world !')
    ['hello', 'world', '!']

    >>> splitstring('hello world !', ' ', None)
    ['hello', 'world', '!']

    >>> splitstring('hello world !', ' ', None)
    ['hello', 'world', '!']

    >>> splitstring('hello world !', ' ', 0)
    'hello'

    """

    # If the part is empty
    if part in [None, '']:
        # Return an array of the splitted text
        return str(string).split(splitcharacter)

    # Return an array of the splitted text with a specific part
    return str(string).split(splitcharacter)[part]


def pykeyword(operation='list', keywordtotest=None):
    """
    Check if a keyword exists in the Python keyword dictionary.

    :type operation: string
    :param operation: Whether to list or check the keywords. Possible options are 'list' and 'in'.

    :type keywordtotest: string
    :param keywordtotest: The keyword to check.

    :return: The list of keywords or if a keyword exists.
    :rtype: list or boolean

    >>> "True" in pykeyword("list")
    True

    >>> pykeyword("in", "True")
    True

    >>> pykeyword("in", "foo")
    False

    >>> pykeyword("foo", "foo")
    Traceback (most recent call last):
      ...
    ValueError: Invalid operation specified.
    """

    # If the operation was 'list'
    if operation == 'list':
        # Return an array of keywords
        return str(keyword.kwlist)

    # If the operation was 'in'
    elif operation == 'in':
        # Return a boolean for if the string was a keyword
        return keyword.iskeyword(str(keywordtotest))

    # Raise a warning
    raise ValueError("Invalid operation specified.")


def binboolflip(item):
    """
    Convert 0 or 1 to False or True (or vice versa).
    The converter works as follows:

    - 0 > False
    - False > 0
    - 1 > True
    - True > 1

    :type item: integer or boolean
    :param item: The item to convert.

    >>> binboolflip(0)
    False

    >>> binboolflip(False)
    0

    >>> binboolflip(1)
    True

    >>> binboolflip(True)
    1

    >>> binboolflip("foo")
    Traceback (most recent call last):
      ...
    ValueError: Invalid item specified.
    """

    if item in [0, False, 1, True]:
        return int(item) if isinstance(item, bool) else bool(item)

    # Raise a warning
    raise ValueError("Invalid item specified.")


def modulereload(modulename):
    """
    Reload a module.

    :type modulename: module
    :param modulename: Name of module to reload.
    """

    # Reload the module
    importlib.reload(modulename)


def warnconfig(action='default'):
    """
    Configure the Python warnings.

    :type action: string
    :param action: The configuration to set. Options are: 'default', 'error', 'ignore', 'always', 'module' and 'once'.
    """

    # If action is 'default'
    if action.lower() == 'default':
        # Change warning settings
        warnings.filterwarnings('default')

    # If action is 'error'
    elif action.lower() == 'error':
        # Change warning settings
        warnings.filterwarnings('error')

    # If action is 'ignore'
    elif action.lower() == 'ignore':
        # Change warning settings
        warnings.filterwarnings('ignore')

    # If action is 'always'
    elif action.lower() == 'always':
        # Change warning settings
        warnings.filterwarnings('always')

    # If action is 'module'
    elif action.lower() == 'module':
        # Change warning settings
        warnings.filterwarnings('module')

    # If action is 'once'
    elif action.lower() == 'once':
        # Change warning settings
        warnings.filterwarnings('once')

    # Raise runtime warning
    raise ValueError("Invalid action specified.")


def printmessage(text, amount=1):
    """
    Print out a console message.

    :type text: string
    :param text: The text to print out.

    :type amount: integer
    :param amount: The amount of times to print it out.
    """

    # Repeat for value of amount
    for _ in range(amount):
        # Print the text
        print(text)


def delay(seconds):
    """
    Delay for a specific amount of seconds.

    :type seconds: number
    :param seconds: The amount of seconds to delay.
    """

    # Perform the delay
    time.sleep(seconds)


def waitenter(times=1):
    """
    Wait for the user to press enter.

    :type times: integer
    :param times: The times to ask for the user to press enter.
    """

    # For each time
    for _ in range(times):
        # Ask for user input
        input("")


def typematch(variable, expectedtype):
    """
    Check if a variable is a specific type

    :type variable: variable
    :param variable: The variable to check the type of

    :type expectedtype: type
    :param expectedtype: The type to check against

    >>> typematch(True, bool)
    True

    >>> typematch("foo", str)
    True

    >>> typematch(True, str)
    False

    >>> binboolflip("foo")
    Traceback (most recent call last):
      ...
    ValueError: Invalid item specified.
    """

    # Return the result
    return isinstance(variable, expectedtype)


def sametype(variable1, variable2):
    """
    Check if 2 variables have the same type

    :type variable1: variable
    :param variable1: The first variable to check

    :type variable2: variable
    :param variable2: The second variable to check

    >>> sametype(True, False)
    True

    >>> sametype(True, "foo")
    False
    """

    # Return the result
    return isinstance(variable1, type(variable2))


def happybirthday(person):
    """
    Sing Happy Birthday
    """
    print('Happy Birthday To You')
    time.sleep(2)
    print('Happy Birthday To You')
    time.sleep(2)
    print('Happy Birthday Dear ' + str(person[0].upper()) + str(person[1:]))
    time.sleep(2)
    print('Happy Birthday To You')


def difference(num1, num2):
    """
    Find the difference between 2 numbers.

    :type num1: number
    :param num1: The first number to use.

    :type num2: number
    :param num2: The second number to use.

    >>> difference(1, 4)
    3
    """

    # Return the calculated value
    return abs(num1 - num2)


def divisable(num1, num2):
    """
    Check if a number is divisible by another number

    :type num1: number
    :param num1: The first number to check.

    :type num2: number
    :param num2: The second number to check.

    >>> divisable(4, 2)
    True
    """

    # Return the calculated boolean
    return bool(num1 % num2 == 0)


def length(value):
    """
    Find the length of a value

    :type value: variable
    :param value: The value to find the length of
    """

    # Try to return the length
    return len(value)


def cowsay(text='', align='centre'):
    """
    Simulate an ASCII cow saying text.

    :type text: string
    :param text: The text to print out.

    :type align: string
    :param algin: Where to align the cow. Can be 'left', 'centre' or 'right'
    """

    # Make align lowercase
    align = align.lower()

    # Set the cowtext
    cowtext = str(text)

    # Set top part of speech bubble to the length of the text plus 2
    topbar = ' ' * (len(text) + 2)

    # Set bottom part of speech bubble to the length of the text plus 2
    bottombar = ' ' * (len(text) + 2)

    # If align is centre
    if align in ["center", "centre"]:
        # Set the spacing before the cow to the length of half of the length of topbar plus 1
        spacing = " " * (int(len(topbar) / 2) + 1)

    # If align is left
    elif align == 'left':
        # Set spacing to a single space
        spacing = ' '

    # If align is right
    elif align == 'right':
        # Set the spacing to the length of the text plus 2
        spacing = " " * (len(text) + 2)

    else:
        # Raise a runtime warning
        raise ValueError("Invalid alignment provided.")

    # Print the top bar
    print(topbar)

    # Print the text
    print('( ' + repr(str(cowtext)) + ' )')

    # Print the bottom bar
    print(bottombar)

    # Print the cow with the spacing
    print(spacing + r'o   ^__^ ')
    print(spacing + r' o  (oO)\_______')
    print(spacing + r'    (__)\       )\/\ ')
    print(spacing + r'     U  ||----w | ')
    print(spacing + r'        ||     || ')


def getletter(variable, letternumber):
    """
    Get the corresponding item in a object

    :type variable: string
    :param variable: The string to get the letter from

    :type letternumber: integer
    :param letternumber: The index of the letter to get
    """

    # Get the corresponding letter
    return str(variable)[letternumber - 1]


def onlist(listtocheck, item):
    """
    Check if something is on a list.

    :type listtocheck: list
    :param listtocheck: The list to check.

    :type item: object
    :param item: The item to check if on the list.
    """

    # Return the result
    return item in listtocheck


def jointext(firststring, secondstring):
    """
    Join two strings together

    :type firststring: string
    :param firststring: The first string.

    :type secondstring: string
    :param secondstring: The second string.
    """

    # Return the joined strings
    return str(firststring) + str(secondstring)


def pyname(ifmain=False):
    """
    Get the value of __name__

    :type ifmain: boolean
    :param ifmain: If set to True then True will be returned if __name__ is equal to __main__

    :return: The value of __name__ or if ifmain is True, then if __name__ is equal to __main__
    :rtype: string or boolean
    """

    if ifmain is True:
        return __name__ == "__main__"
    return __name__


def convertbinary(value, argument):
    """
    Convert text to binary form or backwards.

    :type value: string
    :param value: The text or the binary text

    :type argument: string
    :param argument: The action to perform on the value. Can be "to" or "from".
    """

    if argument == 'to':
        return bin(value)
    elif argument == 'from':
        return format(value)
    raise ValueError("Invalid argument specified.")


def reversetext(contenttoreverse, reconvert=True):
    """
    Reverse any content

    :type contenttoreverse: string
    :param contenttoreverse: The content to be reversed

    :type reeval: boolean
    :param reeval: Wether or not to reconvert the object back into it's initial state. Default is "True".
    """

    # If reconvert is specified
    if reconvert is True:
        # Return the evalated form
        return eval(
            str(type(contenttoreverse)).split("'")[1] + "('" +
            str(contenttoreverse)[::-1] + "')")

    # Return the raw version
    return contenttoreverse[::-1]


def reverselist(listtoreverse):
    """
    Reverse a list.

    :type listtoreverse: list
    :param listtoreverse: The list to reverse
    """

    # Return the reversed list
    return listtoreverse.reverse()


def replacetext(string, texttofind, texttoreplace):
    """
    Replace text with other text.

    :type string: string
    :param string: The string with the text to replace.

    :type texttofind: string
    :param texttofind: The text to look for in the string.

    :type texttoreplace: string
    :param texttoreplace: The text to replace the matching text with.
    """

    # Return the replaced string
    return string.replace(texttofind, texttoreplace)


def gettype(value):
    """
    Get the type of an object

    :type value: string
    :param value: The object to check.
    """

    # Return the type
    return type(value)


def convertascii(value, command='to'):
    """
    Convert an ASCII value to a symbol

    :type value: string
    :param value: The text or the text in ascii form.

    :type argument: string
    :param argument: The action to perform on the value. Can be "to" or "from".
    """
    command = command.lower()
    if command == 'to':
        return chr(value)
    elif command == 'from':
        return ord(value)
    else:
        raise ValueError('Invalid operation provided.')


def availchars(charactertype):
    """
    Get all the available characters for a specific type.

    :type charactertype: string
    :param charactertype: The characters to get. Can be 'letters', 'lowercase, 'uppercase', 'digits', 'hexdigits', 'punctuation', 'printable', 'whitespace' or 'all'.

    >>> availchars("lowercase")
    'abcdefghijklmnopqrstuvwxyz'
    """

    # If the lowercase version of the character type is 'letters'
    if charactertype.lower() == 'letters':
        # Return the result
        return string.ascii_letters

    # If the lowercase version of the character type is 'lowercase'
    elif charactertype.lower() == 'lowercase':
        # Return the result
        return string.ascii_lowercase

    # If the lowercase version of the character type is 'uppercase'
    elif charactertype.lower() == 'uppercase':
        # Return the result
        return string.ascii_uppercase

    # If the lowercase version of the character type is 'digits'
    elif charactertype.lower() == 'digits':
        # Return the result
        return string.digits

    # If the lowercase version of the character type is 'hexdigits'
    elif charactertype.lower() == 'hexdigits':
        # Return the result
        return string.hexdigits

    # If the lowercase version of the character type is 'punctuation'
    elif charactertype.lower() == 'punctuation':
        # Return the result
        return string.punctuation

    # If the lowercase version of the character type is 'printable'
    elif charactertype.lower() == 'printable':
        # Return the result
        return string.printable

    # If the lowercase version of the character type is 'whitespace'
    elif charactertype.lower() == 'whitespace':
        # Return the result
        return string.whitespace

    # If the lowercase version of the character type is 'all'
    elif charactertype.lower() == 'all':
        # Return the result
        return string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits + string.hexdigits + string.punctuation + string.printable + string.whitespace

    # Raise a warning
    raise ValueError("Invalid character type provided.")


def textbetween(variable,
                firstnum=None,
                secondnum=None,
                locationoftext='regular'):
    """
    Get The Text Between Two Parts
    """
    if locationoftext == 'regular':
        return variable[firstnum:secondnum]
    elif locationoftext == 'toend':
        return variable[firstnum:]
    elif locationoftext == 'tostart':
        return variable[:secondnum]


def letternum(letter):
    """
    Get The Number Corresponding To A Letter
    """
    if not isinstance(letter, str):
        raise TypeError("Invalid letter provided.")
    if not len(letter) == 1:
        raise ValueError("Invalid letter length provided.")
    letter = letter.lower()
    alphaletters = string.ascii_lowercase
    for i in range(len(alphaletters)):
        if letter[0] == alphaletters[i]:
            return i + 1


def wordvalue(word):
    """
    Get the value of each letter of a string's position in the alphabet added up

    :type word: string
    :param word: The word to find the value of
    """

    # Set total to 0
    total = 0

    # For each character of word
    for i in enumerate(word):
        # Add it's letter value to total
        total += letternum(word[i[0]])

    # Return the final value
    return total


def spacelist(listtospace, spacechar=" "):
    """
    Convert a list to a string with all of the list's items spaced out.

    :type listtospace: list
    :param listtospace: The list to space out.

    :type spacechar: string
    :param spacechar: The characters to insert between each list item. Default is: " ".
    """
    output = ''
    space = ''
    output += str(listtospace[0])
    space += spacechar
    for listnum in range(1, len(listtospace)):
        output += space
        output += str(listtospace[listnum])
    return output


def numlistbetween(num1, num2, option='list', listoption='string'):
    """
    List Or Count The Numbers Between Two Numbers
    """
    if option == 'list':
        if listoption == 'string':
            output = ''
            output += str(num1)
            for currentnum in range(num1 + 1, num2 + 1):
                output += ','
                output += str(currentnum)
        elif listoption == 'list':
            output = []
            for currentnum in range(num1, num2 + 1):
                output.append(str(currentnum))
            return output
    elif option == 'count':
        return num2 - num1


def textalign(text, maxlength, align='left'):
    """
    Align Text When Given Full Length
    """
    if align == 'left':
        return text
    elif align == 'centre' or align == 'center':
        spaces = ' ' * (int((maxlength - len(text)) / 2))
    elif align == 'right':
        spaces = (maxlength - len(text))
    else:
        raise ValueError("Invalid alignment specified.")
    return spaces + text


def decintfix(decorint=0):
    """
    Fix The Formatting Of Decimals And Integers
    """
    if str(decorint)[-2:] == '.0':
        return int(decorint)
    return float(decorint)


"""
Maths
"""


def shapesides(inputtocheck, inputtype='shape'):
    """
    Get the sides of a shape.

    inputtocheck:
    The amount of sides or the shape to be checked,
    depending on the value of inputtype.

    inputtype:
    The type of input provided.
    Can be: 'shape', 'sides'.
    """

    # Define the array of sides to a shape
    shapestosides = {
        'triangle': 3,
        'square': 4,
        'pentagon': 5,
        'hexagon': 6,
        'heptagon': 7,
        'octagon': 8,
        'nonagon': 9,
        'decagon': 10,
        'hendecagon': 11,
        'dodecagon': 12,
        'triskaidecagon': 13,
        'tetrakaidecagon': 14,
        'pentadecagon': 15,
        'hexakaidecagon': 16,
        'heptadecagon': 17,
        'octakaidecagon': 18,
        'enneadecagon': 19,
        'icosagon': 20,
        'triacontagon': 30,
        'tetracontagon': 40,
        'pentacontagon': 50,
        'hexacontagon': 60,
        'heptacontagon': 70,
        'octacontagon': 80,
        'enneacontagon': 90,
        'hectagon': 100,
        'chiliagon': 1000,
        'myriagon': 10000,
        'megagon': 1000000,
        'googolgon': pow(10, 100),
        'ngon': 'n'
    }

    # Define an array with the flipped version of the sides to a shape
    sidestoshapes = dictflip(shapestosides)

    # If the lowercase version of the input type is 'shape'
    if inputtype.lower() == 'shape':
        # If the lowercase version of the shape is in the array
        if inputtocheck.lower() in shapestosides:
            # Return the corresponding sides
            return shapestosides[inputtocheck.lower()]

        # Return 'n'
        return shapestosides['n']

    if inputtype.lower() == 'sides':
        # If the lowercase version of the shape is in the array
        if inputtocheck.lower() in sidestoshapes:
            # Return the corresponding sides
            return sidestoshapes[inputtocheck.lower()]

        # Return 'ngon'
        return sidestoshapes['ngon']

    # Raise a warning
    raise ValueError("Invalid input type.")


def autosolve(equation):
    """
    Automatically solve an easy maths problem.

    :type equation: string
    :param equation: The equation to calculate.

    >>> autosolve("300 + 600")
    900
    """

    try:
        # Try to set a variable to an integer
        num1 = int(equation.split(" ")[0])

    except ValueError:
        # Try to set a variable to a decimal
        num1 = float(equation.split(" ")[0])

    try:
        # Try to set a variable to an integer
        num2 = int(equation.split(" ")[2])

    except ValueError:
        # Try to set a variable to a decimal
        num2 = float(equation.split(" ")[2])

    # If the lowercase version of the operator is '+', 'plus' or 'add'
    if equation.split(" ")[1].lower() in ["+", "plus", "add"]:

        # Return the answer
        return num1 + num2

    # If the lowercase version of the operator is '-', 'minus' or 'subtract'
    elif equation.split(" ")[1].lower() in ["-", "minus", "subtract"]:

        # Return the answer
        return num1 - num2

    # If the lowercase version of the operator is '*', 'times', 'multiply'
    elif equation.split(" ")[1].lower() in ["*", "times", "multiply"]:

        # Return the answer
        return num1 * num2

    # If the lowercase version of the operator is '/', 'divide' or 'quotient'
    elif equation.split(" ")[1].lower() in ["/", "divide", "quotient"]:

        # Return the answer
        return num1 / num2

    # If the lowercase version of the operator is '%, 'remainder' or 'rem'
    elif equation.split(" ")[1].lower() in ["%", "remainder", "rem"]:

        # Return the answer
        return num1 % num2

    # Raise a warning
    raise ValueError("Invalid operation provided.")


def autohard(equation):
    """
    Automatically solve a hard maths problem.

    :type equation: string
    :param equation: The equation to solve.

    >>> autohard("log 10")
    2.302585092994046
    """

    try:
        # Try to set a variable to an integer
        num1 = int(equation.split(" ")[1])

    except ValueError:
        # Try to set a variable to a decimal
        num1 = float(equation.split(" ")[1])

    # If the lowercase version of the operation equals 'log'
    if equation.split(" ")[0].lower() == "log":
        # Return the answer
        return math.log(num1)

    # If the lowercase version of the operation equals 'acos'
    elif equation.split(" ")[0].lower() == "acos":
        # Return the answer
        return math.acos(num1)

    # If the lowercase version of the operation equals 'asin'
    elif equation.split(" ")[0].lower() == "asin":
        # Return the answer
        return math.asin(num1)

    # If the lowercase version of the operation equals 'atan'
    elif equation.split(" ")[0].lower() == "atan":
        # Return the answer
        return math.atan(num1)

    # If the lowercase version of the operation equals 'cos'
    elif equation.split(" ")[0].lower() == "cos":
        # Return the answer
        return math.cos(num1)

    # If the lowercase version of the operation equals 'hypot'
    elif equation.split(" ")[0].lower() == "hypot":
        try:
            # Try to set a variable to an integer
            num2 = int(equation.split(" ")[2])

        except ValueError:
            # Try to set a variable to an decimal
            num2 = float(equation.split(" ")[2])

        # Return the answer
        return math.hypot(num1, num2)

    # If the lowercase version of the operation equals 'sin'
    elif equation.split(" ")[0].lower() == "sin":
        # Return the answer
        return math.sin(num1)

    # If the lowercase version of the operation equals 'tan'
    elif equation.split(" ")[0].lower() == "tan":
        # Return the answer
        return math.tan(num1)

    # Raise a warning
    raise ValueError("Invalid operation entered.")


def equation(operation, firstnum, secondnum):
    """
    Solve a simple maths equation manually
    """
    if operation == 'plus':
        return (firstnum + secondnum)
    elif operation == 'minus':
        return (firstnum - secondnum)
    elif operation == 'multiply':
        return (firstnum * secondnum)
    elif operation == 'divide':
        if not secondnum == 0:
            return (firstnum / secondnum)
    raise ValueError('Invalid operation provided.')


def scientific(number, operation, number2=None, logbase=10):
    """
    Solve scientific operations manually
    """
    if operation == 'log':
        return math.log(number, logbase)
    elif operation == 'acos':
        return math.acos(number)
    elif operation == 'asin':
        return math.asin(number)
    elif operation == 'atan':
        return math.atan(number)
    elif operation == 'cos':
        return math.cos(number)
    elif operation == 'hypot':
        return math.hypot(number, number2)
    elif operation == 'sin':
        return math.sin(number)
    elif operation == 'tan':
        return math.tan(number)


def fracsimplify(numerator, denominator):
    """
    Simplify a fraction.

    :type numerator: integer
    :param numerator: The numerator of the fraction to simplify

    :type denominator: integer
    :param denominator: The denominator of the fraction to simplify

    :return: The simplified fraction
    :rtype: list
    """

    # If the numerator is the same as the denominator
    if numerator == denominator:
        # Return the most simplified fraction
        return '1/1'

    # If the numerator is larger than the denominator
    elif int(numerator) > int(denominator):
        # Set the limit to half of the numerator
        limit = int(numerator / 2)

    elif int(numerator) < int(denominator):

        # Set the limit to half of the denominator
        limit = int(denominator / 2)

    # For each item in range from 2 to the limit
    for i in range(2, limit):
        # Set the number to check as the limit minus i
        checknum = limit - i
        # If the number is divisible by the numerator and denominator
        if numerator % checknum == 0 and denominator % checknum == 0:
            # Set the numerator to half of the number
            numerator = numerator / checknum
            # Set the denominator to half of the number
            denominator = denominator / checknum

    # Return the integer version of the numerator and denominator
    return [int(numerator), int(denominator)]


def circleconvert(amount, currentformat, newformat):
    """
    Convert a circle measurement.

    :type amount: number
    :param amount: The number to convert.

    :type currentformat: string
    :param currentformat: The format of the provided value.

    :type newformat: string
    :param newformat: The intended format of the value.

    >>> circleconvert(45, "radius", "diameter")
    90
    """

    # If the same format was provided
    if currentformat.lower() == newformat.lower():
        # Return the provided value
        return amount

    # If the lowercase version of the current format is 'radius'
    if currentformat.lower() == 'radius':
        # If the lowercase version of the new format is 'diameter'
        if newformat.lower() == 'diameter':
            # Return the converted value
            return amount * 2

        # If the lowercase version of the new format is 'circumference'
        elif newformat.lower() == 'circumference':
            # Return the converted value
            return amount * 2 * math.pi

        # Raise a warning
        raise ValueError("Invalid new format provided.")

    # If the lowercase version of the current format is 'diameter'
    elif currentformat.lower() == 'diameter':
        # If the lowercase version of the new format is 'radius'
        if newformat.lower() == 'radius':
            # Return the converted value
            return amount / 2

        # If the lowercase version of the new format is 'circumference'
        elif newformat.lower() == 'circumference':
            # Return the converted value
            return amount * math.pi

        # Raise a warning
        raise ValueError("Invalid new format provided.")

    # If the lowercase version of the current format is 'circumference'
    elif currentformat.lower() == 'circumference':
        # If the lowercase version of the new format is 'radius'
        if newformat.lower() == 'radius':
            # Return the converted value
            return amount / math.pi / 2

        # If the lowercase version of the new format is 'diameter'
        elif newformat.lower() == 'diameter':
            # Return the converted value
            return amount / math.pi


def amountdiv(number, minnum, maxnum):
    """
    Get the amount of numbers divisable by a number.

    :type number: number
    :param number: The number to use.

    :type minnum: integer
    :param minnum: The minimum number to check.

    :type maxnum: integer
    :param maxnum: The maximum number to check.

    >>> amountdiv(20, 1, 15)
    5
    """

    # Set the amount to 0
    amount = 0

    # For each item in range of minimum and maximum
    for i in range(minnum, maxnum + 1):
        # If the remainder of the divided number is 0
        if number % i == 0:
            # Add 1 to the total amount
            amount += 1

    # Return the result
    return amount


def constant(constanttype):
    """
    Get A Constant
    """
    constanttype = constanttype.lower()
    if constanttype == 'pi':
        return math.pi
    elif constanttype == 'e':
        return math.e
    elif constanttype == 'tau':
        return math.tau
    elif constanttype == 'inf':
        return math.inf
    elif constanttype == 'nan':
        return math.nan
    elif constanttype in ['phi', 'golden']:
        return (1 + 5**0.5) / 2


def power(number, power):
    """
    Find The Power Of A Number
    """
    return math.pow(number, power)


def squareroot(number):
    """
    Find The Square Root Of A Number
    """
    return math.sqrt(number)


def factorial(n):
    """
    Find the factorial of a number
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)


def average(numbers, averagetype='mean'):
    """
    Find the average of a list of numbers

    :type numbers: list
    :param numbers: The list of numbers to find the average of.

    :type averagetype: string
    :param averagetype: The type of average to find.

    >>> average([1, 2, 3, 4, 5], 'median')
    3
    """

    try:
        # Try to get the mean of the numbers
        statistics.mean(numbers)

    except RuntimeError:
        # Raise a warning
        raise ValueError('Unable to parse the list.')

    # If the lowercase version of the average type is 'mean'
    if averagetype.lower() == 'mean':
        # Return the answer
        return statistics.mean(numbers)

    # If the lowercase version of the average type is 'mode'
    elif averagetype.lower() == 'mode':
        # Return the answer
        return statistics.mode(numbers)

    # If the lowercase version of the average type is 'median'
    elif averagetype.lower() == 'median':
        # Return the answer
        return statistics.median(numbers)

    # If the lowercase version of the average type is 'min'
    elif averagetype.lower() == 'min':
        # Return the answer
        return min(numbers)

    # If the lowercase version of the average type is 'max'
    elif averagetype.lower() == 'max':
        # Return the answer
        return max(numbers)

    # If the lowercase version of the average type is 'range'
    elif averagetype.lower() == 'range':
        # Return the answer
        return max(numbers) - min(numbers)

    # Raise a warning
    raise ValueError('Invalid average type provided.')


def numprop(value, propertyexpected):
    """
    Check If A Number Is A Type
    """
    if propertyexpected == 'triangular':
        x = (math.sqrt(8 * value + 1) - 1) / 2
        return bool(x - int(x) > 0)
    elif propertyexpected == 'square':
        return math.sqrt(value).is_integer()
    elif propertyexpected == 'cube':
        x = value**(1 / 3)
        x = int(round(x))
        return bool(x**3 == value)
    elif propertyexpected == 'even':
        return value % 2 == 0
    elif propertyexpected == 'odd':
        return not value % 2 == 0
    elif propertyexpected == 'positive':
        return bool(value > 0)
    elif propertyexpected == 'negative':
        return bool(value < 0)
    elif propertyexpected == 'zero':
        return bool(value == 0)


def posnegtoggle(number):
    """
    Toggle a number between positive and negative.
    The converter works as follows:

    - 1 > -1
    - -1 > 1
    - 0 > 0

    :type number: number
    :param number: The number to toggle.
    """
    if bool(number > 0):
        return number - number * 2
    elif bool(number < 0):
        return number + abs(number) * 2
    elif bool(number == 0):
        return number


def isrealnum(variable):
    """
    Check if the variable resembles a rational number.

    :type variable: integer
    :type param: The variable to check.
    """
    return bool(math.isfinite(variable))


def isfalse(variable):
    """
    Check if a variable is essentially "False"

    :type variable: variable
    :param variable: The variable to check
    """

    # Return the answer
    return variable in [0, 0.0, False, [], {}, math.nan, "", (), None]


def rounddown(number):
    """
    Round down a number

    :type number: number
    :param number: The number to round down
    """

    # Return the answer
    return math.floor(number)


def compare(value1, value2, comparison):
    """
    Compare 2 values

    :type value1: object
    :param value1: The first value to compare.

    :type value2: object
    :param value2: The second value to compare.

    :type comparison: string
    :param comparison: The comparison to make. Can be "is", "or", "and".

    :return: If the value is, or, and of another value
    :rtype: boolean
    """
    if not isinstance(comparison, str):
        raise TypeError("Comparison argument must be a string.")
    if comparison == 'is':
        return value1 == value2
    elif comparison == 'or':
        return value1 or value2
    elif comparison == 'and':
        return value1 and value2
    raise ValueError("Invalid comparison operator specified.")


def factors(number):
    """
    Find all of the factors of a number and return it as a list.

    :type number: integer
    :param number: The number to find the factors for.
    """

    if not (isinstance(number, int)):
        raise TypeError(
            "Incorrect number type provided. Only integers are accepted.")

    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


def euler(faces, edges, verticies):
    """
    Calculate the value of Euler's formula of a shape.

    :type faces: integer
    :param faces: The faces of the shape

    :type edges: integer
    :param edges: The edges of the shape

    :type verticies: integer
    :param verticies: The verticies of the shape

    :return: The result of the euler operation
    :rtype: number
    """

    # Return the calculated value
    return verticies + edges - faces


def sigmoid(number):
    """
    Find the sigmoid of a number.

    :type number: number
    :param number: The number to find the sigmoid of

    :return: The result of the sigmoid
    :rtype: number

    >>> sigmoid(1)
    0.7310585786300049
    """

    # Return the calculated value
    return 1 / (1 + math.exp(-number))


def randomnum(minimum=1, maximum=2, seed=None):
    """
    Generate a random number.

    :type minimum: integer
    :param minimum: The minimum number to generate.

    :type maximum: integer
    :param maximum: The maximum number to generate.

    :type seed: integer
    :param seed: A seed to use when generating the random number.

    :return: The randomized number.
    :rtype: integer

    :raises TypeError: Minimum number is not a number.
    :raises TypeError: Maximum number is not a number.

    >>> randomnum(1, 100, 150)
    42
    """

    if not (isnum(minimum)):
        raise TypeError("Minimum number is not a number.")

    if not (isnum(maximum)):
        raise TypeError("Maximum number is not a number.")

    if seed is None:
        return random.randint(minimum, maximum)

    random.seed(seed)
    return random.randint(minimum, maximum)


def tokhex(length=10, urlsafe=False):
    """
    Return a random string in hexadecimal
    """
    if urlsafe is True:
        return secrets.token_urlsafe(length)
    return secrets.token_hex(length)


def isfib(number):
    """
    Check if a number is in the Fibonacci sequence.

    :type number: integer
    :param number: Number to check
    """

    num1 = 1
    num2 = 1
    while True:
        if num2 < number:
            tempnum = num2
            num2 += num1
            num1 = tempnum
        elif num2 == number:
            return True
        else:
            return False


def isprime(number):
    """
    Check if a number is a prime number

    :type number: integer
    :param number: The number to check
    """

    if number == 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def convertbase(number, base=10):
    """
    Convert a number in base 10 to another base

    :type number: number
    :param number: The number to convert

    :type base: integer
    :param base: The base to convert to.
    """

    integer = number
    if not integer:
        return '0'
    sign = 1 if integer > 0 else -1
    alphanum = string.digits + string.ascii_lowercase
    nums = alphanum[:base]
    res = ''
    integer *= sign
    while integer:
        integer, mod = divmod(integer, base)
        res += nums[mod]
    return ('' if sign == 1 else '-') + res[::-1]


def isnum(value):
    """
    Check if a value is a type of number (decimal or integer).

    :type value: object
    :param value: The value to check.
    """

    try:
        return bool(isinstance(value, (float, int)))
    except RuntimeError:
        return False


def quadrant(xcoord, ycoord):
    """
    Find the quadrant a pair of coordinates are located in

    :type xcoord: integer
    :param xcoord: The x coordinate to find the quadrant for

    :type ycoord: integer
    :param ycoord: The y coordinate to find the quadrant for
    """

    xneg = bool(xcoord < 0)
    yneg = bool(ycoord < 0)
    if xneg is True:
        if yneg is False:
            return 2
        return 3
    if yneg is False:
        return 1
    return 4


def flipcoords(xcoord, ycoord, axis):
    """
    Flip the coordinates over a specific axis, to a different quadrant

    :type xcoord: integer
    :param xcoord: The x coordinate to flip

    :type ycoord: integer
    :param ycoord: The y coordinate to flip

    :type axis: string
    :param axis: The axis to flip across. Could be 'x' or 'y'
    """

    axis = axis.lower()
    if axis == 'y':
        if xcoord > 0:
            return str(xcoord - xcoord - xcoord) + ', ' + str(ycoord)
        elif xcoord < 0:
            return str(xcoord + abs(xcoord) * 2) + ', ' + str(ycoord)
        elif xcoord == 0:
            return str(xcoord) + ', ' + str(ycoord)
        raise ValueError(
            "The X coordinate is neither larger, smaller or the same as 0.")

    elif axis == 'x':
        if ycoord > 0:
            return str(xcoord) + ', ' + str(ycoord - ycoord - ycoord)
        elif ycoord < 0:
            return str(ycoord + abs(ycoord) * 2) + ', ' + str(xcoord)
        elif ycoord == 0:
            return str(xcoord) + ', ' + str(ycoord)
        raise ValueError(
            "The Y coordinate is neither larger, smaller or the same as 0.")
    raise ValueError("Invalid axis. Neither x nor y was specified.")


def lcm(num1, num2):
    """
    Find the lowest common multiple of 2 numbers

    :type num1: number
    :param num1: The first number to find the lcm for

    :type num2: number
    :param num2: The second number to find the lcm for
    """

    if num1 > num2:
        bigger = num1
    else:
        bigger = num2
    while True:
        if bigger % num1 == 0 and bigger % num2 == 0:
            return bigger
        bigger += 1


def hcf(num1, num2):
    """
    Find the highest common factor of 2 numbers

    :type num1: number
    :param num1: The first number to find the hcf for

    :type num2: number
    :param num2: The second number to find the hcf for
    """

    if num1 > num2:
        smaller = num2
    else:
        smaller = num1
    for i in range(1, smaller + 1):
        if ((num1 % i == 0) and (num2 % i == 0)):
            return i


def pythrule(first, second):
    """
    Calculate the area of a right angled trangle based on Pythagoras' Theorem

    :type first: number
    :param first: The length of the first axis (x or y)

    :type second: number
    :param second: The length of the second axis (x or y)
    """

    return (first * second) / 2


"""
Secure
"""


def randstring(length=1):
    """
    Generate a random string consisting of letters, digits and punctuation

    :type length: integer
    :param length: The length of the generated string.
    """
    charstouse = string.ascii_letters + string.digits + string.punctuation
    newpass = ''
    for _ in range(length):
        newpass += str(charstouse[random.randint(0, len(charstouse) - 1)])
    return newpass


"""
String
"""


def dictflip(dictionary):
    """
    Flip the names and keys in a dictionary.

    This means that this:
    {'key1': 'value1', 'key2': 'value2'}
    will be converted into this:
    {'value1': 'key1', 'value2': 'key2'}

    :type dictionary: dictionary
    :param dictionary: The dictionary to flip.
    """

    return {v: k for k, v in dictionary.items()}


def catwalk(text):
    """
    Replace multiple spaces in a string with a single space.

    :type text: string
    :param text: The text to fix.

    >>> catwalk("this  is    a long  sentence")
    'this is a long sentence'
    """

    # Return the fixed version
    return ' '.join(text.split())


def converttabs(text, spaces=4):
    """
    Convert all the tabs to a specific amount of spaces

    :type text: string
    :param text: The text to convert tabs to spaces on

    :type spaces: integer
    :param spaces: The amount of spaces to replace tabs to.
    """

    return text.replace('\t', ' ' * spaces)


def shortentext(text, minlength, placeholder='...'):
    """
    Shorten some text by replacing the last part with a placeholder (such as '...')

    :type text: string
    :param text: The text to shorten

    :type minlength: integer
    :param minlength: The minimum length before a shortening will occur

    :type placeholder: string
    :param placeholder: The text to append after removing protruding text.
    """

    return textwrap.shorten(text, minlength, placeholder=str(placeholder))


def wraptext(text, maxlength):
    """
    Wrap text around the execution window according to a given size

    :type text: string
    :param text: The text to be wraped

    :type maxlength: integer
    :param maxlength: The amount of text until a wrap will be added
    """

    return textwrap.wrap(text, maxlength)


def unindent(text):
    """
    Remove indention for some text

    :type text: string
    :param text: The text to unindent
    """

    return textwrap.dedent(text)


def newline(lines=1):
    """
    Print 1 or more paragraph spaces in the terminal.

    :type lines: integer
    :param lines: The amount of paragraph spaces to print.
    """

    # Print the new line iterated by the amount of new lines
    print('\n' * lines)


def randomstr(valuelist):
    """
    Choose a random item from a list.

    :type valuelist: list
    :param valuelist: The list to choose a random item from.

    :raises IndexError: List not specified.
    """

    # Choose a random item and return it
    return random.choice(valuelist)


def case(text, casingformat='sentence'):
    """
    Change the casing of some text.

    :type text: string
    :param text: The text to change the casing of.

    :type casingformat: string
    :param casingformat: The format of casing to apply to the text. Can be 'uppercase', 'lowercase', 'sentence' or 'caterpillar'.

    :raises ValueError: Invalid text format specified.

    >>> case("HELLO world", "uppercase")
    'HELLO WORLD'
    """

    # If the lowercase version of the casing format is 'uppercase'
    if casingformat.lower() == 'uppercase':
        # Return the uppercase version
        return str(text.upper())

    # If the lowercase version of the casing format is 'lowercase'
    elif casingformat.lower() == 'lowercase':
        # Return the lowercase version
        return str(text.lower())

    # If the lowercase version of the casing format is 'sentence'
    elif casingformat.lower() == 'sentence':
        # Return the sentence case version
        return str(text[0].upper()) + str(text[1:])

    # If the lowercase version of the casing format is 'caterpillar'
    elif casingformat.lower() == 'caterpillar':
        # Return the caterpillar case version
        return str(text.lower().replace(" ", "_"))

    # Raise a warning
    raise ValueError("Invalid text format specified.")


"""
System
"""


def absolutedir(relativedirectory):
    """
    Convert a relative directory to an absolute directory.

    :type relativedirectory: string
    :param relativedirectory: The directory path to convert.

    >>> absolutedir("src") # doctest: +SKIP
    "C:/Users/richi/Documents/GitHub/quilt/src"
    """

    # Return the absolute version of the directory
    return os.path.abspath(str(relativedirectory))


def getplatform():
    """
    Get the current system platform.
    """

    # Return the system platform
    return sys.platform


def encryptstring(text, password):
    """
    Encrypt a string according to a specific password.

    :type text: string
    :param text: The text to encrypt.

    :type pass: string
    :param pass: The password to encrypt the text with.
    """

    enc = []
    for i in enumerate(text):
        key_c = password[i[0] % len(password)]
        enc_c = chr((ord(i[1]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def decryptstring(enc, password):
    """
    Decrypt an encrypted string according to a specific password.

    :type enc: string
    :param enc: The encrypted text.

    :type pass: string
    :param pass: The password used to encrypt the text.
    """

    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in enumerate(enc):
        key_c = password[i[0] % len(password)]
        dec_c = chr((256 + ord(i[1]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


def tempdir():
    """
    Generate and get a path to a temporary directory
    """

    # Create a directory and return the path
    return tempfile.mkdtemp()


def shellcommand(command):
    """
    Execute a command in the host's terminal/shell/bash
    command:
    Specify the command to be executed
    """

    subprocess.call(str(command))


def pipinstall(packages):
    """
    Install one or more pip packages.

    :type packages: string or list
    :param packages: The package or list of packages to install.

    :raises TypeError: Nor a string or a list was provided.
    """

    if isinstance(packages, str):
        if hasattr(pip, 'main'):
            pip.main(['install', packages])
        else:
            pip._internal.main(['install', packages])
    elif isinstance(packages, list):
        for i in enumerate(packages):
            if hasattr(pip, 'main'):
                pip.main(['install', i[1]])
            else:
                pip._internal.main(['install', i[1]])
    else:
        raise TypeError("Nor a string or a list was provided.")


def pipupdate():
    """
    Update all currently installed pip packages
    """

    packages = [d for d in pkg_resources.working_set]
    subprocess.call('pip install --upgrade ' + ' '.join(packages))


def dirtool(operation, directory):
    """
    Tools For Directories (If Exists, Make And Delete)

    :raises ValueError: Nor a string or a list was provided.
    """
    operation = operation.lower()
    if operation == 'exists':
        return bool(os.path.exists(directory))
    if operation == 'create':
        os.makedirs(directory)
    elif operation == 'delete':
        os.rmdir(directory)
    else:
        raise ValueError('Invalid operation provided.')


def file(operation, path):
    """
    Tools For Files (If Exists, Make And Delete)
    """
    operation = operation.lower()
    if operation == 'exists':
        return bool(os.path.isfile(path))
    if operation == 'read':
        with open(path, 'r') as f:
            return [line.strip() for line in f]
    elif operation == 'delete':
        os.remove(path)
    elif operation == 'create':
        open(path, 'w').close()
    elif operation == 'clear':
        open(path, 'w').close()
    else:
        raise ValueError('Invalid operation provided.')


def exitexec(arguments=0):
    """
    Exit the current execution
    """
    sys.exit(arguments)


def charlimit():
    """
    Get the maximum amount of characters allowed by your system.

    >>> charlimit() # doctest: +SKIP
    9223372036854775807
    """

    # Return the value
    return sys.maxsize


def unilimit():
    """
    Get The Highest Unicode Value
    """
    return sys.maxunicode


def pyversion(part=None):
    """
    Get the version of Python
    """
    if part is None:
        return sys.version_info
    return sys.version_info[part]


def pyexec():
    """
    Get the executable used by Python
    """
    return sys.executable


def loglevel(leveltype=None, isequal=False):
    """
    Set or get the logging level of Quilt

    :type leveltype: string or integer
    :param leveltype: Choose the logging level. Possible choices are none (0), debug (10), info (20), warning (30), error (40) and critical (50).

    :type isequal: boolean
    :param isequal: Check if level is equal to leveltype.

    :return: If the level is equal to leveltype.
    :rtype: boolean

    >>> loglevel()
    30
    """
    log = logging.getLogger(__name__)
    leveltype = leveltype
    loglevels = {
        "none": 0,
        "debug": 10,
        "info": 20,
        "warning": 30,
        "error": 40,
        "critical": 50
    }
    if leveltype is None and isequal is False:
        return log.getEffectiveLevel()
    if leveltype is not None and isequal is True:
        if leveltype in loglevels.values():
            return leveltype == log.getEffectiveLevel()
        elif leveltype in loglevels:
            return loglevels[leveltype] == log.getEffectiveLevel()
        raise ValueError(
            "Incorrect input provided. It should be none, debug, info, warning, error or critical."
        )
    if leveltype in loglevels.values():
        log.basicConfig(level=leveltype)
    elif leveltype in loglevels:
        log.basicConfig(level=loglevels[leveltype])
    else:
        raise ValueError(
            "Incorrect input provided. It should be none, debug, info, warning, error or critical."
        )


def logfile(targetfile="ros.log"):
    """
    Set the file for Quilt to log to
    targetfile:
    Change the file to log to.
    """
    log = logging.getLogger(__name__)
    log.basicConfig(filename=str(targetfile))


def text(path, operation, content):
    """
    Perform changes on text files

    :type path: string
    :param path: The path to perform the action on

    :type operation: string
    :param operation: The operation to use on the file

    :type content: string
    :param content: The content to use with the operation
    """

    # If the operation is "write"
    if operation.lower() == 'write':
        # Open the file as "fh"
        with open(path, 'w') as fh:
            # Write to the file
            fh.write(content)

    # If the operation is "append"
    elif operation.lower() == 'append':
        # Open the file as "fh"
        with open(path, 'a') as fh:
            # Write to the file
            fh.write(content)

    # Raise a warning
    raise ValueError("Invalid operation provided")


"""
Time
"""


def dayofweek(day, month, year, formatresult=True):
    """

    Get the day of the week for a specific day

    :type day: integer
    :param day: The day to include in the search

    :type month: integer
    :param month: The month to include in the search

    :type year: integer
    :param year: The year to include in the search

    :type formatresult: boolean
    :param formatresult: Whether or not to format the result. A formatted date would look like: "Monday". A non formatted date would look like: 1.

    """
    if formatresult is False:
        return calendar.weekday(year, month, day) + 1
    days = {
        0: 'Monday',
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
    return days[calendar.weekday(year, month, day)]


def leapyear(year):
    """
    Check if a year in particular is a leap year

    :type year: integer
    :param year: The year to check for
    """

    # Return the answer
    return bool(calendar.isleap(year))


def closeyear(year):
    """
    Find how many years away was the closest leap year to a specific year.

    :type year: number
    :param year: The year to check for.
    """

    # Return the specific year
    return int(year % 4)


def converttime(time, currentformat, newformat):
    """
    Convert a specific time format to another type.

    :type time: integer
    :param time: The time to convert

    :type currentformat: string
    :param currentformat: The current format of the time. Can be milliseconds, seconds, minutes, hours, days, weeks, fortnights, years, decades, centuries or millenniums.

    :type newformat: string
    :param newformat: The new format of the time. Can be milliseconds, seconds, minutes, hours, days, weeks, fortnights, years, decades, centuries or millenniums.
    """

    # Define conversion dictionary
    conversions = {
        "milliseconds": {
            "milliseconds": "time",
            "seconds": "time / 1000",
            "minutes": "time / 1000 / 60",
            "hours": "time / 1000 / 60 / 60",
            "days": "time / 1000 / 60 / 60 / 24",
            "weeks": "time / 1000 / 60 / 60 / 24 / 7",
            "fortnights": "time / 1000 / 60 / 60 / 24 / 14",
            "years": "time / 1000 / 60 / 60 / 24 / 365",
            "decades": "time / 1000 / 60 / 60 / 24 / 365 / 10",
            "centuries": "time / 1000 / 60 / 60 / 24 / 365 / 100",
            "millenniums": "time / 1000 / 60 / 60 / 24 / 365 / 1000"
        },
        "seconds": {
            "milliseconds": "time * 1000",
            "seconds": "time",
            "minutes": "time / 60",
            "hours": "time / 60 / 60",
            "days": "time / 60 / 60 / 24",
            "weeks": "time / 60 / 60 / 24 / 7",
            "fortnights": "time / 60 / 60 / 24 / 14",
            "years": "time / 60 / 60 / 24 / 365",
            "decades": "time / 60 / 60 / 24 / 365 / 10",
            "centuries": "time / 60 / 60 / 24 / 365 / 100",
            "millenniums": "time / 60 / 60 / 24 / 365 / 1000"
        },
        "minutes": {
            "milliseconds": "time * 60 * 1000",
            "seconds": "time * 60",
            "minutes": "time",
            "hours": "time / 60",
            "days": "time / 60 / 24",
            "weeks": "time / 60 / 24 / 7",
            "fortnights": "time / 60 / 24 / 14",
            "years": "time / 60 / 24 / 365",
            "decades": "time / 60 / 24 / 365 / 10",
            "centuries": "time / 60 / 24 / 365 / 100",
            "millenniums": "time / 60 / 24 / 365 / 1000"
        },
        "hours": {
            "milliseconds": "time * 60 * 60 * 1000",
            "seconds": "time * 60 * 60",
            "minutes": "time * 60",
            "hours": "time",
            "days": "time / 24",
            "weeks": "time / 24 / 7",
            "fortnights": "time / 24 / 14",
            "years": "time / 24 / 365",
            "decades": "time / 24 / 365 / 10",
            "centuries": "time / 24 / 365 / 100",
            "millenniums": "time / 24 / 365 / 1000"
        },
        "days": {
            "milliseconds": "time * 24 * 60 * 60 * 1000",
            "seconds": "time * 24 * 60 * 60",
            "minutes": "time * 24 * 60",
            "hours": "time * 24",
            "days": "time",
            "weeks": "time / 7",
            "fortnights": "time / 14",
            "years": "time / 365",
            "decades": "time / 365 / 10",
            "centuries": "time / 365 / 100",
            "millenniums": "time / 365 / 1000"
        },
        "weeks": {
            "milliseconds": "time * 7 * 24 * 60 * 60 * 1000",
            "seconds": "time * 7 * 24 * 60 * 60",
            "minutes": "time * 7 * 24 * 60",
            "hours": "time * 7 * 24",
            "days": "time * 7",
            "weeks": "time",
            "fortnights": "time / 2",
            "years": "time / 52",
            "decades": "time / 52 / 10",
            "centuries": "time / 52 / 100",
            "millenniums": "time / 52 / 1000"
        },
        "fortnights": {
            "milliseconds": "time * 14 * 24 * 60 * 60 * 1000",
            "seconds": "time * 14 * 24 * 60 * 60",
            "minutes": "time * 14 * 24 * 60",
            "hours": "time * 14 * 24",
            "days": "time * 14",
            "weeks": "time * 2",
            "fortnights": "time",
            "years": "time / 26",
            "decades": "time / 26 / 10",
            "centuries": "time / 26 / 100",
            "millenniums": "time / 26 / 1000"
        },
        "years": {
            "milliseconds": "time * 256 * 24 * 60 * 60 * 1000",
            "seconds": "time * 256 * 24 * 60 * 60",
            "minutes": "time * 256 * 24 * 60",
            "hours": "time * 256 * 24",
            "days": "time * 256",
            "weeks": "time * 52",
            "fortnights": "time * 26",
            "years": "time",
            "decades": "time / 10",
            "centuries": "time / 100",
            "millenniums": "time / 1000"
        },
        "decades": {
            "milliseconds": "time * 10 * 256 * 24 * 60 * 60 * 1000",
            "seconds": "time * 10 * 256 * 24 * 60 * 60",
            "minutes": "time * 10 * 256 * 24 * 60",
            "hours": "time * 10 * 256 * 24",
            "days": "time * 10 * 256",
            "weeks": "time * 10 * 52",
            "fortnights": "time * 10 * 26",
            "years": "time * 10",
            "decades": "time",
            "centuries": "time / 10",
            "millenniums": "time / 100"
        },
        "centuries": {
            "milliseconds": "time * 100 * 256 * 24 * 60 * 60 * 1000",
            "seconds": "time * 100 * 256 * 24 * 60 * 60",
            "minutes": "time * 100 * 256 * 24 * 60",
            "hours": "time * 100 * 256 * 24",
            "days": "time * 100 * 256",
            "weeks": "time * 100 * 52",
            "fortnights": "time * 100 * 26",
            "years": "time * 100",
            "decades": "time * 10",
            "centuries": "time",
            "millenniums": "time / 10"
        },
        "millenniums": {
            "milliseconds": "time * 1000 * 256 * 24 * 60 * 60 * 1000",
            "seconds": "time * 1000 * 256 * 24 * 60 * 60",
            "minutes": "time * 1000 * 256 * 24 * 60",
            "hours": "time * 1000 * 256 * 24",
            "days": "time * 1000 * 256",
            "weeks": "time * 1000 * 52",
            "fortnights": "time * 1000 * 26",
            "years": "time * 1000",
            "decades": "time * 100",
            "centuries": "time * 10",
            "millenniums": "time"
        }
    }

    # Return evaluated value
    return eval(conversions[currentformat][newformat])


def minyear():
    """
    Get the minimum year allowed by the current OS.
    """

    return datetime.MINYEAR


def maxyear():
    """
    Get the maxiumum year allowed by the current OS.
    """

    return datetime.MAXYEAR


def timezone():
    """
    Get the current timezone code.
    """

    return time.timezone


def timesince():
    """
    Get the amount of time since 00:00 on 1 January 1970,
    the raw date before formatting it.
    """

    return time.time()


def getdatetime(timedateformat='complete'):
    """
    Get the current date or time in a specific format.

    :type timedateformat: string
    :param timedateformat: The type of date to query for. Can be: day, month, year, hour, minute, second, millisecond, yearmonthday, daymonthyear, hourminutesecond, secondminutehour, complete, datetime or timedate.
    """

    timedateformat = timedateformat.lower()
    if timedateformat == 'day':
        return ((str(datetime.datetime.now())).split(' ')[0]).split('-')[2]
    elif timedateformat == 'month':
        return ((str(datetime.datetime.now())).split(' ')[0]).split('-')[1]
    elif timedateformat == 'year':
        return ((str(datetime.datetime.now())).split(' ')[0]).split('-')[0]
    elif timedateformat == 'hour':
        return (((str(datetime.datetime.now())).split(' ')[1]).split('.')[0]
               ).split(':')[0]
    elif timedateformat == 'minute':
        return (((str(datetime.datetime.now())).split(' ')[1]).split('.')[0]
               ).split(':')[1]
    elif timedateformat == 'second':
        return (((str(datetime.datetime.now())).split(' ')[1]).split('.')[0]
               ).split(':')[2]
    elif timedateformat == 'millisecond':
        return (str(datetime.datetime.now())).split('.')[1]
    elif timedateformat == 'yearmonthday':
        return (str(datetime.datetime.now())).split(' ')[0]
    elif timedateformat == 'daymonthyear':
        return ((str(datetime.datetime.now())).split(' ')[0]).split(
            '-')[2] + '-' + ((str(
                datetime.datetime.now())).split(' ')[0]).split('-')[1] + '-' + (
                    (str(datetime.datetime.now())).split(' ')[0]).split('-')[0]
    elif timedateformat == 'hourminutesecond':
        return ((str(datetime.datetime.now())).split(' ')[1]).split('.')[0]
    elif timedateformat == 'secondminutehour':
        return (((str(datetime.datetime.now())).split(' ')[1]).split('.')[0]
               ).split(':')[2] + ':' + (((str(datetime.datetime.now())).split(
                   ' ')[1]).split('.')[0]).split(':')[1] + ':' + (
                       ((str(datetime.datetime.now())).split(' ')[1]
                       ).split('.')[0]).split(':')[0]
    elif timedateformat == 'complete':
        return str(datetime.datetime.now())
    elif timedateformat == 'datetime':
        return (str(datetime.datetime.now())).split('.')[0]
    elif timedateformat == 'timedate':
        return ((str(
            datetime.datetime.now())).split('.')[0]).split(' ')[1] + ' ' + (
                (str(datetime.datetime.now())).split('.')[0]).split(' ')[0]
    else:
        raise ValueError("Invalid time date format used.")


def timeit(command, round_result=True):
    """

    Time how long a command takes to execute

    command:
    The command to time.

    round_result:
    Whether or not to round the number to an integer.

    """
    t1 = time.clock()
    exec(command)
    t2 = time.clock()
    if round_result is True:
        return int(t2 - t1)
    return t2 - t1


"""
Web
"""

def isonline():
    """
    Check if you are currently connected to the internet.
    """

    conn = httplib.HTTPConnection("www.google.com", timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False

def mailto(to, cc=None, bcc=None, subject=None, body=None):
    """
    Generate and run mailto.

    :type to: string
    :param to: The recipient email address.

    :type cc: string
    :param cc: The recipient to copy to.

    :type bcc: string
    :param bcc: The recipient to blind copy to.

    :type subject: string
    :param subject: The subject to use.

    :type body: string
    :param body: The body content to use.
    """

    mailurl = 'mailto:' + str(to)
    if cc is None and bcc is None and subject is None and body is None:
        return str(mailurl)
    mailurl += '?'
    if cc is not None:
        mailurl += 'cc=' + str(cc)
        added = True
    added = False
    if bcc is not None:
        if added is True:
            mailurl += '&'
        mailurl += 'bcc=' + str(cc)
        added = True
    if subject is not None:
        if added is True:
            mailurl += '&'
        mailurl += 'subject=' + str(subject)
        added = True
    if body is not None:
        if added is True:
            mailurl += '&'
        mailurl += 'body=' + str(body)
        added = True
    return mailurl


def openurl(url):
    """
    Open a URL in a web browser.

    :type url: string
    :param url: The url to open.

    :raises webbrowser.Error: Unable to open URL
    """

    # Open the URL
    webbrowser.open(url)


def newwindow(url):
    """
    Open a URL in a new window of a web browser.

    :type url: string
    :param url: The url to open.

    :raises webbrowser.Error: Unable to open URL
    """

    # Open the URL
    webbrowser.open_new(url)


def newtab(url):
    """
    Open a URL in a new tab of a web browser.

    :type url: string
    :param url: The url to open.

    :raises webbrowser.Error: Unable to open URL
    """

    # Open the URL
    webbrowser.open_new_tab(url)


def getbrowser():
    """
    Get the name of the browser currently being used
    """

    # Try to find the browser
    try:
        # Get the browser name
        webbrowser.get(using=None)

    # Catch an error
    except RuntimeError:
        # Return nothing
        return None


def filedownload(source, destination):
    """
    Download a file and save it to a specific destination

    :type source: string
    :param source: The url to download from

    :type destination: string
    :param destination: The path to save the file to
    """

    # Initiate the download
    urllib.request.urlretrieve(source, destination)


class DictObject(object):
    """
    Fancier way of converting nested dictionary to an object!

    :type _dict: dictionary
    :param _dict: Already defined dictionary

    >>> d = {'a': 1, 'b': {'c': 2}, 'd': ["hi", {'foo': "bar"}]}
    >>> x = DictObject(d)
    >>> x.b.c
    2
    >>> x.d[1].foo
    'bar'
    """

    def __init__(self, _dict):
        for key, value in _dict.items():
            if isinstance(value, (list, tuple)):
                setattr(self, key, [
                    DictObject(x) if isinstance(x, dict) else x for x in value
                ])
            else:
                setattr(self, key,
                        DictObject(value) if isinstance(value, dict) else value)


"""
Copyright and Quilt Information
"""

# About information in a constant
about = """You are using the Quilt Lang Programming Library
Quilt is licensed under the Apache License 2.0"""
    
# Set a constant which can be checked to verify if Quilt is ready.
ready = True

if __name__ == "__main__":
    import doctest
    doctest.testmod()
