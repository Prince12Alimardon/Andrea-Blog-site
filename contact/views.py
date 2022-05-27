from django.shortcuts import render
from .forms import CreateContactForm

# Create your views here.
from .models import Contact


def contact_view(request):
    form = CreateContactForm(request.POST or None)
    if form.is_valid():
        form.save()
    obj = Contact.objects.order_by('-id')
    context = {
        'form': form,
        'objects': obj
    }

    return render(request, 'contact/contact.html', context)
