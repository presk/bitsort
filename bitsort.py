#!interpreter [optional-arg]
# -*- coding: utf-8 -*-

import struct
import math
#import threading


ascending = '0'
descending = '1'


#Converts each float to a string of their 64 bit IEEE 754 big endian representation
#Or converts each int to a string of bits with compacted length
def num2bin(nlist):
    slist = []
    #Checks if the array is all floats
    if all(isinstance(x, float) for x in nlist):
        for f in nlist:
            [d] = struct.unpack(">Q", struct.pack(">d", f))
            slist.append(f'{d:064b}')
        return slist
    
    #Checks if the array is all integers
    if all(isinstance(x, int) for x in nlist):
        #Finds the biggest absolute integer to find the smallest possible bit length and adds 1 for the sign representation
        max = abs(nlist[0])
        for i in range (len(nlist)):
            if abs(nlist[i]) > max:
                max = abs(nlist[i])
        count = math.ceil(math.log2(max)) + 1
        i = 0
        for n in nlist:
            slist.append("{0:{fill}{bitcount}b}".format(n, fill='0', bitcount=count))
            #Converts the negative into a 1 bit to match float representation
            if slist[i][0] == "-":
                slist[i] = "1" + slist[i][1:]
            i += 1
        return slist
#Swaps two values in both the string representation array and actual float array
def swap(i, swapPos, nlist, slist):
    temp = nlist[swapPos]
    nlist[swapPos] = nlist[i]
    nlist[i] = temp

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
                         
def innersort(nlist, slist, start, end, bit, order):
    #Defines the first leftmost location of a non-ordered number i.e. where a number to be moved
    #gets to be placed without removing an already moved number
    swapPos = start
    
    #Checks if the current number's bit needs to be placed towards the left
    for i in range(start, end + 1):
        if slist[i][bit] == order: 
            #If the number should be moved towards the left and is not already in the leftmost position,
            #swap it with the current number in the leftmost position
            if not i == swapPos:
                swap(i, swapPos, nlist, slist)
            swapPos += 1
    #Checks for the edge case where all the bits are identical and not leftmost (all 0s, but 1 is leftmost)
    if swapPos == start:
        swapPos = end + 1
    #Execute recursively until you reach the last bit or until the sub-array's length is < 2
    if bit < len(slist[0])-1 :  
        if start < swapPos-1:
            innersort(nlist, slist, start, swapPos-1, bit+1, order)

        if swapPos < end:
            innersort(nlist, slist, swapPos, end, bit+1, order)





def bitsort(ilist):
    #Split positive numbers from negative number and sets proper sorting order for each sub-array
    #Note that the sorting is done in aboslute value, as such negative numbers are ordered
    #from the biggest absolute values to the smallest vice versa for the positive numbers
    #e.g. -9, -8, 8, 9   absolute negatives: 9, 8 (descending order) 
    #                    absolute positive:  8, 9 (ascending order)
    swapPos = 0
    nlist = ilist.copy()
    slist = []
    #threads = []
    slist = num2bin(nlist)
    for i in range(len(slist)):
        if slist[i][0] == descending:
            swap(i, swapPos, nlist, slist)
            swapPos += 1

    #Sort the sub-array of negative numbers in descending order
    innersort(nlist, slist, 0, swapPos-1, 1, descending)
    """x = threading.Thread(target = innersort, args=(nlist, slist, 0, swapPos-1, 1, descending,))
    threads.append(x)
    x.start()"""

    #Sort the sub-array of positive numbers in ascending order
    innersort(nlist, slist, swapPos, len(slist)-1, 1, ascending)
    """y = threading.Thread(target = innersort, args=(nlist, slist, swapPos, len(slist)-1, 1, ascending,))
    threads.append(y)
    y.start()"""

    #Note: Threading only seem to improve performance for ~ n > 10000
    """for t in threads:
        t.join()"""
    return nlist


