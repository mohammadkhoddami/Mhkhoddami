from core.models.contact import ContactInfo, ContactNote
from django.views import View
from django.shortcuts import render, redirect
from core.forms.contact import ContactForm
from django.utils.translation import gettext_lazy as _
from django.contrib import messages

class ContactMeView(View):
    form_class = ContactForm
    
    
    def get(self, request):
        form = self.form_class()
        contact_info = ContactInfo.objects.last()
        return render(request, 'home/contact.html', {'contact_info': contact_info,
                                                     'form': form})
        
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Your message was successful'), 'success')
            return redirect('home:home')
        messages.warning(request, _('Please fill all fields'), 'warning')
        return render(request, 'home/contact.html', {'form': form})