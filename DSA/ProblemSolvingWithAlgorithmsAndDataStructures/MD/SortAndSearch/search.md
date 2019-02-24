# Search

- [順序查找 Sequential Search](#sequential-search)
- [二分查找 Binary Search](#binary-search)
- [Hash 查找](#hash-search)

## Sequential Search

### 列表隨機排序

- 假設：列表不以任何方式排序，換言之裡面的元素是隨機被放置在列表中的
- 複雜度分析：`O(n)`
  - `item` 在 `list` 中：
    - 最差：`n`
    - 最好：`1`
    - 平均： `n/2`
  - `item` 不在 `list` 中
    - 最差：`n`
    - 最好：`n`
    - 平均： n`
- 程式

```python
def sequentialSearch(alist, item):
    """
    alist [1, 4, 20, 5]
    item = 4
    """
    found = False
    pos = 0
    ## 按順序從頭開始找
    while not found and pos < len(alist):
        if alist[pos] == item:
            found = True
        else:
            pos += 1
    
    return found
```

### 列表由小到大排序

- 假設：列表以小到大排序
- 複雜度分析：`O(n)`
  - `item` 在 `list` 中：
    - 最差：`n`
    - 最好：`1`
    - 平均： `n/2`
  - `item` 不在 `list` 中
    - 最差：`n`
    - 最好：`1`
    - 平均： `n/2`
- 程式

```python
def orderedSequentialSearch(alist, item):
    """
    """
    pos = 0
    found = False
    stop = False
    while not found and pos < len(alist) and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                ## 因為 list 是小到大排序，因此當 alist[pos] 大於 item
                ## 那在後面也不會出現 item
                stop = True
            else:
                pos += 1
    
    return found
```

## Binary Search

有序列表的查詢

- 複雜度分析

經過每一輪比較，平均而言樣本數會是前一次比較的一半

| Comparison | Approximate Number of Items Left |
| :--------: | -------------------------------- |
|     1      | `n / 2`                          |
|     2      | `n / 4`                          |
|     3      | `n / 8`                          |
|    ...     | ...                              |
|     i      | `n / 2^(i)`                      |

假設在 `k` 輪後只剩下最後一個樣本（結果可能是找到或沒找到），查找結束。因此可得到複雜度為 `O(logn)`
$$
\frac{n}{2^k} = 1
$$

$$
k= log(n)
$$

- 附註
  - 需要去思考「排序對查詢的必要性」
    - 若會需要查找多次，那排序的成本就相對低。
    - 若列表長度很小，那排序所造成的額外成本可能就不值得
    - 若列表長度很大，那一次排序所需要的成本很可能非常高

- 程式

```python
## 寫法一：直覺寫法
def binarySearch(alist, item):
    """
    alist = [1, 2, 3, 10, 20, 25, 30]
    item = 11
    binarySearch(alist, item)
    """
    first_idx = 0
    last_idx = len(alist) - 1
    found = False

    ## 當 last 和 first 是隔壁（中間無數值）且 not found
    while (last_idx - first_idx) > 1 and not found:
        ## 定義如何取 middle_idx
        middle_idx = (last_idx - first_idx) // 2 + first_idx
        if alist[middle_idx] == item:
            found = True
        else:
            if alist[middle_idx] > item:
                last_idx = middle_idx
            else:
                first_idx = middle_idx
    return found

## 寫法二：Recursion
def binarySearchDivideAndConquer(alist, item):
    """
    利用 Divide and Conquery 把問題切成更小的問題來解決
    """
    if len(alist) == 0: 
        return False
    else:
        mid_idx = len(alist) // 2
        if alist[mid_idx] == item:
            return True
        else:
            ## 大問題和小問題相同，只差在參數範圍 => Divide and Conquer
            if alist[mid_idx] > item:
                ## 取前段
                ## 不用包含 mid_idx
                return binarySearchDivideAndConquer(alist[:mid_idx], item)
            else:
                ## 取後段
                ## 不用包含 mid_idx
                return binarySearchDivideAndConquer(alist[mid_idx + 1:], item)
```



## Hash Search

##### 大綱

- [筆記](#note)
- [目標](#target)
- [方法](#method)
- [衝突解決 Collision Resolution](#collision-resolution)
- [實現 Map](#implementing-map)

##### Note

- 名詞
  - 哈希表 Hash Table: 可以用 `O(1)` 的方式取得的儲存方式。
  - 哈希函數 Hash Function: 項目和此項在表中所屬的槽之間的映射關係
    - 例：同個餘數的放在同一個槽。`h(item) = item % 11`
  - 負載因子 Load Factor: 多少槽已被使用
  - 衝突 ( 碰撞) Collison: 同一個槽有多個值
- 重點
  - 不需要哈希函數是完美的，仍然能有效提高性能。
  - 增加表的大小，是一種完美建構哈希函數的方式，但會浪費大量內存
- `Dictionary`, `Hash Table`, `Map` 的關係 
  - `字典 Dictionary`：一種可以透過 `key` 去查找 `value` 的資料儲存方式。也可稱作 `Map`。但具體怎麼找，可以有不同實現。
  - 實現方式：
    - 二叉樹 (`binary tree`)：當數據進來後，根據 `key` 排序，再使用二分查找，便能根據 `key` 找到 `value`。
    - 哈希表 ( `hash table` )：利用 `hash function`，來達到 `O(1)` 複雜度。

##### Target

建立一個哈希函數，最大限度地減少衝突，並將項目均勻得分布在哈希表中。

##### Method

以下列出幾種常見建立哈希函數的方法。

1. 餘數法：將項目除槽的數量所得的餘數作為放入哪個槽的依據
   1. 例：共 `11` 個槽，則 `44%11 = 0`，便放入指標為 `0` 的槽。
2. 分組求和法 `Folding Method`: 將列表中的項目分成大小相同的子列表，並各自求和，再根據可存入槽的數量，套用餘數法。
   1. 例：電話號碼為 `436-555-4601`，兩兩作為一個數字並加總，可得 `43 + 65 + 55 + 46 + 1 = 210`，`210 % 11 = 1`，便放入指標為 `1` 的槽。
3.  平方取中法 `Mid-square mtehod`: 將項目平方後，取中間一部分數字進行餘數法
   1. 例：項目為 `44`，`44^2 = 1936`，則存在 `93 % 11 = 5`的槽。
4. 若項目是字串，則可利用 `ascii` 值
   1. 例：項目為 `cat`，分別的 **ascii** 為 `99`, `97`, `116`，便可以相加在用餘數法。
   2. 亦可使用字串的位置作為權重。來區別 `cat` 和 `tac`。

##### Collision Resolution

`Rehash`: 在衝突後尋找另一個槽的過程。

###### 開放尋址 Open Addressing

按照一定順序將衝突後的項目填入另一個槽。

1. 線性探測 Linear Probing
   1. 概念：接續著往下找尚未被填入值的槽
   2. 搜索：必須以同樣方式尋找項目
      1. 找到欲查詢的值或是遇到空槽
   3. 缺點：在相同的 `hash value` 發生很多衝突，可能會導致後續要插入的值，因為前面發生衝突，而被迫跳到其他槽。
2. 延伸版本的線性探測 extend the linear probing
   1. 概念：當遇到衝突時，固定往下看第 `k` 個槽來跳過接續的槽。
   2. 注意：設 `k` 的目的是在於讓所有槽能被訪問。因此這也是為何槽的數量 (表的大小) 很常設定為**質數**。

###### 使用鏈接 Chaining

允許每個槽可以儲存多個項目的集合（鏈接）。便可以在同一個槽中儲存多個項目。

平均來說，每個槽的項目應該會遠小於總項目數，因此可以大大減少搜尋時間。

##### Implementing Map

```python
class HashTable:
    def __init__(self):
        ## 槽的大小定為質數，使得衝突解決的算法可以更有效率（避免某些槽都不會用到）
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
    
    def put(self, key, data):
        """
        """
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            ## 空的 => 填入
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if key == self.slots[hashvalue]:
                ## 如果 key 一樣，代表不是 Collision
                ## 則把舊資料替換成新資料
                self.data[hashvalue] = data
            else:
                ## 發生 Collision
                ## Rehash
                nextslot = self.rehash(hashvalue, self.size)
                while self.slots[nextslot] != None and key != self.slots[nextslot]:
                    ## rehash 後，得到新的值 (index)
                    ## 1. 當已經有塞值了（key 不為 None）且
                    ## 2. 裡面存的 key，跟現在的 key 不一樣 
                    ##    => 欲取代先前造成 Collision 的 key
                    ##    ex: 
                    #        1. put(key=12, val='a') => 在第 1 格放入 kv = {12, 'a'}
                    #        2. put(key=23, val='b') => Collision! => 在第 1 + 1 格放入 kv = {23, 'b'}
                    #        3. put(key=23, val='d') => Collision! => 移動到 1 + 1 後發現 key => 在第 2 格放入 kv = {23, 'd'}
                    nextslot = self.rehash(nextslot, self.size)
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = nextslot
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data

    def hashfunction(self, key, size):
        return key % size
    
    def rehash(self, oldhash, size):
        ## 要在得一次餘數，而不是直接 + k
        ## 因為可能 oldhash + k 後大於 size
        ## 要讓 hash value 可以回到第一個槽開始填值
        return (oldhash + 1) % size
    
    def get(self, key):
        """
        """
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                data = self.data[position]
                found = True
            else:
                ## 根據 rehash 的定義來找可能的 position
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    ## 若已經回到原點還找不到，則停止尋找
                    stop = True
        return data

    def __getitem__(self, key):
        ## 重新定義使得可以用 [] 來運作
        return self.get(key)
    
    def __setitem__(self, key, data):
        ## 重新定義使得可以用 [] 來運作
        self.put(key, data)
    
def main():
    H = HashTable()
    H[54]="cat"
    H[26]="dog"
    H[93]="lion"
    H[17]="tiger"
    H[77]="bird"
    H[31]="cow"
    H[44]="goat"
    H[55]="pig"
    H[20]="chicken"
    print(H.slots)
    print(H.data)
    H[20]="duck"
    H.data
```

