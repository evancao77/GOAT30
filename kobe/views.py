# -*- coding: utf-8 -*-
import json

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from kobe.models import Tb_Instances


def add_instance(request):
    response = {}
    instance_name =  request.GET.get('instance_name','')
    instance_role = request.GET.get('instance_role')
    host_name =  request.GET.get('host_name', '')
    host_ip = request.GET.get('host_ip', '')
    port = request.GET.get('port', '')
    db_type = request.GET.get('db_type', '')
    user_name = request.GET.get('user_name', '')
    user_pwd = request.GET.get('user_pwd', '')
    memo = request.GET.get('memo', '')
    print(instance_role)
    try:
        instance =  Tb_Instances(instance_name = instance_name,instance_role = instance_role,
                                   host_name = host_name,host_ip = host_ip,port = port,db_type = db_type,
                                   user_name = user_name,user_pwd = user_pwd,memo = memo)
        instance.save()
        response['msg'] = 'success'
    except Exception as e:
        response['msg'] = str(e)

    return JsonResponse(response)
