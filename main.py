#!interpreter [optional-arg]
# -*- coding: utf-8 -*-

import struct
import random
import timeit
import bitsort as bt
import seqbitsort as sq
import Cseqbitsort as csq


testlist = []
testlist1 = []
testlist2 = []
testlist3 = []
def timedSorted():
    sorted(testlist)
def timedBitSort():
    bt.bitsort(testlist1)
def timedsqBitSort():
    sq.bitsort(testlist2)
def timedcsqBitSort():
    csq.Bitsort(testlist3).sort()

def main():
    tlist = []
    for x in range(10000):
        tlist.append(random.uniform(-100000000000, 10000000000000))

    tlist.append(0.0)
    """for x in range(100000):
        tlist.append(random.randint(-1000000000, 1000000000))
    tlist.append(0)"""
    global testlist, testlist1, testlist2, testlist3
    testlist = tlist.copy()
    testlist1 = tlist.copy()
    testlist2 = tlist.copy()
    testlist3 = tlist.copy()

    
    print(timeit.timeit(timedSorted, number=10))
    print(timeit.timeit(timedBitSort, number=10))
    print(timeit.timeit(timedsqBitSort, number=10))
    print(timeit.timeit(timedcsqBitSort, number=10))

    testlist = sorted(testlist)
    testlist1 = bt.bitsort(testlist1)
    testlist2 = sq.bitsort(testlist2)
    testlist3 = csq.Bitsort(testlist3).sort()
    #print(flist)
    #print(testlist)
    #print(testlist1)
    #print(testlist2)
    #print(testlist3)

    if (testlist == testlist1):
        print("1: True")
    if (testlist == testlist2):
        print("2: True")
    if (testlist == testlist3):
        print("3: True")
        
if __name__ == "__main__":
    main()