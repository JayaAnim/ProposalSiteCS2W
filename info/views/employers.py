#Employers page view

from .base import *

class Employers(BaseTemplateView):
    template_name = 'info/Employers/Employers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['content'] = 'Employers'
        return context