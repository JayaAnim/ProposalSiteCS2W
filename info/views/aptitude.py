#Cyber aptitude view
from .base import *

class AptitudeBanner(Banner):
    image_link = 'info/img/cyber-aptitude-banner.png'
    banner_title = 'Determine Your Cyber Aptitude' 
    banner_sub_title = 'Take our cyber aptitude assessment to uncover your flair for cybersecurity work' 

class Section1(Section):
    section_style = 'light'
    section_title = 'Finding The Best Cybersecurity Work Role For You'
    section_text = "Our cyber aptitude assessment helps determine which cybersecurity work roles best suit your abilities. Basically, it reveals your potential to perform cybersecurity work. The National Initiative for Cybersecurity Education (NICE) Cybersecurity Workforce Framework sets skill standards for a broad spectrum of work in the industry. Those job skills can be learned since CyberSkills2Work imparts computer and cybersecurity knowledge. However, a learner needs natural thinking ability to succeed in any cybersecurity work role. The assessment reveals an individual's natural critical thinking ability and identifies strengths that are ideal for certain cybersecurity jobs. Take it, now."

class Section2Content(BaseTemplateView):
    template_name = 'info/aptitude/CyberAptitude.html'

class Section2Button(SimpleButton):
    button_text = 'Assessment'
    button_link = '/'

class Section2(Section):
    section_style = 'dark'
    section_title = 'About the Cyber Aptitude Assessment'
    section_text = "Cognitive ability, processing speed, and matrix reasoning are just some of the skills that the cyber aptitude assessment measures. It evaluates a participant's comfort level with accomplishing critical thinking tasks, solving complex puzzles, and taking deliberate action to resolve problems. It does not test your knowledge of cybersecurity. It specifically recognizes essential abilities needed to fulfill basic cybersecurity work role duties.</br></br>The online assessment takes approximately 45 minutes to complete, so give yourself plenty of time to finish the exam. It is recommended that you take the assessment in a quiet setting, free of distractions, and use a reliable internet service. You are not required to take the assessment in one sitting. You may take it in parts and complete any remaining sections later. However, we strongly urge you to complete given tasks that you've started to avoid receiving incomplete assessment results."
    section_content = Section2Content
    section_button = Section2Button
    
class Aptitude(SectionWrapper):
    banner = AptitudeBanner
    sections = [Section1, Section2]