from django.contrib import admin
from main.models import Pyspark


class PysparkAdmin( admin.ModelAdmin ) :
    list_display = ( "id","name", "day", "time", "prediction")
admin.site.register( Pyspark, PysparkAdmin )