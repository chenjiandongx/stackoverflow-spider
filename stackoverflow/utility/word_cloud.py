from collections import Counter
from collections import OrderedDict
import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from pprint import pprint


tags = []
with open(r"e:\python\stackoverflow\data\result.json", "r", encoding="utf-8") as f1:
    data1 = json.load(f1)
    for _, value in enumerate(data1):
        tags.extend(value['tags'])

# 使用 Counter 统计词频
counter = Counter(tags)
counter_most = counter.most_common(200)


# 排序输出关键词词频情况
# counter_dict = dict(counter_most)
# sort_dict= sorted(counter_dict.items(), key=lambda value:value[1], reverse=True)
# pprint(OrderedDict(sort_dict))


# 生成词云
wordcloud = WordCloud(font_path=r"e:\Font\msyh.ttf",
                      width=1200,
                      height=600,
                      max_words=200).generate_from_frequencies(dict(counter_most))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()

wordcloud.to_file(r'e:\python\stackoverflow\images\word_cloud.jpg')
