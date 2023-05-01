#Training program page view
from .base import *

class Training(BaseTemplateView):
    template_name = 'info/training/training.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['content'] = 'Training'
        return context