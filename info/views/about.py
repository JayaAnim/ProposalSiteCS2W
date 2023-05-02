#About us view

from .base import *

class About(BaseTemplateView):
    template_name = 'info/about/About.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['content'] = 'About'
        return context