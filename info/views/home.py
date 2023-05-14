#Home page view
from .base import *
from .discourse import Testimonial, TestimonialRow, testimonial_data

""""
This views file renders the static content for the homepage and passes the static content to the homepage view
"""

# ============================== Section 1 View/Content Views ============================== #

class Card1(Card):
    card_image = "info/img/cybercrime.jpg"
    card_text = "The annual global cost of cybercrime damages is about $6 trillion and is expected to increase to $10.5 trillion by 2025. In 2020, reported financial losses from cybercrime in the U.S. cost over $4.1 billion, a 69% increase from 2019. Source: CyberSecurity Ventures, FBI"

class Card2(Card):
    card_image = "info/img/cybersecurity-workforce-gaps.jpg"
    card_text = "Currently, there are 3.5 million unfilled cybersecurity jobs globally and close to 600,000 nationally. Source: CyberSecurity Ventures"

class Card3(Card):
    card_image = "info/img/cybersecurity-training-needs.jpg"
    card_text = "Reportedly, 95% of all cybersecurity breaches are due to human error and 69% of organizations indicate that their cybersecurity teams are understaffed. Source: IBM and ISACA"

class Section1Button(SimpleButton):
    button_text = 'Learn More'
    button_link = '/'

class Section1(Section):
    section_style = 'light'
    section_title = "Cybersecurity Today: A Call to Action"
    section_text = "CyberSkills2Work supporters hear the nation’s call for more cybersecurity in today’s ever-evolving cyberage. Cyberspace is continually advancing with more sophisticated ways to conduct business, socialize, and shop online. As it evolves, so does cybercrime. Cybersecurity analysts emphasize the need to take action on cybercriminals and develop a solid cyberdefense against computer crimes. Having skilled cybersecurity professionals at the frontline of cyberdefense helps protect networks, devices, and data from unlawful internet activity. According to <a href='https://www.cyberseek.org/' target='_blank'>CyberSeek</a>, the U.S. has a shortfall of about 597,767 cybersecurity professionals. More skilled professionals are needed to tackle the nation’s top cybersecurity challenges:"
    section_content = CardSlider
    section_button = Section1Button

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section_content'] = self.section_content.as_view(cards=[Card1, Card2, Card3])(self.request).rendered_content
        return context
    
# ============================== Section 2 View/Content Views ============================== #

class Section2Button(SimpleButton):
    button_text = 'Learn More'
    button_link = '/'
    
class Section2(Section):
    section_style = 'dark'
    section_title = "CyberSkills2Work Responds to the Call"
    section_text = "CyberSkills2Work, established in 2020, is responding to the nation’s call for more cybersecurity measures. It is building a strong labor force to fight cyberthreats to organizations across critical infrastructure sectors, including finance. CyberSkills2Work equips transitioning military members, veterans, and first responders with necessary skills to combat today’s top cybersecurity threats. The program, a network of America’s leading cybersecurity universities and Fortune 500 companies, provides training, career development, and job placement support to its learners. With in-person and virtual course options, CyberSkills2Work is one of the best free, online cybersecurity training programs in the USA. After completing the program, graduates receive certification and digital badges that document their earned credentials. They also are connected with employers and cybersecurity job opportunities to begin or advance their careers. CyberSkills2Work addresses an urgent demand to fill the cybersecurity workforce gap with skilled individuals who can help curtail cybercrimes."
    section_image = 'info/img/military-cybersecurity-person.jpg'
    section_button = Section2Button

# ============================== Section 3 View/Content Views ============================== #

class Image1(Image):
    image_interval = 2500
    image_link = 'info/img/program-impact-certifications-offered.png'
    image_description = 'Program certifications offered' 

class Image2(Image):
    image_interval = 1750
    image_link = 'info/img/program-impact-education-value.png'
    image_description = 'Education value'

class Image3(Image):
    image_interval = 1750
    image_link = 'info/img/program-impact-employers.png'
    image_description = 'Employers impact'

class Image4(Image):
    image_interval = 1750
    image_link = 'info/img/program-impact-work-roles.png'
    image_description = 'Work roles impact'

class Image5(Image):
    image_active = True
    image_interval = 1750
    image_link = 'info/img/program-impact-trained-professionals.png'
    image_description = 'Trained professionals impact'

class Section3Button(SimpleButton):
    button_text = 'Learn More'
    button_link = '/'

class Section3(Section):
    section_style = 'light'
    section_title = 'Program Impact'
    section_content = ImageSlider
    section_button = Section3Button

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section_content'] = self.section_content.as_view(images=[Image1, Image2, Image3, Image4, Image5])(self.request).rendered_content
        return context
    
# ============================== Section 4 View/Content Views ============================== #

class HomeTestimonials(TestimonialRow):
    testimonial_array = testimonial_data[:3]

class Section4Button(SimpleButton):
    button_text = 'View More'
    button_link = '/'

class Section4(Section):
    section_style = 'dark'
    section_title = 'What People Say About CyberSkills2Work'
    section_content = HomeTestimonials
    section_button = Section4Button

# ============================== Section 5 View/Content Views ============================== #

class ImageRow(BaseTemplateView):
    template_name = 'info/home/ImageRow.html'
    row_image = None
    row_text = None
    row_title = None
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['row_image'] = self.row_image
        context['row_text'] = self.row_text
        context['row_title'] = self.row_title
        return context
    
class ImageRow1(ImageRow):
    row_image = 'info/img/CyberSkills2Work-learning.jpg'
    row_text = 'Do you have some IT or cybersecurity experience and want to further your career in the field? If you’re a transitioning military person, veteran or first responder, apply to CyberSkills2Work. Take our aptitude test to see what cybersecurity work role or career path is best for you. This program could be your free ticket to journey a long and rewarding career in cybersecurity. </br> <a href="/" target="_blank">Learn More >>></a>'
    row_title = 'Learners'

class ImageRow2(ImageRow):
    row_image = 'info/img/CyberSkills2Work-Institution.jpg' 
    row_text = 'CyberSkills2Work comprises nine educational institutions that are designated National Centers of Academic Excellence in Cybersecurity (NCAE-C). Each institution offers free, certified and credentialed cybersecurity courses that prepare learners for entry-level employment in pursued work roles. Is your institution an NCAE-C that offers a cybersecurity workforce program? If so, join us! </br> <a href="/" target="_blank">Learn More >>></a>'
    row_title = 'Institutions'

class ImageRow3(ImageRow):
    row_image = 'info/img/CyberSkills2Work-Employers-Network.jpg'
    row_text = 'Finding skilled workers to fill cybersecurity jobs can be difficult. However, CyberSkills2Work has simplified the hiring and job-finding process. Join our network of 40+ employers who are actively filling and sharing cybersecurity job vacancies with program graduates. </br> <a href="/" target="_blank">Learn More >>></a>'
    row_title = 'Employers Network'

class ImageRow4(ImageRow):
    row_image = 'info/img/CyberSkills2Work-Partners.jpg'
    row_text = 'CyberSkills2Work invites individuals and organizations to support the program and help it reach underrepresented and underserved populations. With your help, the program can provide opportunities to transitioning and retired military persons, first responders, veterans, women, and minorities. Help us promote, market, and expand the program. </br> <a href="/" target="_blank">Learn More >>></a>'
    row_title = 'Program Partners'

class RowWrapper(BaseTemplateView):
    template_name = 'info/home/RowWrapper.html'
    rows = []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        rendered_rows = []
        rendered_rows.append(ImageRow1.as_view()(self.request).rendered_content)
        rendered_rows.append(ImageRow2.as_view()(self.request).rendered_content)
        rendered_rows.append(ImageRow3.as_view()(self.request).rendered_content)
        rendered_rows.append(ImageRow4.as_view()(self.request).rendered_content)
        context['rows'] = rendered_rows
        return context


class Section5(Section):
    section_style = 'light'
    section_title = 'Take Action! Join the Community'
    section_content = RowWrapper

# ============================== Section 6 View/Content Views ============================== #

class Section6Button(SimpleButton):
    button_text = 'Programs'
    button_link = '/'

class Section6(Section):
    section_style = 'dark'
    section_title = 'Cybersecurity Work Roles, Pathways, and Training Institutions'
    section_text = 'Develop work-ready skills in the cybersecurity field. Choose from various different work roles for cybersecurity training. Follow the pathway of courses offered by CyberSkills2Work’s coalition of NCAE-C institutions.'
    section_button = Section6Button

# ============================== Home View ============================== #

class Home(BaseTemplateView):
    template_name = 'info/home/Home.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        home_sections = []
        home_sections.append(Section1.as_view()(self.request).rendered_content)
        home_sections.append(Section2.as_view()(self.request).rendered_content)
        home_sections.append(Section3.as_view()(self.request).rendered_content)
        home_sections.append(Section4.as_view()(self.request).rendered_content)
        home_sections.append(Section5.as_view()(self.request).rendered_content)
        home_sections.append(Section6.as_view()(self.request).rendered_content)
        context['sections'] = home_sections
        return context
