#!/usr/bin/python
import sys
class StringManipulation():
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

    def find_and_replace(self):
        res = self.s2
        for ch in self.s1:
            res = res.replace(ch, '')
        return res

try:
    errors = []
    print "Enter string S1"
    s1 = raw_input()

    print "Enter string S2"
    s2 = raw_input()

    if not s1 or not isinstance(s1, str):
        errors.append("Invalid S1 provided, string expected")

    if not s2 or not isinstance(s2, str):
        errors.append("Invalid S2 provided, sring expected")

    if errors:
        print "\n".join(errors)
        sys.exit(-1)

    string_manipulation = StringManipulation(s1, s2)
    result = string_manipulation.find_and_replace()
    print "S1 = %s, S2 = %s, replaced_string = %s" %(s1, s2, result) 

except Exception, ex:
    print "create_clean_string: Exception: %s" %str(ex)
