'''
List là tập hợp các phần tử dữ liệu bất kỳ, có thể thay đổi 
'''
myDict = {'name':'abc','age':22}
myList = ['a','b','c',[1,2,3],myDict]

print(myList[3][2])
print(myList[0:1])
print('temp: ',myList[0:1])
print(myList[:3]) 
print(myList[0:3]) 
print('here:',myList[2:])
# Thêm phần tử trong list 
myList.insert(-1,9)
myList.append('abc')
print(myList)
# ==> append, insert

# sửa phần tử
myList[0] = 'abcxyz'
myList[0:3] = ['linh','phuong','ha']
print(myList)
myList.pop(0)
print(myList)
#

#xóa phần tử
'''
del myList[0]
del myList[0:3]
del myList[2:] # giữ lại 2 phần tử đầu
del myList[0:] # xóa hết

myList[0:1] = []
myList.clear() # xóa hết
myList.remove('linh')  # xóa phần tử đầu tiên có giá trị trên được tìm thấy trong list 

myList.pop() # xóa phần tử cuối 
myList.pop(0)
=>> del, clear, remove ,pop , myList[0] = []
'''

'''
một số phương thức khác: sort(), extend(), count(x),reverse(),

all(list) : trả về true nếu tất cả phần tử của list đều true hoặc list rỗng
any(list) : trả về true nếu list chứa phần tử ,nếu rỗng là false
enucumate(list) : trả về đối tượng enucumate, chứa index và giá trị 
sorted(list): trả về list mới theo thứ tự tăng dần
min(list) : trả về phần tử nhỏ nhất trong list
max(list) : trả về phần tử lớn nhất trong list  
len(list) : độ dài
sum(list) : tổng
'''
temp = ['x','y','z']
print(temp[0:])
del temp [0:]
print('del:',temp)