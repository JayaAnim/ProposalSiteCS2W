#What people say view
from .base import *

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
    }
]


class Testimonial(BaseTemplateView):
    template_name = 'info/discourse/Testimonial.html'
    image_link = ''
    testimonial_name = ''
    testimonial_position = ''
    testimonial_text = ''
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_link'] = kwargs.get('image_link')
        context['testimonial_name'] = kwargs.get('testimonial_name')
        context['testimonial_position'] = kwargs.get('testimonial_position')
        context['testimonial_text'] = kwargs.get('testimonial_text')
        return context