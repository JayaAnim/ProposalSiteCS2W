#Home page view
from .base import *

class Home(BaseTemplateView):
    template_name = 'info/home/Home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['content'] = 'Home'
        return context
    

