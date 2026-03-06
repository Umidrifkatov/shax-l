from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import ContactRequest
from .forms import ContactForm
from django.utils.translation import gettext_lazy as _

class ContactCreateView(CreateView):
    model = ContactRequest
    form_class = ContactForm
    template_name = 'contacts/contact.html'
    success_url = reverse_lazy('contacts:contact')

    def form_valid(self, form):
        form.instance.ip_address = self.request.META.get('REMOTE_ADDR')
        messages.success(self.request, _('Ваша заявка успешно отправлена! Мы свяжемся с вами в ближайшее время.'))
        return super().form_valid(form)
