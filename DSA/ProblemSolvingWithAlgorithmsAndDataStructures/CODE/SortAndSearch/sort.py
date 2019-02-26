## Bubble Sort
def bubbleSort(alist):
    """
    氣泡排序
    """
    len_loop = len(alist)
    while len_loop > 1:
        ## while 的第 1 輪會把最大的歸位（排在最後面）
        ## while 的第 2 輪會把次大的歸位（排在倒數第二）
        ## ...
        ## 附註：第 k 輪只需檢查前 n - (k - 1) 個元素
        for idx in range(len_loop - 1): # 0, ..., len_loop - 1
            if alist[idx] > alist[idx + 1]:
                ## 交換!
                ## 把值存到一個變數，再交換
                tmp = alist[idx]
                alist[idx] = alist[idx + 1]
                alist[idx + 1] = tmp
        ## 下一輪可以少檢查一次，逐次遞減
        len_loop -= 1        

def shortBubbleSort(alist):
    """
    短氣泡搜尋

    起因：如果在遍尋的期間都沒有交換，代表當下其實列表已經排序，便可以停止遍尋
    """
    ## 初始 exchange 為 True
    exchange = True
    len_loop = len(alist)
    while len_loop > 1 and exchange:
        ## 先假設是排序
        exchange = False
        for idx in range(len_loop - 1):
            ## 一但發現要加換，那便代表此列表尚未排序完全
            exchange = True
            if alist[idx] > alist[idx + 1]:
                tmp = alist[idx]
                alist[idx] = alist[idx + 1]
                alist[idx + 1] = tmp
        len_loop -= 1

## Selection Sort
def selectionSort(alist):
    """
    選擇排序
    """
    len_loop = len(alist)
    exchange_cnt = 0
    while len_loop > 1:
        ## 不交換，而是指紀錄最大值的指標
        ## 初始 index 為 0
        idx_argmax = 0
        for idx in range(1, len_loop):
            if alist[idx] > alist[idx_argmax]:
                idx_argmax = idx
        ## 若最大值的指標不在最後一個
        ## 則進行交換
        if idx_argmax != (len_loop - 1):
            max_value = alist[idx_argmax]
            alist[idx_argmax] = alist[len_loop - 1]
            alist[len_loop - 1] = max_value
        ##
        len_loop -= 1

## Insertion Sort
def insertionSort(alist):
    """
    插入排序
    """
    for i in range(len(alist)):
        stop = False
        current_idx = i
        comparison_idx = i - 1
        while comparison_idx >= 0 and not stop:
            if alist[current_idx] > alist[comparison_idx]:
                ## 如果當前值比前一個大，那就結束
                ## 因為更前面的都是排序過的
                stop = True
            else:
                ## 交換
                tmp = alist[comparison_idx]
                alist[comparison_idx] = alist[current_idx]
                alist[current_idx] = tmp
                ## index 也要跟著移動
                current_idx = comparison_idx
                comparison_idx -= 1      

## Shell Sort
def shellSort(alist):
    """
    先和距離 n // 2 的進行 insertionSort
    再和距離 n // 4 的進行 insertionSort
    ...

    """
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startpoint in range(sublistcount):
            gapInsertionSort(alist, startpoint, sublistcount)
        print("After increments of size: {}".format(sublistcount))
        print("      The list is {}".format(alist))
                                   
        sublistcount = sublistcount // 2


def gapInsertionSort(alist, start, gap):
    """
    insertionSort 的一般化版本：
        可以和彼此距離 gap 的元素進行 insertionSort
    """
    for i in range(start + gap, len(alist), gap):
        current_idx = i
        comparison_idx = i - gap
        while comparison_idx >= 0 and alist[comparison_idx] > alist[current_idx]:
            ## 交換
            temp = alist[comparison_idx]
            alist[comparison_idx] = alist[current_idx]
            alist[current_idx] = temp
            ## index 跟著動
            current_idx = comparison_idx
            comparison_idx -= gap

## Merge Sort
def mergeSort(alist):
    """
    Divide and Conquer
    """
    if len(alist) > 1:
        print('Splitting: {}'.format(alist))
        ## 分割並且再次呼叫 mergeSort 函數
        midpoints = len(alist) // 2
        sublist_l = alist[:midpoints]
        sublist_r = alist[midpoints:]
        print('            into: {} and {}'.format(sublist_l, sublist_r))
        ## [Recursion]
        ## 想像 base case 來幫助理解
        ## 若 sublist_l 的長度是 2
        ## 則下一步的 mergeSort 不會被調用
        ## 接著就處理長度是 2 的 mergeSort
        mergeSort(sublist_l)
        mergeSort(sublist_r)
        ## 想像 alist 長度為 2
        ## 因此 sublist_l 和 sublist_r 長度都為 1
        ## 同理，當長度為 4 時也一樣
        ## 並且此時的 sublist_l 和 sublist_r 都排好序
        print('Merge: {} and {}'.format(sublist_l, sublist_r))
        left_idx = 0
        right_idx = 0
        alist_idx = 0
        while left_idx < len(sublist_l) and right_idx < len(sublist_r):
            ## 當 left_idx 和 right_idx 都還在向量長度內
            if sublist_l[left_idx] < sublist_r[right_idx]:
                ## 若 left_idx 所屬的值較大，則將此值填到 alist 中
                alist[alist_idx] = sublist_l[left_idx]
                left_idx += 1
            else:
                ## 若 right_idx 所屬的值較大，則將此值填到 alist 中
                alist[alist_idx] = sublist_r[right_idx]
                right_idx += 1
            ## 往下看 alist 的下一個 index
            alist_idx += 1
        while left_idx < len(sublist_l):
            ## 當右邊的都填完了，而左邊的還有剩，就把左邊剩下的依序填入 alist
            alist[alist_idx] = sublist_l[left_idx]
            alist_idx += 1
            left_idx += 1
        while right_idx < len(sublist_r):
            ## 當左邊的都填完了，而右邊的還有剩，就把右邊剩下的依序填入 alist
            alist[alist_idx] = sublist_r[right_idx]
            alist_idx += 1
            right_idx += 1
        print("            into {}".format(alist))

## Quick Sort
def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)

def quickSortHelper(alist, first, last):
    """
    Divide and Conquer
    """
    if first < last:
        ## 先找出當前 alist 以第一個值為 pivotvalue 的分割點
        splitpoint = partition(alist, first, last)
        ## 在針對分割後左邊的 list 和 右邊的 list，再次進行 quickSort
        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)

def partition(alist, first, last):
    """
    為 alist 尋找以第一個值為 pivotvalue 的分割點
    以及將小於 pivotvalue 的放在 pivotvalue 的左邊
    大於 pivotvalue 的放在 pivotvalue 的右邊
    """
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            ## 從左邊找到一個大於 pivotvalue 的值，並把 mark 移到該指標
            leftmark += 1
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            ## 從右邊邊找到一個小於 pivotvalue 的值，並把 mark 移到該指標
            rightmark -= 1
        
        if rightmark <= leftmark:
            ## 當左指標往右邊遞增，右指標往左邊遞減達到上述條件後
            ## 右指標在左指標的左側，那代表這次尋找沒有意義，已經結束
            done = True
        else:
            ## 若找到左指標小於右指標的前提下
            ## 且存在左指標的值大於 pivotvalue 且
            ## 右指標的值小於 pivotvalue
            ## 則這兩個值互換位置
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
    ## 當完成後，把 pivotvalue 移到正確的位置上
    ## 使得在 pivotvalue 左邊的值都小於 pivotvalue
    ## 在 pivotvalue 右邊的值都大於 pivotvalue
    ## 而此位置也就是當前的 first 的位置
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark

def main():
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    #bubbleSort(alist)
    #shortBubbleSort(alist)
    #selectionSort(alist)
    #insertionSort(alist)
    #gapInsertionSort(alist, 0, 1)
    #shellSort(alist)
    #mergeSort(alist)
    quickSort(alist)
    print(alist)

main()