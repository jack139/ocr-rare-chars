# 生僻字OCR识别优化训练

- 原始模型和训练数据来自 https://github.com/YCG09/chinese_ocr
- 在实际应用中，如果需要识别姓名，一定会遇到生僻字的问题。原始模型权重包含5990个汉字，涵盖了一些生僻字，还够全。所以这里增加一些，提高生僻字的识别能力。



## 模型

[DenseNet + CTC](https://github.com/YCG09/chinese_ocr#densenet--ctc%E8%AE%AD%E7%BB%83)



## 训练方案

在原有训练集上（5990个label），增加生僻字（增加1917个），图片构造延用原有方法：灰白字、印刷体。



## 生僻字来源

- 通用规范汉字表 [二级字表](http://cidian.zwbk2009.com/index.php?title=%E9%80%9A%E7%94%A8%E8%A7%84%E8%8C%83%E6%B1%89%E5%AD%97%E8%A1%A8%EF%BC%88%E4%BA%8C%E7%BA%A7%E5%AD%97%E8%A1%A8%EF%BC%89)　（3000字）
- 通用规范汉字表 [三级字表](http://cidian.zwbk2009.com/index.php?title=%E9%80%9A%E7%94%A8%E8%A7%84%E8%8C%83%E6%B1%89%E5%AD%97%E8%A1%A8%EF%BC%88%E4%B8%89%E7%BA%A7%E5%AD%97%E8%A1%A8%EF%BC%89)　（1605字）
- 康熙字典 [TXT来源](https://github.com/7468696e6b/kangxiDictText)

增补在康熙字典中出现的二级和三级字表的汉字。



## 训练集

1. 原始训练集

- 共约364万张图片，按照99:1划分成训练集和验证集
- 数据利用中文语料库（新闻 + 文言文），通过字体、大小、灰度、模糊、透视、拉伸等变化随机生成
- 包含汉字、英文字母、数字和标点共5990个字符
- 每个样本固定10个字符，字符随机截取自语料库中的句子
- 图片分辨率统一为280x32



2. 生僻字训练集

- 共约100万张图片，按照99:1划分成训练集和验证集
- 数据利用中文语料库（康熙字典），通过字体、大小、灰度、模糊、透视、拉伸等变化随机生成
- 在原训练集上，新增汉字1917个（未包括3级字库之外的生僻字）
- 每个样本固定10个字符，字符随机截取自语料库中的句子
- 图片分辨率统一为280x32



训练时将两个数据集混合。



## 生成语料库

```
python3 kxzd_convert.py
python3 kxzd_char_std.py
```



## 文本图片生成

```
cd src/text_renderer
python3 main.py --length 10 --img_height 32 --img_width 280 --corpus_mode chn --strict --output_dir ../../data/train_data --tag images_kxzd_1m --num_img 1000000
```

参考：[Text Renderer](https://github.com/Sanster/text_renderer)



## 标签生成

```
cd src/prepare_data
python3 kxzd_gen_labels.py
python3 combine_labels.py
```



## 统计训练集字频

```
cd src/prepare_data
python3 stat_data.py
```



## 训练

```
cd src/train
python3 train.py
```



## 训练集和权重下载

- 训练结果：

| train_loss | val_loss | val_acc |
| ---------- | -------- | ------- |
| 0.9318     | 0.0749   | 0.9848  |



- 下载：

[百度网盘](https://pan.baidu.com/s/1MYOKmN-RUBKllAA9v4LcqQ) 提取码: il8r 



## 附：三级字库中未包含的字

```
𠙶戋氕冮汈𬣙讱圲𨙸吖钆伣𬇕䜣讻𬣞𬘓纩玘玚刬𫭟坜𫭢㧑苊苉𫇭杄杧杩尪轪𫐄旵呙𫵷岜觃岙㑇伲飏闶𣲘𣲗𬇙𬣡祃诇诐屃𫸩䢺妧𨚕驲𫘜𬘘𫘝纼玱坬坽䢼𦭜㭎𬨂𬀩𬀪岽岞峂𬬩钐钔钖垈肷饳炆泇峃𫍣𬣳𬩽鸤𬮿𬯀乸𫰛迳𬳵𬳶䌹𫠊绋玶𬍛玿韨垯垲垍鿍垴垵垏荙荛茽𬜬𦰡荭㭕䴓砄䶮轷轹𪾢昽哒𪨰峧帡钘𫓧𬬮𬬱𬬭钪钬钭俫舣鸧䏡𦙶胩飐饻炣㶲洘㳚浈浉袆陧𬘡𬳽𬘩𫄧骉珹𪟝𬍤𫭼埗埇莰𬜯莶䓖𬂩𫠆砵砫硁𨐈辀辁𬌗唝𫑡帱崁𪨶崄赆𬬸钷𬬻𬬹𬬿𬭁倻𫢸倧舯鸰脎鱽𫗧烠𬊈涍涄涢涐𬒈袯疍𨺙㛚翀𬳿𫄨绤𬘫琎珺堎堐𫮃壸㙍聍萚䓫勚䓬菍萣䓨梼梽梾厣硔鿎硙硚䴕啫𬱖𬟽啴铏𫓯𫟹铕𫟼铖铘铞铥铴鸺㿠鸼悆䝙脶鱾猄𠅤庼䴔阌淏𬇹𬍡𬤇𫍯裈𬤊𫍲谞𬯎媖婳婌𬘬𬘭𬴂𫘦绹𫟅𬘯骕𫘧堾堼㙘塅𪣻𡎚萳蒇蒈蒎蒄𬃊鹀𬷕酦詟𫐐辌𬹼晪𧿹𫶇崾嵚翙𫖮圐赑赒鿏铹𬭊铽𨱇𫓶锊锍锎𬭎锓颋筜舾𫖯腘腙𬱟鲃𫛭馉𫷷鄌遆𬮱𬊤𣸣溁溇敩裣毵𬴃𫘨缊缐骙瑓瑆䴖瑝瑔𤧛瑂蓢蓣榃榅𬪩碃𬒔䃅辒𬨎𫐓龆暕鹍𫫇赗锖𫓹锘锳锧锪𬭚锫锬𬭛䅟𬕂筻筼筶鹎艉腽鲉鲊鲌䲟𬶋𬶍鲏飔𦝼馌瘅鹒阘𫔶煃煋滠滧滘愭塱𫌀禒谫鹔𫖳戤𫘪𫘬瑧𫞩瑨瑷墘𡐓墚撖𪤗蔹槚𣗋槜𬸘酾碶𬒗𥔲碹𫚖䴗嶍圙𨱏锼𬭤锿镃镄镅鹙箨㙦鲒鲕𫚕鲖鲗鲘鲙𬶐𬶏𩽾飗𬸚鲝漖潆㽏㮾𬤝𬙂麹叇鹝慭暶䗖㠇镆镈镋镎𬭩䴘鹟𩾃鲦鲪鲬橥鹠鹡鹢潖潵澛潽𬸣禤𫍽𬴊璥璒𬞟𥕢豮𫟦𬺈𫠜鹾蹅䗛𪩘嶦𬭬𨱑𬭯篯衠鲭鲯鲺鲹𫗴亸𬸦熻燊燚燏澪黉鹨𫄷𤩽璮櫆蟏㘎𬭳镤𬭶𫔍镥镨𬭸𨱔𬭼𫔎穙簕𬸪䲠𬶟鲾𬶠鲿鳁鳂鳈鳉襕𬶨𦈡𫄸鬶𬟁鹲𥖨䗴镮镱酂簰䲢鳑鳒鹱鹯𦒍䎖瀔䴙𬙊㰀鳘𬶭𩾌鳚鳛彟颥𨟠𬶮𨭉㸌骦𬙋𤫉𬺓鳠鳡鳣礵鹴鳤𫚭
```

