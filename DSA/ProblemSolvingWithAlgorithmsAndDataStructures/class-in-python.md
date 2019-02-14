# Define Class

## Outline

* [Code](#code)
    * [Define Class](#define-code)
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

graph LR
  单独节点
  开始 -- 带注释写法1 --> 结束
  开始 -->|带注释写法2| 结束
  实线开始 --- 实线结束
  实线开始 --> 实线结束
  实线开始 -->|带注释| 实线结束
  虚线开始 -.- 虚线结束
  虚线开始 -.-> 虚线结束
  虚线开始 -.->|带注释| 虚线结束
  粗线开始 === 粗线结束
  粗线开始 ==> 粗线结束
  粗线开始 ==>|带注释| 粗线结束
  subgraph 子图标题
    子图开始 --> 子图结束
  end
  节点1[方形文本框] --> 节点2{菱形文本框}
  节点3(括号文本框) --> 节点4((圆形文本框))
  


```python

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