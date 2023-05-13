#About us view

from .base import *

""""
This views file renders the static content for the about us page and passes the static content to the homepage view
"""

class AboutBanner(Banner):
    image_link = 'info/img/about-banner.png'
    banner_title = 'About the National Cybersecurity Workforce Development Program'
    banner_sub_title = 'Educating, training, and employing our nation’s heroes in cybersecurity.'

class Section1(Section):
    section_style = "light"
    section_title = "Vision And Mission"
    section_text = "The National Cybersecurity Workforce Development Program, CyberSkills2Work, unites the efforts of U.S. colleges and universities to groom and diversify the next generation of cyber professionals. The program is dedicated to producing qualified professionals to bolster America’s cyberdefense. Its mission is to provide professional development training and job-seeking support to transitioning military personnel, veterans, first responders, and others pursuing the cybersecurity field. CyberSkills2Work aims to bridge the gap between cybersecurity workforce employers in critical infrastructure sectors and professionals trained in cyberdefense."

class Section2(Section):
    section_style = "dark"
    section_title = "Our Team"
    section_text = "A nationwide coalition of educational institutions and partnering employers make up the CyberSkills2Work team. Scholars from colleges and universities, designated as National Centers of Academic Excellence in Cybersecurity (NCAE-C), develop and offer the program’s training curricula. The University of West Florida Center of Cybersecurity oversees the program and coalition efforts. The institutions collaborate with 40+ businesses in the National Cybersecurity Employers Network to prepare learners for work roles in the cybersecurity field. Learners develop skills that align with and support the National Initiative for Cybersecurity Education (NICE) Framework standards for work roles. Through this partnership, the team provides career development support to meet current cybersecurity workforce needs."

class Section3(Section):
    section_style = "light"
    section_title = "Our Funding"
    section_text = "The National Security Agency’s NCAE-C program funds CyberSkills2Work. The NSA, an arm of the U.S. Department of Defense, leads government efforts in cybersecurity intelligence, insight, and combat support. The workforce program, with its NCAE-C designation, spearheads the nation’s charge to advance cybersecurity education as a cyberdefense strategy. Thanks to the NCAE-C program, CyberSkills2Work offers high-caliber education and job resources, free of charge, to accepted program participants."
    section_image = "info/img/cae_seal_print.png"

class Section4(Section):
    section_style = 'dark'
    section_title = "Our History"
    section_text = "Follow the National Cybersecurity Workforce Development Program’s journey to becoming CyberSkills2Work. </br></br>12.8.21 - News release</br></br><a href='https://news.uwf.edu/uwf-receives-3-million-nsa-grant-to-expand-the-national-cybersecurity-workforce-development-program/' target='_blank'>UWF receives $3 million NSA grant to expand the National Cybersecurity Workforce Development Program</a></br></br>10.27.20 - News release</br></br><a href='https://news.uwf.edu/uwf-awarded-6-million-grant-to-lead-national-cybersecurity-workforce-development-program/' target='_blank'>UWF awarded $6 million grant to lead national cybersecurity workforce development program</a>"

class About(BaseTemplateView):
    template_name = 'info/about/About.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banner'] = AboutBanner.as_view()(self.request).rendered_content
        sections = []
        sections.append(Section1.as_view()(self.request).rendered_content)
        sections.append(Section2.as_view()(self.request).rendered_content)
        sections.append(Section3.as_view()(self.request).rendered_content)
        sections.append(Section4.as_view()(self.request).rendered_content)
        context['sections'] = sections
        return context