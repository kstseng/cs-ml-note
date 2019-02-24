def sequentialSearch(alist, item):
    """
    alist [1, 4, 20, 5]
    item = 4
    """
    found = False
    pos = 0
    ## 按順序從頭開始找
    while not found and pos < len(alist):
        if alist[pos] == item:
            found = True
        else:
            pos += 1
    
    return found

def orderedSequentialSearch(alist, item):
    """
    """
    pos = 0
    found = False
    stop = False
    while not found and pos < len(alist) and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                ## 因為 list 是小到大排序，因此當 alist[pos] 大於 item
                ## 那在後面也不會出現 item
                stop = True
            else:
                pos += 1
    
    return found

def binarySearch(alist, item):
    """
    alist = [1, 2, 3, 10, 20, 25, 30]
    item = 11
    binarySearch(alist, item)
    """
    first_idx = 0
    last_idx = len(alist) - 1
    found = False

    ## 當 last 和 first 是隔壁（中間無數值）且 not found
    while (last_idx - first_idx) > 1 and not found:
        ## 定義如何取 middle_idx
        middle_idx = (last_idx - first_idx) // 2 + first_idx
        if alist[middle_idx] == item:
            found = True
        else:
            if alist[middle_idx] > item:
                last_idx = middle_idx
            else:
                first_idx = middle_idx
    return found

def binarySearchDivideAndConquer(alist, item):
    """
    """
    if len(alist) == 0: 
        return False
    else:
        mid_idx = len(alist) // 2
        if alist[mid_idx] == item:
            return True
        else:
            if alist[mid_idx] > item:
                ## 不用包含 mid_idx
                return binarySearchDivideAndConquer(alist[:mid_idx], item)
            else:
                ## 不用包含 mid_idx
                return binarySearchDivideAndConquer(alist[mid_idx + 1:], item)


def main():
    alist = [1, 2, 3, 10, 20, 25, 30]
    item = 11
    print(binarySearch(alist, item))
    print(binarySearchDivideAndConquer(alist, item))

