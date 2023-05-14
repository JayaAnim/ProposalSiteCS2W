#Resources page view
from .base import *

class ResourcesBanner(Banner):
    image_link = 'info/img/about-banner.png'
    banner_title = 'Cybersecurity Workforce Resources'
    banner_sub_title = 'Additional cybersecurity workforce resources to help you make an informed decision about pursuing a cyber career.'

class ResourcesList(BaseTemplateView):
    template_name = 'info/resources/ResourcesList.html'

class Section1(Section):
    section_style = 'light'
    section_text = 'Explore online cybersecurity workforce resources to learn more about national standards for work roles. Find out what cybersecurity jobs are in demand, where they’re located, industry certifications you need to get hired, and more. We connect you to the most reliable resources for cybersecurity career information:'
    section_content = ResourcesList

class Resources(SectionWrapper):
    banner = ResourcesBanner
    sections = [Section1]