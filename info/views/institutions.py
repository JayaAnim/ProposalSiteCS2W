#Institutions page view
from .base import *

class EmployersBanner(Banner):
    image_link = 'info/img/institutions-banner.png'
    banner_title = 'Educational Institutions' 
    banner_sub_title = 'Educational Institutions' 

class InstitutionImages(BaseTemplateView):
    template_name = 'info/institutions/InstitutionImages.html'

class Section1(Section):
    section_style = 'light'
    section_title = 'Our Coalition of Educational Institutions'
    section_text = "The nation's top colleges and universities have joined forces as CyberSkills2Work institutions to spawn a new generation of cybercrime fighters. Scholars of schools designated as National Centers of Academic Excellence in Cybersecurity (NCAE-C) are grooming talent for cybersecurity work. These NCAE-Cs, delegated by the National Security Agency, are training bright minds to fuel the cyberworkforce and safeguard virtual information.</br></br>CyberSkills2Work institutions collaborate to develop training curricula centered around the National Initiative for Cybersecurity Education (NICE) Cybersecurity Workforce Framework. Then, they use state-of-the-art techniques to teach training programs that align with NICE Framework work roles for America's workforce. After receiving training from CyberSkills2Work institutions, program graduates are highly qualified to tackle the demands of various cybersecurity jobs."
    section_content = InstitutionImages 

class Card1(Card):
    card_image = 'info/img/pathway-program-components-icon.png'
    card_text = "1. Earn recognition as an educational institution at the forefront of national cybersecurity workforce development and training.</br>2. Expand your institution’s educational programs and enrollment via training pathways for diverse learners."

class Card2(Card):
    card_image = 'info/img/educational-institutions-curriculum-icon.png'
    card_text = "1. Leverage curricula that NCAE-C institutions develop to offer cybersecurity workforce programs that support NICE Framework guidelines.</br></br>2. Get additional resources to enrich your institution’s cybersecurity workforce program."

class Card3(Card):
    card_image = 'info/img/credentialing-icon.png'
    card_text = "1. Utilize a cutting-edge, credentialing system to offer digital badges and other incentives for your courses and pathways.</br></br>2. Track learners' training progress and earned badges in a comprehensive portal."

class Card4(Card):
    card_image = 'info/img/cyber-skills-2-work-portal.png'
    card_text = "1. Easily market your training pathways, recruit and select learners, and connect with employers on a one-stop-shop portal. It’s available at the national level, at no cost."

class Card5(Card):
    card_image = 'info/img/employers-icon.png'
    card_text = "1. Connect with companies and organizations from the nation’s key critical infrastructure sectors. Put your training program graduates in touch with members of the National Cybersecurity Employers Network to access job opportunities."

class Section2(Section):
    section_style = 'dark'
    section_title = 'Launch a CyberSkills2Work Training Pathway'
    section_text = "Can your institution support national efforts to fortify the cybersecurity workforce and help fill the professional talent gap? Launch a CyberSkills2Work training pathway. Our team will help you leverage the CyberSkills2Work platform, resources, and NCAE-C-designated curricula. Experience the benefits of taking part in this initiative and helping to fortify the country's cyberdefense with qualified workers."
    section_content = CardSlider

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section_content'] = self.section_content.as_view(cards=[Card1, Card2, Card3, Card4, Card5])(self.request).rendered_content
        return context
    
class Section3Button(SimpleButton):
    button_text = 'Contact Us'
    button_link = '/'

class Section3(Section):
    section_style = 'light'
    section_title = 'Join Our Coalition'
    section_text = "Is your college or university making strides in the cybersecurity field as an NCAE-C institution? Are you developing or currently offering a cybersecurity workforce program? Join forces with like institutions in the CyberSkills2Work program. Take part in a national initiative that's helping to strengthen the cybersecurity workforce and secure information in critical infrastructure sectors."
    section_button = Section3Button
    
class Institutions(SectionWrapper):
    banner = EmployersBanner
    sections = [Section1, Section2, Section3]