"""
This is the one and only Quilt Lang file.
"""
# Python modules
import warnings
import keyword
import importlib

# String modules
import string
import pprint
import secrets
import textwrap

# System modules
import subprocess
import os
import sys
import logging
import pkg_resources

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

# External Modules
import loremipsum
import colour
import clipboard
"""
Uncatagorised
"""


def userinput(prompttext=""):
    """
    Get the input of the user via a universally secure method

    prompttext:
    The text to display while receiving the data.
    """
    return input(str(prompttext))


def shellinput(initialtext='>> ', splitpart=' '):
    """
    Give the user a shell-like interface to enter commands which
    are returned as a multi-part list containing the command
    and each of the arguments.

    :type initialtext: string
    :param initialtext: Set the text to be displayed as the prompt.

    :type splitpart: string
    :param splitpart: The character to split when generating the list item.
    """

    try:
        # Convert shell user input to a string and set it to a variable
        shelluserinput = userinput(str(initialtext))
    except RuntimeError:
        # If it fails then raise a warning
        raise RuntimeWarning("Cannot convert type " + str(type(initialtext)) +
                             "to str")

    # If the part to split doesn't exist
    if splitpart == '' or splitpart is None:
        # Return the text
        return shelluserinput

    # Create en empty list object
    commands = []

    # For each item after splitting the output
    for item in enumerate(shelluserinput.split(splitpart)):

        # Append it to the list
        commands.append(item[1])

    # Return the command arguments
    return commands


def colourcode(startcolourcode, destinationtype, longhex=False):
    """
    Convert a colour code from one format to another.

    :type startcolourcode: string
    :param startcolourcode: Set the colour code to convert from.

    :type destinationtype: string
    :param destinationtype: Set the colour code type to convert to. Possible options are HEX, HSL, RGB, red, blue, green, hue, sat and lum.

    :type longhex: boolean
    :param longhex: If converting to hex, provided the long and unsimplified version.
    """

    # Create a colour object
    c = colour.Color(str(startcolourcode))

    # If the lowercase version of the destination type is 'hex'
    if destinationtype.lower() == 'hex':
        # If the long hex variable is True
        if longhex is True:
            # Return the long hex
            return c.hex_l

        # Return the hex
        return c.hex

    # If the lowercase version of the destination type is 'hsl'
    elif destinationtype.lower() == 'hsl':
        # Return the HSL
        return c.hsl

    # If the lowercase version of the destination type is 'rgb'
    elif destinationtype.lower() == 'rgb':
        # Return the RGB
        return c.rgb

    # If the lowercase version of the destination type is 'red'
    elif destinationtype.lower() == 'red':
        # Return the red amount
        return c.red

    # If the lowercase version of the destination type is 'blue'
    elif destinationtype.lower() == 'blue':
        # Return the blue amount
        return c.blue

    # If the lowercase version of the destination type is 'green'
    elif destinationtype.lower() == 'green':
        # Return the green amount
        return c.green

    # If the lowercase version of the destination type is 'hue'
    elif destinationtype.lower() == 'hue':
        # Return the hue amount
        return c.hue

    # If the lowercase version of the destination type is 'sat'
    elif destinationtype.lower() == 'sat':
        # Return the saturation amount
        return c.saturation

    # If the lowercase version of the destination type is 'lum'
    elif destinationtype.lower() == 'lum':
        # Return the luminance amount
        return c.luminance

    # If nothing matches raise a warning
    raise RuntimeWarning("Invalid destination code specified.")


def changecolour(colourcode, action, amount=100):
    """
    Modify a parameter of a colour code.

    :type colourcode: string
    :param colourcode: The colour code representing the colour to convert from.

    :type action: string
    :param action: The action to perform on the colour. Possible options are red, blue, green, hue, sat and lum.

    :type amount: integer
    :param amount: The percentage of the action to perform. For example, 100 means apply 100% of the colour (no change).

    >>> quilt_lang.changecolour("#f44336", "blue", 80)
    "#f443cc"
    """

    # Create a colour object
    c = colour.Color(colourcode)

    # If the lowercase version of the action is 'red'
    if action.lower() == 'red':
        # Modify the redness
        c.red = amount / 100

        # Return the result
        return str(c)

    # If the lowercase version of the action is 'blue'
    elif action.lower() == 'blue':
        # Modify the blueness
        c.blue = amount / 100

        # Return the result
        return str(c)

    # If the lowercase version of the action is 'green'
    elif action.lower() == 'green':
        # Modify the greenness
        c.green = amount / 100

        # Return the result
        return str(c)

    # If the lowercase version of the action is 'hue'
    elif action.lower() == 'hue':
        # Modify the hue
        c.hue = amount / 100

        # Return the result
        return str(c)

    # If the lowercase version of the action is 'sat'
    elif action.lower() == 'sat':
        # Modify the saturation
        c.saturation = amount / 100

        # Return the result
        return str(c)

    # If the lowercase version of the action is 'lum'
    elif action.lower() == 'lum':
        # Modify the luminance
        c.luminance = amount / 100

        # Return the result
        return str(c)

    raise RuntimeWarning("Invalid action specified.")


def leadingzero(number, minlength):
    """
    Add leading zeros to a number.

    :type number: number
    :param number: The number to add the leading zeros to.

    :type minlength: integer
    :param minlength: If the number is shorter than this length than add leading zeros to make the length correct.
    """

    # Return the number as a string with the filled number
    return str(number).zfill(int(minlength))


def absolutenum(number):
    """
    Get the absolute value for a number.

    :type number: number
    :param number: The number to get the absolute value for.

    >>> quilt_lang.absolutenum(-1)
    1
    """

    # Return the absolute number
    return abs(number)


def splitstring(string, splitcharacter=' ', part=None):
    """
    Split a string based on a character and get the parts as a list.

    string:
    The string to split.

    splitcharacter:
    The character to split for the string.

    part:
    Get a specific part of the list.
    """

    # If the part is empty
    if part in [None, '']:
        # Return an array of the splitted text
        return str(string).split(splitcharacter)

    # Return an array of the splitted text with a specific part
    return str(string).split(splitcharacter)[part]


def sort(listtosort, key=None, reversesort=False):
    """
    Sort a list alphabetically.

    listtosort:
    The list which will be sorted.

    key:
    The key to use when sorting.

    reverse:
    If to sort backwards.
    """

    # Return the sorted version of a list
    return sorted(listtosort, key=key, reverse=reversesort)


def pykeyword(operation='list', keywordtotest=None):
    """
    Check if a keyword exists in the Python keyword dictionary.

    operation:
    Whether to list or check the keywords.
    Possible options are 'list' and 'check'.

    keywordtotest:
    The keyword to check.
    """

    # If the operation was 'list'
    if operation == 'list':
        # Return an array of keywords
        return str(keyword.kwlist)

    # If the operation was 'check'
    elif operation == 'check':
        # Return a boolean for if the string was a keyword
        return keyword.iskeyword(str(keywordtotest))

    # Raise a warning
    raise RuntimeWarning("Invalid operation specified.")


def prettyprinter(listtoprint, stream=None, indent=1, width=80, depth=None):
    """
    Pretty Print a list.

    listtoprint:
    The list to pretty print.

    stream:
    The stream to use.

    indent:
    The indention to use.

    width:
    The width to use.

    depth:
    The depth to use.
    """

    # Pretty print the array
    pprint.pprint(listtoprint, stream, indent, width, depth)


def genipsum(sentences=1):
    """
    Generate an array of Lorem Ipsum

    sentences:
    The amount of sentences to generate.
    """

    # Return the generated ipsum
    return loremipsum.get_sentences(int(sentences))


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

    >>> quilt_lang.binboolflip(0)
    False
    """

    # Set the keys for coversion
    keys = {0: False, False: 0, 1: True, True: 1}

    try:
        # Try to return the converted value
        return keys[item]

    except RuntimeError:
        # Raise a warning
        raise RuntimeWarning("Invalid item specified.")


def modulereload(modulename):
    """
    Reload a module.

    modulename:
    Name of module to reload.
    """

    # Reload the module
    importlib.reload(modulename)


def warnconfig(action='default'):
    """
    Configure the Python warnings.

    action:
    The configuration to set.
    Options are: 'default', 'error', 'ignore', 'always', 'module' and 'once'.
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
    raise RuntimeWarning("Invalid action specified.")


def printmessage(text, amount=1):
    """
    Print out a console message.

    text:
    The text to print out.

    amount:
    The amount of times to print it out.
    """

    # Repeat for value of amount
    for _ in range(amount):
        # Print the text
        print(text)


# Compare 2 Numbers


def comparenum(value1, value2, comparison):
    if isnum(value1) and isnum(value2):
        comparison = comparison.lower()
        if comparison == 'equals':
            return value1 == value2
        elif comparison == 'not equal':
            return value1 != value2
        elif comparison == 'less than':
            return value1 < value2
        elif comparison == 'greater than':
            return value1 > value2
        elif comparison == 'more than':
            return value1 > value2
        elif comparison == 'less than or equal to':
            return value1 <= value2
        elif comparison == 'greater than or equal to':
            return value1 >= value2
        elif comparison == 'more than or equal to':
            return value1 >= value2


def throwerror(errortext):
    """
    Throw a Runtime Error

    :type errortext: string
    :param errortext: The text to print in the error.
    """

    # Throw the error
    raise RuntimeError("Forced Error: " + str(errortext))


# Delay For A Specific Amount Of Seconds


def delay(seconds):
    time.sleep(seconds)


# Waits For The User To Press Enter


def waitenter(times=1):
    for _ in range(times):
        userinput('')


# Convert A Variable To A String


def convertstring(value):
    return str(value)


# Return The Opposite Of A Boolean


def opposite(boolean):
    try:
        return not boolean
    except RuntimeError:
        raise RuntimeWarning(
            'An Error Has Occurred: Nor A Bool Or Len Was Provided (0014)')


# Check If A Number Is A Decimal


def isdecimal(value):
    return bool(isinstance(value, float))


# Check If A Variable Is A String


def isstring(variable):
    return bool(isinstance(variable, str))


# Check If A Variable Is A Specific Type


def istypematch(variable, typeexpected):
    return bool(isinstance(variable, typeexpected))


# Check If A Number Is An Integer (Full Number)


def isinteger(value):
    return bool(isinstance(value, int))


# Check For A Boolean


def isboolean(value):
    return isinstance(value, bool)


# Sing Happy Birthday


def happybirthday(person):
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

    >>> quilt_lang.difference(1, 4)
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

    >>> quilt_lang.divisable(4, 2)
    True
    """

    # Return the calculated boolean
    return bool(num1 % num2 == 0)


# Check If A Variable Is Empty


def isempty(variable):
    return bool(variable == '')


# Find The Length Of A Value


def length(value):
    try:
        return len(convertstring(value))
    except OverflowError:
        raise RuntimeWarning(
            'An Error Has Occured: The length of the object exceeds \
        the limit of ' + str(sys.maxsize))


# Simulate A Cow Saying Text


def cowsay(text='', align='centre'):
    align = align.lower()
    cowtext = str(text)
    topbar = ' '
    bottombar = ' '
    spacing = ''
    for _ in range(len(text) + 2):
        topbar = topbar + '_'
        bottombar = bottombar + '-'
    if align in ["center", "centre"]:
        for _ in range((int(len(topbar) / 2)) + 1):
            spacing = spacing + ' '
    elif align == 'left':
        spacing = ' '
    elif align == 'right':
        for _ in range(len(text) + 2):
            spacing = spacing + ' '
    print(topbar)
    print('( ' + cowtext + ' )')
    print(bottombar)
    print(spacing + r'o   ^__^ ')
    print(spacing + r' o  (oO)\_______')
    print(spacing + r'    (__)\       )\/\ ')
    print(spacing + r'     U  ||----w | ')
    print(spacing + r'        ||     || ')


# Get The Corresponding Letter In A String


def getletter(variable, letternumber):
    return str(variable)[letternumber - 1]


# Check If Something Is On The List


def onlist(listtocheck, item):
    return item in listtocheck


# Join Two Strings


def jointext(firststring, secondstring):
    return str(firststring) + str(secondstring)


# Get the value of __name__


def pyname(ifmain=False):
    if ifmain is True:
        return __name__ == "__main__"
    return __name__


# Convert Text To Binary Form


def convertbinary(value, argument):
    if argument == 'to':
        try:
            return bin(value)
        except RuntimeError:
            raise RuntimeWarning('Invalid Value (0016)')
    elif argument == 'from':
        try:
            return format(value)
        except RuntimeError:
            raise RuntimeWarning('Invalid Value (0016)')


# Make The Text Forwards Or Backwards


def reversetext(texttoreverse, ignoretype=False):
    if ignoretype is False:
        if isinteger(texttoreverse):
            return int(str(texttoreverse)[::-1])
        elif isdecimal(texttoreverse):
            return float(str(texttoreverse)[::-1])
        return str(texttoreverse)[::-1]
    return str(texttoreverse)[::-1]


# Reverse A List


def reverselist(listtoreverse):
    return listtoreverse.reverse()


# Replace Text In A Variable


def replacetext(string, texttofind, texttoreplace):
    return string.replace(texttofind, texttoreplace)


# Evaluate A Expression Or Operation


def evaluate(evaluation):
    return eval(str(evaluation))


# Execute A Line Of Python Code


def execute(execution):
    exec(str(execution))


# Get The Type Of A Value


def gettype(value):
    return type(value)


# Do a quick module test


def pingtest(returntrue=False):
    if returntrue:
        return True
    print("Pong!")


# Convert A ASCII Value To A Symbol


def convertascii(value, command='to'):
    command = command.lower()
    if command == 'to':
        try:
            return chr(value)
        except ValueError:
            raise RuntimeWarning('Invalid Symbol Value (0014)')
    elif command == 'from':
        try:
            return ord(value)
        except ValueError:
            raise RuntimeWarning('Invalid Symbol (0015)')
    else:
        raise RuntimeWarning(
            'An Error Has Occurred: Invalid Operation Entered (0008)')


# Get All Available Characters For A Type


def availchars(charactertype):
    """
    Get all the available characters for a specific type.

    :type charactertype: string
    :param charactertype: The characters to get. Can be 'letters', 'lowercase, 'uppercase', 'digits', 'hexdigits', 'punctuation', 'printable', 'whitespace' or 'all'.

    >>> quilt_lang.availchars("lowercase")
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
        return string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + \
            string.digits + string.hexdigits + string.punctuation + string.printable + string.whitespace

    # Raise a warning
    raise RuntimeWarning("Invalid character type provided.")


# Get The Value Of A Word


def wordvalue(word):
    total = 0
    for i in enumerate(word):
        total += letternum(word[i])
    return total


# Get the Range Of The Length


def enum(arguments):
    return enumerate(arguments)


# Get The Text Between Two Parts


def textbetween(variable,
                firstnum=None,
                secondnum=None,
                locationoftext='regular'):
    if locationoftext == 'regular':
        return variable[firstnum:secondnum]
    elif locationoftext == 'toend':
        return variable[firstnum:]
    elif locationoftext == 'tostart':
        return variable[:secondnum]


# Get The Number Corresponding To A Letter


def letternum(letter):
    if len(letter) == 1 and isstring(letter):
        letter = letter.lower()
        alphaletters = string.ascii_lowercase
        for i in range(len(alphaletters)):
            if getletter(letter, 1) == getletter(alphaletters, i + 1):
                return i + 1


# Return The List Equally Spaced


def spacelist(listtospace):
    output = ''
    space = ''
    output += str(listtospace[0])
    space += ' '
    for listnum in range(1, len(listtospace)):
        output += space
        output += str(listtospace[listnum])
    return output


# List Or Count The Numbers Between Two Numbers


def numlistbetween(num1, num2, option='list', listoption='string'):
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


# Align Text When Given Full Length


def textalign(text, maxlength, align='left'):
    spaces = ''
    if align == 'left':
        return text
    elif align == 'centre' or align == 'center':
        for _ in range(int((maxlength - len(text)) / 2)):
            spaces += ' '
    elif align == 'right':
        for _ in range(maxlength - len(text)):
            spaces += ' '
    return spaces + text


# Fix The Formatting Of Decimals And Integers


def decintfix(decorint=0):
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
    raise RuntimeWarning("Invalid input type.")


def autosolve(equation):
    """
    Automatically solve an easy maths problem.

    :type equation: string
    :param equation: The equation to calculate.

    >>> quilt_lang.autosolve("300 + 600")
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
    raise RuntimeWarning("Invalid operation provided.")


def autohard(equation):
    """
    Automatically solve a hard maths problem.

    :type equation: string
    :param equation: The equation to solve.

    >>> quilt_lang.autohard("log 10")
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
    raise RuntimeWarning("Invalid operation entered.")


# Solve a simple maths equation manually


def equation(operation, firstnum, secondnum):
    if not isnum(firstnum) and isnum(secondnum):
        raise RuntimeWarning(
            'An Error Has Occured: One Of The Values Specified Is Not A Number (0002)'
        )
    if operation == 'plus':
        return (firstnum + secondnum)
    elif operation == 'minus':
        return (firstnum - secondnum)
    elif operation == 'multiply':
        return (firstnum * secondnum)
    elif operation == 'divide':
        if not secondnum == 0:
            return (firstnum / secondnum)
    else:
        raise RuntimeWarning(
            'An Error Has Occured: You Entered An Invalid Operation (0003)')


# Solve scientific operations manually (May be deprecated)


def scientific(number, operation, number2=None, logbase=10):
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


# Simplify A Fraction


def fracsimplify(numerator, denominator):
    if numerator == denominator:
        return '1/1'
    elif numerator > denominator:
        limit = int(numerator / 2)
    elif numerator < denominator:
        limit = int(denominator / 2)
    for i in range(2, limit):
        checknum = limit - i
        if numerator % checknum == 0 and denominator % checknum == 0:
            numerator = numerator / checknum
            denominator = denominator / checknum
    return str(int(numerator)) + '/' + str(int(denominator))


def circleconvert(amount, currentformat, newformat):
    """
    Convert a circle measurement.

    :type amount: number
    :param amount: The number to convert.

    :type currentformat: string
    :param currentformat: The format of the provided value.

    :type newformat: string
    :param newformat: The intended format of the value.

    >>> quilt_lang.circleconvert(45, "radius", "diameter")
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
        raise RuntimeWarning("Invalid new format provided.")

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
        raise RuntimeWarning("Invalid new format provided.")

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

    >>> quilt_lang.amountdiv(20, 1, 15)
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


# Get A Constant


def constant(constanttype):
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


# Find The Power Of A Number


def power(number, power):
    return math.pow(number, power)


# Find The Square Root Of A number


def squareroot(number):
    return math.sqrt(number)


# Find the factorial of a number


def factorial(n):
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

    >>> quilt_lang.average([1, 2, 3, 4, 5], 'median')
    3
    """

    try:
        # Try to get the mean of the numbers
        statistics.mean(numbers)

    except RuntimeError:
        # Raise a warning
        raise RuntimeWarning('Unable to parse the list.')

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
    raise RuntimeWarning('Invalid average type provided.')


# Check If A Number Is A Type


def numprop(value, propertyexpected):
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


# Toggle A Number Between Positive And Negative


def posnegtoggle(number):
    if bool(number > 0):
        return number - number * 2
    elif bool(number < 0):
        return number + abs(number) * 2
    elif bool(number == 0):
        return number


# Check If A Variable Is Infinite


def isinfinite(variable):
    return bool(math.isfinite(variable))


# Check if a variable is essetially "False"


def isfalse(variable):
    if variable in [0, 0.0, False, [], {}, math.nan, ""]:
        return True
    return False


# Get The Largest Integer Less Than Or Equal To


def lessorequal(number):
    try:
        return math.floor(number)
    except RuntimeError:
        raise RuntimeWarning(
            'An Error Has Occured: Number Not Provided (0016)')


# Compare 2 Values


def compare(value1, value2, comparison):
    if not isinstance(comparison, str):
        raise RuntimeWarning("ERROR: comparison argument must be a string.")
    if comparison == 'is':
        return value1 == value2
    elif comparison == 'or':
        return value1 or value2
    elif comparison == 'and':
        return value1 and value2
    raise RuntimeWarning("Invalid comparison operator specified.")


# Find all the factors of a number


def factors(number):
    """
    Find all of the factors of a number and return it as a list
    number:
    The number to find the factors for
    """

    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


def eulercalc(faces, edges, verticies):
    """
    Calculate the value of Euler's formula of a shape
    faces:
    The faces of the shape
    edges:
    The edges of the shape
    verticies:
    The verticies of the shape
    """

    return verticies + edges - faces


def randomnum(minimum=1, maximum=2):
    """
    Generate a random number
    minimum:
    The minimum number to generate.
    maximum:
    The maximum number to generate.
    """

    if isnum(minimum):
        if isnum(maximum):
            return random.randint(minimum, maximum)
        raise RuntimeWarning("Maximum number is not a number.")
    raise RuntimeWarning('Minimum number is not a number.')


def isfib(number):
    """
    Check if a number is in the Fibonacci sequence
    number:
    Number to check
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
    number:
    The number to check
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
    number:
    The number to convert
    base:
    The base to convert to.
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
    Check if a value is a type of number (decimal or integer)
    value:
    The value to check
    """

    try:
        return bool(isinstance(value, (float, int)))
    except RuntimeError:
        return False


def quadrant(xcoord, ycoord):
    """
    Find the quadrant a pair of coordinates are located in
    xcoord:
    The x coordinate to find the quadrant for
    ycoord:
    The y coordinate to find the quadrant for
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
    xcoord:
    The x coordinate to flip
    ycoord:
    The y coordinate to flip
    axis:
    The axis to flip across. Could be 'x' or 'y'
    """

    axis = axis.lower()
    if axis == 'y':
        if xcoord > 0:
            return str(xcoord - xcoord - xcoord) + ', ' + str(ycoord)
        elif xcoord < 0:
            return str(xcoord + abs(xcoord) * 2) + ', ' + str(ycoord)
        elif xcoord == 0:
            return str(xcoord) + ', ' + str(ycoord)
        raise RuntimeWarning(
            "The X coordinate is neither larger, smaller or the same as 0.")

    elif axis == 'x':
        if ycoord > 0:
            return str(xcoord) + ', ' + str(ycoord - ycoord - ycoord)
        elif ycoord < 0:
            return str(ycoord + abs(ycoord) * 2) + ', ' + str(xcoord)
        elif ycoord == 0:
            return str(xcoord) + ', ' + str(ycoord)
        raise RuntimeWarning(
            "The Y coordinate is neither larger, smaller or the same as 0.")
    raise RuntimeWarning("Invalid axis. Neither x nor y was specified.")


def lcm(num1, num2):
    """
    Find the lowest common multiple of 2 numbers
    num1:
    The first number to find the lcm for
    num2:
    The second number to find the lcm for
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
    num1:
    The first number to find the hcf for
    num2:
    The second number to find the hcf for
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
    first:
    The length of the first axis (x or y)
    second:
    The length of the second axis (x or y)
    """

    return (first * second) / 2


"""
Secure
"""


def randstring(length=1):
    """

    Generate a random string consisting of letters, digits and punctuation

    length:
    The length of the generated string.

    """
    charstouse = string.ascii_letters + string.digits + string.punctuation
    newpass = ''
    for _ in range(length):
        newpass += str(charstouse[random.randint(0, len(charstouse) - 1)])
    return newpass


# Return A Random String In Hexadecimal


def tokhex(length=10, urlsafe=False):
    if urlsafe is True:
        return secrets.token_urlsafe(length)
    return secrets.token_hex(length)


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

    dictionary:
    The dictionary to flip.
    """

    return {v: k for k, v in dictionary.items()}


def catwalk(text):
    """
    Replace multiple spaces in a string with a single space.

    :type text: string
    :param text: The text to fix.

    >>> quilt_lang.catwalk("this  is    a long  sentence")
    'this is a long sentence'
    """

    # Return the fixed version
    return ' '.join(text.split())


def converttabs(text, spaces=4):
    """
    Convert all the tabs to a specific amount of spaces
    text:
    The text to convert tabs to spaces on
    spaces:
    The amount of spaces to replace tabs to.
    """

    return text.replace('\t', ' ' * spaces)


def shortentext(text, minlength, placeholder='...'):
    """
    Shorten some text by replacing the last part with a placeholder (such as '...')
    text:
    The text to shorten
    minlength:
    The minimum length before a shortening will occur
    placeholder:
    The text to append after removing protruding text.
    """

    return textwrap.shorten(text, minlength, placeholder=str(placeholder))


def wraptext(text, maxlength):
    """
    Wrap text around the execution window according to a given size
    text:
    The text to be wraped
    maxlength:
    The amount of text until a wrap will be added
    """

    return textwrap.wrap(text, maxlength)


def unindent(text):
    """
    Remove indention for some text
    text:
    The text to unindent
    """

    return textwrap.dedent(text)


def paraspace(paragraphspaces=1):
    """
    Print 1 or more paragraph spaces in the terminal output
    paragraphspaces:
    The amount of paragraph spaces to print.
    """

    for _ in range(paragraphspaces):
        print('', end='\n')


# Choose A Random Item From A List


def randomstr(valuelist):
    try:
        return random.choice(valuelist)
    except IndexError:
        raise RuntimeWarning('An Error Has Occured: List Not Specified (0018)')


def case(text, casingformat='sentence'):
    """
    Change the casing of some text.

    :type text: string
    :param text: The text to change the casing of.

    :type casingformat: string
    :param casingformat: The format of casing to apply to the text. Can be 'uppercase', 'lowercase', 'sentence' or 'caterpillar'.

    >>> quilt_lang.case("HELLO world", "uppercase")
    "HELLO WORLD"
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
    raise RuntimeWarning("Invalid text format specified.")


"""
System
"""


def absolutedir(relativedirectory):
    """
    Convert a relative directory to an absolute directory.

    :type relativedirectory: string
    :param relativedirectory: The directory path to convert.

    >>> quilt_lang.absolutedir("src") # doctest: +SKIP
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


def shellcommand(command):
    """
    Execute a command in the host's terminal/shell/bash
    command:
    Specify the command to be executed
    """

    subprocess.call(str(command))


def pipupdate():
    """
    Update all currently installed pip packages
    """

    packages = [d for d in pkg_resources.working_set]
    subprocess.call('pip install --upgrade ' + ' '.join(packages))


# Tools For Directories (If Exists, Make And Delete)


def dirtool(operation, directory):
    operation = operation.lower()
    if operation == 'exists':
        return bool(os.path.exists(directory))
    if operation == 'create':
        if os.path.exists(directory):
            raise RuntimeWarning(
                'An Error Has Occured: Directory Already Exists (0007)')
        else:
            os.makedirs(directory)
    elif operation == 'delete':
        if os.path.exists(directory):
            os.rmdir(directory)
        else:
            raise RuntimeWarning(
                'An Error Has Occured: Directory Doesn\'t Exist (0009)')
    else:
        raise RuntimeWarning(
            'An Error Has Occured: Invalid Operation Entered (0008)')


# Tools For Files (If Exists, Make And Delete)


def file(operation, path):
    operation = operation.lower()
    if operation == 'exists':
        return bool(os.path.isfile(path))
    if operation == 'read':
        if os.path.isfile(path):
            with open(path, 'r') as f:
                return [line.strip() for line in f]
        raise RuntimeWarning('An Error Has Occured: File Not Found (0012)')
    elif operation == 'delete':
        if os.path.isfile(path):
            os.remove(path)
        else:
            raise RuntimeWarning('An Error Has Occured: File Not Found (0012)')
    elif operation == 'create':
        if not file('exists', path):
            open(path, 'w').close()
        else:
            raise RuntimeWarning(
                'An Error Has Occured: File Already Exists (0013)')
    elif operation == 'clear':
        if os.path.isfile(path):
            open(path, 'w').close()
        raise RuntimeWarning('An Error Has Occured: File Not Found (0012)')
    else:
        raise RuntimeWarning(
            'An Error Has Occured: Invalid Operation Entered (0008)')


# Exit the current execution


def exitexec(arguments=0):
    sys.exit(arguments)


def charlimit():
    """
    Get the maximum amount of characters allowed by your system.

    >>> quilt_lang.charlimit() # doctest: +SKIP
    9223372036854775807
    """

    # Return the value
    return sys.maxsize


# Get The Highest Unicode Value


def unilimit():
    return sys.maxunicode


# Get the version of Python


def pyversion(part=None):
    if part is None:
        return sys.version_info
    return sys.version_info[part]


# Get the executable used by Python


def pyexec():
    return sys.executable


def loglevel(leveltype=None, isequal=False):
    """
    Set or get the logging level of Quilt

    :type leveltype: string or integer
    :param leveltype: Choose the logging level. Possible choices are none (0), debug (10), info (20), warning (30), error (40) and critical (50).

    :type isequal: boolean
    :param isequal: If set to True, instead of setting the level, returns True if the level is equal to leveltype. Otherwise, returns False.

    >>> quilt_lang.loglevel()
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
        raise RuntimeWarning(
            "Incorrect input provided. It should be none, debug, info, warning, error or critical."
        )
    if leveltype in loglevels.values():
        log.basicConfig(level=leveltype)
    elif leveltype in loglevels:
        log.basicConfig(level=loglevels[leveltype])
    else:
        raise RuntimeWarning(
            "Incorrect input provided. It should be none, debug, info, warning, error or critical."
        )


def logfile(targetfile="ros.log"):
    """
    Set the file for Quilt to log to
    targetfile:
    Change the file to log to.
    """
    log = logging.getLogger(__name__)
    try:
        str(targetfile)
    except RuntimeError:
        raise RuntimeWarning("Cannot convert type " + str(type(targetfile)) +
                             "to str")
    try:
        log.basicConfig(filename=str(targetfile))
    except RuntimeError:
        raise RuntimeWarning("Invalid target file specified")


def clipaction(action='get', text=None):
    """
    Gets, sets, appends or preceeds the clipboard contents.

    :type action: string
    :param action: The action to perform on the clipboard. Can be 'get', 'set' or 'append'.

    >>> quilt_lang.clipaction("get") # doctest: +SKIP
    "Sample text"
    """
    if action == 'get':
        return clipboard.paste()
    elif action == 'set':
        clipboard.copy(str(text))
    elif action == 'append':
        clipboard.copy(str(clipboard.paste) + str(text))
    elif action == 'preceed':
        clipboard.copy(str(text) + str(clipboard.paste))
    raise RuntimeWarning("Invalid clipboard action specified.")


# Tools For Text Files


def text(operation, path, argument):
    operation = operation.lower()
    if operation == 'write':
        if os.path.isfile(path):
            fh = open(path, 'w')
            fh.write(argument)
        else:
            raise RuntimeWarning('An Error Has Occured: File Not Found (0012)')
    elif operation == 'append':
        if os.path.isfile(path):
            fh = open(path, 'a')
            fh.write(argument)
        else:
            raise RuntimeWarning('An Error Has Occured: File Not Found (0012)')


"""
Time
"""


def dayofweek(day, month, year, formatresult=True):
    """

    Get the day of the week for a specific day

    day:
    The day to include in the search

    month:
    The month to include in the search

    year:
    The year to include in the search

    formatresult:
    Whether or not to format the result.
    A formatted date would look like: "Monday".
    A non formatted date would look like: 1.

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

    year:
    The year to check for

    """
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

    Convert a specific time format to another type

    time:
    The time to convert

    currentformat:
    The current format of the time.
    Can be seconds, milliseconds, minutes, hours, days, weeks, fortnights, years, decades, centuaries or millenniums.

    newformat:
    The new format of the time.
    Can be seconds, milliseconds, minutes, hours, days, weeks, fortnights, years, decades, centuaries or millenniums.

    """
    currentformat = currentformat.lower()
    newformat = newformat.lower()
    if currentformat == newformat:
        return time
    if currentformat == 'seconds':
        if newformat == 'milliseconds':
            return time * 1000
        elif newformat == 'minutes':
            return time / 60
        elif newformat == 'hours':
            return time / 60 / 60
        elif newformat == 'days':
            return time / 60 / 60 / 24
        elif newformat == 'weeks':
            return time / 60 / 60 / 24 / 7
        elif newformat == 'fortnights':
            return time / 60 / 60 / 24 / 14
        elif newformat == 'years':
            return time / 60 / 60 / 24 / 365
        elif newformat == 'decades':
            return time / 60 / 60 / 24 / 365 / 10
        elif newformat == 'centuaries':
            return time / 60 / 60 / 24 / 365 / 100
        elif newformat == 'millenniums':
            return time / 60 / 60 / 24 / 365 / 1000
        else:
            raise RuntimeWarning("Incorrect new time format specified.")
    elif currentformat == 'minutes':
        if newformat == 'milliseconds':
            return time * 60 * 1000
        elif newformat == 'seconds':
            return time * 60
        elif newformat == 'hours':
            return time / 60
        elif newformat == 'days':
            return time / 60 / 24
        elif newformat == 'weeks':
            return time / 60 / 24 / 7
        elif newformat == 'fortnights':
            return time / 60 / 24 / 14
        elif newformat == 'years':
            return time / 60 / 24 / 365
        elif newformat == 'decades':
            return time / 60 / 24 / 365 / 10
        elif newformat == 'centuaries':
            return time / 60 / 24 / 365 / 100
        elif newformat == 'millenniums':
            return time / 60 / 24 / 365 / 1000
        else:
            raise RuntimeWarning("Incorrect new time format specified.")
    elif currentformat == 'hours':
        if newformat == 'milliseconds':
            return time * 60 * 60 * 1000
        elif newformat == 'seconds':
            return time * 60 * 60
        elif newformat == 'minutes':
            return time / 60
        elif newformat == 'days':
            return time / 24
        elif newformat == 'weeks':
            return time / 24 / 7
        elif newformat == 'fortnights':
            return time / 24 / 14
        elif newformat == 'years':
            return time / 24 / 7 / 365
        elif newformat == 'decades':
            return time / 24 / 365 / 10
        elif newformat == 'centuaries':
            return time / 24 / 365 / 100
        elif newformat == 'millenniums':
            return time / 24 / 365 / 1000
        else:
            raise RuntimeWarning("Incorrect new time format specified.")
    elif currentformat == 'days':
        if newformat == 'milliseconds':
            return time * 24 * 60 * 60 * 1000
        elif newformat == 'seconds':
            return time * 24 * 60 * 60
        elif newformat == 'minutes':
            return time * 24 * 60
        elif newformat == 'hours':
            return time * 24
        elif newformat == 'weeks':
            return time / 24 / 7
        elif newformat == 'fortnights':
            return time / 60 / 24 / 14
        elif newformat == 'years':
            return time / 60 / 24 / 7 / 365
        elif newformat == 'decades':
            return time / 7 / 365 / 10
        elif newformat == 'centuaries':
            return time / 7 / 365 / 100
        elif newformat == 'millenniums':
            return time / 7 / 365 / 1000
        else:
            raise RuntimeWarning("Incorrect new time format specified.")
    elif currentformat == 'weeks':
        if newformat == 'milliseconds':
            return time * 7 * 24 * 60 * 60 * 1000
        elif newformat == 'seconds':
            return time * 7 * 24 * 60 * 60
        elif newformat == 'minutes':
            return time * 7 * 24 * 60
        elif newformat == 'hours':
            return time * 7 * 24
        elif newformat == 'fortnights':
            return time * 7 / 14
        elif newformat == 'years':
            return time * 7 / 365
        elif newformat == 'decades':
            return time * 7 / 365 / 10
        elif newformat == 'centuaries':
            return time * 7 / 365 / 100
        elif newformat == 'millenniums':
            return time * 7 / 365 / 1000
        else:
            raise RuntimeWarning("Incorrect new time format specified.")
    elif currentformat == 'fortnights':
        if newformat == 'milliseconds':
            return time * 14 * 24 * 60 * 60 * 1000
        elif newformat == 'seconds':
            return time * 14 * 24 * 60 * 60
        elif newformat == 'minutes':
            return time * 14 * 24 * 60
        elif newformat == 'hours':
            return time * 14 * 24
        elif newformat == 'weeks':
            return time * 14
        elif newformat == 'years':
            return time * 14 / 365
        elif newformat == 'decades':
            return time * 14 / 365 / 10
        elif newformat == 'centuaries':
            return time * 14 / 365 / 100
        elif newformat == 'millenniums':
            return time * 14 / 365 / 1000
        else:
            raise RuntimeWarning("Incorrect new time format specified.")
    elif currentformat == 'years':
        if newformat == 'milliseconds':
            return time * 365 * 24 * 60 * 60 * 1000
        elif newformat == 'seconds':
            return time * 365 * 24 * 60 * 60
        elif newformat == 'minutes':
            return time * 365 * 24 * 60
        elif newformat == 'hours':
            return time * 365 * 24
        elif newformat == 'days':
            return time * 365
        elif newformat == 'weeks':
            return time * 365 / 7
        elif newformat == 'fortnights':
            return time * 365 / 14
        elif newformat == 'decades':
            return time / 10
        elif newformat == 'centuaries':
            return time / 100
        elif newformat == 'millenniums':
            return time / 1000
        else:
            raise RuntimeWarning("Incorrect new time format specified.")
    elif currentformat == 'decades':
        if newformat == 'milliseconds':
            return time * 10 * 365 * 24 * 60 * 60 * 1000
        elif newformat == 'seconds':
            return time * 10 * 365 * 24 * 60 * 60
        elif newformat == 'minutes':
            return time * 10 * 365 * 24 * 60
        elif newformat == 'hours':
            return time * 10 * 365 * 24
        elif newformat == 'days':
            return time * 10 * 365
        elif newformat == 'weeks':
            return time * 10 * 365 / 7
        elif newformat == 'fortnights':
            return time * 10 * 365 / 14
        elif newformat == 'years':
            return time * 10
        elif newformat == 'centuaries':
            return time * 10 / 100
        elif newformat == 'millenniums':
            return time * 10 / 1000
        else:
            raise RuntimeWarning("Incorrect new time format specified.")
    elif currentformat == 'centuaries':
        if newformat == 'milliseconds':
            return time * 100 * 365 * 24 * 60 * 60 * 1000
        elif newformat == 'seconds':
            return time * 100 * 365 * 24 * 60 * 60
        elif newformat == 'minutes':
            return time * 100 * 365 * 24 * 60
        elif newformat == 'hours':
            return time * 100 * 365 * 24
        elif newformat == 'days':
            return time * 100 * 365
        elif newformat == 'weeks':
            return time * 100 * 365 / 7
        elif newformat == 'fortnights':
            return time * 100 * 365 / 14
        elif newformat == 'years':
            return time * 100
        elif newformat == 'decades':
            return time * 100 / 10
        elif newformat == 'millenniums':
            return time * 100 / 1000
        else:
            raise RuntimeWarning("Incorrect new time format specified.")
    elif currentformat == 'millenniums':
        if newformat == 'milliseconds':
            return time * 1000 * 365 * 24 * 60 * 60 * 1000
        elif newformat == 'seconds':
            return time * 1000 * 365 * 24 * 60 * 60
        elif newformat == 'minutes':
            return time * 1000 * 365 * 24 * 60
        elif newformat == 'hours':
            return time * 1000 * 365 * 24
        elif newformat == 'days':
            return time * 1000 * 365
        elif newformat == 'weeks':
            return time * 1000 * 365 / 7
        elif newformat == 'fortnights':
            return time * 1000 * 365 / 14
        elif newformat == 'years':
            return time * 1000
        elif newformat == 'decades':
            return time * 1000 / 10
        elif newformat == 'centuaries':
            return time * 1000 / 100
        else:
            raise RuntimeWarning("Incorrect new time format specified.")
    else:
        raise RuntimeWarning("Incorrect old time format specified.")


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
    the raw date before formatting by computers.

    """
    return time.time()


def getdatetime(timedateformat='complete'):
    """
    Get the current date or time in a specific format

    timedateformat:
    The type of date to query for.
    Can be: day, month, year, hour, minute, second, millisecond, yearmonthday,
    daymonthyear, hourminutesecond, secondminutehour, complete,
    datetime or timedate.
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
        return ((str(datetime.datetime.now(
        ))).split(' ')[0]).split('-')[2] + '-' + ((str(
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
        raise RuntimeWarning("Invalid time date format used.")


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

# Generate And Run MailTo


def mailto(to, cc, bcc, subject, body, autorun=True):
    mailurl = 'mailto:' + str(to)
    if cc is None and bcc is None and subject is None and body is None:
        if autorun is True:
            webbrowser.open_new_tab(str(mailurl))
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
    if autorun is True:
        webbrowser.open_new_tab(str(mailurl))
    else:
        return mailurl


# Open A Link In A Web Browser


def openurl(url):
    try:
        webbrowser.open(url)
    except webbrowser.Error:
        raise RuntimeWarning('An Error Has Occured: Unable To Open URL (0017)')


# Open A Link In A New Window Of A Web Browser


def newwindow(url):
    try:
        webbrowser.open_new(url)
    except webbrowser.Error:
        raise RuntimeWarning('An Error Has Occured: Unable To Open URL (0017)')


# Open A Link In A New Tab Of A Web Browser


def newtab(url):
    try:
        webbrowser.open_new_tab(url)
    except webbrowser.Error:
        raise RuntimeWarning('An Error Has Occured: Unable To Open URL (0017)')



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

    # Try to download the file
    try:
        # Initiate the download
        urllib.request.urlretrieve(source, destination)

    # Catch a download error
    except RuntimeError:
        # Throw a warning
        raise RuntimeWarning('Unable to download file')


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
                setattr(
                    self, key,
                    DictObject(value) if isinstance(value, dict) else value)


"""
Copyright
"""


def about():
    """
    Print the about information.

    >>> quilt_lang.about()
    You are using the Quilt Lang Programming Library
    Quilt is licensed under Apache License 2.0
    """
    print('You are using the Quilt Lang Programming Library')
    print('Quilt is licensed under Apache License 2.0')


def quiltlicense(raw=False):
    """
    Print the Quilt Lang license.

    raw:
    Set to True in order to print the raw text while
    only leveraging ASCII characters.
    """
    if raw is False:
        print('Quilt is licensed under the Apache License 2.0')
        print(
            u'\u2714' +
            ' Permissions: Commercial use, Modification, Distribution, Patent use And Private use'
        )
        print(u'\u274c' +
              ' Limitations: Trademark use, Liability And Warranty')
        print(u'\u2139' +
              ' Conditions: License and copyright notice And State changes')
        print('To view the full license, go to https://git.io/fp4x2')
    else:
        print('Quilt Is licensed Under The Apache License 2.0')
        print(
            'Permissions: Commercial use, Modification, Distribution, Patent use And Private use'
        )
        print('Limitations: Trademark use, Liability And Warranty')
        print('Conditions: License and copyright notice And State changes')
        print('To view the full license, go to https://git.io/fp4x2')


def pycopyright():
    """
    Return the Python copyright information.
    """

    return sys.copyright
