mySet = {'set','dict','tuple','list','list',True}
print(mySet)

'''
Thêm: add(),update(set or dict or tuple or list),set1+set2 
Xóa : remove(value), del nameSet, discard(value),pop(),clear
''' 
mySet.add('python')
mySet.remove('python')
mySet.discard('set')
mySet.pop() # xóa ngẫu nhiên 
#mySet.clear() # xóa hết
#del mySet
print(mySet)
myList = ['a','b','c']
myTuple = (100,200)
myDict = {'name':'linh','age':22}
mySet.update(myList)
mySet.update(myDict)
mySet.update(myTuple)
print(mySet)