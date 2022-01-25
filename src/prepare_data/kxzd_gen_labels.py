# 从康熙字典的 已生成图片label.txt 生成训练用txt

import random
from tqdm import tqdm

train_ratio = 0.99

with open('../../data/char_std_kxzd_zk123.txt', 'r') as f:
    char_kxzd = f.read().split('\n')

with open('../../data/train_data/images_kxzd_1m/tmp_labels.txt', 'r') as f:
    tmp_labels = f.read().split('\n') # 00000160 俗溷爲一非又姓譜毫豪

# 转换为索引
new_labels = []
for l0 in tqdm(tmp_labels):
    l = l0.split()
    if len(l)<2:
        continue
    #print(l)
    l[0] += '.jpg'
    t = []
    for c in l[1]:
        t.append('%d'%char_kxzd.index(c))
    l[1] = ' '.join(t)
    new_labels.append(' '.join(l))

# 随机分配 训练集 和 测试集
random.shuffle(new_labels)
n = len(new_labels)
train_n = int(n*train_ratio)

with open('../../data/train_data/kxzd_train.txt', 'w') as output_data:
    for s in new_labels[:train_n]:
        output_data.write(s.strip() + '\n')

with open('../../data/train_data/kxzd_test.txt', 'w') as output_data:
    for s in new_labels[train_n:]:
        output_data.write(s.strip() + '\n')
