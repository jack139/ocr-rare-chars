#康熙字典文本精简，只保留释义部分

from tqdm import tqdm

with open('../../data/char_std_5990.txt', 'r') as f:
    char_5990 = f.read().split('\n')[:5990]

with open('../../data/kangxizidian-v3f.txt', 'r') as f:
    kxzd = f.read().split('\n')

#  釀        《康熙字典》〈酉集下〉【酉字部】頁1289第23【唐韻】【集韻】女亮切【韻會】汝亮切【正韻】魚向切，𠀤音𥽬。【說文】醞也。作酒曰釀。【廣韻】醞酒也。【史記·孟嘗君傳】乃多釀酒買肥牛。【貨殖傳】通邑大都酤一歲千釀。【前漢·食貨志】一釀用麤米二斛，麴一斛，得成酒六斛六斗。　又【增韻】後人因謂酒爲釀。【世說新語】劉惔曰：見何次道飮，令人欲傾家釀。　又【禮·內則】鶉羹、雞羹、鴽，釀之蓼。【註】釀謂切雜之也。
#  '釀\t\t《康熙字典》〈酉集下〉【酉字部】頁1289第23\ueab1\ueab1【唐韻】【集韻】女亮切【韻會】汝亮切【正韻】魚向切，𠀤音𥽬。\ueab1【說文】醞也。作酒曰釀。\ueab1【廣韻】醞酒也。\ueab1【史記·孟嘗君傳】乃多釀酒買肥牛。\ueab1【貨殖傳】通邑大都酤一歲千釀。\ueab1【前漢·食貨志】一釀用麤米二斛，麴一斛，得成酒六斛六斗。\u3000又【增韻】後人因謂酒爲釀。\ueab1【世說新語】劉惔曰：見何次道飮，令人欲傾家釀。\u3000又【禮·內則】鶉羹、雞羹、鴽，釀之蓼。\ueab1【註】釀謂切雜之也。\ueab1\ueab1'


for k, v in enumerate(kxzd):
    tt = kxzd[k].split('\ueab1\ueab1')
    #print(tt)
    if len(tt)>2:
        t2 = ''.join([ c for c in ''.join(tt[1:]).replace('\ueab1', '').replace('\u3000', ' ') if c<'\uffff'])
        kxzd[k] = t2.replace('【','') \
                    .replace('】','') \
                    .replace('，','') \
                    .replace('。','') \
                    .replace('·','') \
                    .replace('〔','') \
                    .replace('〕','') \
                    .replace('《','') \
                    .replace('》','') \
                    .replace('：','') \
                    .replace('、','') \
                    .replace('〈','') \
                    .replace('〉','') \
                    .replace('（','') \
                    .replace('）','') \
                    .replace('(','') \
                    .replace(')','') \
                    .replace(',','') \
                    .replace('•','') \
                    .replace('','') \
                    .replace(' ','')

    else:
        print(kxzd[k])

#print(kxzd[-4])
#for k, i in enumerate(kxzd[-4]):
#    print(k, i, '%x'%ord(i), i>'\uffff')

with open('../../data/kangxizidian-converted.txt', 'w') as output_data:
    for s in kxzd:
        output_data.write(s.strip() + '\n')
