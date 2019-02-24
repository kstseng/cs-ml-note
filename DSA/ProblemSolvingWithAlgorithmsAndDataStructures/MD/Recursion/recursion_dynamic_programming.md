# Dynamic Programming

* [範例：硬幣找零](#example)
* [概念](#concept)
* [解法](#solution)
  * [貪婪法 Greedy Search](#greedy-search)
  * [遞迴 Recursion](#recursion)
  * [遞迴加上快取（ 記憶化 ）Recursion with Caching \( Memorization \)](#recursion-with-caching) : 自頂向下
  * [動態規劃 Dynamic Programming](#dynamic-programming) : 自底向上
* [參照](#reference)

## Example

硬幣找零：找出最少硬幣數的找零組合

變數命名：

* 要換的錢：change
* 零錢種類：coinValueList

## Concept

1. 貪婪法：從**最大金額**的硬幣開始**盡可能多**的兌換，然後再往次大金額的硬幣兌換。

   1. **問題**：假設總共要換 $63，硬幣種類有 1, 5, 10, 21, 25，那便找不到最佳解。所以此解可能不正確。

2. 遞迴概念：

   1. Base Case: 假設 change 可以在 coinValueList 找到 =&gt; 直接兌換，且硬幣數為 1。

   2. Other Case: 假設 change 在 coinVlauList 找不到 =&gt;

      ```
      numCoins(change) = min(
          1 + numCoins(change - 1), 
          1 + numCoins(change - 5), 
          1 + numCoins(change - 10), 
          1 + numCoins(change - 25)
      )
      ```

## Solution

### Greedy Search

```python
def gdMC(change, coinValueList):
    """ Greedy Search
    change = 63
    coinValueList = [1, 5, 10, 20, 21, 25]
    """
    numCoins = 0
    candidates = [c for c in coinValueList if c <= change]
    coinsUsed = [0] * len(coinValueList)
    for i in range(len(candidates)):
        ## 從最大的硬幣開始找
        idx = (len(candidates) - 1) - i
        c = candidates[idx]
        while change >= c:
            ## 當 change 大於等於「不大於 change」的最大硬幣
            ## 則開始兌換
            change -= c
            numCoins += 1
            coinsUsed[idx] += 1

    return sum(numCoins)
```

### Recursion

##### 概念

```
numCoins(change) = min(
    1 + numCoins(change - 1), 
    1 + numCoins(change - 5), 
    1 + numCoins(change - 10), 
    1 + numCoins(change - 25)
)
```

##### 筆記

效率很低，原因在於**重複計算**。解決方法為存儲已計算過的結果，需要時再調用。

![](http://interactivepython.org/runestone/static/pythonds/_images/callTree.png)

##### 程式

```python
def recMC(coinValueList, change):
    """
    coinValueList = [1, 5, 10, 25]
    change = 63
    usage: 
        recMC([1, 5, 10, 25], 63)
    """
    ## 最差狀況 (最多硬幣) => 全部用 1 塊
    minCoins = change 
    if change in coinValueList:
        ## base case: 
        ## 可直接支付 -> 一枚硬幣即可
        return 1
    else:
        ## 先選出比當前 change 小的可兌換硬幣金額
        candidates = [c for c in coinValueList if c <= change]
        ## 對每個 candidate 去計算可支付的最少硬幣數
        for c in candidates:
            numCoins = 1 + recMC(coinValueList, change - c)
            if numCoins < minCoins:
                minCoins = numCoins

    return minCoins
```

### Recursion with Caching

##### 概念

利用一個列表來記錄已經計算過的結果，在要計算前先確認是否算過，若有的話便直接調用。

關鍵字：**自頂向下**

##### 筆記

此方法並非**動態規劃**，只是利用一個列表去儲存結果，已避免重複計算。

例：從上圖可看出在處理 `change = 26` 時，執行順序會是從左到右，換言之在處理 `change = 21 & coin = 1` 時，已經處理過 `change = 15` 的狀況並且儲存結果。因此在處理 `change = 21 & coin = 5` 時又遇到 `change = 15`，便不用重複算，而是直接取出結果。

##### 程式

```python
def recDC(coinValueList, change, knownResult):
    """
    不是動態規劃 => 記憶化 (緩存) memoization / caching
    usage: 
        recDC([1, 5, 10, 25], 63, [0]*64)
    """
    minCoins = change
    if minCoins in coinValueList:
        return 1
    elif knownResult[change] > 0:
        ## 如果曾經算過，則取出結果（記憶）
        return knownResult[change]
    else:
        candidates = [c for c in coinValueList if c <= change]
        for c in candidates:
            numCoins = 1 + recDC(coinValueList, change - c, knownResult)
            if numCoins < minCoins:
                minCoins = numCoins
                ## 如果找到更小的硬幣數，則存入 knownResult
                knownResult[change] = minCoins

    return minCoins
```

### Dynamic Programming

##### 概念

利用**最佳化子問題**加上**記憶化儲存**，來解決原來的問題。

白話文就是「記住已經求過的解」。

[演算法筆記](http://www.csie.ntnu.edu.tw/~u91029/DynamicProgramming.html)：

```
Dynamic Programming = Divide and Conquer + Memoization
```

###### 附註

動態規劃只能應用在**存在**`最佳子結構`的問題。`最佳子結構`的意思是**局部最佳解**能決定**全域最佳解**。

###### 自問自答

問：為何在 Recursion with Caching 時，這篇教學不會稱之為動態規劃？但有些介紹會將其認為是動態規劃？

答：動態規劃一般分為「**自頂而下 \(Top-down\)**」和「**自底而上 \(Bottom-up\)**」兩種形式。而**自頂而下**就是 Recursion with Caching，比較常被稱為記憶法或是備忘錄法，其脈絡為當遇到問題時，先看之前有沒有解決過；**自底而上**則比較被認為是動態規劃，因為其脈絡便是動態規劃的核心概念：**先計算子問題，再由子問題計算父問題**。

關鍵字：**自底向上**

##### 個人心得

從[演算法筆記](http://www.csie.ntnu.edu.tw/~u91029/DynamicProgramming.html)中的重點記錄如下：

```
 Dynamic Programming = Divide and Conquer + Memoization
```

1. 把原問題遞迴分割成許多小問題 \(recurrence, **not** `recursion`\)
   1. `recurrence` ：子問題與原問題完全相同，只有數值範圍不同
   2. `recursion` : 在函數定義中使用函數自身的方法
   3. **\[註\]**：中問都叫遞迴，但意義完全不同。
2. 再運用記憶法儲存這些答案，避免重複求解，以空間換取時間。
3. 實作上的兩種方式
   1. Top-down \(recursion with caching\)
      1. 好處：不用計較計算順序，因為遞迴結構會迫使先解決最小的問題
      2. 壞處：
         1. 因為採用遞迴，會不斷呼叫程序，因此執行效率較差。
         2. 因為不能控制計算順序，因而無法妥善運用記憶體
   2. Bottom-up：與 Top-down 互補。

其實從演算法筆記和此篇的原始教學文比對可發現，`Recursion with Caching` 應該也可以被稱為是**動態規劃**中的**自頂而下 (Top-down)**的實作，因為也用到了**問題分解**跟**記憶法**的解決方式。

使用 `Recursion with Caching (Top-down)` 的好處就是直接從大問題下手，而遞迴 (recursion) 的實作方式會迫使先解決小問題，但缺點就是會一直重複呼叫函數，即使是已經有透過記憶法來避免重複運算。

##### 流程分析

1. 當 `change <= 4` 時，candidate 都只有 1，因此都是唯一解。
2. 當 `change <= 5` 時，candidate 有 `1` 和 `5`，則結果有一個 `5` 或是五個 `1`。因此在表中儲存一個硬幣。
3. ...
4. 當 `change <= 11` 時，有三個選項 \(`1`, `5`, `10` 元\)
   1. 一個`1`元 + `10` 元的最小硬幣數 = 兩個硬幣
   2. 一個`5`元 + `6` 元的最小硬幣數 = 四個硬幣
   3. 一個`10`元 + `1` 元的最小硬幣數 = 兩個硬幣

![](http://interactivepython.org/runestone/static/pythonds/_images/changeTable.png)

![](http://interactivepython.org/runestone/static/pythonds/_images/elevenCents.png)

##### 程式

```python
def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    """ dynamica programming

    coinValueList = [1, 5, 10, 20]
    change = 64

    舉例：以 change = 5 去思考
    """
    ## 當 change = 5
    for cents in range(change + 1):
        ## 最差狀況：全部由 $1 元組成
        ## 則硬幣數就是 cents
        coinCount = cents
        ## 硬幣金額 $1
        newCoin = 1
        ## candidates = [1, 5]
        candidates = [c for c in coinValueList if c <= cents]
        for c in candidates:
            if minCoins[cents - c] + 1 < coinCount:
                ## 紀錄硬幣數量
                coinCount = minCoins[cents - c] + 1
                ## 紀錄最後一個加上的硬幣金額
                newCoin = c
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    return minCoins[change]

def printCoins(coinsUsed, change):
    """
    """
    coin = change
    while coin > 0:
        ## 因為 coinsUsed 是記錄最後一個加上去的硬幣金額
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin -= thisCoin

def main():
    amnt = 63
    clist = [1, 5, 10, 21, 25]
    coinsUsed  = [0] * (amnt + 1)
    coinsCount = [0] * (amnt + 1)

    print("Making change for {} requires".format(amnt))
    print(dpMakeChange(clist, amnt, coinsCount, coinsUsed))
    print('They are: ')
    printCoins(coinsUsed, amnt)
    print("The used list is as follows: ")
    print(coinsUsed)
    #print(coinsCount)
```

### Reference

1. [演算法-動態規劃 Dynamic Programming–從菜鳥到老鳥](https://codertw.com/程式語言/586686/)



