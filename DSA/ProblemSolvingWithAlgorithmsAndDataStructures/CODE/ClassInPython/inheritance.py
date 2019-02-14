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