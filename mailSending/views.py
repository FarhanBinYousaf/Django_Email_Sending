from django.shortcuts import render,redirect
from .forms import MailForm
from django.conf import settings
from django.core.mail import send_mail
from .models import Form
# Create your views here.
def Index(request):
    form = MailForm()
    if request.method == 'POST': 
        name = request.POST['name']
        sonOf = request.POST['fatherName']
        email = request.POST['email']
        msg = request.POST['msg']
        user = Form.objects.create(name=name,fatherName=sonOf,email=email,msg=msg)
        user.save()

        subject = 'Welcome to the Testing Mailer'
        message = '<h1>Hi, Dear, Thanks for joining Testing Mailer.</h1>'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email,]
        send_mail(subject,message,email_from,recipient_list)
        return redirect('welcome')
    context = {'form':form}
    return render(request,'mailSending/index.html',context)

def welcome(request):
    return render(request,'mailSending/welcome.html')
