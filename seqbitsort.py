#!interpreter [optional-arg]
# -*- coding: utf-8 -*-

import struct
from collections import deque 


ascending = '0'
descending = '1'


#Converts each float to a string of their 64 bit IEEE 754 big endian representation
def float2bin(f):
    [d] = struct.unpack(">Q", struct.pack(">d", f))
    return f'{d:064b}'

#Swaps two values in both the string representation array and actual float array
def swap(i, swapPos, flist, slist):
    temp = flist[swapPos]
    flist[swapPos] = flist[i]
    flist[i] = temp

    temp = slist[swapPos]
    slist[swapPos] = slist[i]
    slist[i] = temp

#Recursive function that sorts subsections of arrays depending on which bit is selected
#   0111111101010101010101010101010101010101010101010101010101010101
#    ^                                                             ^
#   highest weight bit, is sorted first                lowest weight bit, sorted last  
#
#
# note1: the leftmost bit is the sign bit 
# note2: Python does not have tail call optimization (TODO: find a sequential/iterative solution)                         
def innersort(start, end, bit, order, flist, slist, oplist):
    #Defines the first leftmost location of a non-ordered number i.e. where a number to be moved
        #gets to be placed without removing an already moved number
        swapPos = start
    
        #Checks if the current number's bit needs to be placed towards the left
        for i in range(start, end + 1):
            if slist[i][bit] == order: 
                #If the number should be moved towards the left and is not already in the leftmost position,
                #swap it with the current number in the leftmost position
                if not i == swapPos:
                    swap( i, swapPos, flist, slist)
                swapPos += 1
        #Checks for the edge case where all the bits are identical and not leftmost (all 0s, but 1 is leftmost)
        if swapPos == start:
            swapPos = end + 1
        #Execute recursively until you reach the last bit or until the sub-array's length is < 2
        if bit < len(slist[0])-1 :  
            if start < swapPos-1:
                oplist.append([start, swapPos-1, bit+1, order])
                #innersort(slist, start, swapPos-1, bit+1, order)

            if swapPos < end:
                oplist.append([swapPos, end, bit+1, order])
                #innersort(slist, swapPos, end, bit+1, order)




def bitsort(floatList):
    #Split positive numbers from negative number and sets proper sorting order for each sub-array
    #Note that the sorting is done in aboslute value, as such negative numbers are ordered
    #from the biggest absolute values to the smallest vice versa for the positive numbers
    #e.g. -9, -8, 8, 9   absolute negatives: 9, 8 (descending order) 
    #                    absolute positive:  8, 9 (ascending order)
    swapPos = 0
    flist = floatList.copy()
    slist = []
    oplist = deque()
    for i in range(len(flist)):
        slist.append(float2bin(flist[i]))
    for i in range(len(slist)):
        if slist[i][0] == descending:
            swap(i, swapPos, flist, slist)
            swapPos += 1
    oplist.append([0, swapPos-1, 1, descending])
    oplist.append([swapPos, len(slist)-1, 1, ascending])
    while oplist:
        op = oplist.pop()
        innersort(op[0], op[1], op[2], op[3], flist, slist, oplist)
    return flist

