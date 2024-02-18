from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_subject = request.POST['message-subject']
        umessage = request.POST['umessage']

        send_mail(
            message_name, # user name
            message_subject, # message subject
            umessage, # messages
            message_email, # from email
            ['rethoplayer@gmail.com'], # To email
        )

        return render(request, 'contact.html', {'message_name': message_name})

    else:
        return render(request, 'contact.html', {})
    