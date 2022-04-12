from django.urls import URLPattern, path 
from . import views

urlpatterns=[
    path("",views.ShowMain),
    path("login",views.login_page),

    
]
