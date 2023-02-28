import re
import pandas as pd
from tqdm import tqdm
from konlpy.tag import Okt
from pykospacing import Spacing
from collections import Counter

def extract_word(text):
    hangul = re.compile('[^가-힣]') 
    result = hangul.sub(' ', str(text)) 
    return result

df = pd.read_csv("강남구맛집.csv")
result = extract_word(df)

print("Before Extraction : ",df['review'][0])
print("After Extraction : ", extract_word(df['review'][0]))

print("Before Extraction : ",df['review'][150])
print("After Extraction : ", extract_word(df['review'][150]))

spacing = Spacing()
# print("Before Fixing : ",df['review'][136])
# print("After Fixing : ", spacing(df['review'][136]))
# print("Before Fixing : ",df['review'][150])
# print("After Fixing : ", spacing(df['review'][150]))

from konlpy.tag import Okt
okt = Okt()
words = " ".join(df['review'].tolist())
words = okt.morphs(words, stem=True)
remove_one_word = [x for x in words if len(x)>1 or x=="닉"]
len(remove_one_word)

frequent = Counter(remove_one_word).most_common()
print(frequent)


with open('stopwords.txt', 'r') as f:
    list_file = f.readlines()
stopwords = list_file[0].split(",")
remove_stopwords = [x for x in remove_one_word if x not in stopwords]
len(remove_stopwords)




