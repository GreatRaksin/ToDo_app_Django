from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact


# Create your views here.
def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        msg = form.save(commit=False)
        msg.save()
        return redirect('contact')
    return render(request, 'form.html', {'title': 'Contact us', 'form': form})
