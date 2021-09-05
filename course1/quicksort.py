"""
QuickSort Algorithm and the related swab counting
"""

count = 0
root = True


def swap(array, a:int, b:int):
    temp = array[b]
    array[b] = array[a]
    array[a] = temp


def partition(A, left: int, right: int):
    global count
    # if pivot != 0:
    pivot = A[left]
    i = left + 1

    for j in range(left+1, right+1):
        if A[j] < pivot:
            swap(A, i, j)
            i = i+1
    swap(A, left, i-1)

    return A, i


def quicksort(myarray, left, right):

    tmp_array = myarray[left:right+1]

    if right <= left: return

    # pick pivot betweeen 3 of them as a median
    pivot1 = myarray[left]
    pivot2 = myarray[right]

    if len(tmp_array) % 2 != 0:
        mid = (len(tmp_array) // 2) + 1
    else:
        mid = int(len(tmp_array) / 2)
    pivot3 = tmp_array[mid-1]
    pivot = (sorted((pivot1, pivot2, pivot3)))[1]

    swap(myarray, left, pivot-1)
    myarray, position = partition(myarray, left, right)

    # that's a perticular way of counting swabs required by the course Algorithms at Stanford
    global count
    count = count + len(tmp_array) - 1

    quicksort(myarray, left, position-2)
    quicksort(myarray, position, right)


if __name__ == '__main__':
    # mylist = [2, 20, 1, 15, 3, 11, 13, 6, 16, 10, 19, 5, 4, 9, 8, 14, 18, 17, 7, 12]
    # # mylist = [3, 1, 2]
    # quicksort(mylist, 0, len(mylist)-1)
    # print(mylist)
    # print(count)

    myListFromFile = list()
    f = open("QuickSort.txt", "r")
    for line in f:
        myListFromFile.append(int(line))
    f.close()

    quicksort(myListFromFile, 0, len(myListFromFile)-1)
    print(myListFromFile)
    print(count)
