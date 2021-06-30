
from django.views.generic import TemplateView

class TestPage(TemplateView):
    template_name = 'index.html'