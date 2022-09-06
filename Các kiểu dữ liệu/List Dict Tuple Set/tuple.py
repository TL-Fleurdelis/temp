my_tuple = ('a','a',['long','linh','phuong'],{'name':'pitaya','age':"22"})
print(my_tuple)
print(tuple.__dir__)
# nếu khai báo tuple 1 đơn vị phải thêm 1 dấu phẩy còn không sẽ in ra một giá trị biến chứ k phải tuple
t1 = ('hihi','huhu')
print(t1)
print(set(t1))
# một số phương thức: index(value): tìm vị trí phần tử
# len(): độ dài phần tử  
#count: đếm 
del my_tuple
print(my_tuple)