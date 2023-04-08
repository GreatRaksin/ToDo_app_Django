from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact
from django.core.mail import send_mail


# Create your views here.
def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        msg = form.save(commit=False)
        msg.save()
        send_mail(
            msg.subject, msg.message,
            msg.email, ['legorobotsbel@gmail.com'],
            fail_silently=False,
        )
        return redirect('contact')
    return render(request, 'form.html', {'title': 'Contact us', 'form': form})
