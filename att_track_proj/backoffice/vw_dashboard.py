from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from django.views.generic import (View,TemplateView)
import json
from .common import Repeated
from django.db import connection, connections

class dashboardView(TemplateView):
    template_name = 'backoffice/dashboard/dashboard.html'

