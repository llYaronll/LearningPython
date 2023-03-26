# 函式 function

# 定義函式名稱
def Yo() : 
    print("Yo")

# 例子運用方式結合使用者輸入

def Say(name):
    print("You name is " + name)

name = input("輸入你的名字")
Say(name)

# return絕對覆蓋使用，如果函式外部要使用將預設是None