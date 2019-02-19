def listsumLoop(numList):
    total = 0
    for i in range(len(numList)):
        total += numList[i]
    
    return total

def listsumRecursion(numList):
    """ 
    """
    if len(numList) == 1:
        ## base case (函數的「例外條款」)
        return numList[0]
    else:
        total = numList[0] + listsumRecursion(numList[1:])

    return total

def main():
    numList = [1, 3, 5, 2, 5]
    assert listsumLoop(numList) == listsumRecursion(numList)
