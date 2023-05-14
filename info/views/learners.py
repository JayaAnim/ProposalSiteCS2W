#Learners page view
from .base import *

class LearnersBanner(Banner):
    image_link = 'info/img/learners-banner.png'
    banner_title = 'Program Learners'
    banner_sub_title = 'Developing skills for diverse cybersecurity roles.'

class Section1(Section):
    section_style = 'light'
    section_title = "Navigating the Field of Cybersecurity"
    section_text = "The future is bright for CyberSkills2Work program learners. The growing cybersecurity field needs skilled professionals who can expose and fight cybercrimes. The program trains people who are keenly interested in working in the broad cybersecurity field. We’ll help you identify an ideal work role to pursue, based on your experience, interests, and aptitude. With the right qualifications and drive to succeed, you might be a perfect fit for CyberSkills2Work. Participation is free for qualifying veterans, transitioning military personnel, and first responders interested in launching or advancing a cybersecurity career."

class Section2(Section):
    section_style = 'dark'
    section_title = "Choose CyberSkills2Work"
    section_text = "CyberSkills2Work sharpens your technical skills so you become cyber savvy. Besides gaining a better understanding of threats to the cyberworld, you’ll learn hands-on how to foil them with real-world techniques. If accepted to the program, you’ll enjoy the training experience and milestones along the way as you make these strides:"

class Section3(Section):
    section_style = 'light'
    section_title = "Getting Started"
    section_text = "If you have a passion for computers and the internet and you’re interested in joining the cyberworkforce, try CyberSkills2Work. Find out if you’re an ideal fit for the cybersecurity workforce program. You’re only steps away from finding out if a career of fighting cybercrime is truly your destiny."

class Section4(Section):
    section_style = 'dark'
    section_title = "Are you up for the task?"
    section_text = "Apply to CyberSkills2Work and get a jumpstart on your cybersecurity career. You're headed in the right cyber direction."
    section_button = "Apply Now"
    section_button_link = "/"

class Learners(SectionWrapper):
    banner = LearnersBanner
    sections = [Section1, Section2, Section3, Section4]
