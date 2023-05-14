#FAQ page view
from .base import *

class FAQBanner(Banner):
    image_link = 'info/img/faq-banner.png'
    banner_title = 'Frequently Asked Questions'
    banner_sub_title = 'Get answers to most frequently asked questions about CyberSkills2Work.'

class Accordian(BaseTemplateView):
    template_name = 'info/faq/Accordian.html'
    questions = []
    accordion_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questions'] = self.questions
        context['accordion_name'] = self.accordion_name
        return context

section1_questions = [
    {'heading_control': 'flush-headingOne', 'collapse_control': 'flush-collapseOne', 'question': 'Why is CyberSkills2Work offered free to participants?', 'answer': 'It is a federally funded program designed to expand the nation’s cybersecurity workforce. It supports national efforts to get more qualified men, women, and minorities into cybersecurity work roles. It is offered free as an incentive, especially for veterans, transitioning military personnel, and first responders.'},
    {'heading_control': 'flush-headingTwo', 'collapse_control': 'flush-collapseTwo', 'question': 'Is there a certain age requirement to participate in the program?', 'answer': 'Eligible applicants must be at least 18 years old to participate in the program.'},
    {'heading_control': 'flush-headingThree', 'collapse_control': 'flush-collapseThree', 'question': 'What is considered a first responder?', 'answer': 'A first responder is a person who is trained and works professionally to respond to emergency situations and provide assistance during crisis incidents. Firefighters, emergency medical technicians, paramedics, 911 dispatchers, and law enforcement officers are considered first responders.'},
    {'heading_control': 'flush-headingFour', 'collapse_control': 'flush-collapseFour', 'question': 'Do I need to get my overseas transcript reviewed to apply?', 'answer': 'Yes. It is encouraged. The minimum requirement for an applicant is a high school diploma, so we need to obtain your recent transcript to further support your application, no matter if you attended a school overseas.'},
    {'heading_control': 'flush-headingFive', 'collapse_control': 'flush-collapseFive', 'question': 'Can I reapply if my application is not accepted?', 'answer': 'Indeed. We welcome any unselected applicants to reapply in following years, after meeting eligibility requirements. Once background, education, or any other requirements are met, applicants are encouraged to reapply to the program.'},
    {'heading_control': 'flush-headingSix', 'collapse_control': 'flush-collapseSix', 'question': 'Are the courses self-paced or are participants required to attend classes virtually at a certain time?', 'answer': 'It depends on the pathway training selected. Course delivery formats vary from in-person to hybrid, asynchronous synchronous online, depending on the institution providing the training.'},
    {'heading_control': 'flush-headingSeven', 'collapse_control': 'flush-collapseSeven', 'question': 'Can I apply to more than one pathway training program?', 'answer': 'Certainly. However, we require that accepted learners enroll in one training program at a time. They must complete one training program before applying to another one.'},
    {'heading_control': 'flush-headingEight', 'collapse_control': 'flush-collapseEight', 'question': 'Does CyberSkills2Work offer assistance with acquiring needed course materials, such as a laptop or high-speed internet?', 'answer': 'The program covers courses, exam vouchers, and all other materials (including e-books, videos, and training labs) free of charge to accepted learners. The program does not provide laptop and high-speed internet.'},
    {'heading_control': 'flush-headingNine', 'collapse_control': 'flush-collapseNine', 'question': 'Am I automatically placed in a job after graduating from CyberSkills2Work?', 'answer': 'No. CyberSkills2Work assists learners with job placement and connects them with employers who are looking to fill vacant cybersecurity positions via the National Cybersecurity Employers Network. Learners also have free access to a job board on the MyCyberSkills2Work portal, where they’re able to search for openings and apply to positions there. The program also provides career development resources to help participants market themselves for future job opportunities.'},
    {'heading_control': 'flush-headingTen', 'collapse_control': 'flush-collapseTen', 'question': 'If I am unable to complete a pathway training program, due to unforeseen circumstances, will I be able to reconvene at another time?', 'answer': 'Yes. You may reapply, but acceptance isn’t guaranteed. If you are readmitted, the corresponding institution will confer with you on the best course of action for resuming your program training.'},
    {'heading_control': 'flush-headingEleven', 'collapse_control': 'flush-collapseEleven', 'question': 'Am I required to take the cyber aptitude assessment before applying to the program?', 'answer': 'Not at all. The cyber aptitude assessment is optional but definitely encouraged. The assessment will help you determine what cybersecurity work roles best suit you, based on your aptitude.'},
]

class Section1Accordian(Accordian):
    questions = section1_questions
    accordion_name = 'accordionExample1'

class Section1(Section):
    section_style = 'light'
    section_title = 'Learners'
    section_content = Section1Accordian

section2_questions = [
    {'heading_control': 'flush-headingTwelve', 'collapse_control': 'flush-collapseTwelve', 'question': 'Does it cost to join the coalition?', 'answer': 'No, it does not. Membership is free for NCAE-C colleges and universities to participate in CyberSkills2Work. We only require that representatives of institutions devote time and effort to help promote CyberSkills2Work, contribute ideas, teach learners, and provide data on program and participant outcomes.'},
    {'heading_control': 'flush-headingThirteen', 'collapse_control': 'flush-collapseThirteen', 'question': "Can I still join the coalition if my institution isn’t designated a National Center of Academic Excellence in Cybersecurity?", 'answer': 'No. Only NCAE-C designated institutions with established or developing cybersecurity workforce programs are eligible to teach and help develop curricula for CyberSkills2Work at this time. However, if interested, your institution could support the program as a partner. Contact us to express your interest in the program.'},
    {'heading_control': 'flush-headingFourteen', 'collapse_control': 'flush-collapseFourteen', 'question': 'Does CyberSkills2Work help NCAE-C designated colleges or universities develop a cybersecurity workforce program?', 'answer': 'Yes. Eligible institutions can leverage the CyberSkills2Work platform and tools to offer workforce development programs, including an aptitude assessment tool, common application, and Employers Network. In addition, they can use or adapt available curricula and resources to develop training courses and pathways.'},
    {'heading_control': 'flush-headingFifteen', 'collapse_control': 'flush-collapseFifteen', 'question': 'If accepted to the coalition, can my institution drop out at any time?', 'answer': 'Yes. There is currently no required length of participation for institutions accepted to the coalition. However, institutions must meet performance measures to retain membership.'},
]

class Section2Accordian(Accordian):
    questions = section2_questions
    accordion_name = 'accordionExample2'

class Section2(Section):
    section_style = 'light'
    section_title = 'Institutions'
    section_content = Section2Accordian

section3_questions = [
    {'heading_control': 'flush-headingSixteen', 'collapse_control': 'flush-collapseSixteen', 'question': 'Is a membership fee required to join the National Cybersecurity Employers Network?', 'answer': 'No. Network membership doesn’t cost anything; only your time and effort are required.'},
    {'heading_control': 'flush-headingSeventeen', 'collapse_control': 'flush-collapseSeventeen', 'question': 'What are the requirements for admission to the network?', 'answer': 'Any organization with current or future cybersecurity job opportunities is eligible to join the National Cybersecurity Employers Network. Organizations are encouraged to support the program by considering the recruitment of program graduates and/or providing feedback on employment needs and program pathways and curricula.'},
    {'heading_control': 'flush-headingEighteen', 'collapse_control': 'flush-collapseEighteen', 'question': 'Can my organization still join if it doesn’t fall under a critical infrastructure sector?', 'answer': 'Yes. While the program emphasizes organizations in the critical infrastructure sectors, all employers with cybersecurity positions are eligible to join.'},
    {'heading_control': 'flush-headingNineteen', 'collapse_control': 'flush-collapseNineteen', 'question': 'What is the primary role of a network member?', 'answer': 'Basically, our network employers connect program learners and graduates to career opportunities within their organizations. They interact with learners via webinars and other program activities. They share cybersecurity career opportunities, consider program graduates for job openings, and provide feedback to improve the program. Get more information.'},
    {'heading_control': 'flush-headingTwenty', 'collapse_control': 'flush-collapseTwenty', 'question': 'Can I recommend other organizations to join the network?', 'answer': 'Certainly. We welcome employers who are interested in CyberSkills2Work. If you know an organization that is specifically interested in hiring and mentoring cybersecurity professionals, please encourage it to apply for membership to the National Cybersecurity Employers Network.'},
]

class Section3Accordian(Accordian):
    questions = section3_questions
    accordion_name = 'accordionExample3'

class Section3(Section):
    section_style = 'light'
    section_title = 'Employers'
    section_content = Section3Accordian
    
class FAQ(SectionWrapper):
    banner = FAQBanner
    sections = [Section1, Section2, Section3]