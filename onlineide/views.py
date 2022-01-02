import json

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .serializer import userserializer,SubmissionSerializer
from .models import user,submissions
from rest_framework.response import Response
#from rest_framework import serializer
from rest_framework.decorators import api_view
from .util import createfile,execute_file
from rest_framework.renderers import TemplateHTMLRenderer


# Create your views here.
def home(request):
    return render(request,"form.html")

class UserVeiwSet(ModelViewSet):
    queryset = user.objects.all()
    serializer_class = userserializer
    renderer_classes = [TemplateHTMLRenderer]

    def list(self,request,*args,**kwargs):

        res = super().list(request, *args, **kwargs)
        res=json.loads(json.dumps(res.data))
        return Response({'data':res},template_name ='user.html')


class SubmissionVeiwSet(ModelViewSet):
    queryset = submissions.objects.all()
    serializer_class = SubmissionSerializer
    renderer_classes = [TemplateHTMLRenderer]

    def list(self, request, *args, **kwargs):
        res = super().list(request, *args, **kwargs)
        res = json.loads(json.dumps(res.data))
        return Response({'data': res}, template_name='submision.html')

    def create(self,request,*args,**kwargs):
        request.data["status"] = 'p'
        # name=user.objects.get(pk=request.data["user"]).full_name
        # print(name)
        # request.data["user"] = name
        file_name = createfile(request.data.get("language"),request.data.get("code"))
        output   = execute_file(file_name,request.data.get("language"))
        request.data["user_output"]= output.decode("utf-8")
        res= super().create(request, *args, **kwargs)

        return Response({'code':request.data["code"],'user_output':request.data["user_output"]},template_name ='form.html')




