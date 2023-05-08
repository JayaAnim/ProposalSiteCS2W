#Home page view
from .base import *
from .discourse import Testimonial, testimonial_data

class Home(BaseTemplateView):
    template_name = 'info/home/Home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['content'] = 'Home'

        testimonial_views = []
        testimonials = testimonial_data[:3]
        for testimonial in testimonials:
            testimonial_view = Testimonial.as_view(
                image_link=testimonial['image_link'],
                testimonial_name=testimonial['testimonial_name'],
                testimonial_position=testimonial['testimonial_position'],
                testimonial_text=testimonial['testimonial_text']
            )
            testimonial_html = testimonial_view(self.request).rendered_content
            testimonial_views.append(testimonial_html)
        
        context['testimonial_views'] = testimonial_views

        return context
    

"""
        # Create instances of Testimonial view and render them
        testimonial_views = []
        for testimonial in testimonials:
            testimonial_view = Testimonial.as_view(
                image_link=testimonial['image_link'],
                testimonial_name=testimonial['testimonial_name'],
                testimonial_position=testimonial['testimonial_position'],
                testimonial_text=testimonial['testimonial_text']
            )
            testimonial_html = testimonial_view(self.request).rendered_content
            testimonial_views.append(testimonial_html)

        # Add rendered Testimonial views to context
        context['testimonial_views'] = testimonial_views

        """