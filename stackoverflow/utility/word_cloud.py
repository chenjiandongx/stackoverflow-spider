from collections import Counter
from collections import OrderedDict
import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from pprint import pprint


tags = []
with open(r"e:\python\stackoverflow\data\data1.json", "r", encoding="utf-8") as f1:
    data1 = json.load(f1)
    for _, value in enumerate(data1):
        tags.extend(value['tags'])


with open(r"e:\python\stackoverflow\data\data2.json", "r", encoding="utf-8") as f2:
    data2 = json.load(f2)
    for _, value in enumerate(data2):
        tags.extend(value['tags'])

counter = Counter(tags)
counter_most = counter.most_common(200)

# counter_dict = dict(counter_most)
# sort_dict= sorted(counter_dict.items(), key=lambda value:value[1], reverse=True)
# pprint(OrderedDict(sort_dict))

wordcloud = WordCloud(font_path=r"e:\Font\msyh.ttf",
                      width=1200,
                      height=600,
                      max_words=200).generate_from_frequencies(dict(counter_most))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()

wordcloud.to_file(r'e:\python\stackoverflow\images\word_cloud.jpg')
