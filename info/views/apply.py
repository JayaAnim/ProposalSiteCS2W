#Apply page view
from .base import *

class ApplyBanner(BaseTemplateView):
    template_name = 'info/apply/ApplyBanner.html'

class Section1(Section):
    section_style = 'light'
    section_title = 'Before You Apply'
    section_text = 'Wait! Make sure that you meet basic program criteria before you apply for cybersecurity training with CyberSkills2Work. Keep these key qualifications in mind:'

class Section2(Section):
    section_style = 'dark'
    section_title = 'What You Will Need'
    section_text = "Before attempting to fill out the application, gather all essential documents and keep them on hand. The following materials must be submitted with your CyberSkills2Work application:"

class Section3(Section):
    section_style = 'light'
    section_title = 'Additional Requirements by Institution'
    section_text = "Besides meeting minimum requirements for program participation, eligible applicants must also meet the prerequisites of our educational institutions. Each institution may have additional qualification requirements for acceptance in CyberSkills2Work pathway training programs. Choose from the following list of educational institutions to get information about a school’s eligibility requirements:"

class Section4(Section):
    section_style = 'dark'
    section_title = 'Understanding the Terms of Participation'
    section_text = "CyberSkills2Work offers an extraordinary learning experience and career development opportunity for program participants. Learners of our program are privileged to receive free cybersecurity education and career guidance from national experts. In order to enjoy the full benefits of the program, all eligible participants must comply with these terms:"

class Section5(Section):
    section_style = 'light'
    section_title = "Ready to Apply?"
    section_text = "Don’t delay. Start your CyberSkills2Work application, today. Provide all requested materials, and check your personal, educational, and work history information for accuracy before submitting the application. Don’t fret if you can’t complete the application in one sitting. You may save your application and finish it later with your application login credentials."

class Section6(Section):
    section_style = 'dark'
    section_title = "After You Apply"
    section_text = "Now that you’ve applied, what’s next? With your login credentials, you can manage your application while you await an acceptance decision. Here’s what you can do:"

class Apply(SectionWrapper):
    banner = ApplyBanner
    sections = [Section1, Section2, Section3, Section4, Section5, Section6]