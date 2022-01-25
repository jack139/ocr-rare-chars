# 从康熙字典的字符集 keys

with open('../../data/char_std_kxzd_zk123.txt', 'r') as f:
    char_kxzd = f.read().split('\n')

with open('./keys.py', 'w') as output_data:
    output_data.write('alphabet = u"""%s"""'%''.join(char_kxzd) + '\n')
