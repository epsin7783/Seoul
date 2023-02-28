from django.shortcuts import render
from django.views.generic.base import View
from django.template import loader
from django.http.response import HttpResponse
from plan.models import Plan, LiveRank, Eatplace
from main.models import Pyspark
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model._ridge import Ridge
from sklearn.linear_model._coordinate_descent import Lasso
import json

logger = logging.getLogger( __name__ )


class MainView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def get(self, request ) :
        template = loader.get_template( "index.html" )
        
        dtoRank = LiveRank.objects.raw(
            '''
            select * from plan_liverank order by counts desc limit 10
            '''
            )        
        
        dtos = Plan.objects.all()
        dtoLike = Plan.objects.raw(
            '''
            select distinct a.p_no, count(b.id) as cnt, a.* from plan_plan a left join plan_like b on a.p_no=b.p_no where a.p_content != "" group by a.p_no having cnt > 0 order by cnt desc limit 4
            '''
            )
        # dtoCount = Plan.objects.all()[:4]
        dtoCount = Plan.objects.raw(
            '''
            select *, count from plan_plan a, plan_plancount b where a.p_no=b.p_no and a.p_content != "" order by count desc limit 4
            '''
            )
        memid = request.session.get('memid')
        nickname = request.session.get('nickname')
        context ={
            'memid' :memid,
            'nickname' : nickname,
            "dtoRank" : dtoRank,
            "dtos" : dtos,
            "dtoLike" : dtoLike,
            "dtoCount" : dtoCount,
            }
        # s = pd.read_csv('/home/bit/Seoul/final.csv')
        # ss=[]
        # for i in range(len(s)):
        #                     st = (s['no'][i],s['name'][i],s['address'][i],s['review_star'][i],s['review_text'][i],s['gu'][i])
        #                     ss.append(st)
        # for i in range(len(s)):
        #             Eatplace.objects.create(no=ss[i][0], name=ss[i][1], address=ss[i][2], review_star=ss[i][3], review_text=ss[i][4], gu=ss[i][5])
        return HttpResponse(template.render( context, request ))
       
    # def post(self, request):
    #     template = loader.get_template( "index.html" )
    #
    #     locationk = request.POST['locationk']
    #     day = request.POST['day']
    #     dayint = int(day)
    #
    #
    #
    #     # 로그 데이터 불러오기
    #     pop_rate = pd.read_csv("/home/bit/Seoul/log/logfile4.log", names=["place", "datetime", "min", "max"])
    #
    #     ##데이터 전처리
    #     # 데이터 날짜 시간 나누기
    #     test1 = pop_rate["datetime"].str.split(' ')
    #     pop_rate["date"] = test1.str.get(0)
    #     pop_rate["time"] = test1.str.get(1) 
    #
    #     # 날짜와 시간 데이터 형식 변환
    #     pop_rate["date"] = pd.to_datetime(pop_rate["date"])
    #     pop_rate["time"] = pd.to_datetime(pop_rate["time"])
    #     pop_rate["time"] = pop_rate["time"].dt.hour
    #
    #     # 요일 칼럼 추가
    #     pop_rate["day"] = pop_rate["date"].dt.weekday
    #     # 월요일 0, 화요일 1.... 일요일 6
    #
    #     # weekday_list = ['월', '화', '수', '목', '금', '토', '일']
    #     # test["day"] = test.apply(lambda x : weekday_list[x['weekday']], axis=1)
    #
    #     # 해당 시간대 인구수 평균
    #     pop_rate["population"] = (pop_rate["min"] + pop_rate["max"])/2
    #     pop_rate = pop_rate.astype({"population" : "int"})
    #
    #     # 머신러닝에 필요 없는 데이터 삭제
    #     pop_rate = pop_rate.drop(["date", "datetime"], axis='columns')
    #
    #     # 머신러닝에 사용할 데이터셋 만들기
    #     # 돌릴때 With n_samples=0, test_size=0.3 and train_size=None.... 이런 오류가 뜨면 scikit-learn 버전을 0.19.1로 수정
    #
    #
    #     x = pop_rate[pop_rate["place"]==locationk]
    #     x = x[x["day"]==dayint]
    #     x = x.drop(["place"], axis='columns')
    #     y = x["population"]
    #
    #     logger.info(x)
    #     logger.info("--------------------------")
    #     logger.info(y)
    #
    #     pred_sum=[];
    #     pred_value=[];
    #
    #     for i in range(24):
    #         t = x[x["time"]==i]
    #         xx = t.drop(["population"], axis='columns')
    #         yy = t.drop(["min", "max", "time", "day"], axis='columns')
    #
    #         data_x = xx      # min, max, time, day 값 들어간 데이터셋
    #         data_y = yy      # population 값 들어간 데이터셋
    #
    #         # logger.info("--------------------------")
    #         # logger.info(xx)
    #         # logger.info("--------------------------")
    #         # logger.info(yy)
    #
    #         # 훈련시키기
    #         train_x, test_x, train_y, test_y = train_test_split(data_x, data_y, test_size=0.3, random_state=100)
    #
    #         # 릿지회귀 사용 -> 사용 이유) 수치 분석하여 예측값을 추측하는데 사용을 많이하며 두개 이상의 참고데이터가 있을때 사용
    #         rg = Ridge()
    #         model = rg.fit(data_x, data_y)
    #         pred_y = model.predict(test_x)      # 예측값    
    #
    #         sum=0;
    #         for j in range(len(pred_y)) : 
    #             sum += int(pred_y[j])
    #
    #
    #         aver = int(sum/len(pred_y))
    #         pred_sum.append(aver)
    #
    #
    #     logger.info(pred_sum)    
    #     # logger.info(x)       
    #     # logger.info(y)
    #
    #
    #     context ={
    #         "pred_sum" : pred_sum,
    #         "locationk" : locationk,
    #         "dayint" : dayint
    #         }
    #
    #     return HttpResponse(json.dumps(context), content_type='application/json') 
    def post(self, request):
        template = loader.get_template( "index.html" )
        
        locationk = request.POST['locationk']
        day = request.POST['day']
        # dayint = int(day)
       
        get_pred = Pyspark.objects.filter(name=locationk).values()
        get_pred = Pyspark.objects.filter(day=day).values()
        
        pred_sum = []
        for i in range(len(get_pred)):
            pred_sum.append(get_pred[i]['prediction'])
            
        
       
        context ={
            'locationk':locationk,
            'pred_sum':pred_sum
            }

        return HttpResponse(json.dumps(context), content_type='application/json') 

class GoogleView( View ):
    def get(self, request):
        template = loader.get_template( "googleapitest.html" )
        context={
            }
        return HttpResponse( template.render( context, request ) )
    def post(self, request):
        pass

class TestView( View ):
    def get(self, request):
        template = loader.get_template( "index.html" )
        context={
            }
        return HttpResponse( template.render( context, request ) )
    def post(self, request):
        pass
    
