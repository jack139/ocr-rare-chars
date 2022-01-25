# 统计训练数据的字频

import os
import pickle
from tqdm import tqdm

data_cache = 'test_data/stat_data.pkl'

with open('../../data/char_std_kxzd_zk123.txt', 'r') as f:
    char_5990 = f.read().split('\n')

# 统计频数
if os.path.exists(data_cache):
    # 从cache装入
    with open(data_cache, "rb") as f:
        stat_char = pickle.load(f)
    print("Load cache ...")

else:

    stat_char = [0]*len(char_5990)

    with open('../../data/train_data/combined_train.txt', 'r') as f:
        for l in tqdm(f):
            line = l.split()
            for i in line[1:]:
                stat_char[int(i)] += 1

    # 保存 cache
    with open(data_cache, "wb") as f:
        pickle.dump(stat_char, f)
        print("Saving cache ...")


# 输出结果

t = []
for k, v in enumerate(stat_char):
    if v<1:
        t.append((char_5990[k], k, v))

print("zero samples =", len(t))

with open('test_data/char_stat.txt', 'w') as output_data:
    for k, v in enumerate(stat_char):
        output_data.write('%d\t%s\t%d\n'%(k, char_5990[k], v))