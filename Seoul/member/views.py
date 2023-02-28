from django.shortcuts import render, redirect
import logging
from django.views.generic.base import View
from django.template import loader
from django.http.response import HttpResponse, JsonResponse
from member.models import Member
from django.utils.dateformat import DateFormat
from datetime import  datetime, timedelta
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist, ValidationError
import json, traceback
from django.contrib.auth.hashers import BCryptPasswordHasher
from django.template.context_processors import request
from plan.models import Plan, Wishlist
from Seoul.settings import get_secret
import requests
import urllib

logger = logging.getLogger( __name__ )



class MainView(View):
    def get(self, request ) :
        template = loader.get_template( "index.html" )
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

class JoinView( View ) :
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def get(self, request ) :
        template = loader.get_template( "join.html" )
        context = {}
        logger.info( "join.html" )
        return HttpResponse( template.render( context, request ) )        
    def post(self, request ) :
        phone=""
        phone1=request.POST.get('phone1')
        phone2=request.POST.get('phone2')
        phone3=request.POST.get('phone3')
        if phone1 and phone2 and phone3:
            phone = phone1 + '-' + phone2 + '-' +phone3 
        dto=Member(
            id=request.POST['id'],
            pw=request.POST['pw'],
            name=request.POST['name'],
            nickname=request.POST['nickname'],
            addr0=request.POST['addr0'],
            addr1=request.POST['addr1'],
            addr2=request.POST['addr2'],
            level=1,
            email=request.POST['email'],
            phone=phone,
            regdate=DateFormat(datetime.now()).format("Y-m-d"),
            catePlace = request.POST.getlist("place"),
            cateFood = request.POST.getlist("food")
            ) 
        dto.save()
        return redirect('login') #추후에 로그인창 만들면 바꿀것
 

class LoginView(View):
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def get(self,request):
        template = loader.get_template( "login.html" )
        context={
            }
        return HttpResponse( template.render( context, request ) )
    def post(self,request):
        id = request.POST["id"]
        pw = request.POST["pw"]
        message = ""
        try :
            dto = Member.objects.get( id=id )
            if pw == dto.pw :
                request.session["memid"] = id
                request.session["nickname"] = dto.nickname
                return redirect( "/main" )
            else : 
                message = "입력하신 비밀번호가 다릅니다"
        except ObjectDoesNotExist :
            message = "입력하신 아이디가 없습니다"            
        template = loader.get_template( "login.html" )    
        context = {
            "message" : message,
            }
        return HttpResponse( template.render( context, request ) )
        

class ConfirmView(View):
    def get(self,request):
        template = loader.get_template( "confirm.html" )
        id = request.GET['id']
        result =0
        try:
            # 아이디 중복
            Member.objects.get(id=id)
            result=1
        except ObjectDoesNotExist:
            # 아이디 없음
            result=0
            
        context={
            'id':id,
            'result':result,
            }
        return HttpResponse( template.render( context, request ) )


class LogoutView( View ) :
    def get( self, request ) :
        del( request.session["memid"] )
        return redirect( "/main" )


class MypageView(View):
    def get(self, request):
        template = loader.get_template("mypage.html")
        memid = request.session.get('memid')
        nickname = request.session.get('nickname')
        dto = Member.objects.get( id=memid )
        if memid :
            dtos = Plan.objects.filter(id=memid).order_by("-p_no")
            context ={
                'dto' : dto,
                'dtos' : dtos,
                'memid' :memid,
                'nickname' : nickname,
                
                }
        else:
            context={
                }
        return HttpResponse(template.render( context, request ))
    
    def post(self, request):
        pass


class MypageDeleteView( View ) :
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def get(self, request ) :
        template = loader.get_template( "mypagedelete.html" )
        memid = request.session.get('memid')
        nickname = request.session.get('nickname')
        dto = Member.objects.get( id=memid )
        if memid :
            context ={
                'memid' :memid,
                'nickname' : nickname,
                'dto':dto,
                }
        else:
            context={
                }
        return HttpResponse(template.render( context, request ))     
    def post(self, request ) :
        id = request.session.get( "memid" )
        dto = Member.objects.get( id=id )
        social = dto.social
        if social == "k" or social == "n":
            dto.delete()
            del( request.session["memid"] )
            return redirect( "main" ) 
        else : 
            pw = request.POST["pw"]
            if pw == dto.pw :
                dto.delete()
                del( request.session["memid"] )
                return redirect( "main" )                        
            else :
                template = loader.get_template( "mypagedelete.html" )
                context = {
                    "message" : "비밀번호가 다릅니다",
                    }
                return HttpResponse( template.render( context, request ) )


# 회원정보 수정
class MypageModifyView( View ) :
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def get(self, request ) :
        template = loader.get_template( "mypagemodify.html" )
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
    def post(self, request ) :
        id = request.session.get( "memid" )
        nickname = request.session.get("nickname")
        pw = request.POST["pw"]
        dto = Member.objects.get( id=id )
         # 받아오기
        catePlace = dto.catePlace.replace("\'", "")
        catePlace = catePlace.replace("[", "")
        catePlace = catePlace.replace("]", "")
        catePlace = catePlace.replace(" ", "")
        catePlace = catePlace.split(",")
        
        cateFood = dto.cateFood.replace("\'", "")
        cateFood = cateFood.replace("[", "")
        cateFood = cateFood.replace("]", "")
        cateFood = cateFood.replace(" ", "")
        cateFood = cateFood.split(",")
        if pw == dto.pw :
            template = loader.get_template( "mypagemodifyPro.html" )
            e = dto.email.split( "@" )
            if dto.phone :
                t = dto.phone.split( "-" )            
                context = {
                    "dto" : dto,
                    "e" : e,
                    "t" : t,
                    "catePlace" : catePlace,
                    "cateFood" : cateFood,
                    "memid" : id,
                    "nickname" : nickname
                    }  
            else :
                context = {
                    "dto" : dto,
                    "e" : e,
                    "catePlace" : catePlace,
                    "cateFood" : cateFood,
                    "memid" : id,
                    "nickname" : nickname
                    }           
            return HttpResponse( template.render( context, request ) )                        
        else :
            template = loader.get_template( "mypagemodify.html" )
            context = {
                "message" : "비밀번호가 다릅니다",
                }
            return HttpResponse( template.render( context, request ) )

class MypageModifyProView( View ) :
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)    
    def post(self, request ) :
        id = request.session.get( "memid" )
        pw = request.POST["pw"]
        nickname = request.POST["nickname"]
        email = request.POST["email"]
        phone = ""
        phone1 = request.POST["phone1"]
        phone2 = request.POST["phone2"]
        phone3 = request.POST["phone3"]
        if( phone1 and phone2 and phone3 ) :
            phone = phone1 + "-" + phone2 + "-" + phone3
        addr0 = request.POST["addr0"]
        addr1 = request.POST["addr1"]
        addr2 = request.POST["addr2"]
        # catePlace = request.POST["place"]
        # cateFood = request.POST["food"]
        catePlace = request.POST.getlist("place")
        cateFood = request.POST.getlist("food")
        
        dto = Member.objects.get( id=id )
        dto.pw = pw
        dto.nickname = nickname
        dto.email = email
        dto.phone = phone
        dto.addr0 = addr0
        dto.addr1 = addr1
        dto.addr2 = addr2
        dto.catePlace = catePlace
        dto.cateFood = cateFood
        dto.save()
        return redirect( "/main" )
        
# 아이디 중복확인 ajax
class IdChkView(View):
    def get(self, request):
        template = loader.get_template("idchk.html")
        context = {}
        return HttpResponse(template.render(context, request))
    
    def post(self, request):
        template = loader.get_template("join.html")
        id = request.POST["id"]
        dto = Member.objects.get(id=id)
        result = 0
        try:
            # 아이디가 있을때
            Member.objects.get(id=id)
            result = 1
        except ObjectDoesNotExist:
            # 아이디가 없을때
            result = 0
        context = {
            "id" : id,
            "result" : result,
            }
        return HttpResponse(template.render(context, request))
    
# 닉네임 중복확인 ajax
class NicknameChkView(View):
    def get(self, request):
        template = loader.get_template("nicknamechk.html")
        context = {}
        return HttpResponse(template.render(context, request))
    
    def post(self, request):
        template = loader.get_template("join.html")
        nickname = request.POST["nickname"]
        dto = Member.objects.get(nickname=nickname)
        result = 0
        try:
            # 아이디가 있을때
            Member.objects.get(nickname=nickname)
            result = 1
        except ObjectDoesNotExist:
            # 아이디가 없을때
            result = 0
        context = {
            "nickname" : nickname,
            "result" : result,
            }
        return HttpResponse(template.render(context, request))


#위시리스트 페이지
class WishlistView(View):
    def get(self, request):
        
        template = loader.get_template("wishlist.html")
        memid = request.session.get('memid')
        dtos = Wishlist.objects.filter(id=memid)
        nickname = request.session.get('nickname')
        dto = Member.objects.get( id=memid )
        if memid :
            context ={
                'dto' : dto,
                'memid' :memid,
                'nickname' : nickname,
                "dtos" : dtos
                }
        else:
            context={
                }
        return HttpResponse(template.render( context, request ))
    
    def post(self, request):
        pass

# 아이디찾기
class FindIdView(View):
    def get(self, request):
        template = loader.get_template("findid.html")
        context = {}
        return HttpResponse(template.render(context, request))

    def post(self, request):
        template = loader.get_template("findid.html")
        email = request.POST["email"]  
        result = 0
        try:
            dto = Member.objects.get(email=email)
            result = 1
            context = {
                "id": dto.id,
                "result": result
                }
        except ObjectDoesNotExist:     
            msg = ""
            result = 0
            context = {
                "result": result,
                "msg": "해당하는 이메일이 없습니다"     
            }
        return HttpResponse(template.render(context, request))


# 비밀번호 찾기
class FindPwView(View):
    def get(self, request):
        template = loader.get_template("findpw.html")
        context = {}
        return HttpResponse(template.render(context, request))
    
    def post(self, request):
        id = request.POST["id"]
        email = request.POST["email"]  
        result = 0
        try:
            dto = Member.objects.get(email=email, id=id)
            if dto.email:
                result = 1
                context = {
                    "result": result,
                    "id" : id,
                }
                template = loader.get_template("changepw.html")
                return HttpResponse(template.render(context, request))
        except ObjectDoesNotExist:     
            msg = ""
            result = 0
            context = {
                "result": result,
                "msg": "해당하는 아이디 또는 이메일이 없습니다"     
            }
            template = loader.get_template("findpw.html")
            return HttpResponse(template.render(context, request))

# 비밀번호 변경페이지
class ChangePwView(View):    
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs) 
    
    def get(self, request ) :
        template = loader.get_template( "changepw.html" )
        context = {}
        return HttpResponse( template.render( context, request ) )   
       
    def post(self, request ) :
        id = request.POST["id"]
        pw = request.POST["pw"]
        
        dto = Member.objects.get( id=id)
        dto.pw = pw
        dto.save()
        return redirect( "/member/login" )


# class KakaoView(View):
#     def get(self, request):
#         kakao_api = "https://kauth.kakao.com/oauth/authorize?response_type=code"
#         redirect_uri = "http://:8000/users/kakao/callback"
#         client_id = ""
#
#         return redirect(f"{kakao_api}&client_id={client_id}&redirect_uri")


class MypageDetailView(View):
    def get(self, request):
        template = loader.get_template("mypagedetail.html")
        no = request.GET["no"]
        dto = Plan.objects.get(p_no=no)
        memid = request.session.get("memid")
        nickname = request.session.get("nickname")
        dtoid = Member.objects.get( id=memid )
        # e_date = datetime.strptime(dto.p_sdate, "%Y-%m-%d")
        # e_date = e_date+timedelta(days=dto.p_days)
        # logger.info(e_date)
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
            
        context = {
            "dtoid" : dtoid,
            "dto" : dto,
            "day1" : day1,
            "day2" : day2,
            "day3" : day3,
            "day4" : day4,
            "day5" : day5,
            "day6" : day6,
            "day7" : day7,
            "memid" : memid,
            "nickname" : nickname,
            }
        
        return HttpResponse(template.render(context, request))
    
    def post(self, request):
        pass


# 마이페이지에서 플랜삭제
class PlanDelView(View):
    def get(self, request):
        no = request.GET["no"]
        
        dto = Plan.objects.get(p_no=no)
        dto.delete()
    
        return redirect("/member/mypage")



class WishlistDetailView(View):
    def get(self, request):
        template = loader.get_template("wishlistdetail.html")
        memid = request.session.get("memid")
        nickname = request.session.get("nickname")
        no = request.GET["no"]
        dto = Wishlist.objects.get(p_no=no)
        dtoid = Member.objects.get( id=memid )
        # e_date = datetime.strptime(dto.p_sdate, "%Y-%m-%d")
        # e_date = e_date+timedelta(days=dto.p_days)
        # logger.info(e_date)
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
            
        context = {
            "dtoid" : dtoid,
            "dto" : dto,
            "day1" : day1,
            "day2" : day2,
            "day3" : day3,
            "day4" : day4,
            "day5" : day5,
            "day6" : day6,
            "day7" : day7,
            "memid" : memid,
            "nickname" : nickname
            }
        
        return HttpResponse(template.render(context, request))
    
    def post(self, request):
        pass

#위시리스트에서 위시목록 삭제
class WishDelView(View):
    def get(self, request):
        no = request.GET["no"]
        
        dto = Wishlist.objects.get(p_no=no)
        message = ""
        
        dto.delete()
    
        return redirect("/member/wishlist")



#######################카카오 로그인#################################
class KakaoLoginView(View):
    def get(self, request):
        with open('secrets.json') as f:
            secrets = json.loads(f.read())
        app_key = get_secret("KAKAO_REST_API")
        redirect_uri = 'http://master:8000/member/callback'
        kakao_auth_api = 'https://kauth.kakao.com/oauth/authorize?response_type=code'
        return redirect(
            f'{kakao_auth_api}&client_id={app_key}&redirect_uri={redirect_uri}'
        )
        
    def post(self, request):
        with open('secrets.json') as f:
            secrets = json.loads(f.read())
        app_key = get_secret("KAKAO_REST_API")
        redirect_uri = 'http://master:8000/member/callback'
        kakao_auth_api = 'https://kauth.kakao.com/oauth/authorize?response_type=code'
        return redirect(
            f'{kakao_auth_api}&client_id={app_key}&redirect_uri={redirect_uri}'
        )
    
   
class KakaoLoginCallbackView(View):
    def get(self, request):
        auth_code = request.GET.get('code')
        kakao_token_api = "https://kauth.kakao.com/oauth/token"
        data = {
            "grant_type" : "authorization_code",
            "client_id" : get_secret("KAKAO_REST_API"),
            "client_secret" : get_secret("KAKAO_SECURITY"),
            "redirect_uri" : "http://master:8000/member/callback",
            "code" : auth_code
            }
        
        token_response =  requests.post(url=kakao_token_api,data=data)
        print(token_response)
        access_token =token_response.json().get('access_token')
        user_info_response = requests.get('https://kapi.kakao.com/v2/user/me', headers={"Authorization":f'Bearer ${access_token}', "Content-type": "application/x-www-form-urlencoded;charset=utf-8"})

        user = user_info_response.json()
        logger.info(user)
        id = user['id']
        nickname = user['properties']['nickname']
        pw = user['id']
        if "email" in user['kakao_account'] : 
            email = user['kakao_account']['email']
        else:
            email = ""
        if "phone_number" in user['kakao_account']:
            phone = user["kakao_account"]['phone_number']
        else:
            phone = ""
           
        regdate = user['connected_at']
        if Member.objects.filter(id=id).exists():
            request.session["memid"]=id
            request.session["nickname"]=nickname
            dto = Member.objects.get(id=id)
            dto.save()
            return redirect("/main")
        else:
            dto = Member(
                id = id,
                name = nickname,
                nickname = nickname,
                pw = pw,
                email = email,
                regdate = regdate,
                phone = phone,
                social = "k",
            )
            dto.save()
        request.session["memid"]=id
        request.session["nickname"]=nickname
        return redirect("/main")




logger= logging.getLogger(__name__)

# Create your views here.
class NaverLoginView(View):
    def get(self, request):
        with open('secrets.json') as f:
            secrets = json.loads(f.read())
        app_key = get_secret("NAVER_ID")
        redirect_uri = 'http://master:8000/member/callback2'
        naver_auth_api = 'https://nid.naver.com/oauth2.0/authorize?response_type=code'
        state = "login"
        return redirect(
            f'{naver_auth_api}&client_id={app_key}&redirect_uri={redirect_uri}&state={state}'
        )
        #네이버 로그인 인증 요청 : https://nid.naver.com/oauth2.0/authorize
        #접근 토큰의 발급, 갱신, 삭제 요청 : https://nid.naver.com/oauth2.0/token
    def post(self):
        pass
    
class NaverLoginCallback2View(View):
    def get(self, request):
        with open('secrets.json') as f:
            secrets= json.loads(f.read())
        client_id = get_secret("NAVER_ID")
        client_secret = get_secret("NAVER_SECRET")
        code = request.GET.get('code')
        logger.info(code)
        state = request.GET.get('state')
        logger.info(state)
        authorization_code = "authorization_code"
        token_api = "https://nid.naver.com/oauth2.0/token"
        token_response = requests.get(token_api, params={'grant_type':authorization_code,'client_id':client_id, 'client_secret':client_secret, 'code':code,'state':state})
        logger.info(token_response)
        access_token = token_response.json().get('access_token')
        logger.info(access_token)
        refresh_token = token_response.json().get('refresh_token')
        token_type=token_response.json().get('token_type')
        expires_in=token_response.json().get('expires_in')
        
        header = "Bearer " + access_token
        url = "https://openapi.naver.com/v1/nid/me"
        requested = urllib.request.Request(url)
        requested.add_header("Authorization", header)
        response = urllib.request.urlopen(requested)
        rescode = response.getcode()
        if(rescode ==200):
            response_body = response.read()
            response_content = response_body.decode('utf-8')
            response_content = json.loads(response_content)
        else:
            print("Error Code : "+rescode)
        
            
        id = response_content["response"]["id"]
        pw = response_content["response"]["id"]
        name = response_content["response"]["name"] 
        email = response_content["response"]["email"]

        if Member.objects.filter(id=id).exists():
            request.session["memid"]=id
            request.session["name"]=name
            dto = Member.objects.get(id=id)

            return redirect("/main")
        else:
            dto = Member(                
                id = id,
                pw = pw,
                name = name,
                email = email,
                social = "n",                
                )
            
            dto.save()
            
        request.session["memid"]=id
        request.session["name"]=name
        return redirect("/main")








