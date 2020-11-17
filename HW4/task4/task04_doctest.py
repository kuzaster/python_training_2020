"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Write a detailed instruction how to run doctests**.
That how first steps for the instruction may look like:
 - Install Python 3.8 (https://www.python.org/downloads/)
 - Install pytest `pip install pytest`
 - Clone the repository <path your repository>
 - Checkout branch <your branch>
 - Open terminal
 - ...
Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - instructions how to run doctest with the pytest are provided
You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
 - how to write instructions
# >>> fizzbuzz(5)
["1", "2", "fizz", "4", "buzz"]
* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """Return n FizzBuzz numbers.

    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']
    >>> fizzbuzz(15)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizz buzz']
    >>> fizzbuzz('string')
    Traceback (most recent call last):
        ...
    ValueError: It is not a number
    """
    try:
        numbers = []
        for i in range(1, n + 1):
            div_3 = not i % 3
            div_5 = not i % 5
            if div_3 and div_5:
                numbers.append("fizz buzz")
            elif div_3:
                numbers.append("fizz")
            elif div_5:
                numbers.append("buzz")
            else:
                numbers.append(str(i))
        return numbers
    except TypeError:
        raise ValueError("It is not a number") from None


if __name__ == "__main__":
    import doctest

    doctest.testmod()
