import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


#reading files

rf = pd.read_csv(r'psy.csv')
yt_comment_words = " "
stopwords = set(STOPWORDS)


for value in rf.content:
    value = str(value)
    tokens = value.split()
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
        yt_comment_words += " ".join(tokens) + " "

wordcloud = WordCloud(width=800,height=800, background_color='white', stopwords=stopwords, min_font_size=10).generate(yt_comment_words)

plt.figure(figsize=(8,8), facecolor=None)
plt.imshow(wordcloud)
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()