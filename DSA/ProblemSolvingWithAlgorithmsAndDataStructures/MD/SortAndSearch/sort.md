# Sort

- [氣泡排序 The Bubble Sort](#the-bubble-sort)
- [選擇排序 The Selection Sort](#the-selection-sort)
- [插入排序 The Insertion Sort](#the-insertion-sort)
- [希爾排序 The Shell Sort](#the-shell-sort)
- [合併排序 The Merge Sort](#the-merge-sort)
- [快速排序 The Quick Sort](#the-quick-sort)
- [總結 Summary](#summary)

## The Bubble Sort

#### 概念

透過兩兩交換，每一輪將該輪的最大值放在正確的位置（像氣泡一樣浮上來）

1. 第`一`輪：把最大的放到最後一個
2. 第`二`輪：把次大的放到倒數第二個
3. ...
4. 第 `k` 輪：把第 `k` 大的放到後面數來第 k 個
5. ...

#### 實作

利用兩層迴圈：

- 外層：選定要比較的向量格數區間。例：第一層要比全部（前 `n` 個）、第二層只要比前 `n - 1` 個...
- 內層：兩兩比較，把較大的排在右邊。

#### 分析

1. 無論初始排序，都將進行 `n-1` 次遍尋，且每次遍尋，都需要 `n-k` 次比較。

| Pass（輪） | Comparisons（比較次數） | 解釋                        |
| ---------- | ----------------------- | --------------------------- |
| 1          | n - 1                   | 第一輪要進行 `n - 1` 次比較 |
| 2          | n - 2                   | 第二輪要進行 `n - 2` 次比較 |
| 3          | n - 3                   | 第三輪要進行 `n - 2` 次比較 |
| ...        | ...                     | ...                         |
| n-1        | 1                       | 第 `n-1`輪要進行 `1` 次比較 |

因此複雜度計算如下，結果為 `O(n^2)`。
$$
(n-1)+(n-2)+(n-3)+1=\frac{[(n-1)+1]\times(n-1)}{2}=\frac{n^2}{2}-\frac{n}{2}\sim O(n^2)
$$
而且上面的複雜度分析還沒包含`交換`的計算成本。

#### 其他

**氣泡搜尋**在遍尋的過程中，即使列表已被排序，但仍會繼續遍尋跟倆倆比較。所以若在某一次遍尋中發現都不用交換，那代表列表已經排好序，並停止排序，此方法稱作**短氣泡搜尋**。

#### 程式

- 氣泡搜尋

```python
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
    return alist
```

- 短氣泡搜尋

```python
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
```

## The Selection Sort

#### 概念

在每一次遍尋，不兩兩交換，而是紀錄最大的 index，並在該次遍尋結束後交換。因此每次遍尋只交換一次。

#### 分析

雖然複雜度仍為 `O(n)`，但因為交換次數減少，因此通常會比氣泡排序執行得更快。

#### 程式

```python
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
```

## The Insertion Sort

#### 概念

始終在列表的較低位置，維護一個已排好的子列表。

#### 實作

因此當欲將子列表的下一個值插入並排序時，依序從子列表的右向左比對，一但遇到比當前值小的，就停止交換，因為在接下來的值都會更小。

![](http://interactivepython.org/runestone/static/pythonds/_images/insertionsort.png)

#### 分析

複雜度為 `O(n^2)`。

#### 程式

```python
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
```

## The Shell Sort

**插入排序 (Insertion Sort)** 的改進版本。

#### 概念

將原始列表分解為多個子列表，各自進行插入排序後，最後再做一次完整的插入排序。

而怎麼選擇子列表是希爾排序的關鍵。不是將列表分為連續的子列表，而是使用**增量**（稱為 `gap`）的方式來選擇子列表。

#### 實作

![](http://interactivepython.org/runestone/static/pythonds/_images/shellsortA.png)

![](http://interactivepython.org/runestone/static/pythonds/_images/shellsortB.png)

#### 分析

乍看之下效果不會比插入排序來得好，因為在最後一步使用了完整的插入排序。

但實際上是最後的這個插入排序，並不用比較非常多次，因為前幾步的增量排序，讓此列表變得比原先的列表「更有序」。

複雜度的分析超出本文範圍，傾向落在 `O(n)` 和`O(n^2)` 之間。舉下面為例，複雜度為 `O(n^2)`，但透過改變增量，例如使用 `2^k - 1`，可以讓希爾排序的複雜度落在 `O(n^(3/2))`。

#### 程式

以下程式碼是使用間隔 `n//2`、`n//4`、...的方式來切割成不同子列表。在 `n//k = 1` 後，便是回到最原始的插入排序。

```python
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
```

## The Merge Sort

#### 概念

利用 **Divide and Conquer 分而治之** 依序向量分割成許多子向量，在子向量排序好後，再接著按順序大小合併。

- 分割

![](http://interactivepython.org/runestone/static/pythonds/_images/mergesortA.png)

- 合併

![](http://interactivepython.org/runestone/static/pythonds/_images/mergesortB.png)

#### 步驟

1. 先將向量對半切
2. 直到向量長度為 1 時，停止分割
3. 將左右向量按大小合併，最後合併成原先向量，排序完成。

#### 複雜度分析

`mergeSort` 由兩個部分組成

1. 列表被分割成兩半
   1. 將列表劃分的複雜度為 `log(n)`
2. 子向量合併
   1. 將大小為 `n` 的向量合併，需要 `n` 次操作（`n` 次比較後放入）
   2. 例：長度為 2 的向量，在切割成兩個長度為 1 的向量後，需要兩次操作才能排序。

複雜度為 `O(nlogn)`：每一次的切割要花 `log(n)` 的時間，切割完後都需要 `n` 次操作排序，因次將複雜度相乘所得。

#### 程式

```python
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

```

## The Quick Sort

#### 概念

使用分而治之將列表分割，分次進行 Quick Sort。

Quick Sort 是使用列表中的某一個數當作樞紐值，並分別從左和右，去和該樞紐值比較，若發現一但左側出現一個大於樞紐值的數，右側出現一個小於樞紐值的數，則兩數交換

並在最後將樞紐值移到正確的位置上。

![](http://interactivepython.org/runestone/static/pythonds/_images/partitionA.png)

#### 複雜度分析

若分區總是出現在列表中間，則會再次出現 `logn`，接著針對樞紐值檢查 n 個項目，那總複雜度會是 `nlogn`。

但最壞狀況是，分裂點不在中間，可能很偏左或右，那對列表進行劃分就會分成 `0` 個項和 `n-1`個項的列表（分裂點很偏左）進行排序。再加上列表排序的結果就會是複雜度 `O(n^2)` 。

#### 筆記

可以透過一些設計來挑選樞紐值，以降低分裂不均勻的機率。像是考慮列表中的第一個、中間和最後一個值。

#### 程式

```python
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
```

## Summary

- Bubble Sort：
  - 一句話：第 `k` 輪會將第 `k` 大的值排好。
  - 優缺點：直覺但效率差
  - 複雜度： `O(n^2)`
- Shell Sort：
  - 一句話：利用 `gap` 優化 Bubble Sort
  - 附註：`gap` 的設計很重要
  - 複雜度： `O(n)` ~ `O(n^2)`
- Merge Sort：
  - 一句話：分而治之得將子向量排序好後再合併
  - 優缺點：複雜度降低但需要額外空間儲存子向量。（在要合併的時候）
  - 複雜度： `O(nlogn)`
- Quick Sort：
  - 一句話：分而治之得以樞紐量為基準將向量分區。
  - 優缺點：複雜度降低且無需額外空間儲存。但若分割點不在列表中間附近，可能會讓複雜度降低到 `O(n)`。
  - 複雜度： `O(nlogn)`