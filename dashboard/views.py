# coding=utf-8
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from django.template import Context,Template
from django.views.generic import TemplateView
from RoyalSFlush.settings import *
from commom.log import logger
    
if RUN_MODE == "PRD":
    from commom.dbconn_prd import *
elif RUN_MODE == "STG":
    from commom.dbconn_stg import *
else:
    from commom.dbconn_dev import *

def index(request):
    #tdedb = TdeToolsDB()
    #tdedb.query("select * from t_access_info;")
    #tdedb.closeConn()
    #logger.info()
    return render_to_response('index.html')

def example(request):
    return render_to_response('example.html')