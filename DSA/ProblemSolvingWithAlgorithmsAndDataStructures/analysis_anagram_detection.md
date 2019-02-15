# Analysis

## Outline

* [Code](#code)
    * [Anagram Detection](#anagram-detection)
        * [Solution 1: Checking Off](#checking-off)
        * [Solution 2: Sort and Compare](#sort-and-compare)
        * [Solution 3: Brute Force](#brute-force)
        * [Solution 4: Count and Compare](#count-and-compare)

### Code

[code in github](https://github.com/kstseng/dsa-ml-tool-note/blob/master/DSA/ProblemSolvingWithAlgorithmsAndDataStructures/CODE/Analysis/anagram_detection.py)

#### Anagram Detection

亂序字串檢查

##### Checking Off

```python
def anagramSolution1(s1, s2):
    """ Solution 1: Checking Off

    概念：
        1. 對每一個存在於 s1 的字，去檢查是否在 s2 出現 (兩層 for loop)
        2. 若有出現，便把 s2 該位置的字，取代為 None (因為此次配對是不只要出現，數量也要一樣，取代為 None 才不會重複計算)
        3. 一但發現找不到，則 break 第一層 while

    複雜度：
        最壞 (但找得到) 的狀況是 s1 = 'abcde', s1 = 'edcba'
        則此方法會需要 5 + 4 + 3 + 2 + 1 次搜尋，亦即 n (n + 1) / 2，複雜度為 O(n^2)

    """
    ## 字串向量化，因為字串在 python 是 immutable
    s1_list = list(s1)
    s2_list = list(s2)

    ## 初始化
    stillOK = True
    s1_start_idx = 0
    ## 第一層 for loop (s1)
    while stillOK and s1_start_idx < len(s1_list):
        s2_start_idx = 0
        found = False
        ## 第二層 for loop (s2)
        while s2_start_idx < len(s2_list) and not found:
            if s1_list[s1_start_idx] == s2_list[s2_start_idx]:
                ## 當找到後，設定 found 為 True，並把 s2 的該 element 取代為 None
                found = True
                s2_list[s2_start_idx] = None
            else:
                ## 沒到到，則在 s2 中繼續往下找
                s2_start_idx += 1

        ## 當尋遍 s2 的過程結束後（"找到" 或是 "尋遍 s2"）
        if found:
            ## 如果是找到，則繼續往 s1 的下個 element 再做一次
            s1_start_idx += 1
        else:
            ## 對第一層 break 
            stillOK = False
        
    
    ## 檢查是否 s2 都已全被取代為 None (因為可能存在長度不依的狀況)
    isS2AllNone = sum([ele == None for ele in s2_list]) == len(s2_list)

    return stillOK and isS2AllNone

```


##### Sort and Compare

```python
def anagramSolution2(s1, s2):
    """ Solution 2: Sort and Compare

    概念：
        1. 先排序 s1 和 s2 
        2. 在比較字串是否相同

    複雜度：
        排序的複雜度通常會是 O(n^2) 或是 O(nlogn)

    """

    s1_list = list(s1)
    s2_list = list(s2)

    if len(s1_list) != len(s2_list):
        return False

    s1_list.sort()
    s2_list.sort()

    start_idx = 0
    match = True
    while start_idx < len(s1_list) and match:
        if s1_list[start_idx] == s2_list[start_idx]:
            start_idx += 1
        else:
            match = False
        
    return match
```

##### Brute Force

生成 s1 的所有亂序字串列表，然後檢查是否存在 s2。
複雜度為 n \* (n-1) \* (n-2) \* ... \* 3 \* 2 \* 1，亦即 O(n!)
O(n!) 會比 n^2 成長還快。

##### Count and Compare

```python
def anagramSolution4(s1, s2):
    """ Solution 4: Count and Compare
    利用兩字串各個字母的計數來確認字串是否相同

    概念：
        1. 先初始化一個長度 26 的向量
        2. 針對每個字串中的字母，利用 ASCII 去找出相對於 'a' 的距離，作為填入的 index
        3. 計數
        4. 比較兩字串計數後的結果

    複雜度：
        n + n + 26 -> O(n)
        
    """
    c1 = [0] * 26
    c2 = [0] * 26

    for char1 in s1:
        ## 利用 ASCII 的次序關係，來填入相對於 'a' 的位置
        idx = ord(char1) - ord('a')
        c1[idx] += 1
    
    for char1 in s2:
        idx = ord(char1) - ord('a')
        c2[idx] += 1
    
    idx = 0
    stillOK = True
    while idx < 26 and stillOK:
        if c1[idx] == c2[idx]:
            idx += 1
        else:
            stillOK = False

    return stillOK
```
