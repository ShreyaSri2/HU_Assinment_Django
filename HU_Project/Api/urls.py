#from django.urls import include, re_path, path
#from django.conf.urls import url
from django.urls import path, re_path
from Api import views


urlpatterns=[
    re_path(r'^issues$',views.issuesApi),
    #re_path(r'^issues/([0-9]+)$',views.issuesApi),
    re_path(r'^issues/([0-9]+)$',views.issues_detail),

    re_path(r'^projects$',views.projectsApi),
    #re_path(r'^projects/([0-9]+)$',views.projectsApi),
    re_path(r'^projects/([0-9]+)$',views.projects_detail),

    path('hello/', views.HelloView.as_view(), name ='hello'),
    path('demo', views.DemoView.as_view(), name="demo"),

    path('register', views.Register.as_view(), name="register"),
]