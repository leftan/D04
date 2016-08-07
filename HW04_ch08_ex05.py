# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 5 for the task.
# Please do provide function calls that test/demonstrate your
# function.

def shift_letter(letter, num):
    '''letter: string, single letter; num: int'''
    # convert the letter to a numeric code 
    letter_to_num = ord(letter) 
    # check if the letter is in alphabet.  
    if letter_to_num < ord('a') or letter_to_num > ord('z'):
        new_letter_to_num = letter_to_num
    # check if the new letter is still in alphabet.  
    else:
        new_letter_to_num = letter_to_num + num
        if new_letter_to_num < ord('a'): 
            new_letter_to_num += 26 # wrapping around to the end ('z')
        elif new_letter_to_num > ord('z'):  
            new_letter_to_num -= 26 # wrapping around to the beginning ('a')
    #convert the numeric code to a new letter
    num_to_newletter = chr(new_letter_to_num)
    return num_to_newletter

def rotate_word(s, num):
    '''s: str; num: int'''
    result = ''
    for letter in s:
        if letter.isupper(): #check if the letter is uppercase
            letter = letter.lower()
            result += shift_letter(letter, num).upper()
        else:
            result += shift_letter(letter, num)

    return result   

def main():
    print(rotate_word('XYZ', 1))
    print(rotate_word('Apple', -3))
    print(rotate_word('Gb trg gb gur bgure fvqr!', 13))

if __name__ == '__main__':
    main()     