# pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
# pop()方法语法：list.pop([index=-1])
# index -- 可选参数，要移除列表元素的索引值，不能超过列表总长度，默认为 index=-1，删除最后一个列表值。
# 返回值：该方法返回从列表中移除的元素对象。
list1 = ['Google', 'Runoob', 'Taobao']
popped_website=list1.pop()
print("列表现在为 : ", list1)
print(popped_website)
popped_website=list1.pop(1)
print("列表现在为 : ", list1)
print(popped_website)
