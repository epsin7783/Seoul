from django.shortcuts import render, redirect
from django.views.generic.base import View
import logging
from django.template import loader
from django.http.response import HttpResponse
from board.models import Board, ImageBoard, Comment
from django.utils.dateformat import DateFormat
from datetime import datetime
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


logger = logging.getLogger( __name__ )

class ListView( View ) :
    def get(self, request ) :
        template = loader.get_template( "list.html" )
        count = Board.objects.all().count()

        pagesize = 10
        pageblock = 3
        pagenum = request.GET.get("pagenum")
        if not pagenum :
            pagenum = "1"
        pagenum = int( pagenum )
        start = ( pagenum -1 ) * pagesize       # ( 5 - 1 ) * 10 + 1    41
        end = start + pagesize                  # 41 + 10 - 1           50
        if end > count :
            end = count 
        
        dtos = Board.objects.order_by( "-ref", "restep" )[start:end]
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
        pages = range( startpage, endpage+1 )
        
        memid = request.session.get('memid')
        nickname = request.session.get('nickname')
        context = {
            "count" : count,
            "dtos" : dtos,
            "number" : number,
            "pagenum" : pagenum,
            "pagecount" : pagecount,
            "startpage" : startpage,
            "endpage" : endpage,
            "pages" : pages,
            "pageblock" : pageblock,
            'memid' :memid,
            'nickname' : nickname,
            }
        return HttpResponse( template.render( context, request ) )
    
    

    
class BWriteView( View ) :
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def get(self, request ) :
        template = loader.get_template( "bwrite.html" )
        memid = request.session.get("memid")
        nickname = request.session.get("nickname")
        # 제목글
        ref = 1
        restep = 0
        relevel = 0
        num = request.GET.get("num")
        if num == None :
            # 제목글 
            try :
                # 글이 있는 경우
                maxnum = Board.objects.order_by("-num").values()[0]["num"]
                ref = maxnum + 1            # 그룹화아이디 = 글번호최대값 + 1
            except IndexError :
                # 글이 없는 경우
                ref = 1
        else :
            # 답변글
            ref = request.GET["ref"]
            restep = request.GET["restep"]
            relevel = request.GET["relevel"]
            res = Board.objects.filter( ref__exact=ref ).filter( restep__gt=restep )
            for re in res :
                re.restep = re.restep + 1
                re.save()
            restep = int( restep ) + 1
            relevel = int( relevel ) + 1
        
        context = {
            "num" : num,
            "ref" : ref,
            "restep" : restep,
            "relevel" : relevel,
            "memid" : memid,
            "nickname" : nickname,
            }
        return HttpResponse( template.render( context, request ) )
        
    def post(self, request ) :
        dto = Board(
            writer = request.POST["writer"],
            subject = request.POST["subject"],
            # passwd = request.POST["passwd"],
            content = request.POST["content"],
            readcount = 0,
            ref = request.POST["ref"],
            restep = request.POST["restep"],
            relevel = request.POST["relevel"],
            regdate = DateFormat( datetime.now() ).format( "Ymd" ),
            ip = request.META.get( "REMOTE_ADDR" ),
            id = request.POST["id"]         
            )
        dto.save()
        return redirect( "board:list" )

class DetailView( View ) :
    def get(self, request ) :
        template = loader.get_template( "detail.html" )
        num = request.GET["num"]
        pagenum = request.GET["pagenum"]
        number = request.GET["number"]
        dto = Board.objects.get( num=num )
        dtos = Comment.objects.filter( boardNum=number ).order_by('-no')
        if dto.ip != request.META.get( "REMOTE_ADDR" ) :
            dto.readcount += 1
            dto.save()
            
        memid = request.session.get('memid')
        nickname = request.session.get('nickname')
        if memid or User.is_authenticated : 
            context = {
                "dtos" : dtos,
                "dto" : dto,
                "num" : num,
                "pagenum" : pagenum,  
                "number" : number,
                'memid' :memid,
                'nickname' : nickname,          
                }
        else:
            context = {}
        return HttpResponse( template.render( context, request ) )
    
class BDeleteView( View ) :
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def get(self, request ) :
        num = request.GET["num"]
        pagenum = request.GET["pagenum"]
        dto = Board.objects.get( num=num )
        dto.delete()
        return redirect( "board:list" )                
    def post(self, request ) :
        # num = request.POST["num"]
        # pagenum = request.POST["pagenum"]
        # passwd = request.POST["passwd"]
        # dto = Board.objects.get( num=num )
        # if passwd == dto.passwd :
        #     # 비밀번호가 같다
        #     res = Board.objects.filter( ref__exact=dto.ref ).filter( restep__exact=dto.restep+1 ).filter( relevel__gt=dto.relevel )
        #     if len( res ) == 0 :
        #         # 답글이 없다
        #         re = Board.objects.filter( ref__exact=dto.ref ).filter( restep__gt=dto.restep )
        #         for r in re :
        #             r.restep = r.restep - 1;
        #             r.save()
        #         dto.delete()
        #     else :
        #         # 답글이 있다        
        #         dto.readcount = -1
        #         dto.save()
        #     return redirect( "board:list" )    
        #
        # else :
        #     # 비밀번호가 다르다
        #     template = loader.get_template( "bdelete.html" )
        #     context = {
        #         "num" : num,
        #         "pagenum" : pagenum,
        #         "message" : "비밀번호가 다릅니다",
        #         }
        #     return HttpResponse( template.render( context, request ) )
        pass
    
    
class BModifyView( View ) :
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def get(self, request ) :
        template = loader.get_template( "bmodify.html" )
        num = request.GET["num"]
        pagenum = request.GET["pagenum"]
        context = {
            "num" : num,
            "pagenum" : pagenum,
            }
        return HttpResponse( template.render( context, request ) )
    def post(self, request ) :    
        num = request.POST["num"]
        pagenum = request.POST["pagenum"]
        passwd = request.POST["passwd"]        
        dto = Board.objects.get( num=num )
        if passwd == dto.passwd :
            # 수정페이지 
            template = loader.get_template( "bmodifypro.html" )
            context = {
                "num" : num,
                "pagenum" : pagenum,
                "dto" : dto,
                }
            return HttpResponse( template.render( context, request ) )        
        else :
            # 비밀번호 입력 페이지
            template = loader.get_template( "bmodify.html" )
            context = {
                "num" : num,
                "pagenum" : pagenum,
                "message" : "비밀번호가 다릅니다",               
                }
            return HttpResponse( template.render( context, request ) )
    
    
class BModifyPro( View ) : 
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def get(self, request):
        num = request.GET["num"]
        pagenum = request.GET["pagenum"]      
        dto = Board.objects.get( num=num )
        # 수정페이지 
        template = loader.get_template( "bmodifypro.html" )
        context = {
            "num" : num,
            "pagenum" : pagenum,
            "dto" : dto,
            }
        return HttpResponse( template.render( context, request ) )        
        
    def post(self, request ) :
        num = request.POST["num"]
        pagenum = request.POST["pagenum"]
        dto = Board.objects.get( num=num )
        dto.subject = request.POST["subject"]
        dto.content = request.POST["content"]
        # dto.passwd = request.POST["passwd"]
        dto.save()
        return redirect( "board:list" )
           


class ImageView( View ) :
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def get(self, request ) :
        template = loader.get_template( "imageupload.html" )
        context = {}
        return HttpResponse( template.render( context, request ) )
    def post(self, request ) :
        title = request.POST["title"]
        img = request.FILES["image"]
        name = request.POST.get["image"]
        dto = ImageBoard(
            title = title,
            image = img,
            name = name,
            );
        dto.save()
        return redirect( "board:imagedown" )

class ImageDownView( View ) :
    def get(self, request ) :
        template =  loader.get_template("imagedown.html")
        dtos = ImageBoard.objects.all()
        context={
            "dtos":dtos,
            }
        return HttpResponse( template.render( context, request ) )

#처리를 하는것이 post 안하면 get방식
class StorageView( View ) :
    def get(self, request ) :
        template = loader.get_template( "storage.html" )
        context = {}
        return HttpResponse( template.render( context, request ) )

class SQLView( View ) :
    def get(self, request ) :
        template=loader.get_template("sql.html")
        context={
            
            }
        return HttpResponse( template.render( context, request ) )


class AjaxView(View):
    def get(self, request):
        template = loader.get_template("ajax.html")
        context = {}
        return HttpResponse(template.render(context, request))
    def post(self, request):
        template=loader.get_template("result.html")
        id = request.POST["id"]
        passwd = request.POST["passwd"];
        context={
            "id":id,
            "passwd":passwd,
            }
        return HttpResponse( template.render( context, request ) )

# JQuery Ajax 를 작성
class AjaxTextView(View):
    def get(self, request):
        template = loader.get_template("ajaxtext.html")
        context = {}
        return HttpResponse(template.render(context, request))


    def post(self, request):
        template=loader.get_template("result.html")
        id = request.POST["id"]
        passwd = request.POST["passwd"];
        context={
            "id":id,
            "passwd":passwd,
            }
        return HttpResponse( template.render( context, request ) )

class AjaxJsonView(View):
    def get(self, request):
        template = loader.get_template("ajaxjson.html")
        context = {}
        return HttpResponse(template.render(context, request))
    def post(self, request):
        template=loader.get_template("books.json")
        context={
            
            }
        return HttpResponse( template.render( context, request ) )

class AjaxXMLView(View):
    def get(self, request):
        template = loader.get_template("ajaxxml.html")
        context = {
            }
        return HttpResponse(template.render(context, request))
    def post(self, request):
        template=loader.get_template("member.xml")
        context={
            
            }
        return HttpResponse( template.render( context, request ) )
    
class AjaxXMLJsonView(View):
    def get(self, request):
        template = loader.get_template("ajaxxmljson.html")
        context = {
            }
        return HttpResponse(template.render(context, request))
    def post(self, request):
        template=loader.get_template("users.xml")
        context={
            }
        return HttpResponse( template.render( context, request ) )
    
    
# 게시판댓글
class CommentWriteView(View):
    def get(self, request):
        pass
    def post(self, request):
        template = loader.get_template("detail.html")
        nick = request.POST["nick"]
        comment = request.POST["comment"]
        boardNum = request.POST["boardNum"]
        num = request.POST["num"]
        pagenum = request.POST["pagenum"]
        number = request.POST["number"]
        date = DateFormat(datetime.now()).format("Y-m-d")
        dto = Comment(
            nick = nick,
            comment = comment,
            boardNum = boardNum,
            date = date
            )
        dto.save()
        
        
        return redirect("/board/detail?num="+num+"&pagenum="+pagenum+"&number="+number)
    
   
    
class ReplyDelView(View):
    def get(self, request):
        no = request.GET["no"]
        num = request.GET["num"]
        pagenum = request.GET["pagenum"]
        number = request.GET["number"]
        dto = Comment.objects.get( no=no )
        dto.delete()
        
        return redirect("/board/detail?num="+num+"&pagenum="+pagenum+"&number="+number)
    

class ReplyModView(View):
    def get(self, request):
        template = loader.get_template("detail.html")
        no = request.GET["no"]
        num = request.GET["num"]
        comment = request.GET["comment"]
        pagenum = request.GET["pagenum"]
        number = request.GET["number"]
        date = DateFormat(datetime.now()).format("Y-m-d")
        dto = Comment.objects.get( no=no )
        dto.comment = comment
        dto.date = date
        dto.save()
        return redirect("/board/detail?num="+num+"&pagenum="+pagenum+"&number="+number)
        
    def post(self, request) :
        pass
    
# 이용안내
class GuideView(View):
    def get(self, request):
        template=loader.get_template("guide.html")
        context={
            }
        return HttpResponse( template.render( context, request ) )
    




