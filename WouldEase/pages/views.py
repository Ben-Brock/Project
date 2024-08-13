from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

