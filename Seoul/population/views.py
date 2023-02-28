from django.shortcuts import render, redirect
import logging
from django.http.response import HttpResponse
from django.template import loader
from django.views.generic.base import View

logger = logging.getLogger( __name__ )

class PopulationMainView( View ):
    def get(self, request):
        template = loader.get_template( "pop_main.html" )
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
    
    def post(self, request):
        template = loader.get_template("pop_main.html")
        name = request.POST["name"]
        min = request.POST["min"]
        max = request.POST["max"]
        time = request.POST["time"]
        
        test = name+ "," + time + "," + min + "," + max
        
        logger.info(test)
        
        context = {
            
            }
        return HttpResponse(template.render( context, request ))

    
