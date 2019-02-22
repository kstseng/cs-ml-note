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

