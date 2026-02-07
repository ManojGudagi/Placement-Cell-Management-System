from django.urls import path
from .views import *


urlpatterns = [

    path("",home, name="home"),
    path("register/",register, name="register"),
    path("login/",login, name="login"),
    path("dashboard/",dashboard, name="dashboard"),
    path("admin/",admin, name="admin"),
    path("admin_dashboard/",admin_dashboard, name="admin_dashboard"),
    path("company_login/",company_login, name="company_login"),
    path("company_dashboard/",company_dashboard, name="company_dashboard"),
    path("job_post/",job_post, name="job_post"),
    path("apti/",apti, name="apti"),

]

