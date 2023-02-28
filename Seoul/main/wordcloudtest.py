import urllib.request as req
import urllib.parse as pa
import requests
import json
import xml.etree.ElementTree as ET
import pandas as pd
from bs4 import BeautifulSoup

# location =  {'name': '창덕궁·종묘',
#              'name' :  "광화문·덕수궁", 'name' : "경복궁·서촌마을",
#              'name' : "서울숲공원", 'name' : "남산공원", 'name' : "국립중앙박물관·용산가족공원", 'name' : "서울대공원", 'name' : "이촌한강공원", 'name' : "월드컵공원", 'name' : "잠실한강공원", 'name' : "반포한강공원", 'name' : "잠실한강공원", 'name' : "뚝섬한강공원", 'name' : "망원한강공원", 'name' : "북서울꿈의숲",
#              'name' : "종로·청계 관광특구", 'name' : "이태원 관광특구", 'name' : "잠실 관광특구", 'name' : "명동 관광특구", 'name' : "동대문 관광특구", 'name' : "강남 MICE 관광특구", 'name' : "홍대 관광특구",
#              'name' : "여의도", 'name' : "인사동·익선동", 'name' : "DMC(디지털미디어시티)", 'name' : "북촌한옥마을", 'name' : "성수카페거리", 'name' : "가로수길", 'name' : "압구정로데오거리", 'name' : "창동 신경제 중심지", 'name' : "영등포 타임스퀘어", 'name' : "노량진", 'name' : "쌍문동 맛집거리", 'name' : "수유리 먹자골목", 'name' : "낙산공원·이화마을",
#              'name' : "구로디지털단지역", 'name' : "선릉역", 'name' : "서울역", 'name' : "가산디지털단지역", 'name' : "역삼역", 'name' : "강남역", 'name' : "고속터미널역", 'name' : "용산역", 'name' : "교대역", 'name' : "연신내역", 'name' : "신촌·이대역", 'name' : "왕십리역", 'name' : "신림역", 'name' : "건대입구역", 'name' : "신도림역"
#             }

location = "서울역"

for i in range(len(location)):
    url = "http://openapi.seoul.go.kr:8088/4f4f44766365737035374170685766/xml/citydata/1/5/"
    response = requests.get(url, params=location)
    
    
    
    # url = url + "?" + params
    # data = req.urlopen(url).read().decode( "utf-8" )
    # print(data)
    result = BeautifulSoup(response.content, 'xml')
    print(result)
    
    
    
# url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
# values = {
#         "stnId" : "109"
#     }
# import urllib.parse as pa
# params = pa.urlencode( values )
# url = url + "?" + params
# data = req.urlopen(url).read().decode( "utf-8" )
#