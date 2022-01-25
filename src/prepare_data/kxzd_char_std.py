# 从康熙字典生成新的字符表

from tqdm import tqdm

with open('../../data/char_std_5990.txt', 'r') as f:
    char_5990 = f.read().split('\n')[:5990]

with open('../../data/kangxizidian-converted.txt', 'r') as f:
    kxzd = f.read().split('\n')

with open('../../data/additional.txt', 'r') as f: # 补齐二级字库
    additional = f.read().split('\n')

# 补齐2级字库字符
kxzd.extend(additional)

with open('../../data/HZ1JZK.txt', 'r') as f:
    zk1 = f.read().replace('\u3000', '\n').split('\n')

with open('../../data/HZ2JZK.txt', 'r') as f:
    zk2 = f.read().replace('\u3000', '\n').split('\n')

with open('../../data/HZ3JZK.txt', 'r') as f:
    zk3 = f.read().replace('\u3000', '\n').split('\n')


for l in tqdm(kxzd):
    for c in l:
        if c in char_5990:
            continue
        if (c not in zk1) and (c not in zk2) and (c not in zk3):
            continue
        char_5990.append(c)
        #print(c)

print(len(char_5990))

with open('../../data/char_std_kxzd_zk123.txt', 'w') as output_data:
    for s in char_5990:
        output_data.write(s.strip() + '\n')
