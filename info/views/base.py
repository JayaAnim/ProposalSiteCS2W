#Parent components and container for other views
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
    
class Base(TemplateView):
    page_title = "CyberSkills2Work"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context

class BaseTemplateView(Base, TemplateView):
    pass


class BaseDetailView(Base, DetailView):
    pass


class BaseListView(Base, ListView):
    pass


class BaseCreateView(Base, CreateView):
    pass