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

main()