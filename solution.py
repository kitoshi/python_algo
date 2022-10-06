## Problem 1: squashNested


def squashNested(val):
    """
    Recursively eliminates nested lists, and always returns a list exactly one layer deep, containing all the elements.

    >>> squashNested(2)
    [2]
    >>> squashNested([2])
    [2]
    >>> squashNested([[2]])
    [2]
    >>> squashNested([[[2]]])
    [2]
    >>> squashNested([[1, 2], 3])
    [1, 2, 3]
    >>> squashNested([[[1, [2]]], 3])
    [1, 2, 3]
    """
    return val


## Problem 2: sumNested


def sumNested(val):
    """
    Recursively finds numbers in nested lists, returning the sum of all the nested numbers.

    >>> sumNested(2)
    2
    >>> sumNested([2])
    2
    >>> sumNested([[2]])
    2
    >>> sumNested([[[2]]])
    2
    >>> sumNested([[1, 2], 3])
    6
    >>> sumNested([[[1, [2]]], 3])
    6
    """
    return val


## Problem 3: binarySearch


def binarySearch(haystack, needle):
    """
    Recursively finds the needle in the haystack, using binary search.

    Haystack is a sorted list of numbers.  Needle is a number.

    If the needle found, returns the index of the found element.
    If multiple copies of the needle are found, may return any correct index.
    If the needle is not found, return None.

    >>> binarySearch([5, 7, 9], 5)
    0
    >>> binarySearch([5, 7, 9], 7)
    1
    >>> binarySearch([5, 7, 9], 8)
    2
    >>> binarySearch([5, 7, 9], 3)
    None
    """
    return -1


## Problem 4: calculator


def calc_helper(str, start):
    # Here's a hint, this is the parameters for the helper function I wrote to do 90% of the work
    return -1


def do_operator(operator, left, right):
    # There are fancier ways to do this, but I thought this would be nice and simple
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    if operator == "/":
        return left // right
    return None


def calculator(str):
    """
    Recursively parses the expression, calculating the result using normal arithmetic rules.

    Be sure to read the README for the complicated rules about what's legal.

    >>> calculator("5")
    5
    >>> calculator("(2 + 3)")
    5
    >>> calculator("(2 + (6 / 2))")
    5
    >>> calculator("((6 + (2 * (5 - 4))) / 2) ")
    4
    """

    # NOTE: you may change the code here if you wish.  But this is exactly the code from my solution, so it help.
    str = str.replace(" ", "")
    val, found_len = calc_helper(str, 0)
    if found_len == len(str):
        return val
    else:
        raise SyntaxError(f"leftover data: {str[found_len:]}")


## Problem 5: makeWeight


def makeWeight(target, weights):
    """
    Recursively calculates a combination of weights that adds up to the target.

    Returns an array showing the count of how many of each weight was used.

    If no solution is possible, return None.

    If more than one solution is possible, it must return the solution that favours the weights earlier in the list of options.

    Each weight may be used once, or not used at all (so the return array is all zeroes and ones).

    This problem is a simplified version of #6.

    >>> makeWeight(5, [2, 3, 4])                # 2 + 3 == 5
    [1, 1, 0]
    >>> makeWeight(7, [2, 3, 4])                # 3 + 4 == 7
    [0, 1, 1]
    >>> makeWeight(5, [1, 2, 3, 4])             # the 1 is first, so it wins, in combination with the 4
    [1, 0, 0, 1]
    >>> makeWeight(5, [2, 3, 4, 1])             # if we rearrange the weights in the list, the 2 and 3 are now earlier, so they win
    [1, 1, 0, 0]
    >>> makeWeight(8, [2, 3, 4]) is None        # no solution without using duplicate weights
    True
    >>> makeWeight(0, [2, 3, 4])                # it's very simple to add up to zero
    [0, 0, 0]
    >>> makeWeight(7, []) is None                     # no weights? no solution!
    True

    """
    return [0]


## Problem 6: makeWeightMany


def makeWeightMany(target, weights):
    """
    Recursively calculates a combination of weights that adds up to the target.

    Returns an array showing the count of how many of each weight was used.

    If no solution is possible, return None.

    If more than one solution is possible, it must return the solution that favours the weights earlier in the list of weights.

    Each weight may be used any integer number of times (no partial weights, though).

    This problem is a more difficult version of #5.

    >>> makeWeightMany(5, [2, 3, 4])    # 2 + 3 == 5
    [1, 1, 0]
    >>> makeWeightMany(7, [4, 3, 2])    # 4 + 3 == 7
    [1, 1, 0]
    >>> makeWeightMany(7, [2, 3, 4])    # this now solves differently from makeWeight
    [2, 1, 0]
    >>> makeWeightMany(0, [2, 3, 4])     # it's very simple to add up to zero
    [0, 0, 0]
    >>> makeWeightMany(7, []) is None   # no weights? no solution!
    True
    >>> makeWeightMany(8, [2, 3, 4])    # it's now possible to solve this one
    [4, 0, 0]
    >>> makeWeightMany(8, [4, 3, 2])      # changing the order of the weights might change the result
    [2, 0, 0]
    """
    return [0]
