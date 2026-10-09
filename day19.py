num=[1,2,2,3,3,3,4,1]
unique=set(num)#set() 把重复的自动去掉 —— [1,2,2,3,3,3,4,1] 变成只有 1、2、3、4
print(unique)
print(len(unique))
fruits={"苹果"}
fruits.add("香蕉")#add和append的区别：append是列表的方法，add是集合的方法。集合没有顺序，不能重复，列表有顺序，可以重复。
fruits.add("苹果")
print(fruits)
print("苹果" in fruits)