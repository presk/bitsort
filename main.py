import struct
import random
import timeit
import copy
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
    for x in range(100000000):
        tlist.append(random.uniform(-10000, 10000))

    tlist.append(0)
    testlist = tlist.copy()
    testlist1 = tlist.copy()
    #testlist2 = tlist.copy()
    #testlist3 = tlist.copy()

    print(timeit.timeit(timedSorted, number=1))
    print(timeit.timeit(timedBitSort, number=1))
    #print(timeit.timeit(timedsqBitSort, number=1))
    #print(timeit.timeit(timedcsqBitSort, number=1))
    #testlist = sorted(testlist)
    #bt.bitsort(testlist1)
    #testlist2 = sq.bitsort(testlist2)
    #testlist3 = csq.Bitsort(testlist3).sort()
    #print(flist)
    #print(testlist)
    #print(testlist1)
    #print(testlist2)
    #print(testlist3)

if __name__ == "__main__":
    main()