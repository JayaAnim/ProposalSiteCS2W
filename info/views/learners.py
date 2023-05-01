#Learners page view
from .base import *

class Learneres(BaseTemplateView):
    template_name = 'info/learners/Learners.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['content'] = 'Learners'
        return context