name = 'truong thanh long'
#name = "truong thanh long"
#name = '''truong thanh long'''
# lấy ký tự cuối cùng
print(name[-1])
'''
format chuỗi: 3 cách:
- Toán tử %
- Format 
- Tiền tố f 
'''
# ví dụ format chuỗi:
n1 = '10'
n2 = 100
n3 = 1000.0
print('Format bằng toán tử: n1 = %s , n2 =%d, n3 =%f ' %(n1,n2,n3))
print('Format chuỗi bằng cú pháp Format: n1 = {} n2 = {} n3 ={}' .format(n1,n2,n3))
print(f"Format chuỗi bằng tiền tố f: n1 = {n1}  n2 = {n2} n3 ={n3}")

'''
Phương thức xử lý chuỗi

lower(): viết thường 
upper(): viết in hoa 
capitalize(): viết kí tự in hoa đầu tiên 
title(): viết hoa ở đầu mỗi từ và viết thường các ký tự còn lại 

strip(x): cắt bỏ ký tự x ở đầu và cuỗi chuỗi
split(x): tách chuỗi thành list nhỏ với x là ký tự phần tách 

replace(a,b): thay thế chuỗi a thành chuỗi b 
find(a) : tìm kiếm chuỗi a từ trái qua phải => vị trí đầu tiên
rfind(a): tìm kiếm chuỗi a từ trái qua phải => vị trí cuối cùng
'ký tự nối'.join(list): ghép 1 list các chuỗi nhỏ thành 1 chuỗi lớn với ký tự nối cho trước
'''
name = 'truong thanh long long'
print('\nViết thường:',name.lower())
print("Viết in hoa: ",name.upper())
print("Viết hoa ký tự đầu tiên:",name.capitalize())
print("Viết hoa ký tự đầu của mỗi từ: ",name.title())
x = name.replace('long','001')
print('here: ',x)
#find sẽ tìm vị trí chuỗi xuất hiện đầu tiên
#rfind sẽ tìm vị trí  chuỗi xuất hiện cuối cùng
print("Tìm kiếm từ phải qua trái rfind: ",name.rfind('long'))
print("Tìm kiếm trái qua phải find: ",name.find('long'))

#print('tách chuỗi: ',name.split(' ')) # return list
#print('cắt bỏ ký tự đầu và cuối chuỗi:',name.strip('t'))
myList =['a','b','c']

# ghép chuỗi
print('a'.join(myList))