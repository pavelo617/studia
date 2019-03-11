from django.shortcuts import render, render_to_response
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import ModelForm
from django.shortcuts import render_to_response, reverse
from django.views import View
from django.core.mail import send_mail, BadHeaderError, EmailMultiAlternatives
from .models import News
from datetime import datetime, timedelta, timezone

def info(request):
    return render(request, 'news/index.html')

def work(request):
    return render(request, 'news/work.html')

def zarplata(request):
    return render(request, 'news/zarplata.html')

def anketa(request):
    return render(request, 'news/anketa.html')

def contact(request):
    name=request.POST.get('name', '')
    phone=request.POST.get('phone', '')
    day=request.POST.get('day', '')
    month=request.POST.get('month', '')
    year=request.POST.get('year', '')
    town=request.POST.get('town', '')
    eng=request.POST.get('eng', '')
    time=request.POST.get('time', '')
    usermsg=request.POST.get('usermsg', '')
    data={"name":name,"phone":phone,"day":day,"month":month,"year":year,"town":town,"usermsg":usermsg, "time":time, "eng":eng}
    if name and phone and town and time and usermsg:
        try:
            msg=EmailMultiAlternatives('Анкета девочки',str("Имя девочки: "+data['name']+"\n"+"Номер телефона: "+data["phone"]+"\n"+"Дата рождения: "+data["day"]+". "+data["month"]+". "+data['year']+"\n"+"Город проживания: "+data["town"]+"\n"+"О себе: "+data["usermsg"]+"\n"+"Удобное время: "+data["time"]+"\n"+"Владение английским: "+data["eng"]+"\n"+"Это письмо сформировано автоматически. Пожалуйста, не отвечайте на него."), 'llipyc999@gmail.com',
            ['charmstudioomsk@mail.ru'],)
            msg.send()

        except BadHeaderError:

            return HttpResponse('<h1>Invalid header found.</h1>')

        return render (request, 'news/anketa.html')

    else:

        return HttpResponse('<h1>Make sure all fields are entered and valid</h1>')

def phone(request):
    return render (request, 'news/phone.html')
    
def news(request):
    posts=News.objects.filter(date_pub__lte=datetime.now()).order_by('-date_pub')
    return render (request, 'news/news.html', context={'posts':posts,})