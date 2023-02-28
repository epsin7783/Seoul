from django.contrib import admin
from plan.models import Plan, Like, PlanCount, Wishlist, LiveRank, Eatplace

class PlanAdmin( admin.ModelAdmin ) :
    list_display = ( "p_no", "p_title", "p_nickname", "p_sdate", "p_edate", "p_days", "p_memo", "p_code", "p_content", "id", "day1", "day2", "day3", "day4", "day5", "day6", "day7", "image", "addr", "place_name", "ref", "restep" )
admin.site.register( Plan, PlanAdmin )

class WishlistAdmin( admin.ModelAdmin ) :
    list_display = ( "p_no", "p_title", "p_nickname", "p_sdate", "p_edate", "p_days", "p_memo", "p_code", "p_content", "id", "day1", "day2", "day3", "day4", "day5", "day6", "day7", "image", "addr", "ref", "restep", "plan_no" )
admin.site.register( Wishlist, WishlistAdmin )

class LikeAdmin( admin.ModelAdmin ) :
    list_display = ( "l_no", "id", "p_no" )
admin.site.register( Like, LikeAdmin )

class PlanCountAdmin( admin.ModelAdmin ) :
    list_display = ( "c_no", "count", "id", "p_no" )
admin.site.register( PlanCount, PlanCountAdmin )

class LiveRankAdmin( admin.ModelAdmin ):
    list_display = ("place", "counts")
admin.site.register( LiveRank, LiveRankAdmin )


class EatplaceAdmin( admin.ModelAdmin ) :
    list_display = ( "no", "name", "address", "review_star", "review_text", "gu" )
admin.site.register( Eatplace, EatplaceAdmin)