# 如何使用字串、字串的用法

#字串換行(字 \n字)
print("今天不想讀書 \n可是明天要考試")

#雙引號也想當字串
print("今天不想讀書\"可是明天要考試")

#字串相連
# 1、變數 + "字串"
today="今天不想讀書"
print(today +"可是明天要考試")


# 2、"字串" + "字串"
print("今天不想讀書"+"可是明天要考試")


#字串函式 function
name="Hello,Yaron"

# 1、全小寫.lower()
print(name.lower())

# 2、全大寫.upper()
print(name.upper())

# 3、判斷是否全大寫.isupper();回傳true,false
print(name.isupper())

# 4、判斷是否全小寫.islower();回傳true,false
print(name.islower())

# 5、函式疊加
print(name.lower().islower())

# 6、抓字母第幾個字[]；從0開始
print(name[2])

# 7、找字母在第幾個字.index("字");會選擇優先最前面的字
print(name.index("o"))

# 8、替換字.replace("舊字","新字")
print(name.replace("Y","y"))