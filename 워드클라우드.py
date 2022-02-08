# -*- coding: utf-8 -*-
"""워드클라우드

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lT5FAfqouZu-Ee6y432GnM3gZZOlhd_g

2021.12.04. 언어정보학연구
"""

!pip install wordcloud

!apt-get install fonts-nanum*
!apt-get install fontconfig

from wordcloud import WordCloud
import matplotlib.pyplot as plt

input(.)WordPhrase =

path = '/user/share/fonts/truetype/nanum/NanumGothic.ttf'
wordcloud = WordCloud(font_path=path, background_color='white', max_words=100, width=1000, height=800).generate(WordPhrase)
#불용어 설정 : 남자, 여자

plt.figure(figsize=(11,11)) 
plt.imshow(wordcloud, interpolation='lanczos') #이미지 부드럽기의 정도
plt.axis('off') 
plt.show()

read = WordPhrase.split()
relen = len(WordPhrase)
print("단어 수: %d" % relen)



