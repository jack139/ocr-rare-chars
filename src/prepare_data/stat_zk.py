# 统计字库与训练数据的重合度

from tqdm import tqdm


# 原始 字典
#with open('../../data/char_std_5990.txt', 'r') as f:
#    char_5990 = f.read().split('\n')[:5990]


# 康熙字典
with open('../../data/char_std_kxzd_zk123.txt', 'r') as f:
    char_5990 = f.read().split('\n')

with open('../../data/HZ1JZK.txt', 'r') as f:
    zk1 = f.read().replace('\u3000', '\n').split('\n')

with open('../../data/HZ2JZK.txt', 'r') as f:
    zk2 = f.read().replace('\u3000', '\n').split('\n')

with open('../../data/HZ3JZK.txt', 'r') as f:
    zk3 = f.read().replace('\u3000', '\n').split('\n')

def stat(zk, name):
    t = []
    for i in tqdm(zk):
        if not i in char_5990:
            t.append(i)
    print(''.join(t))
    print(name, ': %d\t%d\t'%(len(zk), len(t)))

stat(zk1, 'ZK1') 
stat(zk2, 'ZK2') 
stat(zk3, 'ZK3') 

'''
原始字典
ZK1 : 3500   12
ZK2 : 3000   1062
ZK3 : 1605   1450

康熙字典
ZK1 : 3500  2
ZK2 : 3000  478
ZK3 : 1605  607
'''
