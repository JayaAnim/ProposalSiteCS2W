#Learners page view
from .base import *

class LearnersBanner(Banner):
    image_link = 'info/img/learners-banner.png'
    banner_title = 'Program Learners'
    banner_sub_title = 'Developing skills for diverse cybersecurity roles.'

class LearnersChecklist(BaseTemplateView):
    template_name = 'info/learners/LearnersChecklist.html'
    checklist = []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['checklist'] = self.checklist
        return context

checklist1_items = [
    {
        'title': 'Understanding Work Roles',
        'text': "CyberSkills2Work offers training for more than 15 cybersecurity work roles within the <a href='https://niccs.cisa.gov/workforce-development/cyber-career-pathways-tool' target='_blank'>National Initiative for Cybersecurity Education Framework</a>. The NICE Framework sets guidelines for the knowledge, skills, and abilities needed to perform jobs in the cybersecurity industry. Its educational standards guide workforce development for information and critical infrastructure security across public, private, and academic sectors.</br></br><a href='/'>Learn More>>></a>"
    },
    {
        'title': 'Cyber Career Pathways',
        'text': "Choose a cybersecurity career path for the work role of your choice. CyberSkills2Work offers training in more than 15 pathways of learning, including cyber defense analyst and vulnerability assessment analyst. Learn from the nation's best cyber scholars and get on the path to launch or advance your cybersecurity career.</br></br><a href='/'>Learn More>>></a>"
    },
    {
        'title': 'Determine Your Cyber Aptitude',
        'text': "Do you have what it takes to succeed in cybersecurity? Take our aptitude test to determine your cybersecurity competence. Find a work role thats right for you. Your future depends on it.</br></br><a href='/'>Learn More>>></a>"
    }
]

class Section1CheckList(LearnersChecklist):
    checklist = checklist1_items


class Section1(Section):
    section_style = 'light'
    section_title = "Navigating the Field of Cybersecurity"
    section_text = "The future is bright for CyberSkills2Work program learners. The growing cybersecurity field needs skilled professionals who can expose and fight cybercrimes. The program trains people who are keenly interested in working in the broad cybersecurity field. We’ll help you identify an ideal work role to pursue, based on your experience, interests, and aptitude. With the right qualifications and drive to succeed, you might be a perfect fit for CyberSkills2Work. Participation is free for qualifying veterans, transitioning military personnel, and first responders interested in launching or advancing a cybersecurity career."
    section_content = Section1CheckList

section2_bulletpoints = [
    'Learn from experts alongside other aspiring cybersecurity professionals.',
    'Earn industry certifications and digital badges that verify your skills.',
    'Network with employers offering career development assistance.',
]

class Section2List(UnorderedList):
    list_items = section2_bulletpoints 

class Card1(Card):
    card_image = 'info/img/benefits-for-learners-icon.png' 
    card_text = '1. Attend free, if eligible.</br>2. Get the best cybersecurity education designed and delivered by experts.</br>3. Opt for in-person, online, or hybrid learning options that fit your schedule.'

class Card2(Card):
    card_image = 'info/img/benefits-for-learners-icon.png'
    card_text = '4. Learn from colleges and universities dubbed National Centers of Academic Excellence in Cybersecurity.</br>5. Connect with recruiters from top companies and organizations.</br>6. Accelerate through short, focused training programs to launch your career sooner.'

class Card3(Card):
    card_image = 'info/img/program-components-1200.png'
    card_text = '1. CyberSkills2Work puts you on a career path in less time, no matter your cyber quest.</br></br>2. CyberSkills2Work provides in-person and online learning options. Choose from asynchronous, synchronous, hybrid or in-classroom training, which is provided in cohorts (guided group studies).'

class Card4(Card):
    card_image = 'info/img/program-components-1200.png'
    card_text = '3. Elite U.S. colleges and universities with exceptional cybersecurity academics design and deliver our training programs and curricula.</br></br>4. The MyCyberSkills2Work portal is a one-stop-shop for program learners.'

class Card5(Card):
    card_image = 'info/img/CyberSkills2Work-Credentialing.png'
    card_text = '1. Our nationally recognized certificates allow CyberSkills2Work program graduates to showcase and verify their cyber knowledge and abilities.</br>2. Receive digital badges for completing the program and courses. These badges authenticate a learner’s competency to perform work role tasks and concepts in any job industry.'

class Card6(Card):
    card_image = 'info/img/employers-icon.png'
    card_text = 'Connect with representatives and job opportunities at world-renowned companies and organizations from across the country.'

class LearnersWrapper(BaseTemplateView):
    template_name = 'info/learners/LearnersWrapper.html' 
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        content_list = []
        content_list.append(Section2List.as_view()(self.request).rendered_content)
        content_list.append(CardSlider.as_view(cards=[Card1, Card2, Card3, Card4, Card5, Card6])(self.request).rendered_content)
        context['content_list'] = content_list
        return context

class Section2(Section):
    section_style = 'dark'
    section_title = "Choose CyberSkills2Work"
    section_text = "CyberSkills2Work sharpens your technical skills so you become cyber savvy. Besides gaining a better understanding of threats to the cyberworld, you’ll learn hands-on how to foil them with real-world techniques. If accepted to the program, you’ll enjoy the training experience and milestones along the way as you make these strides:"
    section_content = LearnersWrapper

checklist3_items = [
    {
        'title': 'Discover Your Cyber Aptitude',
        'text': "Assess your natural cyber talent and capabilities. Learn what NICE Cybersecurity Framework work roles best fit your abilities.</br></br><a href='/'>Take the aptitude test>>></a>"
    },
    {
        'title': 'Choose a Pathway',
        'text': "After discovering your ideal work role, select the equivalent pathway that gets your cyber training underway.</br></br><a href='/'>Search our programs>>></a>"
    },
    {
        'title': 'Apply',
        'text': "Are you eligible? Find out. Answer a few qualifying questions and ensure that you have all required documents on hand.</br></br><a href='/'>Learn how to apply>>></a>"
    }
]

class Section3Checklist(LearnersChecklist):
    checklist = checklist3_items

class Section3(Section):
    section_style = 'light'
    section_title = "Getting Started"
    section_text = "If you have a passion for computers and the internet and you’re interested in joining the cyberworkforce, try CyberSkills2Work. Find out if you’re an ideal fit for the cybersecurity workforce program. You’re only steps away from finding out if a career of fighting cybercrime is truly your destiny."
    section_content = Section3Checklist

class Section4Button(SimpleButton):
    button_text = 'Apply Now'
    button_link = '/'

class Section4(Section):
    section_style = 'dark'
    section_title = "Are you up for the task?"
    section_text = "Apply to CyberSkills2Work and get a jumpstart on your cybersecurity career. You're headed in the right cyber direction."
    section_button = Section4Button

class Learners(SectionWrapper):
    banner = LearnersBanner
    sections = [Section1, Section2, Section3, Section4]
