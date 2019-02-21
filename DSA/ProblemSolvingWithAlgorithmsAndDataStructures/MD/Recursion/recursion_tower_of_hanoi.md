# Tower of Hanoi

## Outline

* [概念](#concept)
* [圖解](#example)
* [虛擬碼](#pseudo-code)
* [程式](#code)


## Concept


* 總共三個竿，分別是 
 * `fromPole` 起始竿
 * `toPole` 目標竿
 * `withPole` 中間竿
* 先從 base case 往上想
 * 有 1 個 disk 時：把 disk 從 `fromPole` 移動到 `toPole`
 * 有 2 個 disk 時：把第一個（較小的）disk 先放到 `withPole`，把第二個（較大的）disk 放到 `toPole`，再把 `withPole` 上的那個 disk 移動到 `toPole`.
 * 有 n 個 disk 時：把前 n - 1 個 disk 先放到  `withPole`，把剩下最大的 disk 放到 `toPole`，再把 `withPole` 上的 n - 1 disk 移動到 `toPole`.

## Example

舉三個 disk 為例

* 原始狀態

```
  1 |    |    |
  2 |    |    | 
  3 |    |    |
===============
  A    B    C
```

* 要先把 1, 2 移到暫存竿 (B)
 * 怎麼把 1, 2 移到 B ==> 把 B 暫時當作 (1, 2) 的目標竿
 * 先把 1 移動到暫存竿 (C)，再把 2 移動到目標竿 (B)，再把 1 移動到目標竿 (B)

```
    |    |    |
    |  1 |    |
  3 |  2 |    |
===============
  A    B    C

```

* 然後把 3 移動到目標竿 (C)

```
    |    |    |
    |  1 |    |
    |  2 |  3 |
===============
  A    B    C
```


* 再把 1, 2 移動到目標竿 (C)
 * 怎麼把 1, 2 移到 C ==> 把 C 暫時當作 (1, 2) 的目標竿
 * 先把 1 移動到暫存竿 (A)，再把 2 移動到目標竿 (C)，再把 1 移動到目標竿 (C)

```
    |    |  1 |
    |    |  2 |
    |    |  3 |
===============
  A    B    C
```

## Pseudo Code

重點：`fromPole`, `toPole` 和 `withPole` 在不同任務之間的切換

1. 把前 n-1 個 disk 移動到暫存竿 (`withPole`)
2. 把第 n 個 disk 移動到目標竿 (`toPole`)
3. 把在暫存竿 (`withPole`) 的 n-1 個 disk 移動到目標竿 (`toPole`)

## Code

```python
def moveTower(height, fromPole, toPole, withPole):
    """
    """
    if height >= 1:
        ## 把上 n-1 個 disk 從 fromPole 移動到 withPole
        moveTower(height - 1, fromPole, withPole, toPole)
        ## Base case: 當只有一個 disk 時，單純把 disk 從 fromPole 移動到 toPole
        moveDisk(fromPole, toPole)
        ## 把上 n-1 個 disk 從 withPole 移動到 toPole
        moveTower(height - 1, withPole, toPole, fromPole)

def moveDisk(fromPole, toPole):
    print("move disk from {} to {}".format(fromPole, toPole))

def main():
    moveTower(3, 'A', 'B', 'C')

main()
```