# 列表list、列表的用法
#數字、字串、布林值
scores=[70,69,60,50,57,77]
friends=["你","我","他","她","牠","祂"]
win=[True,False,False,True]


#[0]第一位，[-1]倒數第一位
print(scores[0])
print(friends[-1])

#取列表第幾位到第幾位前
print(scores[0:3])

#取列表第幾位到底
print(friends[2:])

#取列表倒數第幾位前到頭
print(scores[:5])

#列表函式

# 1、在列表後加上列表.extend()
scores.extend(friends)
print(scores)

# 2、在列表加上新的值.append()
scores.append(0)
print(scores)

# 3、在列表上插入新的值.insert(插入位置,值)
scores.insert(1,70)
print(scores)

# 4、移除列表上值.remove()
scores.remove(50)
print(scores)

# 5、列表全部清空.clear()
scores.clear()
print(scores)

# 6、移除列表最後一個值.pop()
friends.pop()
print(friends)

#7、移除列表第一個值.sort()
friends.sort()
print(friends)

# 8、反轉列表.reverse()
friends.reverse()
print(friends)

# 9、在列表找值，回傳位置.index()
print(friends.index("他"))

# 10、在列表內有幾個和找的值一樣.count
print(friends.count("她"))

# 11、列表長度資料量len(列表變數)
print(len(friends))