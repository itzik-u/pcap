# Basic string exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in string2.py.
import math


# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'


def donuts(count):
#I am checking in a tinery if the number of donuts is eqwal or bigger
#then 10 return the word many else return number of donuts
    return "Number of donuts: "+("many" if count>=10 else str(count))


# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.


def both_ends(s):
#if the length of the string is bigger then 2 return first 2 letters and last 2 letters
#else return empty string
    return s[:2]+s[-2:] if len(s)>2 else ""


# C. fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.


def fix_start(s):

    # return first letter + a new subString from the second letter
    #while replasing all the letters that are eqwals the first letter with *
    return s[0]+(s[1:].replace(s[0],'*'))


# D. MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.


def mix_up(a, b):
    """ your docstring here """
    # +++your code here+++
    return b[:2]+a[2:]+' '+a[:2]+b[2:]


# E. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.


def verbing(s):
    """ your docstring here """
    # return the string if the size is less than 3 else if the string
    #is not ending with "ing" return string + "ing" else
    #return the string +  "ly"
    return s if len(s)<3 else s+"ing" if s[-3:]!="ing" else s+"ly"


# F. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!


def not_bad(s):
    """ your docstring here """
    # +++your code here+++
    return s if s.find("not")>s.find("bad") else s[:s.find("not"):]+"good"+s[s.find("bad")+3:]

# G. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back


def front_back(a, b):
    """ your docstring here """
    # +++your code here+++
    return a[:math.ceil(len(a)/2)]+b[:math.ceil(len(b)/2)]+a[math.ceil(len(a)/2):]+b[math.ceil(len(b)/2):]


# Provided simple check() function used in main() to print
# what each function returns vs. what it's supposed to return.


def check(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Provided main() calls the above functions with interesting inputs,
# using check() to check if each result is correct or not.
def main():
    print('donuts')
    # Each line calls donuts, compares its result to the expected for that call.
    check(donuts(4), 'Number of donuts: 4')
    check(donuts(9), 'Number of donuts: 9')
    check(donuts(10), 'Number of donuts: many')
    check(donuts(99), 'Number of donuts: many')

    print('both_ends')
    check(both_ends('spring'), 'spng')
    check(both_ends('Hello'), 'Helo')
    check(both_ends('a'), '')
    check(both_ends('xyz'), 'xyyz')

    print('fix_start')
    check(fix_start('babble'), 'ba**le')
    check(fix_start('aardvark'), 'a*rdv*rk')
    check(fix_start('google'), 'goo*le')
    check(fix_start('donut'), 'donut')

    print('mix_up')
    check(mix_up('mix', 'pod'), 'pox mid')
    check(mix_up('dog', 'dinner'), 'dig donner')
    check(mix_up('gnash', 'sport'), 'spash gnort')
    check(mix_up('pezzy', 'firm'), 'fizzy perm')

    print('verbing')
    check(verbing('hail'), 'hailing')
    check(verbing('swiming'), 'swimingly')
    check(verbing('do'), 'do')

    print('not_bad')
    check(not_bad('This movie is not so bad'), 'This movie is good')
    check(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    check(not_bad('This tea is not hot'), 'This tea is not hot')
    check(not_bad("It's bad yet not"), "It's bad yet not")

    print('front_back')
    check(front_back('abcd', 'xy'), 'abxcdy')
    check(front_back('abcde', 'xyz'), 'abcxydez')
    check(front_back('Kitten', 'Donut'), 'KitDontenut')


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()