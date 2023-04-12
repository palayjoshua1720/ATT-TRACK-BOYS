# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status
from django.shortcuts import render
from django.views.generic import (View,TemplateView)
# from ifcav5_proj.settings import DATABASES as dbs

from django.db import connection, connections

# Create your views here.
class BackOffice(TemplateView):
    template_name = 'backoffice/index.html'

class dashboard(TemplateView):
    template_name = 'backoffice/dashboard'
