#!/usr/bin/python
import sys

def reverse(text):
    res = ""
    for ch in text:
        res = ch + res
    return res

def reverse_using_lib(text):
    res = "".join(reversed(text))
    return res

try:
    print "Enter a string to be reversed"
    string = raw_input()
    if not string:
        print "Invalid input received, hence exiting from script !"
        sys.exit(-1)

    reversed_string = reverse(string)
    #reversed_string = reverse_using_lib(string)
    print "input: %s, reversed value: %s" %(string, reversed_string)

except Exception, ex:
    print "reverse_string: Exception: %s"%str(ex)
