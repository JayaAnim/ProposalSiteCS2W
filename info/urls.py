from django.urls import path
from .views import (
    about,
    apply,
    base,
    employers,
    home,
    impact,
    learners,
    training,
    terms
)

app_name = 'info'

urlpatterns = [
    path('', home.Home.as_view(), name='Home'),
    path('about', about.About.as_view(), name='About'),
    path('learners', learners.Learners.as_view(), name='Learners'),
    path('programs', training.Training.as_view(), name='Training'),
    path('employers', employers.Employers.as_view(), name='Employers'),
    path('impact', impact.Impact.as_view(), name='Impact'),
    path('apply', apply.Apply.as_view(), name='Apply'),
    path('privacy-policy', terms.PrivacyPolicy.as_view(), name='Privacy'),
    path('tos', terms.TOS.as_view(), name='TOS'),
]