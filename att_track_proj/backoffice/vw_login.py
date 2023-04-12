from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from django.views.generic import (View,TemplateView)
import json
from .common import Repeated
from django.db import connection, connections

class LoginTemplate(TemplateView):
    template_name = 'backoffice/login/login.html'

class Authenticate(APIView):
    def post(self, request, format=None):
        print('Working!')
        data = request.data
        # data['flag'] = 2
        # data['credential_id'] = 12345
        # data['profile_id'] = 1
        # data['username'] = 'loar'
        # data['password'] = 'Gwapo'
        # data['email'] = 'loar@gmail.com'
        data = json.dumps(data)
        print(data)
        script = f"EXECUTE sp_credent NULL, '{data}'"
        print(script)
        with connection.cursor() as cursor:
            cursor.execute(script)
            row = Repeated.dictfetchall(cursor)
            print(f'Data: {row}')
            return Response(row)
        return Response({'Result':1})
    

    def get(self, request, format=None):
        print('Get Working!')
        return Response({'Result':1})
    