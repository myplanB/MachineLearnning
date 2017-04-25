import jieba

seg_list = jieba.cut(r"小明1995年毕业于北京清华大学",cut_all=False)
print("Default Mode:"," ".join(seg_list))

seg_list = jieba.cut(r"小明1995年毕业于北京清华大学")
print(" ".join(seg_list))

seg_list = jieba.cut(r"小明1995年毕业于北京清华大学",cut_all=True)
print("Full Mode:"," ".join(seg_list))

seg_list = jieba.cut_for_search(r"小明硕士毕业于中国科学院计算所，后在日本京都大学深造")
print("/ ".join(seg_list))