import sys

def loop_reverse(s: str) -> str:
    """
    Reverse a string using a loop.

    loop_reverse("hey") => "yeh"
    loop_reverse("aaa") => "aaa"
    loop_reverse("") => ""
    loop_reverse("1") => "1"

    :param s: input string
    :return: reversed input string
    """
    reversed_string = ""
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string


def recursive_reverse(s: str) -> str:
    """
    Reverse a string using recursion.

    recursive_reverse("hey") => "yeh"
    recursive_reverse("aaa") => "aaa"
    recursive_reverse("") => ""
    recursive_reverse("1") => "1"

    :param s: input string
    :return: reversed input string
    """
    if len(s) <= 1:
        return s
    return recursive_reverse(s[1:]) + s[0]


def loop_sum(n: int) -> int:
    """
    Calculate the sum of all numbers up to n (including n) using a loop.

    loop_sum(0) => 0
    loop_sum(3) => 6
    loop_sum(5) => 15

    :param n: the last number to add to the sum
    :return: sum
    """
    result = 0
    for i in range(n + 1):
        result += i
    return result


def recursive_sum(n: int) -> int:
    """
    Calculate the sum of all numbers up to n (including n) using recursion.

    recursive_sum(0) => 0
    recursive_sum(3) => 6
    recursive_sum(5) => 15

    :param n: the last number to add to the sum
    :return: sum
    """
    if n == 0:
        return 0
    return n + recursive_sum(n - 1)


def sum_digits_recursive(number: int) -> int:
    """
    Return the sum of the digits in number.

    Given a non-negative int n, return the sum of its digits recursively (no loops).

    sum_digits_recursive(123) => 6
    sum_digits_recursive(1) => 1
    sum_digits_recursive(0) => 0
    sum_digits_recursive(999) => 27

    :param number: non-negative number
    :return: sum of digits in the number
    """
    if number < 10:
        return number
    return number % 10 + sum_digits_recursive(number // 10)


def pair_star_recursive(s: str) -> str:
    """
    Add a star between adjacent same characters in the given string.

    For example:
    pair_star_recursive("aa") => "a*a"
    pair_star_recursive("hello") => "hel*lo"

    :param s: input string
    :return: string with stars inserted between adjacent same characters
    """
    if len(s) <= 1:
        return s
    if s[0] == s[1]:
        return s[0] + "*" + pair_star_recursive(s[1:])
    else:
        return s[0] + pair_star_recursive(s[1:])





sys.set_int_max_str_digits(10000)  # Increase the limit for integer string conversion

def test_sum_digits_recursive_one_digit():
    assert sum_digits_recursive(5) == 5

def test_sum_digits_recursive_one_two_digits():
    assert sum_digits_recursive(23) == 5

def test_sum_digits_recursive_numbers_with_ending_zeros():
    assert sum_digits_recursive(100) == 1

def test_sum_digits_recursive_huge_numbers():
    assert sum_digits_recursive(999999) == 54

def test_sum_digits_recursive_recursion_used():
    assert "recursive" in inspect.getsource(sum_digits_recursive)
