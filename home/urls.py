from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    # path("", views.Index, name="index"),
    path("", views.Index, name="index"),
    path("home/", views.Home, name="home"),
    path("experience/", views.AddExperience, name="experience"),
    path("recruits/", views.RecruitInfo, name="recruits"),
    path("contact/", views.ContactPage, name="contact"),
    ]