
from django.urls import path 
from .views import ContactFormView, ThankYouTemplateView


urlpatterns = [
        path('', ContactFormView.as_view(), name='contact'),
        path('thank-you/', ThankYouTemplateView.as_view(), name='thank_you'),
]
