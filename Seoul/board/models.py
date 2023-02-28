from django.db import models
from numpy.f2py.crackfortran import verbose

class Board( models.Model ) :
    num = models.AutoField( verbose_name="글번호", primary_key=True )
    writer = models.CharField( verbose_name="작성자", null=False, max_length=50 )
    subject = models.CharField( verbose_name="글제목", null=False, max_length=300 )
    passwd = models.CharField( verbose_name="비밀번호", null=False, max_length=30 )
    content = models.TextField( verbose_name="글내용", null=False )
    readcount = models.IntegerField( verbose_name="조회수", default=0 )
    ref = models.IntegerField( verbose_name="그룹화아이디" )
    restep = models.IntegerField( verbose_name="글순서" )
    relevel = models.IntegerField( verbose_name="글레벨" )
    regdate = models.DateTimeField( verbose_name="작성일", auto_now_add=True, blank=True )
    ip = models.CharField( verbose_name="아이피", max_length=30 )
    id = models.CharField( verbose_name="아이디", max_length=50)
    # static 이미지는 화면 페이지 구성 이미지
    # ImageBoard 업로드해서 수정할 이미지 
class ImageBoard(models.Model):
    imageid = models.AutoField(verbose_name="아이디", primary_key=True)
    title = models.CharField(verbose_name="제목", max_length=100)
    image = models.ImageField(verbose_name="이미지 경로", upload_to="images")
    name=models.CharField(verbose_name="파일 이름", max_length=100, null=True)


# 댓글
class Comment(models.Model):
    no = models.AutoField(verbose_name="댓글번호",primary_key=True)
    nick = models.CharField(verbose_name="닉네임", max_length=50, null=False)
    comment = models.TextField( verbose_name="댓글", null=False )
    date = models.DateTimeField(verbose_name="작성일", auto_now_add=True, blank=True)
    boardNum = models.IntegerField(verbose_name="게시글번호", null = True)