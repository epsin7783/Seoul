from django.shortcuts import render, redirect
import logging
from django.views.generic.base import View
from django.template import loader
from django.http.response import HttpResponse
from datetime import datetime, timedelta
from plan.models import Plan, Like, PlanComment, PlanCount, Wishlist, LiveRank, Eatplace
from django.core.exceptions import ObjectDoesNotExist
from django.utils.dateformat import DateFormat
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib import messages
from django.contrib.auth.models import User
import pandas as pd
import stylecloud
import schedule
import time
import os
from django.db.models import Q

logger = logging.getLogger( __name__ )

class PlanView(View):
    def get(self, request):
        template = loader.get_template("planwrite.html")
        memid = request.session.get('memid')
        nickname = request.session.get('nickname')
        if memid :
            context ={
                'memid' :memid,
                'nickname' : nickname,

                }
        else:
            context={
                }
        return HttpResponse(template.render( context, request ))

    def post(self, request):
        template = loader.get_template("planwrite.html")
        gu = request.POST["gu"]
        tt = Eatplace.objects.filter(gu=gu).order_by("-review_star").values()[:15]
        ttname = [] 
        ttstar = []
        for i in range(15):
            ttname.append(tt[i]['name'])
            ttstar.append(tt[i]['review_star'])
            
        print(ttname[0])
        context ={
                'ttname' : ttname,
                'ttstar' : ttstar,
                }
        return HttpResponse(json.dumps(context), content_type='application/json')


# 일정만들기
class PlanWriteView(View):
    def get(self, request):
        pass

    def post(self, request):
        p_title = request.POST["title"]
        p_sdate = request.POST["sdate"]
        p_code = 5012

        p_nickname = request.POST["nickname"]
        id = request.POST["id"]

        p_days = int(request.POST["days"])-1
        date = datetime.strptime(p_sdate, "%Y-%m-%d")
        p_edate = date+timedelta(days=p_days)
        p_edate = p_edate.strftime("%Y-%m-%d")


        day1 = ""
        day2 = ""
        day3 = ""
        day4 = ""
        day5 = ""
        day6 = ""
        day7 = ""
        addr_1 = request.POST.getlist("addr_1")
        addr_2 = request.POST.getlist("addr_2")
        addr_3 = request.POST.getlist("addr_3")
        addr_4 = request.POST.getlist("addr_4")
        addr_5 = request.POST.getlist("addr_5")
        addr_6 = request.POST.getlist("addr_6")
        addr_7 = request.POST.getlist("addr_7")
        
        place1 = request.POST.getlist("place_1")
        place2 = request.POST.getlist("place_2")
        place3 = request.POST.getlist("place_3")
        place4 = request.POST.getlist("place_4")
        place5 = request.POST.getlist("place_5")
        place6 = request.POST.getlist("place_6")
        place7 = request.POST.getlist("place_7")
        
        addr = addr_1 + addr_2 + addr_3 + addr_4 + addr_5 + addr_6 + addr_7
        
        place_name = place1 + place2 + place3 + place4 + place5 + place6 + place7
        
        place_log = str(place_name)[1:-1]
        place_log = place_log.replace("'", "")
        place_log = place_log.replace(" ", "")
        place_log = place_log.replace(",", "\n")
        
        logger.info(place_log)
        
        os.remove("/home/bit/Seoul/main/static/images/sctest.png")
        stylecloud.gen_stylecloud(file_path="/home/bit/Seoul/log/logfile3.log",
                                icon_name="fas fa-cloud",
                                palette="colorbrewer.sequential.PuBu_5",
                                size=512,
                                font_path="/home/bit/Seoul/main/static/fonts/H2HDRM.TTF",
                                background_color='white',
                                gradient="horizontal",
                                output_name="/home/bit/Seoul/main/static/images/sctest.png")
        
        
        path = "/home/bit/Seoul/log/logfile3.log"
        df = pd.read_csv(path, names = ['place'])
        
        result = df.groupby(['place']).value_counts().sort_values(ascending=False)
        result = result.to_frame();
        result.rename(columns={0:'counts'}, inplace=True)
        result.reset_index(drop = False, inplace=True)
        
        file_path = '/home/bit/Seoul/log/test.csv'
        result.to_csv(file_path,header=True)
        
        place = result["place"]
        counts = result["counts"]
        
        ### 워드클라우드
        
        # def job():
        #     stylecloud.gen_stylecloud(file_path="E:\Cloud\workspace\Seoul\log\logfile3.log",
        #                               icon_name="fas fa-comment",
        #                               palette="colorbrewer.sequential.Blues_5",
        #                               size=(1024, 512),
        #                               font_path="C:\Windows\Fonts\H2HDRM.TTF",
        #                               background_color='white',
        #                               gradient="horizontal",
        #                               output_name="E:\Cloud\workspace\Seoul\main\static\images\sctest.png")
        #
        # schedule.every(5).seconds.do(job)
        #
        # while True:
        #     schedule.run_pending()
        #     time.sleep(1)
            
            
        
        
        for i in range(len(place_name)) : 
            
            lcount = LiveRank.objects.filter(place=place_name[i]).count()
            
            if lcount == 0 :
                lr = LiveRank(
                    counts = 1,
                    place = place_name[i],
                    ) 
                lr.save()
            else:
                lr = LiveRank.objects.get(place=place_name[i])
                lr.counts = int(lr.counts) + 1
                lr.save()
        

        
        
        
        
        if p_days == 0:
            place1 = request.POST.getlist("place_1")
            plen1 = len(place1)
            addr1 = request.POST.getlist("addr_1")
            time1 = request.POST.getlist("time_1")
            memo1 = request.POST.getlist("memo_1")
            day1 = place1 + addr1 + time1 + memo1
            day1.insert(0, plen1) 
        elif p_days == 1:
            place1 = request.POST.getlist("place_1")
            plen1 = len(place1)
            addr1 = request.POST.getlist("addr_1")
            time1 = request.POST.getlist("time_1")
            memo1 = request.POST.getlist("memo_1")
            day1 = place1 + addr1 + time1 + memo1 
            day1.insert(0, plen1) 
            place2 = request.POST.getlist("place_2")
            plen2 = len(place2)
            addr2 = request.POST.getlist("addr_2")
            time2 = request.POST.getlist("time_2")
            memo2 = request.POST.getlist("memo_2")
            day2 = place2 + addr2 + time2 + memo2
            day2.insert(0, plen2) 
        elif p_days == 2:
            place1 = request.POST.getlist("place_1")
            plen1 = len(place1)
            addr1 = request.POST.getlist("addr_1")
            time1 = request.POST.getlist("time_1")
            memo1 = request.POST.getlist("memo_1")
            day1 = place1 + addr1 + time1 + memo1 
            day1.insert(0, plen1) 
            place2 = request.POST.getlist("place_2")
            plen2 = len(place2)
            addr2 = request.POST.getlist("addr_2")
            time2 = request.POST.getlist("time_2")
            memo2 = request.POST.getlist("memo_2")
            day2 = place2 + addr2 + time2 + memo2
            day2.insert(0, plen2)
            place3 = request.POST.getlist("place_3")
            plen3 = len(place3)
            addr3 = request.POST.getlist("addr_3")
            time3 = request.POST.getlist("time_3")
            memo3 = request.POST.getlist("memo_3")
            day3 = place3 + addr3 + time3 + memo3
            day3.insert(0, plen3)
        elif p_days == 3:
            place1 = request.POST.getlist("place_1")
            plen1 = len(place1)
            addr1 = request.POST.getlist("addr_1")
            time1 = request.POST.getlist("time_1")
            memo1 = request.POST.getlist("memo_1")
            day1 = place1 + addr1 + time1 + memo1 
            day1.insert(0, plen1) 
            place2 = request.POST.getlist("place_2")
            plen2 = len(place2)
            addr2 = request.POST.getlist("addr_2")
            time2 = request.POST.getlist("time_2")
            memo2 = request.POST.getlist("memo_2")
            day2 = place2 + addr2 + time2 + memo2
            day2.insert(0, plen2)
            place3 = request.POST.getlist("place_3")
            plen3 = len(place3)
            addr3 = request.POST.getlist("addr_3")
            time3 = request.POST.getlist("time_3")
            memo3 = request.POST.getlist("memo_3")
            day3 = place3 + addr3 + time3 + memo3
            day3.insert(0, plen3)
            place4 = request.POST.getlist("place_4")
            plen4 = len(place4)
            addr4 = request.POST.getlist("addr_4")
            time4 = request.POST.getlist("time_4")
            memo4 = request.POST.getlist("memo_4")
            day4 = place4 + addr4 + time4 + memo4
            day4.insert(0, plen4)
        elif p_days == 4:
            place1 = request.POST.getlist("place_1")
            plen1 = len(place1)
            addr1 = request.POST.getlist("addr_1")
            time1 = request.POST.getlist("time_1")
            memo1 = request.POST.getlist("memo_1")
            day1 = place1 + addr1 + time1 + memo1 
            day1.insert(0, plen1) 
            place2 = request.POST.getlist("place_2")
            plen2 = len(place2)
            addr2 = request.POST.getlist("addr_2")
            time2 = request.POST.getlist("time_2")
            memo2 = request.POST.getlist("memo_2")
            day2 = place2 + addr2 + time2 + memo2
            day2.insert(0, plen2)
            place3 = request.POST.getlist("place_3")
            plen3 = len(place3)
            addr3 = request.POST.getlist("addr_3")
            time3 = request.POST.getlist("time_3")
            memo3 = request.POST.getlist("memo_3")
            day3 = place3 + addr3 + time3 + memo3
            day3.insert(0, plen3)
            place4 = request.POST.getlist("place_4")
            plen4 = len(place4)
            addr4 = request.POST.getlist("addr_4")
            time4 = request.POST.getlist("time_4")
            memo4 = request.POST.getlist("memo_4")
            day4 = place4 + addr4 + time4 + memo4
            day4.insert(0, plen4)
            place5 = request.POST.getlist("place_5")
            plen5 = len(place5)
            addr5 = request.POST.getlist("addr_5")
            time5 = request.POST.getlist("time_5")
            memo5 = request.POST.getlist("memo_5")
            day5 = place5 + addr5 + time5 + memo5
            day5.insert(0, plen5)
        elif p_days == 5:
            place1 = request.POST.getlist("place_1")
            plen1 = len(place1)
            addr1 = request.POST.getlist("addr_1")
            time1 = request.POST.getlist("time_1")
            memo1 = request.POST.getlist("memo_1")
            day1 = place1 + addr1 + time1 + memo1 
            day1.insert(0, plen1) 
            place2 = request.POST.getlist("place_2")
            plen2 = len(place2)
            addr2 = request.POST.getlist("addr_2")
            time2 = request.POST.getlist("time_2")
            memo2 = request.POST.getlist("memo_2")
            day2 = place2 + addr2 + time2 + memo2
            day2.insert(0, plen2)
            place3 = request.POST.getlist("place_3")
            plen3 = len(place3)
            addr3 = request.POST.getlist("addr_3")
            time3 = request.POST.getlist("time_3")
            memo3 = request.POST.getlist("memo_3")
            day3 = place3 + addr3 + time3 + memo3
            day3.insert(0, plen3)
            place4 = request.POST.getlist("place_4")
            plen4 = len(place4)
            addr4 = request.POST.getlist("addr_4")
            time4 = request.POST.getlist("time_4")
            memo4 = request.POST.getlist("memo_4")
            day4 = place4 + addr4 + time4 + memo4
            day4.insert(0, plen4)
            place5 = request.POST.getlist("place_5")
            plen5 = len(place5)
            addr5 = request.POST.getlist("addr_5")
            time5 = request.POST.getlist("time_5")
            memo5 = request.POST.getlist("memo_5")
            day5 = place5 + addr5 + time5 + memo5
            day5.insert(0, plen5)
            place6 = request.POST.getlist("place_6")
            plen6 = len(place6)
            addr6 = request.POST.getlist("addr_6")
            time6 = request.POST.getlist("time_6")
            memo6 = request.POST.getlist("memo_6")
            day6 = place6 + addr6 + time6 + memo6
            day6.insert(0, plen6)
        elif p_days == 6:
            place1 = request.POST.getlist("place_1")
            plen1 = len(place1)
            addr1 = request.POST.getlist("addr_1")
            time1 = request.POST.getlist("time_1")
            memo1 = request.POST.getlist("memo_1")
            day1 = place1 + addr1 + time1 + memo1 
            day1.insert(0, plen1) 
            place2 = request.POST.getlist("place_2")
            plen2 = len(place2)
            addr2 = request.POST.getlist("addr_2")
            time2 = request.POST.getlist("time_2")
            memo2 = request.POST.getlist("memo_2")
            day2 = place2 + addr2 + time2 + memo2
            day2.insert(0, plen2)
            place3 = request.POST.getlist("place_3")
            plen3 = len(place3)
            addr3 = request.POST.getlist("addr_3")
            time3 = request.POST.getlist("time_3")
            memo3 = request.POST.getlist("memo_3")
            day3 = place3 + addr3 + time3 + memo3
            day3.insert(0, plen3)
            place4 = request.POST.getlist("place_4")
            plen4 = len(place4)
            addr4 = request.POST.getlist("addr_4")
            time4 = request.POST.getlist("time_4")
            memo4 = request.POST.getlist("memo_4")
            day4 = place4 + addr4 + time4 + memo4
            day4.insert(0, plen4)
            place5 = request.POST.getlist("place_5")
            plen5 = len(place5)
            addr5 = request.POST.getlist("addr_5")
            time5 = request.POST.getlist("time_5")
            memo5 = request.POST.getlist("memo_5")
            day5 = place5 + addr5 + time5 + memo5
            day5.insert(0, plen5)
            place6 = request.POST.getlist("place_6")
            plen6 = len(place6)
            addr6 = request.POST.getlist("addr_6")
            time6 = request.POST.getlist("time_6")
            memo6 = request.POST.getlist("memo_6")
            day6 = place6 + addr6 + time6 + memo6
            day6.insert(0, plen6)
            place7 = request.POST.getlist("place_7")
            plen7 = len(place7)
            addr7 = request.POST.getlist("addr_7")
            time7 = request.POST.getlist("time_7")
            memo7 = request.POST.getlist("memo_7")
            day7 = place7 + addr7 + time7 + memo7
            day7.insert(0, plen7)

        # p_code = Null

        dto = Plan(
            p_title = p_title,
            p_sdate = p_sdate,
            p_edate = p_edate,
            p_nickname = p_nickname,
            id = id,
            p_days = p_days,
            p_code = p_code,
            day1 = day1,
            day2 = day2,
            day3 = day3,
            day4 = day4,
            day5 = day5,
            day6 = day6,
            day7 = day7,
            addr = addr,
            place_name = place_name,
            ref = 1,
            restep = 0
            )
        
        dto.save()
        

        return redirect("/member/mypage")


# 일정공유게시판 리스트
class PlanShareView(View):
    def get(self, request):
        template = loader.get_template("plansharepage.html")
        memid = request.session.get('memid')
        count = Plan.objects.all().count()

        pagesize = 8
        pageblock = 3
        pagenum = request.GET.get("pagenum")
        if not pagenum :
            pagenum = "1"
        pagenum = int( pagenum )
        start = ( pagenum -1 ) * pagesize       # ( 5 - 1 ) * 10 + 1    41
        end = start + pagesize                  # 41 + 10 - 1           50
        if end > count :
            end = count 
        nono = ""
        dtostest = Plan.objects.filter(~Q(p_content='')).order_by( "-p_no" )[start:end]
        # dtostest = Plan.objects.raw(
        #     '''
        #     select * from plan_plan where p_content != "" order by p_no desc
        #     '''
        #     )
        number = count - ( pagenum - 1 ) * int( pagesize )

        pagecount = count // int( pagesize )        # 51 // 10    5
        if count % int( pagesize ) > 0 : 
            pagecount += 1                          # 6
        startpage = pagenum // int( pageblock ) * int( pageblock ) + 1
                                                    # 5 // 10 * 10 + 1        1
        if pagenum % pageblock == 0 :
            startpage -= pageblock
        endpage = startpage + pageblock - 1         # 1 + 10 - 1              10
        if endpage > pagecount : 
            endpage = pagecount
        pages = range( startpage, endpage+1)





        if memid == "":
            memid = "n";
        nickname = request.session.get("nickname")
        dtos = Plan.objects.all()

        # dtoLike = Plan.objects.all()[:4]
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
        # dtostest = Plan.objects.raw(
        #     '''
        #     select * from plan_plan where p_content != "" order by p_no desc
        #     '''
        #     )
        context = {
            "memid" : memid,
            "nickname" : nickname,
            "dtos" : dtos,
            "dtoLike" : dtoLike,
            "dtoCount" : dtoCount,
            "count" : count,
            "dtostest":dtostest,
            "number" : number,
            "pagenum" : pagenum,
            "pagecount" : pagecount,
            "startpage" : startpage,
            "endpage" : endpage,
            "pages" : pages,
            "pageblock" : pageblock,

            }

        return HttpResponse(template.render(context, request))

    def post(self, request):
        template = loader.get_template("plansharepage.html")
        count = Plan.objects.all().count()
        memid = request.session.get('memid')
        pagesize = 12
        pageblock = 3
        pagenum = request.GET.get("pagenum")        
        if not pagenum :
            pagenum = "1"
        pagenum = int( pagenum )
        start = ( pagenum -1 ) * pagesize       # ( 5 - 1 ) * 10 + 1    41
        end = start + pagesize                  # 41 + 10 - 1           50
        if end > count :
            end = count 

        dtostest = Plan.objects.filter(~Q(p_content='')).order_by( "-p_no" )[start:end]
        number = count - ( pagenum - 1 ) * int( pagesize )

        pagecount = count // int( pagesize )        # 51 // 10    5
        if count % int( pagesize ) > 0 : 
            pagecount += 1                          # 6
        startpage = pagenum // int( pageblock ) * int( pageblock ) + 1
                                                    # 5 // 10 * 10 + 1        1
        if pagenum % pageblock == 0 :
            startpage -= pageblock
        endpage = startpage + pageblock - 1         # 1 + 10 - 1              10
        if endpage > pagecount : 
            endpage = pagecount
        pages = range( startpage, endpage+1)


        searched = request.POST['searched']
        search_keyword = request.POST['search_keyword']
        if len(search_keyword) > 0:
            if search_keyword == 'title_content':
                #plans = Plan.objects.filter(p_title__contains=searched)  
                plans = Plan.objects.raw(
                    '''
                    select * from plan_plan where p_title like '%%'''+searched+'''%%' and p_content != ""
                    '''
                    )
            elif search_keyword == 'writer_content':
                #plans = Plan.objects.filter(p_nickname__contains=searched) 
                plans = Plan.objects.raw(
                    '''
                    select * from plan_plan where p_nickname like '%%'''+searched+'''%%' and p_content != ""
                    '''
                    )

            dtoLike = Plan.objects.raw(
                '''
                select distinct a.p_no, count(b.id) as cnt, a.* from plan_plan a left join plan_like b on a.p_no=b.p_no where a.p_content != "" group by a.p_no having cnt > 0 limit 4
                '''
                )
            # dtoCount = Plan.objects.all()[:4]
            dtoCount = Plan.objects.raw(
                '''
                select *, count from plan_plan a, plan_plancount b where a.p_no=b.p_no and a.p_content != "" order by count desc limit 4
                '''
                )
        context = {
            "searched" : searched,
            "plans" : plans,
            "dtoLike" : dtoLike,
            "dtoCount" : dtoCount,
            "dtostest" : dtostest,
            "memid" : memid
            }
        return HttpResponse(template.render(context, request))
        


# 일정공유게시판 자세히보기
class PlanShareDetailView(View):
    def get(self, request):
        template = loader.get_template("plansharedetail.html")
        no = request.GET["no"]
        memid = request.session.get('memid')
        nickname = request.session.get("nickname")
        dto = Plan.objects.get(p_no=no)
        dtos = PlanComment.objects.filter( boardNum=no ).order_by('-no')
        count = Like.objects.filter(p_no=no).count()

        day1 = dto.day1.replace("\'", "")
        day1 = day1.replace("[", "")
        day1 = day1.replace("]", "")
        day1 = day1.split(",")
        
        day2 = dto.day2.replace("\'", "")
        day2 = day2.replace("[", "")
        day2 = day2.replace("]", "")
        day2 = day2.split(",")
        
        day3 = dto.day3.replace("\'", "")
        day3 = day3.replace("[", "")
        day3 = day3.replace("]", "")
        day3 = day3.split(",")
        
        day4 = dto.day4.replace("\'", "")
        day4 = day4.replace("[", "")
        day4 = day4.replace("]", "")
        day4 = day4.split(",")
        
        day5 = dto.day5.replace("\'", "")
        day5 = day5.replace("[", "")
        day5 = day5.replace("]", "")
        day5 = day5.split(",")
        
        day6 = dto.day6.replace("\'", "")
        day6 = day6.replace("[", "")
        day6 = day6.replace("]", "")
        day6 = day6.split(",")
        
        day7 = dto.day7.replace("\'", "")
        day7 = day7.replace("[", "")
        day7 = day7.replace("]", "")
        day7 = day7.split(",")
        
        pcount = PlanCount.objects.filter(p_no=no).count()
        if pcount == 0:
            pp = PlanCount(
                count = 1,
                id = memid,
                p_no = no,
                )
            pp.save()
        else:
            pp = PlanCount.objects.get(p_no=no)
            pp.count = pp.count + 1
            pp.save()

        try:
            like = Like.objects.get(p_no=dto.p_no, id=memid)
        except ObjectDoesNotExist:
            like = None

        if memid or User.is_authenticated :
            context = {
                "pp" : pp,
                "memid" : memid,
                "nickname" : nickname,
                "dtos" : dtos,
                "dto" : dto,
                "like" : like,
                "count" : count,
                "day1" : day1,
                "day2" : day2,
                "day3" : day3,
                "day4" : day4,
                "day5" : day5,
                "day6" : day6,
                "day7" : day7,
                }
        else:
            context = {}
        return HttpResponse(template.render(context, request))

# 일정공유게시판 좋아요
class PlanLikeView(View):
    @method_decorator(csrf_exempt)
    def post(self, request):
        template = loader.get_template("plansharedetail.html")
        p_no = request.POST["p_no"]
        id = request.POST['id']
        result = 0
        try:
            sdto = Like.objects.get(id=id, p_no=p_no)
            sdto.delete()
            result = 1
        except ObjectDoesNotExist:
            dto = Like(
            id = id,
            p_no = p_no
            )
            dto.save()
            result = 0
        
        context = {
            "result" : result,
            }
        return HttpResponse(json.dumps(context), content_type='application/json') 


# 일정공유게시판 리플등록
class CommentWriteView(View):
    def get(self, request):
        pass
    def post(self, request):
        template = loader.get_template("detail.html")
        nick = request.POST["nick"]
        comment = request.POST["comment"]
        boardNum = request.POST["boardNum"]
        date = DateFormat(datetime.now()).format("Y-m-d")
        dto = PlanComment(
            nick = nick,
            comment = comment,
            boardNum = boardNum,
            date = date
            )
        dto.save()


        return redirect("/plan/plansharedetail?no="+boardNum)


# 일정공유게시판 리플삭제
class ReplyDelView(View):
    def get(self, request):
        no = request.GET["no"]
        number = request.GET["number"]
        dto = PlanComment.objects.get( no=no )
        dto.delete()

        return redirect("/plan/plansharedetail?no="+number)

# 일정공유게시판 리플수정
class ReplyModView(View):
    def get(self, request):
        template = loader.get_template("detail.html")
        no = request.GET["no"]
        num = request.GET["num"]
        comment = request.GET["comment"]
        date = DateFormat(datetime.now()).format("Y-m-d")
        dto = PlanComment.objects.get( no=no )
        dto.comment = comment
        dto.date = date
        dto.save()
        return redirect("/plan/plansharedetail?no="+num)

    def post(self, request) :
        pass

# 일정공유게시판 글쓰기(내용 및 썸네일 등록)
class PlanShareWriteView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def get(self, request):
        template = loader.get_template("plansharewrite.html")
        memid = request.session.get("memid")
        nickname = request.session.get("nickname")
        context = {
            "memid" : memid,
            "nickname" : nickname,
            }

        return HttpResponse(template.render(context, request))
    def post(self, request):
        id = request.POST["id"]
        content = request.POST["content"]
        # img = request.FILES["image"]
        img = request.FILES.get("image")
        no = request.POST["planno"]
        dto = Plan.objects.get(p_no=no)

        dto.p_content = content
        if img :
            dto.image = img


        dto.save()
        return redirect("/plan/plansharepage")

# 플랜공유 글쓰기 새창에서 일정선택
class PlanSelectView(View):
    def get(self, request):
        template = loader.get_template("planselect.html")
        id = str(request.session.get("memid"))
        # dto = Plan.objects.filter(id=id)
        dto = Plan.objects.raw(
            '''
            select * from plan_plan where id="'''+id+'''" and p_content = "" order by p_no desc
            '''
            )
        context = {
            "dto" : dto
            }

        return HttpResponse(template.render(context, request))


class PlanGuideView(View):
    def get(self, request):
        template = loader.get_template("planguide.html")
        memid = request.session.get('memid')
        nickname = request.session.get('nickname')
        context = {
            'memid' :memid,
            'nickname' : nickname,
            }
        
        return HttpResponse(template.render(context, request))


#공유일정 -> 위시리스트
class WishlistView(View):
    def post(self, request):
        template = loader.get_template("plansharedetail.html")
        no = request.POST["no"]
        id = request.session.get("memid")
        dto = Plan.objects.get(p_no=no)
        wdto = Wishlist.objects.filter(plan_no =no, id=id)
        num = str(dto.p_no)
        if id == dto.id:
            messages.info(request, "본인 일정은 위시리스트에 추가할 수 없습니다.")
            return redirect("/plan/plansharedetail?no="+num)
        
        if wdto:
            messages.info(request, "이미 위시리스트에 추가한 일정입니다.")
            return redirect("/plan/plansharedetail?no="+num)

        else:
            wdto = Wishlist(
                p_title = dto.p_title,
                p_nickname = dto.p_nickname,
                p_sdate = dto.p_sdate,
                p_edate = dto.p_edate,
                p_days = dto.p_days,
                p_memo = dto.p_memo,
                p_code = dto.p_code,
                p_content = dto.p_content,
                id = id,
                day1 = dto.day1,
                day2 = dto.day2,
                day3 = dto.day3,
                day4 = dto.day4,
                day5 = dto.day5,
                day6 = dto.day6,
                day7 = dto.day7,
                addr = dto.addr,
                image = dto.image,
                ref = 1,
                restep = 0,
                plan_no = dto.p_no,
                )
            wdto.save()
            # context = {
            #     "msg" : "저장 완료"
            #     }
            
        # return HttpResponse(template.render(context, request))
        return redirect('/member/wishlist')








