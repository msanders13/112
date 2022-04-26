from django.views.generic import TemplateView

# Home page view is extending Template View child/parent
class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"
