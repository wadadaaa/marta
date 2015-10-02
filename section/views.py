from django.http import HttpResponse
from django.views.generic import ListView
from section.models import Section

class SectionListView(ListView):
    model = Section
