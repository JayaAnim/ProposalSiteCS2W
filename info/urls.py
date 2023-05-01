from django.urls import path
from .views import (
    apply,
    base,
    employers,
    home,
    impact,
    learners,
    training
)

app_name = 'info'

urlpatterns = [
    path('', home.Home.as_view(), name='Home'),
]