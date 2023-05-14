#Partners page view
from .base import *

class EmployersBanner(Banner):
    image_link = 'info/img/institutions-banner.png'
    banner_title = 'Program Partners' 
    banner_sub_title = 'Supporting national efforts to strengthen and advance the cybersecurity workforce.' 

class PartnersList(BaseTemplateView):
    template_name = 'info/partners/PartnersList.html' 
    list_style = None
    list_items = []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list'] = self.list_items
        context['list_style'] = self.list_style
        return context

class Section1(Section):
    section_style = 'light'
    section_title = 'Overview'
    section_text = "CyberSkills2Work program partners are essentially the lifeline of the national workforce development initiative. Without their support, the program wouldn’t be able to offer cybersecurity training and job opportunities to underrepresented and underserved populations. Thanks to our program partners, more transitioning military personnel, first responders, veterans, women, and minorities can launch or advance in cybersecurity jobs. An alliance of federal and multistate government agencies, nonprofit organizations, and American companies devotes time and resources to promote and fund CyberSkills2Work."
    section_image = 'info/img/CyberSkills2Work-Program-Partners.jpg' 

strategic_partners = [
    "Cybersecurity & Infrastructure Security Agency (CISA)",
    "National Initiative for Cybersecurity Education (NICE)",
    "National Security Agency (NSA)",
    "U.S. Department of Labor",
    "U.S. Department of Veterans Affairs"
]

class Section2List(PartnersList):
    list_items = strategic_partners
    list_style = 'dark'

class Section2(Section):
    section_style = 'dark'
    section_title = 'Strategic Partners'
    section_content = Section2List

additional_partners = [
    "Business Executives for National Security",
    "Hetherington Group",
    "IBM",
    "Innovate + Educate",
    "Merkel Foundation",
    "Mescalero Apache Tribal Government, Economic Development & Telecom ISP",
    "Minnesota Department of Employment and Economic Development",
    "National Security Collaboration Center (NSCC)",
    "New Mexico Economic Development Department",
    "New Mexico Department of Workforce Solutions",
    "Region 9 Education Cooperative",
    "South Central Mountain Economic Development Association"
]

class Section3List(PartnersList):
    list_items = additional_partners
    list_style = 'light'

class Section3(Section):
    section_style = 'light'
    section_title = 'Additional Partners'
    section_content = Section3List

class Section4(Section):
    section_style = 'dark'
    section_title = 'Become a Partner'
    section_text = 'Are you interested in supporting CyberSkills2Work and improving the cybersecurity workforce. Reach out to us and tell us how you can help.'
    section_button = 'Contact Us'
    section_button_link = '/' 

class Partners(SectionWrapper):
    sections = [Section1, Section2, Section3, Section4]