from django.shortcuts import render
from django.core.mail import send_mail 

# Create your views here.
def home(request):
    return render(request, "index.html", {})


def about(request):
    return render(request, "about.html", {})


def service(request):
    return render(request, "service.html", {})


def pricing(request):
    return render(request, "pricing.html", {})


def blog(request):
    return render(request, "blog.html", {})


def blog_details(request):
    return render(request, "blog-details.html", {})


def contact(request):
        #variables del form attr name
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        
        #send mail
        send_mail(
            message_name, #subject
            message, #message
            message_email, #from email
            ['servihostings@caribedigital.xyz'], #to email
            fail_silently=False,#en produccion debe cambiarse a True
            )
        return render(request, "contact.html", {'message_name':message_name})       
    else:
        return render(request, "contact.html", {})