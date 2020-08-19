import struct
import random
import threading
import timeit

ascending = '0'
descending = '1'
threads = []
testlist = []
flist = []
c = 0

def float2bin(f):
    [d] = struct.unpack(">Q", struct.pack(">d", f))
    return f'{d:064b}'

def swap(slist, i, swapPos):
    temp = flist[swapPos]
    flist[swapPos] = flist[i]
    flist[i] = temp

    temp = slist[swapPos]
    slist[swapPos] = slist[i]
    slist[i] = temp

def innersort(slist, start, end, bit, order):
    swapPos = start

    for i in range(start, end + 1):
        if slist[i][bit] == order: 
            if not i == swapPos:
                swap(slist, i, swapPos)
            if swapPos <= end:
                swapPos += 1
    if swapPos == 0:
        swapPos = end + 1
    if bit < 63 :  #set to 63 for 64bit float
        if start < swapPos-1:
            innersort(slist, start, swapPos-1, bit+1, order)
            #x = threading.Thread(target = innersort, args=(slist, start, swapPos-1, bit+1, order))
            #threads.append(x)
            #x.start()
        if swapPos < end:
            innersort(slist, swapPos, end, bit+1, order)
            #y = threading.Thread(target = innersort, args=(slist, swapPos, end, bit+1, order))
            #threads.append(y)
            #y.start()



def bitsort(flist):
    #Split positive numbers from negative number
    swapPos = 0
    slist = []
    for i in range(len(flist)):
        slist.append(float2bin(flist[i]))
    for i in range(len(slist)):
        if slist[i][0] == descending:
            swap(slist, i, swapPos)
            swapPos += 1
    #x = threading.Thread(target = innersort, args=(slist, 0, swapPos-1, 1, descending))
    #y = threading.Thread(target = innersort, args=(slist, swapPos, len(slist)-1, 1, ascending))
    #threads.append(x)
    #threads.append(y)
    #x.start()
    #y.start()
    innersort(slist, 0, swapPos-1, 1, descending)
    innersort(slist, swapPos, len(slist)-1, 1, ascending)
    for t in threads:
        t.join()
    #for s in slist:
        #print(s)
def timedSorted():
    sorted(testlist)
def timedBitSort():
    bitsort(flist)

for x in range(1000):
    flist.append(random.uniform(-100000000000, 1000000000000))

#print(flist)
testlist = flist.copy()

print(timeit.timeit(timedSorted, number=1))
print(timeit.timeit(timedBitSort, number=1))
"""bitsort(flist)
testlist = sorted(testlist)

if flist == testlist:
    print("True")"""

