from django.contrib import admin
from member.models import Member
from plan.models import PlanComment

class MemberAdmin( admin.ModelAdmin ) :
    list_display = ( "no", "id", "pw", "name", "nickname", "email", "phone", "addr0", "addr1", "addr2", "regdate", "level", "catePlace", "cateFood" )
admin.site.register( Member, MemberAdmin )

class PlanCommentAdmin( admin.ModelAdmin ) :
    list_display = ( "no", "nick", "comment", "date", "boardNum" )
admin.site.register( PlanComment, PlanCommentAdmin )
