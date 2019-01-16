# How you can help

At the moment, you can help by

- Adding more functions which you or someone else might find useful
- Adding and maintaining the docstrings
- Adding and improving unit tests

## Documenting and adding unit tests

Here is an example of a compliant function.

You may also depend on other functions in the project.
In this example, the function [`isnum`](https://github.com/Richienb/quilt/blob/43ef83d008116683c4b946e30087521d4369e2c9/src/quilt_lang/__init__.py#L17310) is used.

```py
def add(num1, num2):
    """
    Adds 2 numbers together
    
    :type num1: number
    :param num1: The first number to add
    
    :type num2: number
    :param num2: The second number to add
    
    :return: The added number
    :rtype: number
    
    :raises TypeError: Invalid value type provided.
    
    >>> add(1, 2)
    3
    
    >>> add(1, "foo")
    Traceback (most recent call last):
      ...
    TypeError: Invalid value type provided.
    """
    
    # If either num1 or num2 is not a number
    if not(isnum(num1) and isnum(num2)):
        # Raise a TypeError
        raise TypeError("Invalid value type provided.")
    
    # Return the added number
    return num1 + num2
```

Adding unit tests count towards the total code coverage score and should always be included.

All the other fields, affect the module documentation found [here](https://quilt-lang.richie-bendall.ml/commands/quilt_lang.html#module-quilt_lang).

## Testing guide

Using **GNU Make**, you can execute multiple commands with a single one.

- Force install the latest production version of Quilt: `make inst`
- Test the code: `make test`
- Install the dependencies: `make deps`
- Generate the Mkdocs documentation: `make mdoc`
- Generate the Sphinx documentation: `make sdoc`
- Build the PyPi package: `make pack`
