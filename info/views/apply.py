#Apply page view
from .base import *

class Apply(BaseTemplateView):
    template_name = 'info/apply/Apply.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['content'] = 'Apply'
        return context