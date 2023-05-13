#Employers page view

from .base import *

class EmployersBanner(Banner):
    image_link = 'info/img/institutions-banner.png'
    banner_title = 'National Cybersecurity Employers Network' 
    banner_sub_title = 'Connecting employers with well-qualified cybersecurity professionals from across the country.' 

class Card1(Card):
    card_image = 'info/img/opportunities.png'
    card_text = "1. Help steer today's emerging cybersecurity workforce.</br>2. Post job vacancies for free in our interactive MyCyberSkills2Work portal.</br>3. Hire from our graduating pool of fresh cybertalent.</br>4. Offer input on our program and curricula."

class Card2(Card):
    card_image = 'info/img/engagement.png'
    card_text = "1. Connect with academic institutions from across the country.</br>2. Attend regional and national job fairs and networking events.</br>3. Host career information sessions and internships.</br>4. Mentor CyberSkills2Work program learners."

class Section1(Section): 
    section_style = 'light'
    section_title = 'About Our Employers Network'
    section_text = 'The National Cybersecurity Employers Network comprises organizations from critical infrastructure sectors, including energy, defense industrial base, and financial services. This growing cooperative represents public and private U.S. companies and organizations that are keenly interested in advancing the cyberworkforce.</br></br>The network plays a key role in providing insight on the hiring needs of the cybersecurity industry and on training curricula to help produce work-ready graduates. They shine a light on essential qualifications that new hires need to enter and succeed in the cybersecurity field. Employers also gain access to a growing, nationwide pool of qualified cybersecurity professionals. These professionals have the skills and credentials to join their teams and help their organizations achieve their goals.'
    section_content = CardSlider

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section_content'] = self.section_content.as_view(cards=[Card1, Card2])(self.request).rendered_content
        return context
    
employers_list = [
    {
        'title': 'Employer Spotlight',
        'employers': [
            'Booz Allen Hamilton',
            'General Dynamics Information Technology',
            'Navy Federal Credit Union',
            'Raytheon Technologies',
        ]
    },
    {
        'title': 'Defense Industrial Base',
        'employers': [
            'Accenture Federal Services',
            'Air Force Office of Special Investigations',
            'AFCEA',
            'BAE Systems',
            'Booz Allen Hamilton',
            'Corry Station (Pensacola, Florida)',
            'Eglin Air Force Base (Florida)',
            'Elbit Systems of America',
            'Fort Bliss (Texas)',
            'Fort Gordon (Georgia)',
            'General Dynamics Information Technology',
            'Holloman Air Force Base (New Mexico)',
            'Hurlburt Airfield (Florida)',
            'L3Harris Technologies',
            'MacDill Air Force Base (Florida)',
            'National Defense Industrial Association',
            'Naval Air Station (Pensacola, Florida)',
            'Northrop Grumman',
            'Peraton',
            'Raytheon Technologies',
            'Sandia National Laboratories',
            'United States Central Command',
            'USSOCOM',
            'White Sands Test Facility (NASA)',
        ]
    },
    {
        'title': 'Energy',
        'employers': [
            'ExxonMobil',
            'Florida Power & Light',
            'Gulf Power Company',
            'NextEra Energy, Inc.',
            'Pattern Energy',
            'Southern Company',
        ]
    },
    {
        'title': 'Financial Services',
        'employers': [
            'Capital One',
            'Deutsche Bank',
            'Federal Reserve Bank of Atlanta',
            'Goldman Sachs Group, Inc.',
            'Inn of The Mountain Gods Resort & Casino',
            'J.P. Morgan',
            'Navy Federal Credit Union',
            'Regions Bank',
            'U.S. Bank',
            '',
        ]
    },
    {
        'title': 'Communications',
        'employers': [
            'BlackBerry',
        ]
    },
    {
        'title': 'Healthcare and Public Health',
        'employers': [
            'UnitedHealth Group',
        ]
    },
    {
        'title': 'Information Technology',
        'employers': [
            'IPSecure, Inc.',
        ]
    }
]
    
class EmployersList(BaseTemplateView):
    template_name = 'info/employers/EmployersList.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lists'] = employers_list
        return context

class Section2(Section):
    section_style = 'dark'
    section_title = 'The National Cybersecurity Employers Network'
    section_text = 'More than 40 companies and organizations make up our network of employers. It includes nonprofits, private technology firms, federal government agencies, global cybersecurity businesses, and world-renowned defense companies and banking institutions. Join us! Become a part of this growing network.'
    section_content = EmployersList


class Section3(Section):
    section_style = 'light'
    section_title = 'Join Our Employers Network'
    section_text = 'Are you an employer interested in supporting CyberSkills2Work and hiring well-qualified cybersecurity professionals? Reach out to us and join our network.'
    section_button = 'Join Us' 
    section_button_link = '/'

class Employers(BaseTemplateView):
    template_name = 'info/Employers/Employers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banner'] = EmployersBanner.as_view()(self.request).rendered_content
        sections = []
        sections.append(Section1.as_view()(self.request).rendered_content)
        sections.append(Section2.as_view()(self.request).rendered_content)
        sections.append(Section3.as_view()(self.request).rendered_content)
        context['sections'] = sections
        return context