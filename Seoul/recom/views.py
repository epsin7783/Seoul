from django.shortcuts import render
from django.views.generic.base import View
from django.template import loader
from django.http.response import HttpResponse

class RecomView(View):
    def get(self, request):
        template = loader.get_template( "recom.html" )
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
        pass
