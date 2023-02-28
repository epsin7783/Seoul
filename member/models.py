from django.db import models
from MySQLdb.constants.FLAG import AUTO_INCREMENT

class Member( models.Model ) :
    no = models.AutoField(verbose_name="번호", primary_key=True) 
    id = models.CharField( verbose_name="아이디", null=False, max_length=50 )
    pw = models.CharField( verbose_name="비밀번호", null=False, max_length=255 )
    name = models.CharField( verbose_name="이름", null=False, max_length=30)
    nickname=models.CharField( verbose_name="닉네임", null=False, max_length=10 )
    email = models.CharField( verbose_name="이메일", null=False, max_length=50 )
    phone = models.CharField( verbose_name="전화번호", null=False, max_length=13 )
    addr0 = models.CharField( verbose_name="우편번호", default="charField", null=False, max_length=100 )
    addr1 = models.CharField( verbose_name="주소1", null=False, max_length=100 )
    addr2 = models.CharField( verbose_name="주소2", null=False, max_length=100 )
    regdate = models.DateTimeField( verbose_name="작성일", auto_now_add=True, blank=True ) 
    level = models.IntegerField( verbose_name="등급", null=True) 
    catePlace = models.CharField( verbose_name="선호하는 장소", max_length=255, null=False ) 
    cateFood = models.CharField( verbose_name="선호하는 음식", max_length=255, null=False ) 
    social = models.CharField( verbose_name="소셜로그인 여부", null=True, max_length=100 ) 
