#Program impact view
from .base import *

class ImpactBanner(Banner):
    image_link = 'info/img/program-impact.png'
    banner_title = 'Program Impact'
    banner_sub_title = 'See how CyberSkills2Work is making strides and impacting the cybersecurity workforce in more ways than one.'

class MapContent(BaseTemplateView):
    template_name = "info/impact/ImpactMap.html"


class Section1(Section):
    section_style = 'light'
    section_title = 'Nine Institutions, 22 Training Programs'
    section_button = 'More Info'
    section_content = MapContent
    section_button_link = '/'

class ImpactImages(BaseTemplateView):
    template_name = 'info/impact/ImpactImages.html'

class Section2(Section):
    section_style = 'dark'
    section_title = 'Key Program Metrics'
    section_content = ImpactImages
    section_button = 'Join Us'
    section_button_link = '/'

class Impact(BaseTemplateView):
    template_name = 'info/impact/ProgramImpact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banner'] = ImpactBanner.as_view()(self.request).rendered_content
        sections = []
        sections.append(Section1.as_view()(self.request).rendered_content)
        sections.append(Section2.as_view()(self.request).rendered_content)
        context['sections'] = sections
        return context