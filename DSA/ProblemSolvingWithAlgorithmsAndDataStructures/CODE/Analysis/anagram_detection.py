def funcTest(anagramSolution):
    s1, s2 = 'earth', 'heart'
    assert anagramSolution(s1, s2) == True

    s1, s2 = 'rrree', 'rreee'
    assert anagramSolution(s1, s2) == False

    s1, s2 = 'abcde', 'abcdf'
    assert anagramSolution(s1, s2) == False

    s1, s2 = 'aaaaa', 'aaaaa'
    assert anagramSolution(s1, s2) == True

    s1, s2 = 'aaaaaa', 'aaaaa'
    assert anagramSolution(s1, s2) == False

    s1, s2 = 'aaa', 'aaaaa'
    assert anagramSolution(s1, s2) == False

    print('[INFO] pass')

def anagramSolution1(s1, s2):
    """ Solution 1: Checking Off

    概念：
        1. 對每一個存在於 s1 的字，去檢查是否在 s2 出現 (兩層 for loop)
        2. 若有出現，便把 s2 該位置的字，取代為 None (因為此次配對是不只要出現，數量也要一樣，取代為 None 才不會重複計算)
        3. 一但發現找不到，則 break 第一層 while

    複雜度：
        最壞 (但找得到) 的狀況是 s1 = 'abcde', s1 = 'edcba'
        則此方法會需要 5 + 4 + 3 + 2 + 1 次搜尋，亦即 n (n + 1) / 2，複雜度為 n^2

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

def anagramSolution2(s1, s2):
    """ Solution 1: Sort and Compare

    概念：
        1. 

    複雜度：
        最壞 (但找得到) 的狀況是 s1 = 'abcde', s1 = 'edcba'
        則此方法會需要 5 + 4 + 3 + 2 + 1 次搜尋，亦即 n (n + 1) / 2，複雜度為 n^2

    """


def main():
    print('[TEST] anagramSolution1')
    funcTest(anagramSolution1)