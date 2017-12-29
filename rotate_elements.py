#!/usr/bin/python
import sys

def rotate_by_pos(list_elements, pos):
    res = list_elements[pos:] + list_elements[:pos]

try:
    print "Enter list elements"
    elements = raw_input()
    elements = [int(x) for x in elements.split()]
    if not elements:
        print "You have not entered list elements"
        sys.exit(-1)

    print "Entered elements = ", elements
    
    print "Enter Rotating postion"
    pos = raw_input()
    if not pos :
        print "postion is wrong"
        sys.exit(-1)

    pos = int(pos)
    if pos > len(elements):
        print "entered postion is larger than element size"
        sys.exit(-1)

    rotate_res = elements[pos:]+elements[:pos]
    print "After rotate %s" %str(rotate_res)

except Exception, ex:
    print "rotate_elements: Exeption: %s" %str(ex)
