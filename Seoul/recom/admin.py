from django.contrib import admin
from recom.models import recommend

class RecommendAdmin( admin.ModelAdmin ):
    list_display = ("no", "name", "addr", "grade", "review")
admin.site.register( recommend, RecommendAdmin )
