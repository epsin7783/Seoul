import pandas as pd
import datetime as dt

#=============== csv 파일 불러오기 =================
test = pd.read_csv("마포구맛집.csv", index_col=0)
test_name = test['name'] 
test_addr = test['addr']
test_grade = test['grade']
test_review = test['review']


#===================  전처리 ===================================
import re

def extract_word(text):
    hangul = re.compile('[^가-힣]') 
    result = hangul.sub(' ', str(text)) 
    return result

for i in range(len(test_review)):
    test_review[i] = extract_word(test['review'][i])


# print("Before Extraction : ",df['review'][0])
# print("After Extraction : ", extract_word(df['review'][0]))

# print("Before Extraction : ",df['review'][150])
# print("After Extraction : ", extract_word(df['review'][150]))



# ============== 가게 이름, 주소 중복 제거 =====================
test_name_sum = []
for i in range(len(test_name)):
    if (i+1) % 3 == 0:
        test_name_sum.append(test_name[i])

test_name_sum = pd.DataFrame(test_name_sum)
test_name_sum.columns = ['name']


test_addr_sum = []
for i in range(len(test_addr)):
    if (i+1) % 3 == 0:
        test_addr_sum.append(test_addr[i])

test_addr_sum = pd.DataFrame(test_addr_sum)
test_addr_sum.columns = ['addr']


#==================별점 합치기 =====================
test_grade_sum = []
for i in range(len(test_grade)):
    if (i+1) % 3 == 0:
        test_grade_sum.append(test_grade[i]) 

test_grade_sum = pd.DataFrame(test_grade_sum)
test_grade_sum.columns = ['grade']
# print(test_grade_sum)




#================ 리뷰 합치기 =============================
test_review_combine = []
test_review_sum = []
chunk_size = 3;
for i in range(0, len(test_review), chunk_size):
    test_review_combine.append(test_review[i:i+chunk_size])

for i in range(len(test_review_combine)):
    test_review_sum.append(' '.join(map(str, test_review_combine[i])))
    
test_review_sum = pd.DataFrame(test_review_sum)
test_review_sum.columns = ['review']
# print(test_review_sum)


#=============== 합치기 ====================================
# print(test_name_sum) 
# print(test_addr_sum) 
# print(test_grade_sum)
# print(test_review_sum)


result1 = pd.concat([test_name_sum, test_addr_sum],axis=1)
result2 = pd.concat([result1, test_grade_sum], axis=1)
result3 = pd.concat([result2, test_review_sum], axis=1)
result3.to_csv("마포구맛집_전처리최종.csv")
print(result3)



#=================== 크롤링 csv 파일 전처리 ======================
# test = pd.read_csv("../test/마포구맛집.csv", names=['crawl'])
# split_test = test.crawl.str.split(',',expand=True)
# split_test.columns = ['name', 'addr','grade', 'review','1','2','3']
# split_test.drop(labels=['1','2','3'], axis=1, inplace=True)
# split_test.to_csv("마포구맛집.csv")
# print(split_test)