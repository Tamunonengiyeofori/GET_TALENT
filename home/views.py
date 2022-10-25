from django.shortcuts import render, redirect
import requests
from .models import Recruit, Experience, Contact, Review
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Q
# from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def RecruitInfo(request):
    # login_user = request.user
    # recruit_user = Recruit.objects.get(user=login_user)
    # all_experience = Experience.objects.filter(owner=recruit_user)
    # all_reviews = Review.objects.filter(owner=recruit_user)
    # context = {
    #     "experience": all_experience ,
    #     "reviews": all_reviews
    # }
    context = { }
    return render (request, 'home/recruit-info.html', context)

def AddExperience(request):
    # login_user = request.user
    # if request.method == "POST":
    #     employer = request.POST.get("employer")
    #     position = request.POST.get("position")
    #     description = request.POST.get("descriptions")
    #     start_date = request.POST.get("start_date")
    #     end_date = request.POST.get("end_date")
        
    #     new_experience = Experience(
    #         owner = login_user,
    #         employer = employer,
    #         position = position,
    #         description = description,
    #         start_date = start_date,
    #         end_date = end_date)
        
    #     new_experience.save()
        
    #     context = {
    #         "new_experience" :new_experience
    #     }
    context = {}
    return render(request, "home/add-experience.html", context)
    
def send_simple_message(subject, message, recipient_mail):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox31b4632c811b42fb8974578d83aa377a.mailgun.org/messages",
        auth=("api", "YOUR_API_KEY"),
        data={"from": "contactus@gettalent.com",
              "to": recipient_mail,
              "subject": subject,
              "text": message}
        )
    
def ContactPage(request):
    # if request.method == "POST":
    #     name = request.POST.get("name")
    #     email = request.POST.get("email")
    #     message = request.POST.get("message")
    #     subject = f"{name} Complaint"
    #     mail_message = f"{message}"
    #     # email_from = settings.EMAIL_HOST_USER
    #     recipient_mail = [email]
    #     send_simple_message(subject, mail_message, recipient_mail)
    #     return redirect("contact")
    return render(request, "home/contact-page-logged.html")

def Home(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ""

    recruits = Recruit.objects.filter(
        Q(user__icontains=q) |
        Q(country__icontains=q) |
        Q(state__icontains=q)
    )
    
    # recruit_count = recruits.count()
    # context = {
    #     "recruits": recruits,
    #     "recruit_count": recruit_count
    # }
    context = {}
    return render(request, "home/home.html", context)

def Index(request):
    return render(request, 'home/index.html')

