#What people say view
from .base import *

class TestimonialBanner(Banner):
    image_link = 'info/img/what-people-say-banner.png'
    banner_title = 'What People Say About CyberSkills2Work'
    banner_sub_title= 'How graduates, professors, employers, and partners feel about the program.'

# Define an array of dictionaries containing context data for Testimonial view
testimonial_data = [
    {
        'image_link': 'info/img/Janice-Sanders.jpg',
        'testimonial_name': 'Janice Sanders',
        'testimonial_position': "CyberSkills2Work '22 graduate",
        'testimonial_text': '“This program has allowed me to gain invaluable skills through the curriculum, as well as the hands-on application of the learning through the CTF\'s and Tabletop exercises. This program has opened many opportunities for me, and I am eager to see what the journey brings.”'
    },
    {
        'image_link': 'info/img/Steven-MacDonald.jpg',
        'testimonial_name': 'Steven MacDonald',
        'testimonial_position': "CyberSkills2Work '22 graduate",
        'testimonial_text': '“This was an amazing opportunity that I was fortunate to be selected for. This program has greatly enhanced my knowledge of not only networks through the Network+ certification but also the CySA+ certificate. I would highly encourage anyone that has this opportunity to not only further their knowledge but also take advantage of the career advancement that is now within reach.”'
    },
    {
        'image_link': 'info/img/Eman-El-Sheikh.jpg',
        'testimonial_name': 'Dr. Eman El-Sheikh',
        'testimonial_position': "CyberSkills2Work Principal Investigator",
        'testimonial_text': '“CyberSkills2Work has emerged as a nationally recognized cybersecurity training program. We’re honored to have a hand in steering the future of cybersecurity while developing the future workforce. This program is strategically preparing our country against malicious cyberattacks.”'
    },
    {
        'image_link': 'info/img/Justin-Rhoads.jpg',
        'testimonial_name': 'Justin Rhoads',
        'testimonial_position': "CyberSkills2Work '21 graduate",
        'testimonial_text': '“As a veteran, this program equipped me with the valuable skills that I needed to enter into a new career field and secure a job in the cybersecurity industry. Because of the CyberSkills2Work program, I now have a promising new career, a bright future, and I have bettered the lives of myself and my family.”'
    },
    {
        'image_link': 'info/img/Wallace-Williams.jpg',
        'testimonial_name': 'Wallace Williams',
        'testimonial_position': "CyberSkills2Work '21 graduate",
        'testimonial_text': '“The CyberSkills2Work program gave me a new perspective on the many aspects of cybersecurity. I am able to build off the fundamentals and use the knowledge gained from courses to enhance and upskill my current skill set.”'
    },
    {
        'image_link': 'info/img/Cesar-Argueta2.jpg',
        'testimonial_name': 'Cesar Argueta',
        'testimonial_position': "CyberSkills2Work '21 graduate",
        'testimonial_text': '“The program allowed me to enhance my IT skills and provided me with the fundamentals of cybersecurity. Additionally, the program has helped me better understand the importance of cybersecurity and how to incorporate my newly learned skills to improve security measures within my current role as Sr. Security Analyst.”'
    },
    {
        'image_link': 'info/img/William-Mechler-CyberSkills2Work-22.jpg',
        'testimonial_name': 'William Mechler',
        'testimonial_position': "CyberSkills2Work '22 learner",
        'testimonial_text': '“The training and skills I learned through the CyberSkills2Work program gave me the practical skill set needed to land my dream job. The skills I learned in this program I use daily.”'
    },
    {
        'image_link': 'info/img/Jeunz-Rojas.png',
        'testimonial_name': 'Jenuz Rojas',
        'testimonial_position': "CyberSkills2Work '21 graduate",
        'testimonial_text': '“I love that the program was completely FREE, the program invested in me, and all it required was my commitment and time. Also, it was completely 100% asynchronous online, making it easier to be a part of since I was a full-time student and worked full time.”'
    },
    {
        'image_link': 'info/img/Man-Anonymous-Testimony.jpg',
        'testimonial_name': 'Sanjay ​Sey',
        'testimonial_position': "CyberSkills2Work '22 learner",
        'testimonial_text': '"I particularly enjoyed the Public Records and Technical Research week. It is the delivery of the class material that I was the most impressed with. I gained so much confidence towards how to structure my online research more systematically and where to look for information."'
    },
]


class Testimonial(BaseTemplateView):
    template_name = 'info/discourse/Testimonial.html'
    image_link = ''
    testimonial_name = ''
    testimonial_position = ''
    testimonial_text = ''
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_link'] = self.image_link
        context['testimonial_name'] = self.testimonial_name
        context['testimonial_position'] = self.testimonial_position
        context['testimonial_text'] = self.testimonial_text
        return context
    
class TestimonialRow(BaseTemplateView):
    template_name = 'info/discourse/TestimonialRow.html'
    testimonial_array = []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rendered_testimonials = []
        for testimonial in self.testimonial_array:
            rendered_testimonial = Testimonial.as_view(
                image_link=testimonial['image_link'],
                testimonial_name=testimonial['testimonial_name'],
                testimonial_position=testimonial['testimonial_position'],
                testimonial_text=testimonial['testimonial_text']
            )(self.request).rendered_content
            rendered_testimonials.append(rendered_testimonial)
        context['testimonials'] = rendered_testimonials
        return context
    
class Row1(TestimonialRow):
    testimonial_array = testimonial_data[:3]

class Row2(TestimonialRow):
    testimonial_array = testimonial_data[3:6]

class Row3(TestimonialRow):
    testimonial_array = testimonial_data[6:9]
    
class TestimonialWrapper(BaseTemplateView):
    template_name = 'info/discourse/TestimonialWrapper.html'
    testimonial_rows = [Row1, Row2, Row3]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rendered_rows = []
        for testimonial_row in self.testimonial_rows:
            rendered_rows.append(testimonial_row.as_view()(self.request).rendered_content)
        context['testimonial_rows'] = rendered_rows
        return context
    
class Section1(Section):
    section_style = 'light'
    section_title = 'CyberSkills2Work Testimonials'
    section_text = "Knowing what people say about CyberSkills2Work might help you decide if it's worth your time or investment. Consider comments from people, nationwide, who are involved in different facets of the program. Get their firsthand thoughts about the program’s benefits."
    section_content = TestimonialWrapper
    
class Discourse(BaseTemplateView):
    template_name = 'info/discourse/Discourse.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sections = []
        context['banner'] = TestimonialBanner.as_view()(self.request).rendered_content
        sections.append(Section1.as_view()(self.request).rendered_content) 
        context['sections'] = sections
        return context
        
    