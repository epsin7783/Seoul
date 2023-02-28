from django.db import models
from datetime import datetime

class Plan(models.Model):
    p_no = models.AutoField(primary_key=True)
    p_title = models.CharField(max_length=100, null=False)
    p_nickname = models.CharField(max_length=50, null=False)
    p_sdate = models.CharField(max_length=20, null=False)
    p_edate = models.CharField(max_length=20, null=True)
    p_days = models.IntegerField(null=False)
    p_memo = models.TextField(null=False)
    p_code = models.CharField(max_length=10, null=False)
    p_content = models.CharField(max_length=200, null=False)
    id = models.CharField(max_length=50, null=False)
    day1 = models.TextField(null=False)
    day2 = models.TextField(null=False)
    day3 = models.TextField(null=False)
    day4 = models.TextField(null=False)
    day5 = models.TextField(null=False)
    day6 = models.TextField(null=False)
    day7 = models.TextField(null=False)
    addr = models.TextField(null=False)
    place_name = models.TextField(null=False)
    image = models.ImageField(verbose_name="이미지 경로", upload_to="images")
    ref = models.IntegerField( verbose_name="그룹화아이디",)
    restep = models.IntegerField( verbose_name="글순서" )

class Wishlist(models.Model):
    p_no = models.AutoField(primary_key=True)
    p_title = models.CharField(max_length=100, null=False)
    p_nickname = models.CharField(max_length=50, null=False)
    p_sdate = models.CharField(max_length=20, null=False)
    p_edate = models.CharField(max_length=20, null=True)
    p_days = models.IntegerField(null=False)
    p_memo = models.TextField(null=False)
    p_code = models.CharField(max_length=10, null=False)
    p_content = models.CharField(max_length=200, null=False)
    id = models.CharField(max_length=50, null=False)
    day1 = models.TextField(null=False)
    day2 = models.TextField(null=False)
    day3 = models.TextField(null=False)
    day4 = models.TextField(null=False)
    day5 = models.TextField(null=False)
    day6 = models.TextField(null=False)
    day7 = models.TextField(null=False)
    addr = models.TextField(null=False)
    image = models.ImageField(verbose_name="이미지 경로", upload_to="images")
    ref = models.IntegerField( verbose_name="그룹화아이디",)
    restep = models.IntegerField( verbose_name="글순서" )
    plan_no = models.IntegerField(null=False) 

class PlanComment(models.Model):
    no = models.AutoField(verbose_name="댓글번호",primary_key=True)
    nick = models.CharField(verbose_name="닉네임", max_length=50, null=False)
    comment = models.TextField( verbose_name="댓글", null=False )
    date = models.DateTimeField(verbose_name="작성일", auto_now_add=True, blank=True)
    boardNum = models.IntegerField(verbose_name="게시글번호", null = True)

class Like(models.Model):
    l_no = models.AutoField(primary_key=True)
    id = models.CharField(max_length=50, null=False)
    p_no = models.CharField(max_length=10, null=False)

class PlanCount(models.Model):
    c_no = models.AutoField(primary_key=True)
    count = models.IntegerField(null=False)
    id = models.CharField(max_length=50, null=False)
    p_no = models.CharField(max_length=10, null=False)
    
    
class LiveRank(models.Model):
    place = models.CharField(max_length=255, null=False)
    counts = models.CharField(max_length=255, null=False)
    
    
class Eatplace(models.Model):
    no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=255, null=False)
    review_star  = models.TextField(null=False)
    review_text = models.TextField(null=False)
    gu = models.CharField(max_length=255, null=False)