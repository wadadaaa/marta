from django.http import HttpResponse
from django.views.generic import TemplateView

from section.models import (
    MainSection,
    AboutSection,
    Product,

)


class SectionsView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
    	context = super(SectionsView, self).get_context_data(**kwargs)
        context['mains'] = MainSection.objects.all()
        context['abouts'] = AboutSection.objects.all()
        context['products'] = Product.objects.all()
        return context
