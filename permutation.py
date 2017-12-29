#!/usr/bin/python
from itertools import permutations

def permutation_using_lib_fun(string):
    res = [ "".join(p) for p in permutations(string)]
    return res

try:
    print "Enter a string to print in all permutation"
    inp = raw_input()
    res = permutation_using_lib_fun(inp)
    print res

except Exception, ex:
     print "Permutaion: Exception: %s" %str(ex)
