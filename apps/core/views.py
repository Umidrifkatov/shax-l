from django.views.generic import TemplateView
from apps.services.models import Service

class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.filter(is_active=True)[:6]
        return context

class AboutView(TemplateView):
    template_name = 'core/about.html'
