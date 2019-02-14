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
    