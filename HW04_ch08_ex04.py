#!/usr/bin/env python
# HW04_ch08_ex04

# The following functions are all intended to check whether a string contains
# any lowercase letters, but at least some of them are wrong. For each
# function, describe (is the docstring) what the function actually does.
# You can assume that the parameter is a string.

# Do not merely paste the output as a counterexample into the documentation
# string, explain what is wrong.

###############################################################################
# Body


def any_lowercase1(s):
    """the function checks if the first letter is lowercase."""
    for c in s:
        if c.islower(): 
            return True 
        else:
            return False


def any_lowercase2(s):
    """the function checks if letter 'c' is lowercase, so it always returns True.
    In addition, it returns a string value 'True' rather than a boolean value True.
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    """variable 'flag' doesn't have an initial value. 
    e.g. flag = NONE or flag = False.
    """
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    """this is correct! """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):
    """this function returns True only if all letters are lowercase."""
    for c in s:
        if not c.islower():
            return False
    return True


###############################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong,
    # call that function with a string for which the function returns
    # incorrectly.
    # ex.: any_lowercase_("thisstringmessesupthefunction")
    print(any_lowercase1('Itchecksthefirstletter'))
    print(any_lowercase2('THISCANBEANYTHING'))
    print(any_lowercase3(''))
    print(any_lowercase4('THISISCoRRECT'))
    print(any_lowercase5('ithastobeAlllowercase'))

if __name__ == '__main__':
    main()
