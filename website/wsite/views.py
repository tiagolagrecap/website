from django.shortcuts import render
from .models import About, Services, Banner
from django.core.mail import send_mail


def index(request):
    abouts = About.objects.all()
    services = Services.objects.all()
    banners = Banner.objects.all()

    context = {'abouts': abouts, 'services': services,
               'banners': banners}
    return render(request, 'wsite/index.html', context)


def about(request):
    abouts = About.objects.all()

    context = {'abouts': abouts}
    return render(request, 'wsite/about.html', context)


def service(request):
    services = Services.objects.all()

    context = {'services': services}
    return render(request, 'wsite/services.html', context)


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_phone = request.POST['message-phone']
        message = request.POST['message']

        send_mail(
            message_name,
            message,
            message_email,
            message_phone
            ['XYZ'],
        )

        return render(request, 'wsite/contact.html', {'message_name': message_name})

    else:
        return render(request,'wsite/contact.html', {} )

