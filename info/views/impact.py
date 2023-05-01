#Program impact view
from .base import *

class Impact(BaseTemplateView):
    template_name = 'info/impact/Impact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['content'] = 'Impact'
        return context