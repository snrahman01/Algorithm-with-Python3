def binarySearch(alist, value):

    first = 0
    last = len(alist)-1
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2
        if value == alist[midpoint]:
            found =  True
        else:
            if value < alist[midpoint]:
                last = midpoint-1
            else:
                if value > midpoint:
                    first = midpoint+1
    return found

if binarySearch([1,2,3,4,5,6,7,8],0):
    print ("found")