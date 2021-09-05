"""
MergeSort and InvesrionCount by piggybacking on MergeSort
"""

# for performance measure
import time

# this will count inversions
counts = 0


def merge(a, b):

    # global keyword here makes the "counts" variable global
    global counts

    c = list()
    i=0
    j=0
    lastelem_a = False
    lastelem_b = False

    for k in range(len(a)+len(b)):
        if lastelem_a:
            c.append(b[j])
            j = j+1
        elif lastelem_b:
            c.append(a[i])
            i = i+1
        elif a[i] <= b[j]:
            c.append(a[i])
            i = i + 1
            if i == len(a): lastelem_a = True
        elif b[j] < a[i]:
            c.append(b[j])
            j = j + 1
            counts = counts + len(a[i:])
            if j == len(b): lastelem_b = True

        else:
            print("myError")

    return c


def merge_sort(myList):

    if len(myList) == 1:
        return myList
    else:
        # mid_index = int(len(myList) / 2)
        mid_index_ = len(myList) // 2  # this will do the floor too in case of an odd list

        half1 = myList[:mid_index_]
        half2 = myList[mid_index_:]
        # the line below is quite interesting, but it works!
        return merge(merge_sort(half1), merge_sort(half2))

        # interestingly, this does not seem to work
        # merge_sort(half1)
        # merge_sort(half2)
        #
        # return merge(half1, half2)


if __name__ == '__main__':

    ##############################################################
    ### MergeSort testing ########################################
    ##############################################################

    a = (1, 2, 5, 7)
    b = (3, 4, 6, 8)
    # c = merge(a, b)
    # print(c)

    mylist = (10, 2, 2, 5, 7, 3, 4, 6, 6, 8, 12, 9, 11, 1, 13, 13)
    # print(merge_sort(mylist))

    ##############################################################
    ### MergeSort testing - END ##################################
    ##############################################################

    ##############################################################
    ### Inversion count by piggybacking on MergeSort #############
    ##############################################################

    # mylist2 = (4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46, 21, 39, 51, 7, 87, 99, 69, 62, 84, 6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 63, 97, 43, 45, 81, 42, 95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94, 90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77, 30, 22, 13, 29, 38, 16, 88, 61, 31, 85, 33, 54)
    # merge_sort(mylist2)
    # print(counts)

    # read the file as a list of integers
    myListFromFile = list()
    f = open("inversions_IntegerArray.txt", "r")
    for line in f:
        myListFromFile.append(int(line))
    f.close()

    # measrue time
    tic = time.time()
    # count inversions by piggybacking on merge_sort
    merge_sort(myListFromFile)
    toc = time.time()

    # report
    print("number of inversions is: ".format(counts))
    print("time it took: {} seconds".format(toc-tic))
