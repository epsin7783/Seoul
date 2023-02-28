import urllib.request as req 
import urllib
import urllib.parse as pa
import pandas as pd 
from bs4 import BeautifulSoup as bs
import requests
import xmltodict
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.font_manager as fm

##### 폰트 종류 확인법 #####
# fl = [font.name for font in fm.fontManager.ttflist]
# print(fl)


###### api 데이터 값 가져오기 #######

location = [
                   "창덕궁·종묘", "광화문·덕수궁", "경복궁·서촌마을",
                   "서울숲공원", "남산공원", "국립중앙박물관·용산가족공원", "서울대공원", "이촌한강공원", "월드컵공원", "잠실한강공원", "반포한강공원", "잠실한강공원", "뚝섬한강공원", "망원한강공원", "북서울꿈의숲",
                   "종로·청계 관광특구", "이태원 관광특구", "잠실 관광특구", "명동 관광특구", "동대문 관광특구", "강남 MICE 관광특구", "홍대 관광특구",
                   "여의도", "인사동·익선동", "DMC(디지털미디어시티)", "북촌한옥마을", "성수카페거리", "가로수길", "압구정로데오거리", "창동 신경제 중심지", "영등포 타임스퀘어", "노량진", "쌍문동 맛집거리", "수유리 먹자골목", "낙산공원·이화마을",
                   "구로디지털단지역", "선릉역", "서울역", "가산디지털단지역", "역삼역", "강남역", "고속터미널역", "용산역", "교대역", "연신내역", "신촌·이대역", "왕십리역", "신림역", "건대입구역", "신도림역"
                   ]
               

for i in range(len(location)) : 
    key = "485a677978646f6e383450644c6241"
    url = "http://openapi.seoul.go.kr:8088/" + key + "/xml/citydata/1/5/" + location[i] 
    req = requests.get(url).content
    xmlObject = xmltodict.parse(req)
     
    area = xmlObject['SeoulRtd.citydata']['CITYDATA']['AREA_NM']
    time = xmlObject['SeoulRtd.citydata']['CITYDATA']['LIVE_PPLTN_STTS']['LIVE_PPLTN_STTS']['PPLTN_TIME']
    min = xmlObject['SeoulRtd.citydata']['CITYDATA']['LIVE_PPLTN_STTS']['LIVE_PPLTN_STTS']['AREA_PPLTN_MIN']
    max = xmlObject['SeoulRtd.citydata']['CITYDATA']['LIVE_PPLTN_STTS']['LIVE_PPLTN_STTS']['AREA_PPLTN_MAX']
    print(area, ",", time, ",", min, ",", max)
    
    #df = pd.DataFrame.from_dict([allData]) 
    # print(type(df))