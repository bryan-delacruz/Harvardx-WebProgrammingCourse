from django.urls import path
from . import views

urlpatterns =[
    path("",views.index, name="index"),
    path("<str:name>",views.greet, name="greet"),
    path("bryan",views.bryan, name="bryan"),
    path("david",views.bryan, name="david")
]