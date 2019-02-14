# Define Class

## Outline

* [Code](#code)
    * [Define Class](#define-code)
    * [Inheritance: Logic Gates and Circuits](#inheritance)
* [Other Notes](#other-notes)
    * [Comparison of @instancemethod, @classmethod, @staticmethod](comparison-of-instancemethod-classmethod-staticmethod)
    * [Shallow equality and Deep equality](#shallow-equality-and-deep-equality)


### Code

#### Define Class

```python
def maine

```

#### Inheritance

```python

```

### Other Notes

#### Comparison of instancemethod, classmethod, staticmethod
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