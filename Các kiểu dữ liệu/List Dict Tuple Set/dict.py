myList=['1','2','3']
set_check={1,1,1,2}
tup=('11',22,33)
temp={
    'a':'a',
    'b':'b'
}
# dict có thể chứa list,set,tuple,dict
info = {
    'name':'linh',
    'age': '20',
    'sex': 'female',
    'list': temp,
    #'name':'long'
}
print("Ban đầu:",info)
# thêm dict 
info['boyfriend'] = "No"
info.update({'family':4})
#info.setdefault('school:','hust')
info['school'] = 'hust'
print('Sau khi thêm:',info)

# sửa
info['boyfriend'] = "Yes"
info.update({'family':'No'})
info.update({'school':'HUST'})

print('Sau khi sửa:',info)

# xóa dict 
'''
del info #xóa dict
del info ['family']
info.pop('family')
info.popitem() # xóa phần bộ key:value cuối cùng của dict
info.clear() # xóa hết key-value của dict 
'''
# tìm kiếm cặp value của key đang chọn 
print(info.get('name'))
print(info['name'])
'''
Phương thức khác trong dict 
clear()
get(key)
popitem() : xóa key-value cuối cùng của dict 
keys() : return all key of dict 
update(dict) : cập nhật dict
copy(): trả về bản sao của dict
pop(key) : xóa phần tử tương ứng với key 
values() : Lấy các values trong dict
items() : trả về 1 list tuple , mỗi tuple có dạng (key,value)
setdefaultkey(key): trả về key đã tồn tại key đó
, hoặc thêm mới key với giá trị default nếu chưa tồn tại
'''
print(info.items())
print('To tuple:',tuple(info))
print('To list:',list(info))
print('Set:',set(info))
