# -*- coding: utf-8 -*-
"""국어어휘론연구_연어_211031_첨부용.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1701vmjLZPSRj_yOhC4UCpSHH9kZUwYl3

2021.10.31.12:28 국어어휘론연구 주제: 연어 
분석 대상 : 9종의 대학한국어교재의 듣기지문 125,000어절
첨부용
"""

!pip install kss #kss 
import kss #kss 라이브러리

!pip install konlpy #konlpy  패키지
from konlpy.tag import Kkma #(정확도가 높아 느림/ Kkma: 5.6988 secs)
kkma = Kkma()
from konlpy.tag import Okt  #(속도가 빠름/Twitter: 1.4870 secs)

#텍스트 전처리 과정

WordPhrase = input("어절을 확인할 텍스트를 넣어주세요>") #텍스트 변수 입력

print("전체 어절 수 = ", len(WordPhrase.split(' ')))

from wordcloud import WordCloud
import matplotlib.pyplot as plt

!apt-get install fonts-nanum*
!apt-get install fontconfig

path = '/user/share/fonts/truetype/nanum/NanumGothic.ttf'
wordcloud = WordCloud(font_path=path, background_color='white', max_words=150, width=1500, height=1100).generate(WordPhrase)
#불용어 설정 : 남자, 여자

plt.figure(figsize=(22,22)) 
plt.imshow(wordcloud, interpolation='lanczos') #이미지 부드럽기의 정도
plt.axis('off') 
plt.show()

read = WordPhrase.split()
relen = len(WordPhrase)
print("단어 수: %d" % relen)

text = input("텍스트를 넣어주세요>") #Frequency analysis

WordPhrase = kkma.pos(text) #.morphs / pos

read = text.split(" ") # 문자열 공백 기준으로 구분
relen = len(read)
print("어절 수: %d" % relen)

Di = {}
counter1 = 0

for i in range(relen):
  plus = 0
  for j in range(relen):  
    if WordPhrase[i] == WordPhrase[j]:
      plus += 1
      counter1 += 1
  Di[WordPhrase[i]] = plus
  if counter1 > 10000:
    print("10000 iteration") 
    counter1 = 0

As = sorted(Di.items(), key=lambda x: x[1], reverse=True)

Dil = len(Di)

for g in range(Dil):
	print("\'%s\'의 개수 : %s" % (As[g][0], As[g][1]))

# WORDCLOUD/Frequency analysis 10.31.12:37 국어어휘론연구-주제명 : 연어 
# 분석 대상 9종 대학한국어교재 듣기지문 125,000어절