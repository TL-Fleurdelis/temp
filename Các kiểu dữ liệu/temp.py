from multiprocessing.reduction import DupFd


code = 'vip________________________10'
for dup in code:
    dup = code.rfind('_')
    # print('pos:',dup)
    my_split = code.split(code[dup],dup)
print(my_split)
print(my_split[-1])



temp = 'vip___321312'

sp = temp.split('_')
print(sp)
print(sp[-1])