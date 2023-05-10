#Parent components and container for other views
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
    
class Base(TemplateView):
    page_title = "CyberSkills2Work"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context

class BaseTemplateView(Base, TemplateView):
    pass

class Section(BaseTemplateView):
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

    
class CardSlider(BaseTemplateView):
    template_name = 'info/base/CardSlider.html'
    cards = []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rendered_cards = []
        for card in self.cards:
            rendered_cards.append(card.as_view()(self.request).rendered_content)
        context['cards'] = rendered_cards
        return context 
    
class Card(BaseTemplateView):
    template_name = 'info/base/Card.html'
    card_image = ''
    card_text = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['card_image'] = self.card_image
        context['card_text'] = self.card_text
        return context 
    
class ImageSlider(BaseTemplateView):
    template_name = 'info/base/ImageSlider.html'
    images = []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rendered_images = []
        for image in self.images:
            rendered_images.append(image.as_view()(self.request).rendered_content)
        context['images'] = rendered_images
        return context 

class Image(BaseTemplateView):
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


