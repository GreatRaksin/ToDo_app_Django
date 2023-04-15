from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ContactForm
from .models import Contact
from django.core.mail import EmailMessage, get_connection


# Create your views here.
def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        msg = form.save(commit=False)
        msg.save()
        with get_connection(
            host=settings.EMAIL_HOST,
            port=settings.EMAIL_PORT,
            username=settings.EMAIL_HOST_USER,
            password=settings.EMAIL_HOST_PASSWORD,
            use_tls=settings.EMAIL_USE_TLS
        ) as connection:
            subject = msg.subject
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [msg.email,]
            message = msg.messsage
            EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()
        return redirect('contact')
    return render(request, 'form.html', {'title': 'Contact us', 'form': form})
