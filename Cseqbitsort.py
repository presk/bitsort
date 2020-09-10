#!interpreter [optional-arg]
# -*- coding: utf-8 -*-

import struct
from collections import deque 

ascending = '0'
descending = '1'


class Bitsort:
    def __init__ (self, nlist):
        self.nlist = nlist.copy()
        slist = []
        for i in range(len(nlist)):
            slist.append(self.float2bin(nlist[i]))
        self.slist = slist
        self.oplist = deque()


    #Converts each float to a string of their 64 bit IEEE 754 big endian representation
    def float2bin(self, f):
        [d] = struct.unpack(">Q", struct.pack(">d", f))
        return f'{d:064b}'


    def swap(self, currentPos, swapPos):
        temp = self.nlist[swapPos]
        self.nlist[swapPos] = self.nlist[currentPos]
        self.nlist[currentPos] = temp

        temp = self.slist[swapPos]
        self.slist[swapPos] = self.slist[currentPos]
        self.slist[currentPos] = temp


    def sort(self):
        swapPos = 0
        for i in range(len(self.slist)):
            if self.slist[i][0] == descending:
                self.swap(i, swapPos)
                swapPos += 1
        self.oplist.append([0, swapPos-1, 1, descending])
        self.oplist.append([swapPos, len(self.slist)-1, 1, ascending])
        while self.oplist:
            op = self.oplist.pop()
            self.innersort(op[0], op[1], op[2], op[3])
        return self.nlist
    
    
    def innersort(self, start, end, bit, order):
        #Defines the first leftmost location of a non-ordered number i.e. where a number to be moved
        #gets to be placed without removing an already moved number
        swapPos = start
    
        #Checks if the current number's bit needs to be placed towards the left
        for i in range(start, end + 1):
            if self.slist[i][bit] == order: 
                #If the number should be moved towards the left and is not already in the leftmost position,
                #swap it with the current number in the leftmost position
                if not i == swapPos:
                    self.swap( i, swapPos)
                swapPos += 1
        #Checks for the edge case where all the bits are identical and not leftmost (all 0s, but 1 is leftmost)
        if swapPos == start:
            swapPos = end + 1
        #Execute recursively until you reach the last bit or until the sub-array's length is < 2
        if bit < len(self.slist[0])-1 :  
            if start < swapPos-1:
                self.oplist.append([start, swapPos-1, bit+1, order])
                #innersort(slist, start, swapPos-1, bit+1, order)

            if swapPos < end:
                self.oplist.append([swapPos, end, bit+1, order])
                #innersort(slist, swapPos, end, bit+1, order)
