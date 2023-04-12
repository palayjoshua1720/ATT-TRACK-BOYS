from django.urls import path
from backoffice import views, vw_login, vw_dashboard

urlpatterns =[
    path('',views.BackOffice.as_view(), name='main'),
    path('login',vw_login.LoginTemplate.as_view(), name='loginpage'),
    path('dashboard',vw_dashboard.dashboardView.as_view(), name='dashboardpage'),
    # path('override/<ser>',views.OverrideCRHT.as_view(), name='CRHT'),
    # path('override',views.OverrideLicense.as_view(), name='OL'),
    path('authenticate',vw_login.Authenticate.as_view(), name='authenticate'),
    
]