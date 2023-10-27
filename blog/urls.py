from django.urls import path, include
from rest_framework import routers

from .views import ContactViewSet, OurPageViewSet, FAQViewSet

router = routers.DefaultRouter()

router.register('contact', ContactViewSet, basename='contact')
router.register('our', OurPageViewSet, basename='our_page')
router.register('faq', FAQViewSet, basename='faq')

urlpatterns = [
    path('', include(router.urls))
]
