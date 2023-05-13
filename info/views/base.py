#Parent components and container for other views
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

""""
This views file contains reusable views to be passed down to other views for modular rendering
"""

#Base view to be passed to all static views
class Base(TemplateView):
    page_title = "CyberSkills2Work"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context

class BaseTemplateView(Base, TemplateView):
    pass

#Reusable section view to render each section of info pages
class Section(BaseTemplateView):
    """"
    section_style is section background color (light or dark)
    section_title is title displayed above section
    section_text is optional text displayed below title
    section_image is optional image to be displayed next to text
    section_content is optional rendered content from other static views to insert below text
    section_button tells section whether to render a button and specifies the name of that button
    section_button_link specifies link button leads to (uses django url tag)
    """
    template_name = 'info/base/Section.html'
    section_style = 'light'
    section_title = None
    section_text = None
    section_image = None
    section_content = None
    section_button = None
    section_button_link = None
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section_style'] = self.section_style
        context['section_title'] = self.section_title 
        context['section_text'] = self.section_text
        context['section_image'] = self.section_image
        if self.section_content:
            context['section_content'] = self.section_content.as_view()(self.request).rendered_content
        else:
            context['section_content'] = self.section_content
        context['section_button'] = self.section_button
        context['section_button_link'] = self.section_button_link

        return context 

#Reusable cardslider that users to can flip through
class CardSlider(BaseTemplateView):
    """
    cards are the card views to be inserted into cardslider
    """
    template_name = 'info/base/CardSlider.html'
    cards = []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rendered_cards = []
        for card in self.cards:
            rendered_cards.append(card.as_view()(self.request).rendered_content)
        context['cards'] = rendered_cards
        return context 

#Reusable card that is used for cardslider
class Card(BaseTemplateView):
    """
    card_image specifies relative link to image that card will use (static tag is used)
    card_text specifies text that card will use
    """
    template_name = 'info/base/Card.html'
    card_image = ''
    card_text = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['card_image'] = self.card_image
        context['card_text'] = self.card_text
        return context 
    
#Reusable image slider that automatically swipes through static images
class ImageSlider(BaseTemplateView):
    """
    images specifies Image views to be inserted into ImageSlider
    """
    template_name = 'info/base/ImageSlider.html'
    images = []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rendered_images = []
        for image in self.images:
            rendered_images.append(image.as_view()(self.request).rendered_content)
        context['images'] = rendered_images
        return context 

#Reusable Image to be inserted into ImageSlider
#First Image used must have image_active set to True
class Image(BaseTemplateView):
    """
    image_interval specifies how long image will stay on screen before swiping 
    image_link is relative link to image used (django static tag is used in template)
    image_description is alt tag for image
    image_active must be set to true for the first image used in slider
    """
    template_name = 'info/base/Image.html'
    image_interval = None
    image_link = None
    image_description = None
    image_active = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_interval'] = self.image_interval
        context['image_link'] = self.image_link
        context['image_description'] = self.image_description
        context['image_active'] = self.image_active
        return context 
    
#Reusable Banner to be used at top of pages in absence of custome headers  
class Banner(BaseTemplateView):
    #image_link is relative link to image to be used as banner background
    #banner_title is the main title to be used on banner
    #banner_sub_title is the secondary title to be used under main title
    template_name = 'info/base/Banner.html'
    image_link = None
    banner_title = None
    banner_sub_title = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_link'] = self.image_link
        context['banner_title'] = self.banner_title
        context['banner_sub_title'] = self.banner_sub_title
        return context 

