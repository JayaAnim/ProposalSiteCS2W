#Apply page view
from .base import *

class BannerButton(ApplyButton):
    button_text = 'Start Your Application'

class ApplyBanner(BaseTemplateView):
    template_name = 'info/apply/ApplyBanner.html'
    button = BannerButton

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button'] = self.button.as_view()(self.request).rendered_content
        return context
    
class Checklist(BaseTemplateView):
    template_name = 'info/apply/CheckList.html'
    checklist = []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['checklist'] = self.checklist
        return context

section1_checklist = [
    {
        'title': 'Program Eligibility',
        'text': 'A high school diploma and U.S. citizenship are the minimum requirements for program eligibility.',
    },
    {
        'title': 'Pathway Training Programs',
        'text': 'CyberSkills2Work pathway training programs are free to eligible veterans, transitioning military personnel, and first responders.',
    },
    {
        'title': 'Determine Your Cyber Aptitude',
        'text': 'We highly recommend that you take our cyber aptitude assessment before submitting a program application. The assessment will help determine which work roles suit you best, based on your demonstrated abilities. Then, on the program application, you will be able to select the pathway training program for your chosen work role.',
    },
]

class Section1List(Checklist):
    checklist = section1_checklist

class Section1Button(SimpleButton):
    button_text = 'Assessment'
    button_link = '/'

class Section1(Section):
    section_style = 'light'
    section_title = 'Before You Apply'
    section_text = 'Wait! Make sure that you meet basic program criteria before you apply for cybersecurity training with CyberSkills2Work. Keep these key qualifications in mind:'
    section_content = Section1List
    section_button = Section1Button

section2_checklist = [
    {
        'title': 'Service Records',
        'text': 'We must receive proof of your military service. Acceptable documents include a DD214, DD215, or Record of Separation. First responders must furnish a signed verification letter of employment (on the organization’s official letterhead), confirming present or previous job status. The letter should include dates of service, position held, duties performed, and contact information for the employer who can verify your employment.',
    },
    {
        'title': 'Proof of U.S. Citizenship',
        'text': 'Only documented proof of citizenship is accepted, including a birth certificate; U.S. passport or passport card; or a Permanent Resident Card/Alien Registration Receipt Card.',
    },
    {
        'title': 'Résumé',
        'text': 'Provide a complete outline of your current and previous education, job titles and duties, and employers.',
    },
    {
        'title': 'School Transcripts',
        'text': 'Proof of your highest level of formal education is required. A copy of an educational record (such as a high school diploma, GED, or college transcript) is acceptable.',
    },
    {
        'title': 'Letter of Intent',
        'text': 'Express your intentions for the cybersecurity field and CyberSkills2Work in a formal letter of interest.',
    },
    {
        'title': 'Valid Photo ID',
        'text': 'Valid credentials are a state driver’s license or identification card.',
    },
]

class Section2List(Checklist):
    checklist = section2_checklist

class Section2(Section):
    section_style = 'dark'
    section_title = 'What You Will Need'
    section_text = "Before attempting to fill out the application, gather all essential documents and keep them on hand. The following materials must be submitted with your CyberSkills2Work application:"
    section_content = Section2List

"""
UNDER WORK
WAITING FOR PROGRAMS TO BE COMPLETE TO DYNAMICALLY GENERATE THIS CONTENT
class Section3(Section):
    section_style = 'light'
    section_title = 'Additional Requirements by Institution'
    section_text = "Besides meeting minimum requirements for program participation, eligible applicants must also meet the prerequisites of our educational institutions. Each institution may have additional qualification requirements for acceptance in CyberSkills2Work pathway training programs. Choose from the following list of educational institutions to get information about a school’s eligibility requirements:"
"""

section4_list = [
    "Register with CyberSkills2Work upon program approval and manage your learner profile in the MyCyberSkills2Work portal.",
    "Provide your own personal computer with a reliable internet connection.",
    "Reside in the U.S. throughout the duration of an elected training program.",
    "Engage in all program activities, courses, exam preparation, assigned labs, job fairs, and workshops. Participants who fail to participate in activities or exercises or simply fail to show effort may be disqualified.",
    "Remain in good academic standing.",
    "Maintain perfect attendance and provide documentation for any excused absences.",
    "Search for post-program employment with employers in critical infrastructure sectors."
]

class Section4List(UnorderedList):
    list_items = section4_list

class Section4(Section):
    section_style = 'light'
    section_title = 'Understanding the Terms of Participation'
    section_text = "CyberSkills2Work offers an extraordinary learning experience and career development opportunity for program participants. Learners of our program are privileged to receive free cybersecurity education and career guidance from national experts. In order to enjoy the full benefits of the program, all eligible participants must comply with these terms:"
    section_content = Section4List

class Section5Button(ApplyButton):
    button_text = 'Apply'

class Section5(Section):
    section_style = 'dark'
    section_title = "Ready to Apply?"
    section_text = "Don’t delay. Start your CyberSkills2Work application, today. Provide all requested materials, and check your personal, educational, and work history information for accuracy before submitting the application. Don’t fret if you can’t complete the application in one sitting. You may save your application and finish it later with your application login credentials."
    section_button = Section5Button

section6_list = [
    "Print your application.",
    "Update previously provided information.",
    "Upload required documents."
]

class Section6List(UnorderedList):
    list_items = section6_list

class Section6(Section):
    section_style = 'light'
    section_title = "After You Apply"
    section_text = "Now that you’ve applied, what’s next? With your login credentials, you can manage your application while you await an acceptance decision. Here’s what you can do:"
    section_content = Section6List

class Apply(SectionWrapper):
    banner = ApplyBanner
    sections = [Section1, Section2, Section4, Section5, Section6]