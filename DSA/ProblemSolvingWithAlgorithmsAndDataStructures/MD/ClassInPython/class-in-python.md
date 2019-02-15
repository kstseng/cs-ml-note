# Introduction (Define Class)

## Outline

* [Code](#code)
    * [Define Class](#define-class)
    * [Inheritance: Logic Gates and Circuits](#inheritance)
* [Other Notes](#other-notes)
    * [Comparison of @instancemethod, @classmethod, @staticmethod](#comparison-of-instancemethod-classmethod-and-staticmethod)
    * [Shallow equality and Deep equality](#shallow-equality-and-deep-equality)

### Code

#### Define Class

[code in github](https://github.com/kstseng/dsa-ml-tool-note/blob/master/DSA/ProblemSolvingWithAlgorithmsAndDataStructures/CODE/ClassInPython/define_class.py)

```python
class Fraction:
    def __init__(self, top, bottom):
        """ 初始化
        """
        self.num = top
        self.den = bottom
    
    def show(self):
        """ 自定義函數
        """
        print(self.num, "/", self.den)
    
    def __str__(self):
        """ 修改 class 預設的字串化函數
        """
        return str(self.num) + " / " + str(self.den)
    
    def __add__(self, other_fraction):
        """ 修改 class 預設的加法運算
        """
        new_den = self.den * other_fraction.den
        new_num = self.num * other_fraction.den + other_fraction.num * self.den
        gcd = self.get_gcd(new_den, new_num)
        return Fraction(new_num // gcd, new_den // gcd)
    
    def __eq__(self, other_fraction):
        """ 修改 class 預設的相等（從 shallow 改為 deep）
        method: 交叉相乘
        note: 
            shallow: 同一個記憶體空間
            deep: 數值相等
        """
        val1 = self.num * other_fraction.den
        val2 = self.den * other_fraction.num
        return val1 == val2

    @classmethod
    def get_gcd(cls, m, n):
        """ 為了得到最簡分數
        """
        #輾轉相除法
        m, n = max(m, n), min(m, n)
        while n != 0:
            r = m % n
            m = n
            n = r                
        return m

def main():
    print('[test] print')
    myf = Fraction(3, 5)
    print(myf)

    ##
    print('[test] add')
    f1 = Fraction(3, 20)
    f2 = Fraction(1, 4)
    f_plus = f1 + f2
    print(f_plus)

    ## 
    print('[test] deep equal')
    f3 = Fraction(3, 20)
    f4 = Fraction(3, 20)
    print(f3 == f4)

if __name__ == '__main__':
    main()

```

#### Inheritance

[code in github](https://github.com/kstseng/dsa-ml-tool-note/blob/master/DSA/ProblemSolvingWithAlgorithmsAndDataStructures/CODE/ClassInPython/inheritance.py)


```python
""" 基礎門
"""
class LogicGate:
    def __init__(self, n):
        ## 標籤(門的名字)與輸出線
        self.label = n # name
        self.output = None
    
    def getLabel(self):        
        return self.label
    
    def getOutput(self):
        ## 不事先定義 performGateLogic，實作將會定義在各個繼承的子類
        ## "powerful idea in object-oriented programming"
        self.output = self.performGateLogic()
        return self.output

""" 雙輸入以及單輸入們
"""
class BinaryGate(LogicGate):
    def __init__(self, n):
        ## 先初始化從 LogicGate 所繼承的所有屬性
        LogicGate.__init__(self, n)
        ## 再添加自己獨有的屬性
        self.pinA = None
        self.pinB = None
    
    def getPinA(self):
        if self.pinA == None:
            ## 若此 pin 為 None，則手動輸入數值
            val = int(input("Enter Pin A input for gate "+ self.getLabel()+"-->"))
            if val not in [0, 1]:
                raise RuntimeError("Input value should be 0 or 1")
            else:
                return val
        else:
            ## 若此 pin 不為 None (亦即存在 Connector())，則透過 Connector() 取出 fromgate，並呼叫該 gate 執行 getOutput 函數
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            val = int(input("Enter Pin B input for gate "+ self.getLabel()+"-->"))
            if val not in [0, 1]:
                raise RuntimeError("Input value should be 0 or 1")
            else:
                return val
        else:
            return self.pinB.getFrom().getOutput()
    
    def setNextPin(self, source):
        """ source: Connector 的實體
        """
        ## 預設先把 Connector() 設在 pinA
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                return RuntimeError("Error: NO EMPTY PINS")


class UnaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pin = None
    
    def getPin(self):
        if self.pin == None:
            val = int(input("Enter Pin input for gate "+ self.getLabel()+"-->"))
            if val not in [0, 1]:
                raise RuntimeError("Input value should be 0 or 1")
            else:
                return val
        else:
            return self.pin.getFrom().getOutput()
        
    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            return RuntimeError("Error: NO EMPTY PINS")

""" 邏輯門
"""
class AndGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)
    
    def performGateLogic(self):
        ## 實作 performGateLogic
        a = self.getPinA()
        b = self.getPinB()
        
        if a == 1 and b == 1:
            return 1
        else: 
            return 0

class OrGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)
    
    def performGateLogic(self):
        ##
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 or b == 1:
            return 1 
        else: 
            return 0

class NotGate(UnaryGate):
    def __init__(self, n):
        UnaryGate.__init__(self, n)
    
    def performGateLogic(self):
        return 1 - self.getPin()

""" 連接器 (記錄在 pin 中)
"""
class Connector():
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        ## 把 connector 的存在紀錄在 tgate 的 pin 裡 (這裡的 self 就是 Connector 的實體)
        ## 目的為讓此 pin 不為 None，便可以從該 pin 的 getFrom 取出上一個 gate，然後再取出 output
        tgate.setNextPin(self)
    
    def getFrom(self):
        return self.fromgate
    
    def getTo(self):
        return self.togate
    

def main():
    print('=== [Test] And Gate')
    g1 = AndGate("G1")
    print(g1.getOutput())

    print('=== [Test] Or Gate')
    g2 = OrGate("G2")
    print(g2.getOutput())

    print('=== [Test] Not Gate')
    g3 = NotGate("G3")
    print(g3.getOutput())
    
    print('=== [Test] Connector')
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(g4.getOutput())


if __name__ == "__main__":
    main()
```

### Other Notes

#### Comparison of instancemethod, classmethod and staticmethod
[ref in stackoverflow](https://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod)

```python

class A(object):
    def foo(self,x):
        print("executing foo(%s,%s)"%(self,x))

    @classmethod
    def class_foo(cls,x):
        print("executing class_foo(%s,%s)"%(cls,x))

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)"%x)

a=A()

## instance
a.foo(1)

## instance
a.class_foo(1)
A.class_foo(1)

## instance
a.static_foo(1)
A.static_foo(1)

```

* instance method: 需實體化後才能調用函數。
* class method: 默認第一個參數為 class 本身，而非 instance，因此可以對 class 做一些處理。例如若在子類繼承時，所傳入的 class 便為子類。
* static method: 把同樣邏輯的函數包在一個 class 裡以方便調用。

#### Shallow equality and Deep equality

概念同於 Shallow copy 和 Deep copy

* Shallow equality: 是否指向同一塊記憶體位置的物件
* Deep equality: 在此定義為數值是否相同