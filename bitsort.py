import struct
import random
import timeit


ascending = '0'
descending = '1'
testlist = []
flist = []
slist = []

#Converts each float to a string of their 64 bit IEEE 754 big endian representation
#Taken from JavDomGom: https://stackoverflow.com/questions/16444726/binary-representation-of-float-in-python-bits-not-hex
def float2bin(f):
    [d] = struct.unpack(">Q", struct.pack(">d", f))
    return f'{d:064b}'

#Swaps two values in both the string representation array and actual float array
def swap(i, swapPos):
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
def innersort(slist, start, end, bit, order):
    #Defines the first leftmost location of a non-ordered number i.e. where a number to be moved
    #gets to be placed without removing an already moved number
    swapPos = start
    
    #Checks if the current number's bit needs to be placed towards the left
    for i in range(start, end + 1):
        if slist[i][bit] == order: 
            #If the number should be moved towards the left and is not already in the leftmost position,
            #swap it with the current number in the leftmost position
            if not i == swapPos:
                swap(i, swapPos)
            swapPos += 1
    #Checks for the edge case where all the bits are identical and not leftmost (all 0s, but 1 is leftmost)
    if swapPos == 0:
        swapPos = end + 1
    #Execute recursively until you reach the last bit or until the sub-array's length is < 2
    if bit < 63 :  
        if start < swapPos-1:
            innersort(slist, start, swapPos-1, bit+1, order)

        if swapPos < end:
            innersort(slist, swapPos, end, bit+1, order)




def bitsort(flist):
    #Split positive numbers from negative number and sets proper sorting order for each sub-array
    #Note that the sorting is done in aboslute value, as such negative numbers are ordered
    #from the biggest absolute values to the smallest vice versa for the positive numbers
    #e.g. -9, -8, 8, 9   absolute negatives: 9, 8 (descending order) 
    #                    absolute positive:  8, 9 (ascending order)
    swapPos = 0
    
    for i in range(len(flist)):
        slist.append(float2bin(flist[i]))
    for i in range(len(slist)):
        if slist[i][0] == descending:
            swap(i, swapPos)
            swapPos += 1
    #Sort the sub-array of negative numbers in descending order
    innersort(slist, 0, swapPos-1, 1, descending)
    #Sort the sub-array of positive numbers in ascending order
    innersort(slist, swapPos, len(slist)-1, 1, ascending)

def timedSorted():
    sorted(testlist)
def timedBitSort():
    bitsort(flist)
for x in range(10):
    flist.append(random.uniform(-100000000000, 1000000000000))

flist.append(0)
testlist = flist.copy()


print(timeit.timeit(timedSorted, number=1))
print(timeit.timeit(timedBitSort, number=1))


testlist = sorted(testlist)
#print(flist)
#print(testlist)
if flist == testlist:
    print("True")

