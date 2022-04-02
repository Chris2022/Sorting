import random
import math
from timeit import repeat
import sys
# Changing the recursion limit to be 20,000 instead of the default 1000
sys.setrecursionlimit(20000)


def run_sorting_algorithm(algorithm, array):
    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the
    # algorithm function if it's not the built-in `sorted()`.
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")


def GenerateList(n):
    randomList = []
    for i in range(0, n):
        x = random.randint(0, n)
        randomList.append(x)
    return randomList


BubbleCount = 0


def Bubble_Sort(randlist):
    global BubbleCount
    length = len(randlist)
    for i in range(length-1):
        for j in range(0, length-i-1):
            BubbleCount += 1
            if randlist[j] > randlist[j+1]:
                temp = randlist[j]
                randlist[j] = randlist[j+1]
                randlist[j+1] = temp
    return randlist


SelectionCounter = 0


def Selection_Sort(numList):
    # iterate through list
    for i in range(len(numList)-1):
        # obtain the smallest index
        minIndex = findMin(numList, i)
        # hold the current value in a temp variable
        temp = numList[i]
        # assign the value in the list at min index to the list at index i
        numList[i] = numList[minIndex]
        # then assign the temp variable to the list at min index
        numList[minIndex] = temp
    return numList

# method to find the minimum value in a list
# used in selection sort
def findMin(numList, k):
    global SelectionCounter
    # hold the min value from the list at index k
    minVal = numList[k]
    # hold the minimum index in a variable
    minLoc = k
    # assume the value at index k is the smallest
    # so itereate throught the list starting at k+1 till the end
    for i in range(k+1, len(numList)):
        SelectionCounter += 1
        # if the value at index i in the list is less than min value we stored
        if numList[i] < minVal:
            # update the min value
            minVal = numList[i]
            # update the min index
            minLoc = i
    # return the min index
    return minLoc


InsertionCounter = 0


def Insertion_Sort(numList):
    global InsertionCounter
    # We assume that the first element is sorted
    # so we iterate starting from the second element till the end
    for i in range(1, len(numList)):
        # store the value from the list at index i
        x = numList[i]
        # j is a pointer to the previous element, where we should start comparing
        j = i-1
        # while we are still in bounds and the element at index j is greater than x
        while j >= 0 and numList[j] > x:
            # We shift the elements to the right by 1
            numList[j+1] = numList[j]
            # Decrement j by 1
            j -= 1
            InsertionCounter += 1
        # insert the value saved in x into the right location
        numList[j+1] = x
    return numList

# I didn't want the counter variable for the insertion sort to be counted more 
# so decided to have tim sort use its own insertion sort


def InsertionForTimSort(numList):
    global TimCount
    for i in range(1, len(numList)):
        x = numList[i]
        j = i-1
        while j >= 0 and numList[j] > x:
            numList[j+1] = numList[j]
            j -= 1
            TimCount += 1
        numList[j+1] = x
    return numList


def Merge_Sort(numList):
    # if there is 1 element or 0, list is sorted
    if len(numList) == 1:
        return numList
    else:
        # if there is more than 1 element, obtain the midpoint
        midpoint = math.floor(len(numList)/2)
        # Then make a recursive call to Merger_Helper to divide the list into lists
        # of a single element and then return the ordered combined list
        return Merge_Helper(Merge_Sort(numList[:midpoint]), Merge_Sort(numList[midpoint:]))


MergeCounter = 0


def Merge_Helper(left, right):
    global MergeCounter
    global TimCount
    # The merged list
    Merged_Array = []
    i = 0
    j = 0
    # while there are elements in both lists
    while i < len(left) and j < len(right):
        # if the item from the left list is less than the item on the right list
        # add the item on the left then increment i
        if left[i] < right[j]:
            MergeCounter += 1
            TimCount += 1
            Merged_Array.append(left[i])
            i = i + 1
        # in case the item on the right list is smaller
        # add the right element and increment j
        else:
            Merged_Array.append(right[j])
            j = j + 1
    # If reached the end of the left list
    # add everything that is from the right list
    # then increment i
    while i < len(left):
        Merged_Array.append(left[i])
        i = i + 1
    # if reached the end of the right list
    # add everything that is from the left list then increment j
    while j < len(right):
        Merged_Array.append(right[j])
        j = j + 1
    return Merged_Array


QuickSortCounter = 0


def Quick_Sort(numList):
    global QuickSortCounter
    # Allows us to skip over list that have a single item
    if len(numList) <= 1:
        return numList
    else:
        # pop the last element and save it
        pivot = numList.pop()
    # creating list to hold values smaller than pivot
    smaller = []
    # creating list to hold values bigger than the pivot
    bigger = []
    # now go through the rest of unordered list
    # and append to either bigger or smaller list
    # depending on if the element is greater than or less than the pivot
    for element in numList:
        if element > pivot:
            QuickSortCounter += 1
            bigger.append(element)
        else:
            smaller.append(element)
    # Here I am telling the algorithm to apply Quick sort method on
    # the smaller list and we should have the pivot in the middle
    # and then apply the quick sort algorithm on the bigger list
    return Quick_Sort(smaller) + [pivot] + Quick_Sort(bigger)


RUN = 32  # Number I am incrementing by
TimCount = 0


def Tim_Sort(numList):
    # This first for loop is where I split the list passed in
    # I split it based on the RUN value
    # I then call insertion sort on that sub list and update the values in the original list
    for x in range(0, len(numList), RUN):
        numList[x:x+RUN] = InsertionForTimSort(numList[x: x + RUN])
    # I store the value of RUN as I will be changing it later
    size = RUN
    # while the size is less than the list
    while size < len(numList):
        # I begin the process of merging the sub sorted lists until I finally obtain a large list
        for x in range(0, len(numList), 2 * size):
            # I use my merge helper function to merge the sub lists together
            numList[x: x + 2 * size] = Merge_Helper(numList[x: x + size], numList[x + size: x + 2 * size])
        size = size * 2
    return numList


def main():
    num = int(input("Enter a number:"))
    array = [random.randint(0, num) for i in range(num)]
    randone = GenerateList(num)
    randtwo = GenerateList(num)
    randthree = GenerateList(num)
    randfour = GenerateList(num)
    randfive = GenerateList(num)
    randsix = GenerateList(num)

    # Bubble Sort
    print("\nUnordered List of Random Numbers:")
    for number in randone:
        print(number, end=" ")
    print("\n" + "Sorted Array by using Bubble Sort:")
    for bubble in Bubble_Sort(randone):
        print(bubble, end=" ")
    print("\n" + str(BubbleCount) + " comparisons made by using Bubble Sort")
    run_sorting_algorithm(algorithm="Bubble_Sort", array=randone)

    # Selection Sort
    print("\nUnordered List of Random Numbers:")
    for number in randtwo:
        print(number, end=" ")
    print("\n" + "Sorted Array by using Selection Sort:")
    for select in Selection_Sort(randtwo):
        print(select, end=" ")
    print("\n" + str(SelectionCounter) + " comparisons made by using Selection Sort")
    run_sorting_algorithm(algorithm="Selection_Sort", array=randtwo)

    # Insertion Sort
    print("\nUnordered List of Random Numbers:")
    for number in randthree:
        print(number, end=" ")
    print("\n" + "Sorted Array by using Insertion Sort:")
    for insert in Insertion_Sort(randthree):
        print(insert, end=" ")
    print("\n" + str(InsertionCounter) + " comparisons were made by using Insertion Sort")
    run_sorting_algorithm(algorithm="Insertion_Sort", array=array)

    # Merge Sort
    print("\nUnordered List of Random Numbers:")
    for number in randfour:
        print(number, end=" ")
    print("\n" + "Sorted Array by using Merge Sort:")
    for merged in Merge_Sort(randfour):
        print(merged, end=" ")
    print("\n" + str(MergeCounter) + " comparisons made by using Merge Sort")
    run_sorting_algorithm(algorithm="Merge_Sort", array=randfour)

    # Tim Sort
    print("\nUnordered List of Random Numbers:")
    for number in randfive:
        print(number, end=" ")
    print("\n" + "Sorted Array by using Tim  Sort:")
    for tim in Tim_Sort(randfive):
        print(tim, end=" ")
    print("\n" + str(TimCount) + " comparisons made by using Tim Sort")
    run_sorting_algorithm(algorithm="Tim_Sort", array=randfive)

    # Quick Sort
    print("\nUnordered List of Random Numbers:")
    for number in randsix:
        print(number, end=" ")
    print("\n" + "Sorted Array by using Quick Sort:")
    for quick in Quick_Sort(randsix):
        print(quick, end=" ")
    print("\n" + str(QuickSortCounter) + " comparisons made by using Quick Sort")
    run_sorting_algorithm(algorithm="Quick_Sort", array=randsix)


if __name__ == '__main__':
    main()

