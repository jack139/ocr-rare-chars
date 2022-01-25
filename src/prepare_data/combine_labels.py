# 合并原始训练集，和，新训练集，的标签清单

import os
from tqdm import tqdm

orgin_path = 'images'
kxzd_path = 'images_kxzd_1m'

with open('../../data/train_data/combined_test.txt', 'w') as output_data:
    with open('../../data/train_data/kxzd_test.txt', 'r') as f:
        for l in tqdm(f):
            line = l.split()
            line[0] = os.path.join(kxzd_path, line[0])
            output_data.write(' '.join(line)+'\n')

    with open('../../data/train_data/data_test.txt', 'r') as f:
        for l in tqdm(f):
            line = l.split()
            line[0] = os.path.join(orgin_path, line[0])
            output_data.write(' '.join(line)+'\n')

with open('../../data/train_data/combined_train.txt', 'w') as output_data:
    with open('../../data/train_data/kxzd_train.txt', 'r') as f:
        for l in tqdm(f):
            line = l.split()
            line[0] = os.path.join(kxzd_path, line[0])
            output_data.write(' '.join(line)+'\n')

    with open('../../data/train_data/data_train.txt', 'r') as f:
        for l in tqdm(f):
            line = l.split()
            line[0] = os.path.join(orgin_path, line[0])
            output_data.write(' '.join(line)+'\n')
