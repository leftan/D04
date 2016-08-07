#!/usr/bin/env python
# HW04_ch08_ex00
# See 8.7

# The following program counts the number of times the letter 'a' appears in a
# string:

#     word = 'banana'
#     count = 0
#     for letter in word:
#         if letter == 'a':
#             count = count + 1
#     print(count)

# Encapsulate this code in a function named "count", and generalize it so that
# it accepts the string and the letter as arguments.

###############################################################################
# Imports

def count(word, letter):
    '''word, letter: str'''
    result = 0
    for char in word:
        if char == letter:
            result += 1
    return result


# Body


###############################################################################
def main():

    # Remove print("Hello World!") and add several functions calls to count()
    # below, passing various strings and letters
    print(count('banana', 'a'))
    print(count('tree', 'e'))
    print(count('berkeley', 'e'))


if __name__ == '__main__':
    main()
