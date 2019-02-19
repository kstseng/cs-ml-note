# Recursion

## Outline
* [遞歸三定律](#the-three-laws-of-recursion)
* [暖身小範例](#simple-problem)
 * [計算整數列表和](#calculating-the-sum-of-a-list-of-numbers)
 * [整數轉換為任意進位字串符](#converting-an-integer-to-a-string-in-any-base)

## The Three Laws of Recursion

1. 遞迴算法必須要有基本情況。(A recursive algorithm must have a base case.)
2. 遞迴算法必須改變其狀態，並向基本情況靠近。(A recursive algorithm must change its state and move toward the base case.)
3. 遞迴算法必須以遞迴方式呼叫自身。(A recursive algorithm must call itself, recursively.)

## Simple Problem

#### Calculating the Sum of a List of Numbers
計算整數列表之和

[Code]()

* `For loop`

```python
def listsumLoop(numList):
    total = 0
    for i in range(len(numList)):
        total += numList[i]
    
    return total
```

* `Recursion`

```
listsum(numList) = first(numList) + rest(numList)
```

```python
def listsumRecursion(numList):
    """ 
    """
    if len(numList) == 1:
        ## base case (函數的「例外條款」)
        return numList[0]
    else:
        total = numList[0] + listsumRecursion(numList[1:])

    return total
```


### Converting an Integer to a String in Any Base
整數轉換為任意進位字串符