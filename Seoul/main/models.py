from django.db import models

class Pyspark( models.Model ) :
    id = models.IntegerField( primary_key=True )
    name = models.CharField( verbose_name="장소이름", max_length=255 )
    day = models.IntegerField( verbose_name="요일" ) 
    time = models.IntegerField( verbose_name="시간" )
    prediction = models.IntegerField( verbose_name="예측값" )