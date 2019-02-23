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

def recMC(coinValueList, change):
    """
    coinValueList = [1, 5, 10, 25]
    change = 63
    usage: 
        recMC([1,5,10,25],63)
    概念：
    numCoins = min(
        1 + numCoins(original_amount - 1), 
        1 + numCoins(original_amount - 5), 
        1 + numCoins(original_amount - 10), 
        1 + numCoins(original_amount - 25)
    )
    """
    ## 最差狀況 (最多硬幣) => 全部用 1 塊
    minCoins = change 
    if change in coinValueList:
        ## base case: 
        ## 可直接支付 -> 一枚硬幣即可
        return 1
    else:
        candidates = [c for c in coinValueList if c <= change]
        ## 對每個 candidate 去計算可支付的最少硬幣數
        for c in candidates:
            numCoins = 1 + recMC(coinValueList, change - c)
            if numCoins < minCoins:
                minCoins = numCoins
        
    return minCoins

def recDC(coinValueList, change, knownResult):
    """
    不是動態規劃 => 記憶化 (緩存) memoization / caching
    usage: 
        recDC([1,5,10,25],63,[0]*64)
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

def dpMakeChange(coinValueList, change, minCoins):
    """ dynamica programming

    coinValueList = [1, 5, 10, 20]
    change = 64

    舉例：以 change = 5 去思考
    """
    ## 當 change = 5
    for cents in range(change + 1):
        ## 最差狀況（全部由 $1 元組成）
        coinCount = cents
        ## candidates = [1, 5]
        candidates = [c for c in coinValueList if c <= cents]
        for c in candidates:
            if minCoins[cents - c] + 1 < coinCount:
                coinCount = minCoins[cents - c] + 1
        minCoins[cents] = coinCount
    return minCoins[change]
                
def dpMakeChangeTrack(coinValueList, change, minCoins, coinsUsed):
    """ 把 dp 結果紀錄
    """
    for cents in range(change + 1):
        coinCount = cents
        newCoin = 1
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
    print(dpMakeChangeTrack(clist, amnt, coinsCount, coinsUsed))
    print('They are: ')
    printCoins(coinsUsed, amnt)
    print("The used list is as follows: ")
    print(coinsUsed)
    #print(coinsCount)

if __name__ == "__main__":
    main()
